import cv2
import numpy as np

import sys
from PIL import Image
import stepic
from qrGen import qrGen
from barGen import barGen
from dmGen import dmGen
from temp_gen import temp_gen
from propGen import propGen,encode_image,decode_image,encode_image1
#Defining the canvas width and height!
Height = int(sys.argv[2])
Width  = int(sys.argv[2])

for i in range(int(sys.argv[1])):
    #Reading images here
    imgQr = qrGen(i)
    imgBc = temp_gen(i)
    imgDm = dmGen(i)
    imgProp = propGen(1)
    imgProp1 = propGen(2)
    imgProp2 = propGen(4)

    cv2.imshow("a",imgBc)
    # print(imgBc,imgQr)
    imgCanvas = np.zeros([Height,Width,3],dtype=np.uint8)
    imgCanvas.fill(255)

    #Rectangle for the code
    # cv2.rectangle(imgCanvas, (int(0), int(0)), (int(Width), int(Height)), (0,0,255),10)

    #Rectangle for QR code
    cv2.rectangle(imgCanvas,(int(0.19*Width),int(.19*Height)),(int(0.81*Width),int(0.81*Height)),(0,0,0),1)
    #Place image at these coordinates
    imgQrResize = cv2.resize(imgQr,(int(0.8*Width)-int(0.2*Width),int(0.8*Height)-int(0.2*Height)))
    imgCanvas[int(0.2*Width):int(.8*Width),int(0.2*Height):int(0.8*Height)] = imgQrResize

    #Rectangle for Bar code
    cv2.rectangle(imgCanvas,(int(0.02*Width),int(.82*Height)),(int(0.72*Width),int(0.97*Height)),(0,0,0),2)
    # print(imgBc.shape)
    #Place image at these coordinates
    imgBarResize = cv2.resize(imgBc,(int(0.70*Width)-int(0.04*Width),int(0.96*Height)-int(0.83*Height)))
    imgCanvas[int(0.83*Height):int(0.96*Height),int(0.04*Width):int(0.70*Width)] = imgBarResize

    #Rectangle for DataMatrix code
    cv2.rectangle(imgCanvas,(int(0.74*Width),int(.82*Height)),(int(0.98*Width),int(0.97*Height)),(0,0,0),2)
    #Place image at these coordinates
    imgDmResize = cv2.resize(imgDm,(int(0.96*Width)-int(0.76*Width),int(0.96*Height)-int(0.83*Height)))
    imgCanvas[int(0.83*Height):int(0.96*Height),int(0.76*Width):int(0.96*Width)] = imgDmResize

    
    #Rectangle for proprietary code1
    cv2.rectangle(imgCanvas,(int(0.19*Width),int(.03*Height)),(int(0.81*Width),int(0.18*Height)),(0,0,0),2)
    #Place image at these coordinates

    imgPropResize = cv2.resize(imgProp,(int(0.8*Width)-int(0.2*Width),int(0.17*Height)-int(0.04*Height)))
    # cv2.rectangle(imgPropResize, (0, 0), (imgPropResize.shape[1], imgPropResize.shape[0]), (0, 0, 0), 4)
    # image = "img1.png"
    # cv2.imwrite("./prop/" + image, imgPropResize)
    imgCanvas[int(0.04*Height):int(0.17*Height),int(0.2*Width):int(0.8*Width)] = imgPropResize

    #Rectangle for proprietary code2
    cv2.rectangle(imgCanvas,(int(0.82*Width),int(.19*Height)),(int(0.97*Width),int(0.65*Height)),(0,0,0),2)
    #Place image at these coordinates
    if imgProp1.shape[0] < imgProp1.shape[1]:
        imgPropResize1 = cv2.rotate(imgProp1,cv2.ROTATE_90_CLOCKWISE)
    else:
        imgPropResize1 = imgProp1
    imgPropResize1 = cv2.resize(imgPropResize1,(int(0.96 * Width) - int(0.83 * Width), int(0.64 * Height) - int(0.20 * Height)))
    # cv2.rectangle(imgPropResize1, (0, 0), (imgPropResize1.shape[1], imgPropResize1.shape[0]), (0, 0, 0), 4)
    # image = "img2.png"
    # cv2.imwrite("./prop/" + image, imgPropResize1)
    imgCanvas[int(0.20 * Height):int(0.64 * Height), int(0.83 * Width):int(0.96 * Width)] = imgPropResize1

    #Rectangle for proprietry code3
    cv2.rectangle(imgCanvas,(int(0.03*Width),int(.19*Height)),(int(0.18*Width),int(0.65*Height)),(0,0,0),2)
    #Place image at these coordinates
    if imgProp2.shape[0] < imgProp2.shape[1]:
        imgPropResize2 = cv2.rotate(imgProp2,cv2.ROTATE_90_CLOCKWISE)
    else:
        imgPropResize2 = imgProp2

    imgPropResize2 = cv2.resize(imgPropResize2,(int(0.17*Width)-int(0.04*Width),int(0.64*Height)-int(0.20*Height)))
    # cv2.rectangle(imgPropResize2, (0, 0), (imgPropResize2.shape[1], imgPropResize2.shape[0]), (0, 0, 0), 4)
    # image = "img3.png"
    # cv2.imwrite("./prop/" + image, imgPropResize2)
    imgCanvas[int(0.20*Height):int(0.64*Height),int(0.04*Width):int(0.17*Width)] = imgPropResize2

    

    #Rectangle for pivot1
    cv2.rectangle(imgCanvas,(int(0.83*Width),int(0.04*Height)),(int(0.96*Width),int(0.17*Height)),(101,190,255),-1)
    #Rectangle for pivot2
    cv2.rectangle(imgCanvas,(int(0.04*Width),int(0.04*Height)),(int(0.17*Width),int(0.17*Height)),(101,190,255),-1)
    #Rectangle for pivot3
    cv2.rectangle(imgCanvas,(int(0.83*Width),int(0.67*Height)),(int(0.96*Width),int(0.8*Height)),(101,190,255),-1)
    #Rectangle for pivot4
    cv2.rectangle(imgCanvas,(int(0.04*Width),int(0.67*Height)),(int(0.17*Width),int(0.8*Height)),(101,190,255),-1)

    file = "PCF/pcf"+str(i).zfill(4)+".png"
    cv2.imwrite(file, imgCanvas)
    im = Image.open(file)
    test_string = "Product "+str(i)
    res = bytes(test_string, 'utf-8')
    im1 = stepic.encode(im,res)
    im1.save(file, 'PNG')
    print("Saved: "+"PCF/pcf"+str(i).zfill(4)+".png")
    #cv2.waitKey(0)

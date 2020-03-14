import cv2
import numpy as np

#Defining the canvas width and height!
Height = 400
Width  = 400

#Reading images here
imgQr = cv2.imread("Skeleton/qr.png")
imgBc = cv2.imread("Skeleton/bc.png")
imgDm = cv2.imread("Skeleton/dm.png")
imgProp = cv2.imread("Skeleton/prop.png")
imgProp1 = cv2.imread("Skeleton/prop.png")
imgProp2 = cv2.imread("Skeleton/prop2.png")


imgCanvas = np.zeros([Height,Width,3],dtype=np.uint8)
imgCanvas.fill(255)

#Rectangle for QR code
# cv2.rectangle(imgCanvas,(int(0.2*Width),int(.2*Height)),(int(0.8*Width),int(0.8*Height)),(0,0,0),1)
#Place image at these coordinates
imgQrResize = cv2.resize(imgQr,(int(0.8*Width)-int(0.2*Width),int(0.8*Height)-int(0.2*Height)))
imgCanvas[int(0.2*Width):int(.8*Width),int(0.2*Height):int(0.8*Height)] = imgQrResize

#Rectangle for Bar code
# cv2.rectangle(imgCanvas,(int(0.04*Width),int(.83*Height)),(int(0.74*Width),int(0.96*Height)),(0,0,0),1)
#Place image at these coordinates
imgBarResize = cv2.resize(imgBc,(int(0.74*Width)-int(0.04*Width),int(0.96*Height)-int(0.83*Height)))
imgCanvas[int(0.83*Height):int(0.96*Height),int(0.04*Width):int(0.74*Width)] = imgBarResize

#Rectangle for DataMatrix code
# cv2.rectangle(imgCanvas,(int(0.76*Width),int(.83*Height)),(int(0.96*Width),int(0.96*Height)),(0,0,0),1)
#Place image at these coordinates
imgDmResize = cv2.resize(imgDm,(int(0.96*Width)-int(0.76*Width),int(0.96*Height)-int(0.83*Height)))
imgCanvas[int(0.83*Height):int(0.96*Height),int(0.76*Width):int(0.96*Width)] = imgDmResize


#Rectangle for proprietary code1
# cv2.rectangle(imgCanvas,(int(0.2*Width),int(.04*Height)),(int(0.8*Width),int(0.17*Height)),(0,0,0),1)
#Place image at these coordinates
imgPropResize = cv2.resize(imgProp,(int(0.8*Width)-int(0.2*Width),int(0.17*Height)-int(0.04*Height)))
imgCanvas[int(0.04*Height):int(0.17*Height),int(0.2*Width):int(0.8*Width)] = imgPropResize

#Rectangle for proprietary code2
# cv2.rectangle(imgCanvas,(int(0.83*Width),int(.2*Height)),(int(0.96*Width),int(0.64*Height)),(0,0,0),1)
#Place image at these coordinates
if imgProp1.shape[0] < imgProp1.shape[1]:
    imgPropResize1 = cv2.rotate(imgProp1,cv2.ROTATE_90_CLOCKWISE)
    print("hi")
else:
    imgPropResize1 = imgProp1
imgPropResize1 = cv2.resize(imgPropResize1,(int(0.96 * Width) - int(0.83 * Width), int(0.64 * Height) - int(0.20 * Height)))
imgCanvas[int(0.20 * Height):int(0.64 * Height), int(0.83 * Width):int(0.96 * Width)] = imgPropResize1


#Rectangle for proprietry code3
# cv2.rectangle(imgCanvas,(int(0.04*Width),int(.2*Height)),(int(0.17*Width),int(0.64*Height)),(0,0,0),1)
#Place image at these coordinates
if imgProp2.shape[0] < imgProp2.shape[1]:
    imgPropResize2 = cv2.rotate(imgProp2,cv2.ROTATE_90_CLOCKWISE)
    print("hi")
else:
    imgPropResize2 = imgProp2
imgPropResize2 = cv2.resize(imgPropResize2,(int(0.17*Width)-int(0.04*Width),int(0.64*Height)-int(0.20*Height)))
imgCanvas[int(0.20*Height):int(0.64*Height),int(0.04*Width):int(0.17*Width)] = imgPropResize2



#Rectangle for pivot1
cv2.rectangle(imgCanvas,(int(0.83*Width),int(0.04*Height)),(int(0.96*Width),int(0.17*Height)),(101,190,255),-1)
#Rectangle for pivot2
cv2.rectangle(imgCanvas,(int(0.04*Width),int(0.04*Height)),(int(0.17*Width),int(0.17*Height)),(101,190,255),-1)
#Rectangle for pivot3
cv2.rectangle(imgCanvas,(int(0.83*Width),int(0.67*Height)),(int(0.96*Width),int(0.8*Height)),(101,190,255),-1)
#Rectangle for pivot4
cv2.rectangle(imgCanvas,(int(0.04*Width),int(0.67*Height)),(int(0.17*Width),int(0.8*Height)),(101,190,255),-1)

cv2.imshow("Image",imgCanvas)
cv2.imwrite("code_placed.png", imgCanvas)
cv2.waitKey(0)
import cv2
import numpy as np

#Defining the canvas width and height!
Height = 600
Width  = 600

#Reading images here
imgQr = cv2.imread("Skeleton/qr.png")
imgBc = cv2.imread("Skeleton/bc.png")
imgDm = cv2.imread("Skeleton/dm.png")
imgProp = cv2.imread("Skeleton/prop.png")

imgCanvas = np.zeros([Height,Width,3],dtype=np.uint8)
imgCanvas.fill(255)

#Rectangle for QR code
cv2.rectangle(imgCanvas,(int(0.2*Width),int(.2*Height)),(int(0.8*Width),int(0.8*Height)),(0,0,0),1)

#Rectangle for Bar code
cv2.rectangle(imgCanvas,(int(0.04*Width),int(.83*Height)),(int(0.74*Width),int(0.96*Height)),(0,0,0),1)

#Rectangle for DataMatrix code
cv2.rectangle(imgCanvas,(int(0.76*Width),int(.83*Height)),(int(0.96*Width),int(0.96*Height)),(0,0,0),1)

#Rectangle for proprietary code1
cv2.rectangle(imgCanvas,(int(0.2*Width),int(.04*Height)),(int(0.8*Width),int(0.17*Height)),(0,0,0),1)

#Rectangle for proprietary code2
cv2.rectangle(imgCanvas,(int(0.83*Width),int(.2*Height)),(int(0.96*Width),int(0.64*Height)),(0,0,0),1)

#Rectangle for proprietry code3
cv2.rectangle(imgCanvas,(int(0.04*Width),int(.2*Height)),(int(0.17*Width),int(0.64*Height)),(0,0,0),1)


#Rectangle for pivot1
cv2.rectangle(imgCanvas,(int(0.83*Width),int(0.04*Height)),(int(0.96*Width),int(0.17*Height)),(101,190,255),-1)
#Rectangle for pivot2
cv2.rectangle(imgCanvas,(int(0.04*Width),int(0.04*Height)),(int(0.17*Width),int(0.17*Height)),(101,190,255),-1)
#Rectangle for pivot3
cv2.rectangle(imgCanvas,(int(0.83*Width),int(0.67*Height)),(int(0.96*Width),int(0.8*Height)),(101,190,255),-1)
#Rectangle for pivot4
cv2.rectangle(imgCanvas,(int(0.04*Width),int(0.67*Height)),(int(0.17*Width),int(0.8*Height)),(101,190,255),-1)
# cv2.circle(imgCanvas, (int(0.04*Width),int(.8*Height)), radius = 10,color=(0,0,255),thickness=-1 )
# img  = cv2.resize(imgCanvas,(400,400))
cv2.imshow("Image",imgCanvas)
cv2.imwrite("code_skeleton.png", imgCanvas)
cv2.waitKey(0)
import cv2
import numpy as np

################Constants###############
Height = 300
Width = 300

#Creating a white canvas
imgCanvas = np.zeros([700,700,3],dtype=np.uint8)
imgCanvas.fill(255)
print(imgCanvas)
# cv2.imshow("Canvas",imgCanvas)

#Reading the image and Resizing the image
imgQr = cv2.imread("qr.png")
print(imgQr.shape)
imgQr = cv2.resize(imgQr,(Height,Width))
print(imgQr.shape)

imgBc = cv2.imread("bar.jpg")
print("Bar shape",imgBc.shape)
imgBc = cv2.resize(imgBc,(imgBc.shape[0]//4,imgBc.shape[1]//4))
print("Resized bar shape",imgBc.shape)

imgDm = cv2.imread("dm.jpg")
print("Data Matrix",imgDm.shape)
imgDm = cv2.resize(imgDm,(imgDm.shape[0]//3,imgDm.shape[1]//3))
print("Resized Dm shape",imgDm.shape)
#Placing the image on top of image
imgCanvas[50:350,50:350,:] = imgQr
imgCanvas[335:imgBc.shape[0]+335,50:imgBc.shape[1]+50,:] = imgBc
imgCanvas[335:imgDm.shape[0]+335,500:imgDm.shape[1]+500,:] = imgDm
imgCanvas = cv2.resize(imgCanvas,(400,400))
cv2.imshow("Combined2",imgCanvas)

#Dissplaying the image.
# cv2.imshow("QR",imgQr)
cv2.waitKey(0)
import cv2
import numpy as np

################Constants###############
Height = 300
Width = 300

#Creating a white canvas
imgCanvas = np.zeros([500,500,3],dtype=np.uint8)
imgCanvas.fill(255)
imgQr = cv2.imread("qr.png")
imgQr = cv2.resize(imgQr,(Height,Width))
imgCanvas[100:400,100:400:] = imgQr
# imgCanvas = cv2.resize(imgCanvas,(400,400))
cv2.imshow("Combined2",imgCanvas)
cv2.waitKey(0)
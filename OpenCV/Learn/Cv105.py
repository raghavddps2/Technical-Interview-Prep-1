import cv2
import numpy as np

img1 = cv2.imread("lena.png")
img2 = cv2.imread("lena.png")

#We can use the stacking using the easy function, that is omething that is used a lot in various applications!

print(img1.shape)
print(img2.shape)

img1 = cv2.resize(img1,(0,0),None,0.5,0.5)
img2 = cv2.resize(img2,(0,0),None,0.5,0.5)

#This is used to stack the images horizontally
hor = np.hstack((img1,img2))

#This is used to stack the images vertically!
ver = np.vstack((img1,img2))

cv2.imshow("Horizontal stack",hor)
cv2.imshow("Vertical Stack",ver)
cv2.waitKey(0)
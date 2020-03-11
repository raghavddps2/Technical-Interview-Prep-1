import numpy as np
import cv2

img = cv2.imread("composite_code1.png")
imgContours = img.copy()

#PREPROCESSING!

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur,10,50)

##################### Finding all the contours ###############

countours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours,countours,-1,(0,255,0),1)
cv2.imshow("Marked contours",imgContours)
cv2.imwrite("Composite_code_contours.png",imgContours)
cv2.waitKey(0)
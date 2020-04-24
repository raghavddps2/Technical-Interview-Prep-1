import numpy as np
import cv2
import os

dirname = 'detectedCodes'
os.mkdir(dirname)

img = cv2.imread("pcf0000.png")
imgContours = img.copy()
cv2.imshow('',img)
#PREPROCESSING!

imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur,10,50)

##################### Finding all the contours ###############

countours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for i in countours:
    print(cv2.boundingRect(i))

print("ans",len(countours))
cv2.imshow("",imgContours)
i = 1
all_measures = {}
area = []
for c in countours[1:]:
    x,y,w,h=cv2.boundingRect(c)
    print(i," : ",w*h)
    all_measures[i] = [w*h,x,y,w,h]
    area.append(w*h)
    print(x,y,w,h)
    # image = cv2.rectangle(imgContours, (x, y), (x + w, y + h), (36, 255, 12), 1)
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(image,str(i), (x+w//2,y+h//2),font, 0.9, (36, 255, 12), 2,cv2.LINE_AA)
    i = i+1

# cv2.drawContours(imgContours,countours,-1,(255,0,0),1)
print(area)
min_area = min(area)
for i in list(all_measures.keys()):
    print(all_measures[i])
    if all_measures[i][0] <= (min_area+200):
        all_measures.pop(i)

print(len(all_measures))
number = 1
for key in all_measures:
    x = all_measures[key][1]
    y = all_measures[key][2]
    w = all_measures[key][3]
    h = all_measures[key][4]
    temp = imgContours[y:y + h, x:x + w]
    print(temp.shape)
    str1 = "file" + str(number) + ".png"
    number = number + 1
    cv2.imwrite(os.path.join(dirname,str1), temp)

img11 = cv2.resize(imgContours,(600,600))
cv2.imshow("Marked contours",img11)
cv2.imwrite("Composite_code_contours.png",imgContours)
cv2.waitKey(0)
# 65 300 3 80 355 3
# 220 65 3 225 70 3
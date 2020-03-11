import cv2
import numpy as np
"""
    Here, in this we will learn how to create black and white images,
    and how to create text on images and how do we draw lines and all etc..

    Similarly, we can create line and rectangles and various other things in cv2.
    cv2.rectangle
    cv2.circle
    cv2.putText
"""

#This wll generate a white image
imgWhite = np.ones((512,512)) 

#This will generate a black image
imgBlack = np.zeros((512,512))

#Now, let us generate a colur image
# imgColor = np.random.randint(0,100,(100,100,3))
# print(imgColor.shape)

#How to create a line
imageNew = np.ones((512,512,3),np.uint8)
cv2.line(imageNew,(0,0),(100,100),(255,0,0),2)


cv2.imshow("Self created image White",imgWhite)
cv2.imshow("Self created image Black",imgBlack)
cv2.imshow("Self created image Color",imageNew)


  


cv2.waitKey(0)
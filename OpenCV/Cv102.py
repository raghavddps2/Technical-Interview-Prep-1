import cv2
import numpy as np
"""
     So, now to start with there are five functions that anybody whi wants to work with openCv should know.

     1. Converting an image to GrayScale (cv2.cvtColor)
     2. Blurring an image    (cv2.GaussianBlur)
     3. Edge detector (cv2.Canny)
     4. Dilation 
            This basically expands the connected sets of 1s of a binary image.
            It can be used for
                Growing features
                Filling holes and gaps.
            This in general can be used for fixing holes or gaps.    
     5. Erosion
            Erosion shrinks the connected sets of 1s of a binary image
            It can be used for
                Shrinking features.
                Removing bridges, branches, protusions.
"""

kernel = np.ones((5,5),np.uint8)
print(kernel)

img = cv2.imread("lena.png")
cv2.imshow("Lena",img)

#This is the color cvtMethod
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Lena Grayscale",imgGray)

#Blurring an image - The kernel can only be in odd numbers and if we inc our blurryness will inc

imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
cv2.imshow("Lena Blurred",imgBlur)


#For the edge detector, we have to pass the blurred image here, we will even try with grayscale image.
imgCanny = cv2.Canny(imgBlur,100,100)
cv2.imshow("Image canny",imgCanny)

imgCanny1 = cv2.Canny(imgGray,100,100)
cv2.imshow("Image canny 1",imgCanny1)

#Dilation: Kernel is used. (Kernel is basically a matrix that we use to iterate through the image to actually perform a function)
#We even need to tell the iterations. WHen applied on canny images, it willl increase the thickness of the lines.
imgDilation = cv2.dilate(imgCanny,kernel,iterations=1)
cv2.imshow("Img dilation",imgDilation)

#Erosion. even here we will use the kernel
imgErosion = cv2.erode(imgDilation,kernel,iterations=1)
cv2.imshow("Img erosion",imgErosion)



cv2.waitKey(0)
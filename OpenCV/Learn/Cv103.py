import cv2

img = cv2.imread("lena.png")

#The below gives the shape as (512,512,3), here 3 implies 3 channels.
print(img.shape)

#This reshapes our image to 400 by 400
width,height = 400,400
imgResize = cv2.resize(img,(width,height))


#Cropping an image.
# img[i][j] i is the height and j is the weight
imgCropped = img[0:900][300:540]

cv2.imshow("Image",img)
cv2.imshow("Image resized",imgResize)
cv2.imshow("Image cropped",imgCropped)
cv2.waitKey(0)
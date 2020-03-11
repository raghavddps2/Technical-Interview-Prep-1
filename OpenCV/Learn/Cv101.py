import cv2

#The function that reads the image is as follows.
img = cv2.imread("lena.png")

#To show the image, the straight function is, iamshow
cv2.imshow("Lena",img)

#This sets some delay, as to till when we want an image.
cv2.waitKey(1000)

#Now, for a video or a webcam we need a loop for the frame.
frameWidth = 640
frameHeight  = 360

#This is for the capturing device.
cap = cv2.VideoCapture("testVideo.mp4")

#To use the webcam, we directly have this
#Here, 3 and 4 are numbers set by penCv for width and height respectively!
# cap = cv2.VideoCapture(0)
cap.set(3,frameWidth)
cap.set(4,frameHeight)

#We need to declare a loop in which we can read each frame of the video
while True:

    #This reads a frame from this cap, if it gives, it gives success as true, else false, it puts the frame in img
    success,img = cap.read()

    if success == False:
        break
    cv2.imshow("Video",img)

    #This will run the video frame by frame!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
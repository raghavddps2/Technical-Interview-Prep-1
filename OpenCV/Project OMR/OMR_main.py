import cv2
import utils
import numpy as np

######################################
path = "code.jpg"
widthImg = 400
heightImg = 400
questions = 5
choices = 5
answers = [1,2,0,1,4]
######################################


img = cv2.imread(path)
img = cv2.resize(img,(widthImg,heightImg))
imgContours = img.copy()
imgRectCountours = img.copy()
#PREPROCESSING!
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1)
imgCanny = cv2.Canny(imgBlur,10,50)
imgBlank = np.zeros_like(img)
imgFinal = img.copy()

##################### Finding all the contours ###############
countours,hierarchy = cv2.findContours(imgCanny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
cv2.drawContours(imgContours,countours,-1,(0,255,0),10)

rectangleContours = utils.rectContour(countours)
biggestContour = utils.getCornerPoints(rectangleContours[0])
gradePoints = utils.getCornerPoints(rectangleContours[0])



if biggestContour.size != 0 and gradePoints.size != 0:
    cv2.drawContours(imgRectCountours,biggestContour,-1,(0,0,255),10)
    cv2.drawContours(imgRectCountours,gradePoints, -1, (0, 0, 255), 10)
    biggestContour = utils.reorder(biggestContour)
    gradePoints = utils.reorder(gradePoints)

    pt1 = np.float32(biggestContour)
    pt2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix = cv2.getPerspectiveTransform(pt1,pt2)
    imgWrapColored = cv2.warpPerspective(img,matrix,(widthImg,heightImg))
    # cv2.imshow("OMR",imgWrapColored)

    ptG1 = np.float32(gradePoints)
    ptG2 = np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrixG = cv2.getPerspectiveTransform(ptG1,ptG2)
    imgGradeDisplay = cv2.warpPerspective(img,matrixG,(widthImg,heightImg))[1]
    # cv2.imshow("Grade",imgGradeDisplay)


    imgWarpGray = cv2.cvtColor(imgWrapColored,cv2.COLOR_BGR2GRAY)
    imgThresh = cv2.threshold(imgWarpGray,170,255,cv2.THRESH_BINARY_INV)[1]
    boxes = utils.splitBoxes(imgThresh)

    #We need to split the above into 25 different and we need to create our split functions.

    #Getting PixelValues of each box!
    print(cv2.countNonZero(boxes[1]),cv2.countNonZero(boxes[2]))
    myPixelVals =np.zeros((questions,choices))
    countC = 0
    countR = 0

    for image in boxes:
        totalPixels = cv2.countNonZero(image)
        myPixelVals[countR][countC] = totalPixels
        countC += 1
        if (countC == choices):
            countR += 1
            countC  = 0
    print(myPixelVals)


    #FINDING Index values of the Markings
    myIndex = []
    for x in range(0,questions):
        arr = myPixelVals[x]
        myIndexVal = np.where(arr == np.amax(arr))
        myIndex.append(myIndexVal[0])

    print(myIndex)

    #Here we will perform the GRADING!
    grading = []
    for x in range(0,questions):
        if answers[x] == myIndex[x]:
            grading.append(1)
        else:
            grading.append(0)

    print(grading)
    score = np.sum(grading)/questions * 100
    print(score)


    #Displaying Answers!
    imgAnswers = imgWrapColored.copy()
    imgResult = utils.showAnswers(imgAnswers,myIndex,answers,grading,questions,choices)

    imgRawDrawings = np.zeros_like(imgWrapColored)
    imgRawDrawings = utils.showAnswers(img,myIndex,answers,grading,questions,choices)
    invMatrix = cv2.getPerspectiveTransform(pt2,pt1)
    imgInvWrap = cv2.warpPerspective(imgRawDrawings,invMatrix,(widthImg,heightImg))

    #Displaying the grade
    imgRawGrade = np.zeros_like(imgGradeDisplay)
    cv2.putText(imgRawGrade,str(score)+"%",(50,100),cv2.FONT_HERSHEY_COMPLEX,3,(0,255,0),3)
    invMatrixG = cv2.getPerspectiveTransform(ptG2,ptG1)
    imgInvGradeDisplay = cv2.warpPerspective(imgRawGrade,invMatrixG,(widthImg,heightImg))
    imgFinal = cv2.addWeighted(imgFinal, 1, imgInvWrap, 1, 0)
    # imgFinal = cv2.addWeighted(imgFinal,1,imgInvGradeDisplay,1,0)

imageArray = ([img,imgGray,imgBlur,imgContours],[imgContours,imgRectCountours,imgWrapColored,imgThresh],[imgResult,imgInvWrap,imgFinal,imgBlank])
imageStacked = utils.stackImages(imageArray,0.5,)



cv2.imshow("Stacked Images",imageStacked)
cv2.waitKey(0)

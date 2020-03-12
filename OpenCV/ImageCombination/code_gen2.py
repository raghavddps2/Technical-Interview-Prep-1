import cv2
import numpy as np

imgQr = cv2.imread("qr.png")
imgBc = cv2.imread("bc.jpg")
imgDm = cv2.imread("dm.png")
imgProp = cv2.imread("prop.png")
print(imgBc.shape)
print(imgDm.shape)
print(imgQr.shape)
print(imgProp.shape)
Height = 600
Width = 600

imgCanvas = np.zeros([1000,1000,3],dtype=np.uint8)
imgCanvas.fill(255)

imgQrResize = cv2.resize(imgQr,(600,600))
imgCanvas[200:800,200:800:] = imgQrResize
cv2.rectangle(imgCanvas,(200,200),(800,800),(0,0,0),1)
# ##############Logic for width of bar code and dm code############### #
imgBcWidth = imgBc.shape[1]
imgDmWidth = imgDm.shape[1]

imgBcResizeWidth = 360
imgDmResizeWidth =  180

imgBcResize = cv2.resize(imgBc,(imgBcResizeWidth,180))
imgDmResize = cv2.resize(imgDm,(imgDmResizeWidth,180))

imgPropResize = cv2.resize(imgProp,(600,100))

cv2.rectangle(imgCanvas,(50,50),(150,150),(101,190,255),-1)
cv2.rectangle(imgCanvas,(950,950),(850,850),(101,190,255),-1)
cv2.rectangle(imgCanvas,(50,950),(150,850),(101,190,255),-1)
cv2.rectangle(imgCanvas,(850,50),(950,150),(101,190,255),-1)



print(imgBcResize.shape)
print(imgDmResize.shape)
print(imgBcResizeWidth)

imgCanvas[820:1000,200:imgBcResizeWidth+200] = imgBcResize
cv2.rectangle(imgCanvas,(200,800),(600,1000),(0,0,0),1)

imgCanvas[820:1000,imgBcResizeWidth+260:800] = imgDmResize
cv2.rectangle(imgCanvas,(600,800),(800,1000),(0,0,0),1)

imgCanvas[50:150,200:800]  = imgPropResize
cv2.rectangle(imgCanvas,(200,50),(800,150),(0,0,0),1)

imgCanvas[200:800,50:150] = cv2.rotate(imgPropResize,cv2.ROTATE_90_CLOCKWISE)
cv2.rectangle(imgCanvas,(50,200),(150,800),(0,0,0),1)

imgCanvas[200:800,850:950] = cv2.rotate(imgPropResize,cv2.ROTATE_90_CLOCKWISE)
cv2.rectangle(imgCanvas,(850,200),(950,800),(0,0,0),1)

# imgCanvas = cv2.resize(imgCanvas,(100,200))
cv2.imwrite('composite_code1.png',imgCanvas)
cv2.imshow("hi",imgCanvas)
cv2.waitKey(0)
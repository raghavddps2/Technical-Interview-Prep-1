import cv2
import numpy as np

img = cv2.imread("Skeleton/dm.png")
img1 = cv2.resize(img,(100,400))
cv2.imwrite("conv_dm.png",img1)

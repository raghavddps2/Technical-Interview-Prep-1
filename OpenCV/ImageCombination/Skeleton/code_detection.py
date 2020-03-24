from pyzbar.pyzbar import decode
import cv2
import os

def detect_code(path):
    img = cv2.imread(path)
    img = cv2.resize(img,(510,146))
    print(img.shape)
    # img = cv2.resize(img,(120,400))
    cv2.imshow("ans",img)
    print(decode(img))


directory = '../detectedCodes'
for filename in os.listdir(directory):
    if filename.endswith(".png"):
        print(os.path.join(directory, filename))
        continue
import cv2
import os
import shutil
import treepoem
def barGen(i):
    image = treepoem.generate_barcode(barcode_type='code39', data="83515684125412341245"+str(i).zfill(4))
    filename = "barcode"+str(i).zfill(4)+".png"
    image.save("bar/"+filename)
    #shutil.move(filename, "batch/images/"+filename)
    qr = cv2.imread("bar/"+filename)
    return qr
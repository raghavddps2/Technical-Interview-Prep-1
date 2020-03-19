import cv2
import os
import shutil
import treepoem
def dmGen(i):
    image = treepoem.generate_barcode(barcode_type='datamatrix', data="8351:5684:1254:1234:1245:"+str(i).zfill(4))
    filename = "dm"+str(i).zfill(4)+".png"
    image.save("dm/"+filename)
    #shutil.move(filename, "batch/images/"+filename)
    qr = cv2.imread("dm/"+filename)
    return qr
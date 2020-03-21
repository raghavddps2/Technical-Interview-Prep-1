import cv2
import os
import shutil
import treepoem
from pystrich.datamatrix import DataMatrixEncoder
def dmGen(i):
    # image = DataMatrixEncoder("This is a DataMatrix.")
    image = treepoem.generate_barcode(barcode_type='datamatrix', data="8351:5684:1254:1234:1245:"+str(i).zfill(4))
    filename = "dm"+str(i).zfill(4)+".png"
    image.save("dm/"+filename)
    qr = cv2.imread("dm/"+filename)
    return qr
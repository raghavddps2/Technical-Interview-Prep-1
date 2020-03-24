import cv2
import os
import shutil
import treepoem
def qrGen(i):
    image = treepoem.generate_barcode(barcode_type='qrcode', data="12345qr"+str(i).zfill(4))
    filename = "qrcode"+str(i).zfill(4)+".png"
    image.save("qr/"+filename)
    qr = cv2.imread("qr/"+filename)
    return qr
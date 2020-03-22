import cv2
import os
import shutil
import treepoem
def qrGen(i):
    image = treepoem.generate_barcode(barcode_type='qrcode', data="8351:5684:1254:1234:1245:"+str(i).zfill(4))
    filename = "qrcode"+str(i).zfill(4)+".png"
    image.save("qr/"+filename)
    qr = cv2.imread("qr/"+filename)
    return qr
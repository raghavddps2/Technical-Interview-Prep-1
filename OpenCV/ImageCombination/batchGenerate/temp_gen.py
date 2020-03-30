import cv2
import treepoem
import barcode
from barcode.writer import ImageWriter

EAN = barcode.get_barcode_class('ean13')
def temp_gen(i):
    ean = EAN('123456789017', writer=ImageWriter())
    filename = "barcode" + str(i).zfill(4)
    fullname = ean.save("bar/"+filename)
    qr = cv2.imread("bar/"+filename+".png")
    return qr


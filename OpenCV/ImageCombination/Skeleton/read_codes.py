from pyzbar.pyzbar import decode
import cv2
img = cv2.imread("file2.png")
print(img.shape)
img = cv2.resize(img,(510,146))
print(decode(img))
#

from pyzbar.pyzbar import decode
import cv2
img = cv2.imread("qrcode0000.png")
print(img.shape)
img = cv2.resize(img,(510,146))
print(decode(img))
#


from pystrich.datamatrix import DataMatrixEncoder
encoder = DataMatrixEncoder("This is a DataMatrix.")
encoder.save( "datamatrix_test.png" )
print(encoder.get_ascii())

import cv2
from pylibdmtx.pylibdmtx import decode
img = cv2.imread('dm0000.png')
ans = decode(img)
print(ans)

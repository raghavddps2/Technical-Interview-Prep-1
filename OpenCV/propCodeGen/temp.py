from PIL import Image
import stepic
im1 = Image.open('file2.png')
im1.show()
im2 = Image.open('pcf0000.png')
stegoImage = stepic.decode(im2)
print(stegoImage)

im1 = Image.open('file.png')
im1.show()
im2 = Image.open('pcf0000.png')
stegoImage = stepic.decode(im2)
print(stegoImage)

im1 = Image.open('file2.png')
im1.show()
im2 = Image.open('pcf0000.png')
stegoImage = stepic.decode(im2)
print(stegoImage)
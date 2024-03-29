import cv2


def char_generator(message):
    for c in message:
        yield ord(c)

def get_image(image_location):
    img = cv2.imread(image_location)
    return img

def gcd(x, y):
    while(y):
        x, y = y, x % y

    return x

def encode_image1(image_location, msg):
    # print(image_location)
    img = get_image(image_location)
    # img = image_location
    msg_gen = char_generator(msg)
    pattern = gcd(len(img), len(img[0]))
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i+1 * j+1) % pattern == 0:
                try:
                    img[i-1][j-1][0] = next(msg_gen)
                except StopIteration:
                    img[i-1][j-1][0] = 0
                    return img


def encode_image(image_location, msg):
    # print(image_location)
    # img = get_image(image_location)
    img = image_location
    msg_gen = char_generator(msg)
    pattern = gcd(len(img), len(img[0]))
    for i in range(len(img)):
        for j in range(len(img[0])):
            if (i+1 * j+1) % pattern == 0:
                try:
                    img[i-1][j-1][0] = next(msg_gen)
                except StopIteration:
                    img[i-1][j-1][0] = 0
                    return img

def decode_image(img_loc):
  # img = get_image(img_loc)
  img = img_loc
  pattern = gcd(len(img), len(img[0]))
  message = ''
  for i in range(len(img)):
    for j in range(len(img[0])):
      if (i-1 * j-1) % pattern == 0:
        if img[i-1][j-1][0] != 0:
          message = message + chr(img[i-1][j-1][0])
        else:
          return message
def propGen(i):

    image =  "img" + str(i)+".png"
    image2 = cv2.imread(image)
    # image2 = encode_image(image,"Product code: "+str(i))
    # cv2.imwrite("./prop/"+image,image2)
    return image2
import math
def checkKaprekarNumber(number):
    if number == 1:
        return True
    elif number > 1 and number < 4:
        return False
    else:
        sq_no = int(math.pow(number,2))
        sq_no_str = str(sq_no)
        sq_no_str_len = len(sq_no_str)
        d = sq_no_str_len//2
        digit1 = int(sq_no_str[:d])
        digit2 = int(sq_no_str[d:])
        if (digit1+digit2) == number:
            return True
        else:
            return False

number = int(input())
print(checkKaprekarNumber(number))
"""
    Write a program to determine if the number is even or odd.
    Please don't use any modulus operator

    0: 00000
    1: 00001
    2: 00010
    3: 00011
    4: 00100
    5: 00101
    6: 00110
    7: 00111
    8: 01000
    9: 01001

    -----> Looking at the above pattern we notice that if the least significant bit is 0
             * The number turns out to be even
             * Otherwise the number truens out to be odd

"""

#Simply and with 1 and we can dtermine whether the number is even or odd
def is_odd(x: int):

    if x and 1 == 0:
        return True

    return False
a = int(input())
print("The number ",a," is ","odd" if is_odd(a) == True  else "even" )
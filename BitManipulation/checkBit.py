"""
    Write a program to check whether the nth bit for a number is set or unset
    * For example for the number 6:
        The binary representation is given as 110, so here we have two things,
        the Least significant bit and the Most significant bit
    
    0: 0000   Rigtmost: Least significant 
    1: 0001   Leftmost: Most Significant
    2: 0010
    3: 0011
    4: 0100
    5: 0101
    6: 0110
    7: 0111
    8: 1000
    9: 1001

    1 << 0 --> This basically means left shift by zero.
    1 >> 0 --> This basically means right shift by zero

    1 << 1 --> This will basically shift the binary representation by one to the left
    1 << 2 --> This will basically shift the binary representation by two to the right

    #So, now all we have to do is shift the bit to the right by k and then and it with 1
        -> If we get 0, the bit is 0
        -> If we get 1, the bit is 1
"""

#The K passed here assumes that the least significant bit is 0
def check_status(a: int,k: int):

    #This is just right shifting the bit by k places.
    a = a >> k

    #Or alternatively we could have shifted 1 to the left by l 1 << k
    if a & 1:
        return True
    return False

a = int(input("Enter the value of n:\t"))
k = int(input("Enter the value of k:\t"))
print(check_status(a,k))
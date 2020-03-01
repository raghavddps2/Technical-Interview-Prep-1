#To unset the bit, we can basically use the bitwise not operation with the idea as to how we set the nth bit
"""
    
    Unset the 1st bit in the binary representation of 6
    6: 1 1 0 (Thisis the integer)
       1 0 1 (This is shifting 1 by k bits and then negating it )
    &  1 0 0 (This will be simply anding the result)

"""

def unsetBit(n,k):

    return n & ~(1<<k)

n = int(input("Enter the value of n")) 
k = int(input("Enter the value of k"))
print("The result after unsetting the nth bit is ",unsetBit(n,k))





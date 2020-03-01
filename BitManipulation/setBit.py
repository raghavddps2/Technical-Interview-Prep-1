"""
    Write a program that takes an integer and sets the nth bit in binary representation of that integer 
"""

def setBit(n,k):

    print(bin(n))
    #We simply shift one by K bits
    a = 1 << k
    print(a)
    #Now, all we have to do is or the n and the a, this will give the new integer obtained after setting that bit
    print(bin(n|a))
    return (n | a)

n = int(input("Enter the number:\t"))
k = int(input("Enter the bit number:\t"))
print("The result is ",setBit(n,k))

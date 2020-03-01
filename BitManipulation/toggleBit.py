"""
    6: 1 1 0 =   1 1 0
    1 << k(1) :  0 1 0
                 1 0 0
    
"""
def toggleBit(n,k):

    a = n
    b = (1<<k)
    return a^b

n = int(input("Enter the number:\t"))
k = int(input("Enter the shifts:\t"))
print("The number is ",toggleBit(n,k))


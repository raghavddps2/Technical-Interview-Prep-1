def getSum(n):

    if n == 0:
        return 0
    else:
        return n + getSum(n-1)

n = int(input())
print(getSum(n))

def factorial(n):

    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

n = int(input())
print(factorial(n))

def exponentiation(a,b):

    if b == 0:
        return 1
    else:
        return a*exponentiation(a,b-1)

a = int(input())
b = int(input())
print(exponentiation(a,b))
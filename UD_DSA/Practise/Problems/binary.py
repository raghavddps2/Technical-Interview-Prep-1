def getBinary(n):

    if n == 1:
        return "1"
    result = ""
    while n != 1:
        res = n%2
        result = result + str(res)
        n = n//2
    result = result + "1"
    return result[::-1]

def countOf1(binaryRep):
    i = 0
    count = 0
    max1 = 0
    while i < len(binaryRep):
        if (binaryRep[i] == '1'):
            count = count + 1
        else:
            if count > max1:
                max1 = count
            count = 0
        i = i + 1
    if count > max1:
        max1 = count
    return max1

n = int(input())
print(getBinary(n))
print(countOf1(getBinary(n)))

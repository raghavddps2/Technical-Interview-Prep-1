def Anagram(a,b):

    a = set(a)
    b = set(b)

    if a == b:
        return True
    else:
        return False

def leftIndex(s):

    dict1 = {}
    for i in s:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] = dict1[i]+1
    for i in dict1:
        if dict1[i] == 2:
            return s.index(i)
    return -1

def leftIndex1(s):
    dict1 = {}
    for i in s:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] = dict1[i]+1
    
    a = min(dict1.values())
    if a <= 1:
        for i in dict1.keys():
            if(dict1[i] == 1):
                return s.index(i)
    return -1

# a = input()
# print(leftIndex(a))

# a = input()
# print(leftIndex1(a))

# s = input()
# p = input()
# print(Anagram(s,p))


def makeAnagram(a, b):

    dict1 = {}
    dict2 = {}
    for i in a:
        if i not in dict1:
            dict1[i] = 1
        else:
            dict1[i] = dict1[i]+1
    for i in b:
        if i not in dict2:
            dict2[i] = 1
        else:
            dict2[i] = dict2[i] + 1
    for i in dict1:
        if i in dict2:
            if(dict1[i] > dict2[i]):
                dict1[i] = dict1[i]-dict2[i]
                dict2[i] = 0
            elif(dict1[i] < dict2[i]):
                dict2[i] = dict2[i]-dict1[i]
                dict1[i] = 0
            else:
                dict2[i] = 0
                dict1[i] = 0
    
    a = sum(list(dict1.values()))
    b  = sum(list(dict2.values()))
    return (a+b)

a = input()
b = input()
print(makeAnagram(a,b))
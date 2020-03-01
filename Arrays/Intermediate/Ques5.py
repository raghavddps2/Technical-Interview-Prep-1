# Solving in O(n) only
from collections import OrderedDict
def printDuplicates(arr, n):
    dict1 = OrderedDict()
    flag = 0
    for i in arr:
        if(i in dict1.keys()):
            dict1[i] = dict1[i]+1
        else:
            dict1[i] = 1
    # print(dict1)
    for i in dict1.keys():
        if dict1[i] > 1:
            print(i,end=" ")
            flag = 1
    if(flag == 0):
        print("-1")


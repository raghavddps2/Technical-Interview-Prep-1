#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def minimumDistances(a):
    dict1 = {}
    minDistance = sys.maxsize
    # This approach is doing the task in O(n)
    for i in range(0,len(a)):
        if a[i] in dict1:
            if i-dict1[a[i]] < minDistance:
                minDistance = (i-dict1[a[i]])
            dict1[a[i]] = i
        else:
            dict1[a[i]] = i
    if minDistance == sys.maxsize:
        print(-1)
    else:
        print(minDistance)


if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    minimumDistances(a)

    
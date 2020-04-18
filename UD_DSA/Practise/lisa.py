#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the workbook function below.
def workbook(n, k, arr):
    no_of_pages = 0
    special_problem = 0
    for i in range(0,len(arr)):
        pages_in_chapter = math.ceil(arr[i]/k)
        lower_range = no_of_pages+1
        upper_range = no_of_pages + pages_in_chapter
        no_of_pages = no_of_pages + pages_in_chapter
        # print("start page: ",lower_range,"End page: ",upper_range)
        temp = min(arr[i],k)
        curr = arr[i]
        for j in range(lower_range,upper_range+1):
            if j <= temp and temp <=arr[i]:
                special_problem = special_problem + 1
                # print("Page  number: ",j)
            temp = temp + k
    # print(special_problem)
    return special_problem
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the strangeCounter function below.
def strangeCounter(n):
    t = 3
    ref_n = n
    t_pass = 0
    while n > t:
        n = n-t
        t_pass = t_pass + t
        t = t*2
    # print(n,t,t_pass)
    ans = t - (ref_n-t_pass)+1
    return ans
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    result = strangeCounter(t)
    print(result)
    # fptr.write(str(result) + '\n')

    # fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxScore' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER m
#

def maxScore(a, m):
    # Write your code here
    a.sort()
    ans = 0
    j = 0
    no_of_segments = (len(a)//m)
    for i in range(1,no_of_segments):
        ans = ans + i*sum(a[j:j+m])
        j = j + m
    ans = ans + no_of_segments*sum(a[j:])
    return ans%(1000000007)
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    a = list(map(int, input().rstrip().split()))

    ans = maxScore(a, m)
    print(ans)
    # fptr.write(str(ans) + '\n')

    # fptr.close()

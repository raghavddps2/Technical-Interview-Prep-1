#!/bin/python3

import math
import os
import random
import re
import sys

def getMaxHourglassSum(arr):

    hourglassSum = []
    for i in range(0,4):
        for j in range(0,4):
            hourglass = arr[i][j]+arr[i][j+1]+arr[i][j+2]+arr[i+1][j+1]+arr[i+2][j]+arr[i+2][j+1]+arr[i+2][j+2]
            hourglassSum.append(hourglass)
    return max(hourglassSum)
if __name__ == '__main__':
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0], [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0]]
    print(getMaxHourglassSum(arr))
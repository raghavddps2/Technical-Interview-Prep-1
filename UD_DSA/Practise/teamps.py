#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the acmTeam function below.
def acmTeam(topic):
    #Complexity foor this is O(n*n*k)
    dict1 = {}
    info = topic
    for i in range(0,len(info)):
        for j in range(i+1,len(info)):
            a = info[i]
            b = info[j]
            count = 0
            # print(a,b)
            for k in range(0,len(a)):
                if a[k] == '1' or  b[k] == '1':
                    count = count + 1
            # print(count)
            if count in dict1:
                dict1[count] = dict1[count]+1
            else:
                dict1[count] = 1
    # print(dict1)
    ans1 = max(dict1)
    ans2 = dict1[ans1]
    print(ans1)
    print(ans2)
if __name__ == '__main__':

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    topic = []

    for _ in range(n):
        topic_item = input()
        topic.append(topic_item)
    acmTeam(topic)

 

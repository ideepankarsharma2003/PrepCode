#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSort' function below.
#
# The function accepts 2D_STRING_ARRAY arr as parameter.
#


def countSort(arr):
    # Write your code here
    # print(arr)
    sort = ""
    # dict= {}
    # lmid= len(arr)//2
    # l= len(arr)
    # for i in range(lmid):
    #     arr[i][1]= '-'
    # # print(arr)
    # for i in range(l):
    #     x= arr[i][0]
    #     if x not in dict.keys():
    #         dict[x]= [arr[i][1]]
    #     else:
    #         dict[x].append(arr[i][1])
    #     # print(x)

    # # print(dict)
    # lsort= list(dict.keys())
    # lsort.sort()

    # for i in lsort:
    #     m= dict[i]
    #     for j in m:
    #         sort+=j+' '
    #         # sort+=j

    # sort= sort.strip()

    # print(sort)
    ta = [[] for x in range(len(arr))]
    # print(ta)

    for i in range(len(arr)):
        idx = int(arr[i][0])
        if i < len(arr)//2:
            ta[idx].append('-')
        else:
            ta[idx].append(arr[i][1])

    # print(ta)
    for i in ta:
        for j in i:
            sort += j+' '
    sort.strip()
    print(sort)
    # print(( ' '.join([' '.join(i) for i in ta])).strip())


if __name__ == '__main__':
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(input().rstrip().split())

    countSort(arr)

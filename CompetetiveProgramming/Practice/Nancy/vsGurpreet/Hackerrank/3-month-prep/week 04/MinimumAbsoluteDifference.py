#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumAbsoluteDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def minimumAbsoluteDifference(arr):
    # Write your code here
    minDiff = 1000000000
    # l=[]
    arr.sort()
    prev = 0
    for i in arr:
        if abs(i-prev) < minDiff:
            minDiff = abs(i-prev)
        prev = i
    # for i in arr:
    #     if i not in l:
    #         l.append(i)
    #     else:
    #         return 0
    # for i in range(len(l)):
    #     for j in l:
    #         if j!=l[i]:
    #             diff= l[i]-j
    #             if abs(diff)<minDiff:
    #                 minDiff= abs(diff)
    return minDiff


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'closestNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def closestNumbers(arr):
    # Write your code here
    arr.sort()
    minDiff = 10000000000000 # maximum possible difference
    a = []
    for i in range(len(arr)):
        abdiff = abs(arr[i]-arr[i-1])
        if abdiff < minDiff:
            minDiff = abdiff

    # for i in range(1, len(arr)):
    #     for j in arr[i:]:

    #         if abs(j-arr[i]) == minDiff:
    #             a.append(arr[i])
    #             a.append(j)

    for i in range(1, len(arr)):

        if abs(arr[i]-arr[i-1]) == minDiff:
            a.append(arr[i-1])
            a.append(arr[i])
    return a


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

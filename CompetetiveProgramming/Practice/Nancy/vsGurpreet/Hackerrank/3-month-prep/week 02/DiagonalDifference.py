#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(n, arr):
    # Write your code here
    lsum = 0
    rsum = 0
    for i in range(n):
        j = (n-1) - i
        lsum += arr[i][i]
        rsum += arr[i][j]

    return abs(lsum-rsum)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

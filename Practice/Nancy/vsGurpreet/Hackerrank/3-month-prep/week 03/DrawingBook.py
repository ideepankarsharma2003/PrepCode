#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pageCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER p
#


def pageCount(n, p):
    # Write your code here
    minflip = 0
    fflips = 0  # flips from start
    lflips = 0  # flips from end
    mid = int(n//2)
    if p <= mid:
        for i in range(1, mid, 2):
            l = [i, i-1]
            if p in l:
                break
            else:
                minflip += 1
    else:
        if n % 2 == 0:
            n += 1
        for i in range(n, mid, -2):
            l = [i, i-1]
            if p in l:
                break
            else:
                minflip += 1

    return minflip


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = int(input().strip())

    result = pageCount(n, p)

    fptr.write(str(result) + '\n')

    fptr.close()

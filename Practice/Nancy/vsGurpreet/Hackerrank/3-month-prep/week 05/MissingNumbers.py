#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#


def missingNumbers(arr, brr):
    # Write your code here
    dArr = {}
    dBrr = {}
    ans = []

    for i in arr:
        if i not in dArr.keys():
            dArr[i] = 1
        else:
            dArr[i] += 1

    for i in brr:
        if i not in dBrr.keys():
            dBrr[i] = 1
        else:
            dBrr[i] += 1

    la = list(dArr.keys())
    la.sort()
    lb = list(dBrr.keys())
    lb.sort()

    for i in lb:
        if i not in la:
            x = [i]*dBrr[i]
            ans += x
        else:
            # x= [i]*(dBrr[i]-dArr[i])
            if (dBrr[i]-dArr[i]) != 0:
                x = [i]
                ans += x

    return ans


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

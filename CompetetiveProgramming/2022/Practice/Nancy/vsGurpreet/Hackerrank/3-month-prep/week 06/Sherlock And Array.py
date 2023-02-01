#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'balancedSums' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def balancedSums(arr):
    # Write your code here
    str = 'NO'
    l = len(arr)
    if l == 1:
        return 'YES'
    la = 0
    ra = sum(arr[1:])
    for i in range(l-1):
        if la == ra:
            return 'YES'
        la += arr[i]
        ra -= arr[i+1]

    return str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()

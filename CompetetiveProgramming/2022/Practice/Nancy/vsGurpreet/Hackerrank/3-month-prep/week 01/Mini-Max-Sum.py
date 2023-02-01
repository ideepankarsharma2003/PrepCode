#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    # Write your code here
    # arr= list(arr)
    sumi = []
    for i in range(len(arr)):
        x = arr.copy()
        x.pop(i)
        # s= 0
        # for j in x:
        #     s+=j
        sumi.append(sum(x))
    return min(sumi), max(sumi)


if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    a, b = miniMaxSum(arr)
    print(a,  b)

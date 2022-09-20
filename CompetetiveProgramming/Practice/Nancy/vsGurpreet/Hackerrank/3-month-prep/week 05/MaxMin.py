#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#

def maxMin(k, arr):
    # Write your code here
    arr.sort()
    # print(arr)
    # minn= 10000
    l= len(arr)
    # for i in range(l-k+1):
        
    #     temp= arr[i:i+k]
    #     print(temp)
    #     diff= max(temp)- min(temp)
    #     # print(diff)
    #     if diff<minn:
    #         minn= diff
    diff= [arr[i+k-1]-arr[i] for i in range(l-k+1)]
    # # x= arr[k:]
    # return minn
    return min(diff)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

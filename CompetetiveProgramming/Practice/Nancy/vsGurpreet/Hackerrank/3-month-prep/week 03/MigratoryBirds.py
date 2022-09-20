#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    dict = {}
    for i in arr:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1

    # print(dict)

    max = -11111
    freq = -1
    l = list(dict.keys())
    l.sort()
    # print('l= ', l)
    for i in l:
        if dict[i] > max:
            freq = i
            max = dict[i]

    return freq


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()

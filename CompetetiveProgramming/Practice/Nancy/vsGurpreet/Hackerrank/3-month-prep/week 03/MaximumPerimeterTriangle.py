#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maximumPerimeterTriangle' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY sticks as parameter.
#


def maximumPerimeterTriangle(sticks):
    # Write your code here
    res = [-1]
    maxP = -1
    sticks.sort()
    l = len(sticks)
    for i in range(l):
        a = sticks[i]
        for j in range(i+1, l):
            b = sticks[j]

            for k in range(j+1, l):
                c = sticks[k]
                if (a+b) > c and (a+c) > b and (b+c) > a:
                    P = a+b+c
                    if P > maxP:
                        res = [a, b, c]

    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    sticks = list(map(int, input().rstrip().split()))

    result = maximumPerimeterTriangle(sticks)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

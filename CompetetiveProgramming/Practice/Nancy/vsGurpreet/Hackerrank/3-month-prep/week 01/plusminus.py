# https: // www.hackerrank.com/challenges/three-month-preparation-kit-plus-minus/problem?h_l = interview & isFullScreen = true & playlist_slugs % 5B % 5D = preparation-kits & playlist_slugs % 5B % 5D = three-month-preparation-kit & playlist_slugs % 5B % 5D = three-month-week-one

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    p = 0
    n = 0
    z = 0
    l = len(arr)
    x = []
    for i in arr:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    x.append(p/l)
    x.append(n/l)
    x.append(z/l)
    return x


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    x = plusMinus(arr)
    for i in x:
        print(i)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gamingArray' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def gamingArray(arr):
    # Write your code here
    count = 0
    while True:
        m = max(arr)
        idx = arr.index(m)
        arr = arr[:idx]
        # arr.remove(m)
        count += 1
        if len(arr) == 0:
            break

    if count % 2 == 0:
        return 'ANDY'
    else:
        return 'BOB'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        arr_count = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = gamingArray(arr)

        fptr.write(result + '\n')

    fptr.close()

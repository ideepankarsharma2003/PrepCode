#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    # Write your code here
    U = +1
    D = -1

    valleyCrossed = 0
    tpath = 0

    for step in path:
        prevStep = tpath
        if step == 'U':
            tpath += U
        elif step == 'D':
            tpath += D

        if prevStep < 0 and tpath == 0:
            valleyCrossed += 1

    return valleyCrossed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()

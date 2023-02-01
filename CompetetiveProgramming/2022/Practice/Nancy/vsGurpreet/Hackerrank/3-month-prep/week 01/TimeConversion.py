#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def timeConversion(s):
    # Write your code here
    h = (s[:2])
    x = s[-2:]
    date = s[:-2]

    if x[0] == 'A':
        if h == '12':
            h = '00'
    elif x[0] == 'P':
        h = int(h)
        if h != 12:
            h += 12
        h = str(h)
        if h == '24':
            h = '00'

    date = h+date[2:]

    return date


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

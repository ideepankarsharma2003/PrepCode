#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    b = bin(n) # convert to binary decimal string '0b.......'
    b = b[2:]
    length = len(b)
    diff = 32-length
    b = '0'*diff + b
    x = '0b'
    for i in b:
        if i == '1':
            x += '0'
        elif i == '0':
            x += '1'

    m = int(x, 2) # convert to decimal from binary string
    return m


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()

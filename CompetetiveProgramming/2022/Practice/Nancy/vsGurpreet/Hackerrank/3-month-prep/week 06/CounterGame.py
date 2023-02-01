#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'counterGame' function below.
#
# The function is expected to return a STRING.
# The function accepts LONG_INTEGER n as parameter.
#


def counterGame(n):
    # Write your code here
    turn = 0
    while n > 0:
        i = 1
        pow = 1
        while(True):
            pow = 2**i
            if pow == n:
                n /= 2
                break
            elif pow > n:
                n -= pow//2
                break
            i += 1

        turn += 1
        if n == 1:
            break

    if turn % 2 != 0:
        return 'Louise'
    else:
        return 'Richard'


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = counterGame(n)

        fptr.write(result + '\n')

    fptr.close()

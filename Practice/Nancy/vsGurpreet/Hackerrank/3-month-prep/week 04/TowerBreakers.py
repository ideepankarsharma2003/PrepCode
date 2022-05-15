#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def towerBreakers(n, m):
    # Write your code here
    win = 0
    # arr= [m]*n
    # n%2==0 means all moves of 'a' are repeated by 'b'
    # m==1 means all towers are of height 1, so 'a' couldn't even make the first move
    if n % 2 == 0 or m == 1:
        win = 2
    else:
        win = 1
    return win


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + '\n')

    fptr.close()

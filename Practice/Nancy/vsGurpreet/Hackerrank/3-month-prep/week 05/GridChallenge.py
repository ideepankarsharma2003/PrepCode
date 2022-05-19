#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    s = "YES"
    gDash = []
    for gr in grid:
        gr = gr.lower()
        l = [ord(x) for x in gr]
        l.sort()
        gDash.append(l)

    # print(gDash)

    p = [-1]*len(gDash[0])
    for i in range(len(gDash)):
        # p = gDash[i-1]
        # print(f'p= {p}')
        for j in range(len(gDash[i])):
            if gDash[i][j] >= p[j]:
                p[j] = gDash[i][j]
            else:
                return 'NO'

    return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + '\n')

    fptr.close()

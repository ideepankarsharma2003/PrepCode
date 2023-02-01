#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'formingMagicSquare' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY s as parameter.
#


def formingMagicSquare(s):
    # Write your code here
    # https://mindyourdecisions.com/blog/2015/11/08/how-many-3x3-magic-squares-are-there-sunday-puzzle/
    # record all the 8 possible squares :
    M = [[[8, 1, 6], [3, 5, 7], [4, 9, 2]],
         [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
         [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
         [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
         [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
         [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
         [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
         [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
         ]
    # calculate difference of each Matrix with s.
    # record the minimum differences/cost
    # return the minimum cost
    min_cost = sys.maxsize
    for i in range(len(M)):
        cost = 0
        for j in range(len(M[i])):
            for k in range(len(M[i][j])):
                cost += abs(M[i][j][k] - s[j][k])
        min_cost = min(min_cost, cost)
    return min_cost


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()

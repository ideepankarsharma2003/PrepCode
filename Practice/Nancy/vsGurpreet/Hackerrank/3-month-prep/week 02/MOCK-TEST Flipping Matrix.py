#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    maxSum = 0
    n = len(matrix[1])//2
    for i in range(n):
        for j in range(n):
            l = []
            l.append(matrix[i][j])  # current matrix
            l.append(matrix[2 * n - 1 - i][j])  # bottom left
            l.append(matrix[i][2 * n - 1 - j])  # top right
            l.append(matrix[2 * n - 1 - i][2 * n - 1 - j])  # bottom right

            maxv = max(l)
            #print(l)
            #print(max(l))

            maxSum += maxv

    return maxSum


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        fptr.write(str(result) + '\n')

    fptr.close()

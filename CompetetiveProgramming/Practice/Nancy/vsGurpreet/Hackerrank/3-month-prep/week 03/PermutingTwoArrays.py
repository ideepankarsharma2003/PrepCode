#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'twoArrays' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#  3. INTEGER_ARRAY B
#


def twoArrays(k, A, B):

    # Write your code here
    str = 'NO'
    A.sort()
    B.sort()
    ADash = []
    BDash = []

    dict = {}
    for i in B:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1

    for i in A:
        ADash.append(i)
        for j in B:
            if (i+j) >= k and dict[j] > 0:
                BDash.append(j)
                dict[j] -= 1
                break

    if len(ADash) == len(BDash):
        str = 'YES'

    return str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        A = list(map(int, input().rstrip().split()))

        B = list(map(int, input().rstrip().split()))

        result = twoArrays(k, A, B)

        fptr.write(result + '\n')

    fptr.close()

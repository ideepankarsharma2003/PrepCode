#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    s = 0
    # n = n*k
    # print(f'n= {n}, k= {k}')
    # while len(n)!=1:
    #     l= [int(i) for i in n]
    #     s= sum(l)
    #     # k-=1
    #     n= str(s)
    if len(n) == 1:
        s = int(n)
        return s
    else:
        # n= n*k
        x = [int(i) for i in n]
        s = sum(x)
        s *= k
        return superDigit(str(s), 1)
        # n= str(s)
        # if len(n)!=1:
        #     s= superDigit(n, 1)
    # print(f's={s}\n')
    # return s


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()

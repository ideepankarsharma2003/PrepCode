#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here

    '''
        EDGE CASES: If k>26
    '''
    while k > 26:
        k = k % 26
    sDash = ''
    l = [chr(x) for x in range(ord('a'), ord('z')+1)]
    lDash = l[k:]+l[:k]
    L = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    LDash = L[k:]+L[:k]

    for i in s:
        if i in l:
            index = l.index(i)
            sDash += lDash[index]
        elif i in L:
            index = L.index(i)
            sDash += LDash[index]
        else:
            sDash += i
    return sDash


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'separateNumbers' function below.
#
# The function accepts STRING s as parameter.
#


def separateNumbers(s):
    # Write your code here
    st = 'NO'
    l = len(s)
    # print(f'l= {l}')
    l2 = l//2
    for i in range(l2):
        # print(f'i= {i}')
        num = s[:i+1]
        num = int(num)
        # print(type(num))
        # print(f'num= {num}')
        # print(str(num))
        x = num
        beautyString = str(num)
        while len(beautyString) < len(s):
            x += 1
            beautyString += str(x)
            # print(f'beautyString= {beautyString}')

        if beautyString == s:
            st = 'YES ' + str(num)
            break
        # print()

    print(st)


if __name__ == '__main__':
    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        separateNumbers(s)

#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'anagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def anagram(s):
    # Write your code here

    l = len(s)
    if l % 2 != 0:
        return -1
    change = 0
    l = l//2
    sf = s[:l]
    sf = ''.join(sorted(sf))
    # print(f'sf= {sf}')
    sl = s[l:]
    sl = ''.join(sorted(sl))
    # print(f'sl= {sl}')
    change = 0

    dict = {}
    for i in sl:
        if i not in dict.keys():
            dict[i] = 1
        else:
            dict[i] += 1

    # print(f'dict= {dict}')

    for i in sf:
        if i in dict.keys() and dict[i] != 0:
            dict[i] -= 1
            # sl= sl.replace(i, '')
            # break
        # print(f'dict= {dict}')

    for i in dict.values():
        change += i
    return change


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()


# str= 'fdhlvosfpafhalll'

# print(anagram(str))
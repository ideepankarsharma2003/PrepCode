#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#
def checkPal(s):
    # l= [i for i in s]
    # z= l.copy()
    # z.reverse()
    if list(reversed(s)) == s:
        return True
    return False


def palindromeIndex(s):
    l = len(s)
    i = 0
    j = l-1
    while i < l:
        if s[i] != s[j]:
            break
        i += 1
        j -= 1

    # if palindrome !!!
    if i > j:
        return -1
        
    a = i+1
    b = j
    while a < j and b > i+1:
        if s[a] != s[b]:
            return j
        a += 1
        b -= 1
    return i
# def palindromeIndex(s):
#     # Write your code here
#     if checkPal(s):
#         return -1
#     # l= [i for i in s]
#     # lgt= len(l)
#     # for i in range(lgt):
#     #     m= l.copy()
#     #     m.pop(i)
#     #     # ldash= m.copy()
#     #     # ldash.reverse()
#     #     if checkPal(m):
#     #         return i
#     else:
#         for _ in range(1,(len(s)/2)+1):
#             if s[_-1]!= s[-_]:
#                 break
#         s1=s[:]
#         del s[_-1]
#         del s1[-_]
#         if list(reversed(s))==s:
#             return _-1
#         else:
#             return len(s)+1-_

#     # return -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

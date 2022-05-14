#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    a.sort()
    maxLen= 2
    dict= {}
    for i in a:
        if i not in dict.keys():
            dict[i]=1
        else:
            dict[i]+=1
    print(f'dict= {dict}')
    l= list(dict.keys())
    l.sort()
    print(f'l= {l}')
    for i in range(0, len(l)):
        sum=0
        if l[i]-l[i-1]==1:
            sum+=dict[l[i]]+dict[l[i-1]]
        else:
            sum+= dict[l[i]]
        # if l[i+1]-l[i]==1:
        #     sum+=dict[l[i+1]]
        if sum>maxLen:
            maxLen= sum
        
    return maxLen

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()

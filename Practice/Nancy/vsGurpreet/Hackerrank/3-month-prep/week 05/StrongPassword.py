#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumNumber' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING password
#

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    toAdd= 0
    a= [chr(x) for x in range(ord('a'), ord('z')+1)]
    A= [chr(x) for x in range(ord('A'), ord('Z')+1)]
    d= [str(x) for x in range(10)]
    sc= ['!','@','#','$','%','^','&','*','(',')','-','+']
    
        
    for i in range(n):
        if password[i] in a:
            break
        if i==n-1:
            toAdd+=1
        
    for i in range(n):
        if password[i] in A:
            break
        if i==n-1:
            toAdd+=1
        
    for i in range(n):
        if password[i] in d:
            break
        if i==n-1:
            toAdd+=1
        
    for i in range(n):
        if password[i] in sc:
            break
        if i==n-1:
            toAdd+=1
            
    if n+toAdd<6:
        toAdd+=6-(n+toAdd)
            
    return toAdd
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()

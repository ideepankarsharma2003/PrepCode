#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'marsExploration' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def marsExploration(s):
    # Write your code here
    # num_messages= len(s)//3
    # num_s_send= num_messages*2
    # num_o_send= num_messages
    # num_s_received= 0
    # num_o_received= 0
    # for i in s:
    #     if i=='S':
    #         num_s_received+=1
    #     elif i=='O':
    #         num_o_received+=1

    # changed= num_s_send-num_s_received + num_o_send-num_o_received
    changed = 0
    for i in range(0, len(s)-2, 3):
        message = s[i: i+3]
        if message[0] != 'S':
            changed += 1
        if message[1] != 'O':
            changed += 1
        if message[2] != 'S':
            changed += 1

    return changed


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = marsExploration(s)

    fptr.write(str(result) + '\n')

    fptr.close()

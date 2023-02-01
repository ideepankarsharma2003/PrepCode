#!/bin/python3

import math
import os
import random
import re
import sys
from functools import reduce

#
# Complete the 'misereNim' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY s as parameter.
#


def misereNim(s):
    # Write your code here
    if(max(s) == 1):
        return "First" if (len(s) % 2 == 0) else "Second"
    else:
        xor = reduce((lambda x, y: x ^ y), s)
        return "Second" if xor == 0 else "First"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        s = list(map(int, input().rstrip().split()))

        result = misereNim(s)

        fptr.write(result + '\n')

    fptr.close()

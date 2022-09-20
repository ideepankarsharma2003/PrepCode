#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#


def gradingStudents(grades):
    # Write your code here
    newGrades = []
    for grade in grades:
        if grade > 37:
            mo5 = grade # multiple of 5
            for i in range(5):
                if mo5 % 5 == 0:
                    break
                mo5 += 1
            if (mo5-grade) < 3:
                grade = mo5
        else:
            grade = grade
        newGrades.append(grade)
    return newGrades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

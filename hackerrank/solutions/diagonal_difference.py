#!/bin/python3
#
# Problem Author: vatsalchanana @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/diagonal-difference/problem
#
# Solution
#   - Author: Byung Il Choi (choi@byung.org)
#
import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(A):
    n = len(A)
    d1, d2 = 0, 0
    for i in range(n):
        d1 += A[i][i]
        d2 += A[i][-1-i]
    return abs(d2-d1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')
    fptr.close()

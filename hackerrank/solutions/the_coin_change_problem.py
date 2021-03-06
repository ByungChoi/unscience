#!/bin/python3
#
# Problem Author: alanl @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/coin-change/problem
#
# Solution
#   Author: Byung Il Choi (choi@byung.org)
#   Video : https://youtu.be/XR9m3FCF9rs
#
import math
import os
import random
import re
import sys

#
# Complete the 'getWays' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. LONG_INTEGER_ARRAY c
#
def getWays(n, C):
    m = len(C)
    M = [0] * (n+1)
    M[0] = 1

    for j in range(1, m+1):
        for i in range(C[j-1], n+1):
            M[i] += M[i-C[j-1]]
    return M[n]

def getWays_unoptimized(n, C):
    m = len(C)
    M = [*map(lambda x: [x]*(n+1), [0]*(m+1))]

    for j in range(m+1):
        M[j][0] = 1

    for j in range(1, m+1):
        for i in range(1, n+1):
            if j > 1:
                M[j][i] += M[j-1][i]
            if i >= C[j-1]:
                M[j][i] += M[j][i-C[j-1]]
    return M[m][n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])
    m = int(first_multiple_input[1])
    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)

    fptr.write(str(ways) + '\n')

    fptr.close()

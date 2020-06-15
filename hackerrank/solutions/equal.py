#!/bin/python3
#
# Problem Author: amititkgp @ hackerrank
#     Difficulty: Medium
#           link: https://www.hackerrank.com/challenges/equal/problem
#
# Solution
#   Author: Byung Il Choi (choi@byung.org)
#   Video : https://www.youtube.com/watch?v=BQ3wrdxgos8
import math
import os
import random
import re
import sys

infinity = float('inf')

# Complete the equal function below.
def f(A):
    """
    This is a space optimized version using DP.
    For a recursive version, check equal_recursive.py
    """
    n = len(A)
    p = min(A)
    M = [infinity]*5

    for m in range(5):
        l = 0
        for i in range(n):
            v = A[i] - p + m
            n5 = v//5
            n2  = v%5//2
            n1  = v%5%2
            l += n5+n2+n1
        M[m] = l
    return min(M)

def equal(A):
    return f(A)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

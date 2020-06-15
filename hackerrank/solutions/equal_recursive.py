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
sys.setrecursionlimit(10**6)

# Complete the equal function below.
def g(v):
    n5 = v//5
    n2 = v%5//2
    n1 = v%5%2
    return n5+n2+n1

def f(A, n, m, p):
    if m == 5: # base case
        return infinity

    i = n-1
    v = A[i] - p + m
    
    if i == 0: # base case
        return g(v)

    r = g(v) + f(A, n-1, m, p)

    if n == len(A):
        return min(r, f(A, n, m+1, p))

    return r

def equal(A):
    # initial call
    return f(A, len(A), 0, min(A))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

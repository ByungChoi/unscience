#!/bin/python3
#
# Problem Author: HackerRank @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/tutorial-intro/problem
#
# Solution:
#   Author: Byung Il Choi (choi@byung.org)
#
import math
import os
import random
import re
import sys

def f(A, v):
    n = len(A)
    s = 0
    while True:
        if n <= 1:
            return 0 if A[0] == v and s == 0 else -1
        m = n // 2
        if A[s+m] == v:
            return s+m
        elif A[s+m] > v:
            n = m
            continue
        else:
            s = s+m
            n -= m

# Complete the introTutorial function below.
def introTutorial(V, arr):
    return f(arr, V)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    V = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = introTutorial(V, arr)

    fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3
#
# Problem Author: amititkgp @ hackerrank
#     Difficulty: Medium
#           link: https://www.hackerrank.com/challenges/equal/problem
#
import math
import os
import random
import re
import sys

# Complete the equal function below.
def equal(A):
    # your solution

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + '\n')

    fptr.close()


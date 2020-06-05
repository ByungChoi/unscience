#!/bin/python3
#
# Problem Author: darkshadows @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/sherlock-and-array/problem
#
# Solution:
#   - Author: Byung Il Choi (choi@byung.org)
#   - Video : https://youtu.be/X9iYn955byY
import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(A):
    n = len(A)
    s = sum(A)
    l = 0
    for x, i in zip(A, range(n)):
        # r = s - x - l
        if s - x - l - l == 0:
            return True
        l += x
    return False

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(["NO", "YES"][result] + '\n')

    fptr.close()

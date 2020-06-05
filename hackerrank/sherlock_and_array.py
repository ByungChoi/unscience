#!/bin/python3
#
# Problem Author: darkshadows @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/sherlock-and-array/problem
#
import math
import os
import random
import re
import sys

# Complete the balancedSums function below.
def balancedSums(A):
    # your solution

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(["NO", "YES"][result] + '\n')

    fptr.close()

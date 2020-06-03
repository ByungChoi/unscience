#!/bin/python3
#
# Problem Author: MeHdi_KaZemI8 @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/largest-permutation/problem
#
import math
import os
import random
import re
import sys

# Complete the largestPermutation function below.
def largestPermutation(k, A):
    # write your solution here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    arr = list(map(int, input().rstrip().split()))
    result = largestPermutation(k, arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()

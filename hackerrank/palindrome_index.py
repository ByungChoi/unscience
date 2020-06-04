#!/bin/python3
#
# Problem Author: amititkgp @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/palindrome-index/problem
#
import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def palindromeIndex(A):
    # your solution

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

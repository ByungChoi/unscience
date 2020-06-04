#!/bin/python3
#
# Problem Author: amititkgp @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/palindrome-index/problem
#
# Solution:
#   - Author: Byung Il Choi (choi@byung.org)
#   - Video:  https://youtu.be/fDn7QGOWcYo
#
import math
import os
import random
import re
import sys

# Complete the palindromeIndex function below.
def is_palindrome(A):
    return A == A[::-1]

def palindromeIndex(A):
    l = len(A)
    if l <= 1:
        return -1
    n = l//2

    for i in range(n):
        if A[i] == A[-i-1]:
            continue
        if is_palindrome(A[i+1:l-i]):
            return i
        if is_palindrome(A[i:l-i-1]):
            return l-i-1
        return -1
    return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3
#
# Problem Author: MeHdi_KaZemI8 @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/largest-permutation/problem
#
# Solution:
#   - Author: Byung Il Choi (choi@byung.org)
#   - Video:  https://youtu.be/SPQHf3laXIc
#
import math
import os
import random
import re
import sys

def swap(i, j, A, I):
    s = A[i]
    d = A[j]
    I[s] = j
    I[d] = i
    A[i] = d
    A[j] = s

# Complete the largestPermutation function below.
def largestPermutation(k, A):
    if k == 0:
        return

    n = len(A)
    I = list(range(n+1))

    for e, i in zip(A, range(n)):
        I[e] = i

    i, e = 0, 0
    while i < k + e and i < n:
        if A[i] == n - i:
            e, i = e+1, i+1
            continue

        i_A = I[n-i]
        # swap A[i], A[i_A]
        swap(i, i_A, A, I)
        i += 1
    return A

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

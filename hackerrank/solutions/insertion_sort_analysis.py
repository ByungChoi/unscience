#!/bin/python3
#
# Problem Author: HackerRank @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/insertion-sort/problem
#
# Solution
#   Author: Byung Il Choi (choi@byung.org)
#   Video:  https://youtu.be/-POjTcjpjDc
#
import math
import os
import random
import re
import sys

def merge(A, s, m, t):
    r = 0
    i, j, k, u = 0, 0, s, m + 1

    A_1 = A[s:m+1].copy()
    A_2 = A[m+1:t+1].copy()

    while i < len(A_1) and j < len(A_2):
        if A_1[i] <= A_2[j]:
            A[k] = A_1[i]
            i,k = i+1, k+1
            continue

        r += len(A_1) - i #### only part needed for solving the problem
        #                 #### rest is same as merge-sort.

        A[k] = A_2[j]
        j,k = j+1, k+1

    while i < len(A_1):
        A[k] = A_1[i]
        i, k = i+1, k+1

    while j < len(A_2):
        A[k] = A_2[j]
        j, k = j+1, k+1

    return r

def msort(A):
    r = 0
    n = 1
    l = len(A)

    while n <= l:
        s = 0
        while s < l:
            m = s + n - 1
            t = s + 2 * n - 1

            if t >= l:
                t = l - 1

            if t > s:
                r += merge(A, s, m, t)
            s = s + n * 2
        n *= 2
    return r

# Complete the insertionSort function below.
def insertionSort(arr):
    return msort(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

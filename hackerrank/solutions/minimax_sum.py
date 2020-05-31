#!/bin/python3
#
# Problem Author: bishop15 @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/mini-max-sum/problem
#
# Solution
#   - Author: Byung Il Choi (choi@byung.org)
#   - Video : https://youtu.be/ghrRBxM2ixU
#
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(A):
    s = sum(A)
    return s - max(A), s - min(A)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    smin, smax = miniMaxSum(arr)
    print(smin, smax)

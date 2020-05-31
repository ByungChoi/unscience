#!/bin/python3
#
# Problem Author: bishop15 @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/mini-max-sum/problem
#
import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(A):
    # write your solution here

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    smin, smax = miniMaxSum(arr)
    print(smin, smax)

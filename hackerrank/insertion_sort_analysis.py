#!/bin/python3
#
# Problem Author: HackerRank @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/insertion-sort/problem
#
import math
import os
import random
import re
import sys

# Complete the insertionSort function below.
def insertionSort(arr):
    # your solution

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = insertionSort(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

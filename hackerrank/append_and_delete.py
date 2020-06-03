#!/bin/python3
#
# Problem Author: zemen @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/append-and-delete/problem
#
import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    # your code here.

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()

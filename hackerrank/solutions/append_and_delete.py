#!/bin/python3
#
# Problem Author: zemen @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/append-and-delete/problem
#
# Solution
#   - Author: Byung Il Choi (choi@byung.org)
#   - Video:  https://youtu.be/82ho9JGUMNw
#
import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    prefix = os.path.commonprefix([s,t])
    p = len(prefix)
    d = len(s) - p
    a = len(t) - p
    m = a + d
    e = k - m
    if e < 0:
        return "No"
    if e < 2 * p and e % 2 != 0:
        return "No"
    return "Yes"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    t = input()
    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')
    fptr.close()

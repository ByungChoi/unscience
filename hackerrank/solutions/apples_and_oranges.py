#!/bin/python3
#
# Problem Author: nabila_ahmed @ hackerrank
#     Difficulty: Easy
#           link: https://www.hackerrank.com/challenges/apple-and-orange/problem
#
# Solution
#   - Author: Byung Il Choi (choi@byung.org)
#
import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    u,v = s,t+1
    n_apples =  sum([a + d in range(u,v) for d in apples])
    n_oranges = sum([b + d in range(u,v) for d in oranges])
    return n_apples, n_oranges

if __name__ == '__main__':
    st = input().split()
    s  = int(st[0])
    t  = int(st[1])
    ab = input().split()
    a  = int(ab[0])
    b  = int(ab[1])
    mn = input().split()
    m  = int(mn[0])
    n  = int(mn[1])
    apples  = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))

    n1,n2 = countApplesAndOranges(s, t, a, b, apples, oranges)
    print(n1)
    print(n2)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isWinning' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING config
#

g = {}

def f(n):
    if n < 0:
        return -1
    if n not in g:
        h = set()
        h.add(f(n - 1))
        h.add(f(n - 2))
        for i in range(1, n // 2 + 1):
            h.add(f(i) ^ f(n - i - 1))
            h.add(f(i) ^ f(n - i - 2))
        i = 0
        while i in h:
            i += 1
        g[n] = i
    return g[n]

def isWinning(n, config):
    x = 0
    c = 0
    for i in config:
        if i == 'I':
            c += 1
        elif c:
            x ^= f(c)
            c = 0
    if c:
        x ^= f(c)
    return "WIN" if x else "LOSE"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        config = input()

        result = isWinning(n, config)

        fptr.write(result + '\n')

    fptr.close()
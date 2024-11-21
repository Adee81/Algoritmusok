#!/bin/python3

import math
import os
import random
import re
import sys

def countArray(n, k, x):
    MOD = 10**9 + 7
    endx = 1 if x == 1 else 0
    end = 0 if x == 1 else 1

    for i in range(2, n + 1):
        endx, end = end, (end * (k - 2) + endx * (k - 1)) % MOD

    return endx
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nkx = input().split()

    n = int(nkx[0])

    k = int(nkx[1])

    x = int(nkx[2])

    answer = countArray(n, k, x)

    fptr.write(str(answer) + '\n')

    fptr.close()

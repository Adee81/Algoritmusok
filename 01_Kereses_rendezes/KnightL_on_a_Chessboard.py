#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'knightlOnAChessboard' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts INTEGER n as parameter.
#

def knightlOnAChessboard(n):
    result = [[0] * (n - 1) for _ in range(n - 1)]
    
    for a in range(1, n):
        for b in range(1, n):
            queue = [(0, 0, 0)]
            visited = [[False] * n for _ in range(n)]
            visited[0][0] = True
            
            found = False
            
            while queue and not found:
                x, y, steps = queue.pop(0)
                
                if (x, y) == (n - 1, n - 1):
                    result[a - 1][b - 1] = steps
                    found = True
                    break
                
                moves = [
                    (x + a, y + b), (x + a, y - b), (x - a, y + b), (x - a, y - b),
                    (x + b, y + a), (x + b, y - a), (x - b, y + a), (x - b, y - a)
                ]
                
                for nx, ny in moves:
                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append((nx, ny, steps + 1))
            
            if not found:
                result[a - 1][b - 1] = -1
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = knightlOnAChessboard(n)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

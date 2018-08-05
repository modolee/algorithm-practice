#!/bin/python3

import math
import os
import random
import re
import sys


def dfs(grid, i, j):
    positions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

    if not (i in range(len(grid)) and j in range(len(grid[0]))):
        return 0
    if grid[i][j] == 0:
        return 0

    count = 1
    grid[i][j] = 0

    for pos in positions:
        count += dfs(grid, i + pos[0], j + pos[1])

    return count


# Complete the maxRegion function below.
def maxRegion(grid):
    max_count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                max_count = max(max_count, dfs(grid, i, j))
    return max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid)

    fptr.write(str(res) + '\n')

    fptr.close()

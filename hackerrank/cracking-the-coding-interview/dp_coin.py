#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the ways function below.
def ways(n, coins):
    change_way = [1] + [0] * n

    for coin in coins:
        if coin <= n:
            for j in range(0, n - coin + 1):
                change_way[coin + j] += change_way[j]
        else:
            break

    return change_way[n]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    coins = list(map(int, input().rstrip().split()))

    res = ways(n, coins)

    fptr.write(str(res) + '\n')

    fptr.close()

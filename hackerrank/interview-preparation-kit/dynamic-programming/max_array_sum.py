#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    max_arr = [0] * len(arr)

    max_arr[0] = arr[0]
    max_arr[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        max_arr[i] = max(max_arr[i - 1], max_arr[i - 2] + arr[i], arr[i])

    return max_arr[-1]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    min_abs = 2 * 10 ** 9 + 1
    arr.sort()

    for i in range(len(arr) - 1):
        abs_sub = abs(arr[i] - arr[i + 1])
        if abs_sub < min_abs:
            min_abs = abs_sub

    return min_abs


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the findLonely function below.
def findLonely(arr):
    flag = 0

    for val in arr:
        flag ^= (1 << val)

    return int(math.log(flag, 2))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = findLonely(arr)

    fptr.write(str(res) + '\n')

    fptr.close()

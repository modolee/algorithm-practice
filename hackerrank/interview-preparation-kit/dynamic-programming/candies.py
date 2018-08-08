#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the candies function below.
def candies(n, arr):
    if n == 1:
        return 1

    candie_dist = [1] + [0] * (n - 1)

    i = 1
    while i < n:
        if arr[i - 1] > arr[i]:
            j = i
            count = 1
            while j < n and arr[j - 1] > arr[j]:
                count += 1
                j += 1
            candie_dist[i - 1] = max(candie_dist[i - 1], count)

            if count > 2:
                while i < n and arr[i - 1] > arr[i]:
                    count -= 1
                    candie_dist[i] = count
                    i += 1
                continue
            else:
                candie_dist[i] = 1
        elif arr[i - 1] == arr[i]:
            candie_dist[i] = 1
        else:
            candie_dist[i] = candie_dist[i - 1] + 1

        i += 1

    return sum(candie_dist)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
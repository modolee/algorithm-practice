#!/bin/python3

import math
import os
import random
import re
import sys


def merge(left_arr, right_arr):
    result = []
    swaps = 0
    left_cur = 0
    right_cur = 0
    left_end = len(left_arr)
    right_end = len(right_arr)

    ra = result.append  # 이걸 추가해줘야 timeout 안 걸림

    while left_cur < left_end and right_cur < right_end:
        if left_arr[left_cur] <= right_arr[right_cur]:
            ra(left_arr[left_cur])
            left_cur += 1
        else:
            ra(right_arr[right_cur])
            right_cur += 1
            swaps += left_end - left_cur

    result += left_arr[left_cur:]
    result += right_arr[right_cur:]

    return result, swaps


# Complete the countInversions function below.
def mergeSort(arr):
    n = len(arr)
    if n <= 1:
        return arr, 0

    mid = n // 2
    left_result, left_swaps = mergeSort(arr[:mid])
    right_result, right_swaps = mergeSort(arr[mid:])
    result, swaps = merge(left_result, right_result)

    return result, left_swaps + right_swaps + swaps


def countInversions(arr):
    result, swaps = mergeSort(arr)
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result = countInversions(arr)

        fptr.write(str(result) + '\n')

    fptr.close()

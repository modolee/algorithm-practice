#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the luckBalance function below.
def luckBalance(k, contests):
    important_list = []
    unimportant_list = []

    for contest in contests:
        if contest[1]:
            important_list.append(contest[0])
        else:
            unimportant_list.append(contest[0])

    important_list.sort()

    must_win = len(important_list) - k
    if must_win > 0:
        must_lose_luck = sum(important_list[0:must_win])
    else:
        must_lose_luck = 0
    important_sum = sum(important_list)
    unimportant_sum = sum(unimportant_list)

    return unimportant_sum + important_sum - (must_lose_luck * 2)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
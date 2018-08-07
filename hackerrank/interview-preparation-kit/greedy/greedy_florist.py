#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the getMinimumCost function below.
def getMinimumCost(num_of_friends, flower_prices):
    total_price = 0
    remaining_flowers = len(flower_prices)
    multiple = 1
    start_idx = 0
    flower_prices.sort(reverse=True)

    while remaining_flowers > 0:
        if remaining_flowers > num_of_friends:
            total_price += sum(flower_prices[start_idx:start_idx + num_of_friends]) * multiple
            remaining_flowers -= num_of_friends
            start_idx += num_of_friends
        else:
            total_price += sum(flower_prices[start_idx:]) * multiple
            remaining_flowers = 0
        multiple += 1

    return total_price


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
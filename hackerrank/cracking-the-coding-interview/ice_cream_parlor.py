#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    dict = {}
    for idx, val in enumerate(cost):
        dict.setdefault(val, []).append(idx + 1)

    for ice_price in dict.keys():
        another_ice_price = money - ice_price
        if ice_price == another_ice_price:
            if len(dict[ice_price]) >= 2:
                print('{} {}'.format(dict[ice_price][0], dict[ice_price][1]))
                break
        else:
            if another_ice_price in dict.keys():
                for val in sorted(list([dict[ice_price][0], dict[another_ice_price][0]])):
                    print(val, end=' ')
                print('')
                break


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
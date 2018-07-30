#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    dictA = {}
    dictB = {}

    for ch in a:
        if ch in dictA:
            dictA[ch] += 1
        else:
            dictA[ch] = 1

    for ch in b:
        if ch in dictB:
            dictB[ch] += 1
        else:
            dictB[ch] = 1

    for ch, cnt in dictB.items():
        if ch in dictA:
            dictA[ch] = abs(dictA[ch] - cnt)
        else:
            dictA[ch] = cnt

    return sum(dictA.values())


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()

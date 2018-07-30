#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    mgzDict = {}
    for word in magazine:
        if word in mgzDict:
            mgzDict[word] += 1
        else:
            mgzDict[word] = 1

    for word in note:
        if word not in mgzDict or mgzDict[word] == 0:
            print("No")
            return False
        else:
            mgzDict[word] -= 1

    print("Yes")
    return True


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)

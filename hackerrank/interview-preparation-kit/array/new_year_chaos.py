#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumBribes function below.
# 정렬이 되었는지 파악해서 중간에 종료할 수 있어야 되는데,
# 그것을 isSwaped라는 변수를 통해서 j loop를 도는 동안
# swap이 일어나지 않았으면, 정렬 된 것이므로 그 때 loop를 빠져나간다.
def minimumBribes(q):
    minCount = 0
    n = len(q)
    isSwaped = False

    for i in range(n):
        diff = q[i] - (i + 1)
        if diff >= 3:
            print("Too chaotic")
            return False

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if q[j] > q[j + 1]:
                q[j], q[j + 1] = q[j + 1], q[j]
                isSwaped = True
                minCount += 1
        if isSwaped:
            isSwaped = False
        else:
            break

    print(minCount)
    return True


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
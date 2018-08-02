#!/bin/python3

import math
import os

# Complete the primality function below.
def primality(n):
    if n == 1:
        return "Not prime"
    else:
        cnt = 0
        i = 2
        while i <= math.sqrt(n) and cnt < 1:
            if n % i == 0:
                cnt += 1
                break
            i += 1
        if cnt > 0:
            return "Not prime"
        else:
            return "Prime"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    p = int(input())

    for p_itr in range(p):
        n = int(input())

        result = primality(n)

        fptr.write(result + '\n')

    fptr.close()
#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    count = 0
    str_dict = {}
    for length in range(1, len(s) + 1):
        for start_idx in range(len(s) - length + 1):
            sorted_str = ''.join(sorted(s[start_idx:start_idx + length]))
            str_dict[sorted_str] = str_dict.get(sorted_str, 0) + 1
    for key in str_dict:
        count += (str_dict[key] * (str_dict[key] - 1)) // 2
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()

#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the isValid function below.
def isValid(s):
    freq_dict = {}
    freq_of_freq_dict = {}

    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1

    for freq in freq_dict.values():
        freq_of_freq_dict[freq] = freq_of_freq_dict.get(freq, 0) + 1

    freq_keys = sorted(freq_of_freq_dict.keys())
    if len(freq_keys) == 1:
        return "YES"
    elif len(freq_keys) == 2:
        if (freq_keys[1] - freq_keys[0] == 1) and freq_of_freq_dict[freq_keys[1]] == 1:
            return "YES"
        elif freq_keys[0] == 1 and freq_of_freq_dict[freq_keys[0]] == 1:
            return "YES"
        else:
            return "NO"
    else:
        return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()

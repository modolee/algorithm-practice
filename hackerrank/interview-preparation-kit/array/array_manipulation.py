#!/bin/python3

import os

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    result = [0] * (n + 1)
    max_val = 0

    for query in queries:
        start = query[0]
        end = query[1]
        val = query[2]
        result[start] += val
        if end + 1 <= n:
            result[end + 1] -= val

    current = 0
    for i in range(1, n + 1):
        current += result[i]
        if current > max_val:
            max_val = current

    return max_val


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()

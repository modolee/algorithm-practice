from sys import stdin
import itertools

if __name__ == '__main__':
    n = int(stdin.readline())
    arr = list(range(1, n + 1))

    all_per = list(itertools.permutations(arr))

    for values in all_per:
        for val in values:
            print(val, end=' ')
        print('')
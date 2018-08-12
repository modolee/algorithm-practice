from sys import stdin
import itertools


class AllPermutations:
    def __init__(self, n):
        self.data_perm = list(itertools.permutations(list(range(1, n+1))))

    def findList(self, idx):
        return self.data_perm[idx-1]

    def findIndex(self, data_list):
        return self.data_perm.index(data_list) + 1


if __name__ == '__main__':
    n = int(stdin.readline())

    all_permutations = AllPermutations(n)

    line = list(map(int, stdin.readline().strip().split()))
    cmd = line[0]

    if cmd == 1:
        idx = line[1]
        arr = all_permutations.findList(idx)
        for val in arr:
            print(val, end=' ')
    elif cmd == 2:
        arr = tuple(line[1:])
        idx = all_permutations.findIndex(arr)
        print(idx)
from sys import stdin
import itertools

if __name__ == '__main__':
    max = 0
    n = int(stdin.readline())
    arr = list(map(int, stdin.readline().rstrip().split()))
    all_permutations = list(itertools.permutations(arr))

    for permutation in all_permutations:
        sum = 0
        for i in range(0, len(permutation)-1):
            sum += abs(permutation[i] - permutation[i+1])
            if sum > max:
                max = sum

    print(max)
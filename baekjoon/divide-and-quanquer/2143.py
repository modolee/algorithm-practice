from sys import stdin
from collections import defaultdict


if __name__ == '__main__':
    goal = int(stdin.readline().rstrip())
    num_of_a = int(stdin.readline().rstrip())
    list_a = list(map(int, stdin.readline().rstrip().split()))
    num_of_b = int(stdin.readline().rstrip())
    list_b = list(map(int, stdin.readline().rstrip().split()))

    map_a = defaultdict(lambda: 0)

    for i in range(len(list_a)):
        sub_sum = 0
        for j in range(i, len(list_a)):
            sub_sum += list_a[j]
            map_a[sub_sum] += 1

    result = 0
    for i in range(len(list_b)):
        sub_sum = 0
        for j in range(i, len(list_b)):
            sub_sum += list_b[j]
            if goal - sub_sum in map_a:
                result += map_a[goal - sub_sum]

    print(result)
from sys import stdin
import itertools

if __name__ == '__main__':
    n = int(stdin.readline())
    matrix = []
    for i in range(n):
       cost = list(map(int, stdin.readline().strip().split()))
       matrix.append(cost)

    min_cost = 10 ** 7 + 1
    all_permutations = itertools.permutations(list(range(1, n)))

    for permutation in all_permutations:
        sum = 0
        no_way = False

        # 0번 노드부터 시작
        if matrix[0][permutation[0]] == 0:
            continue
        else:
            sum += matrix[0][permutation[0]]

        # 구해 놓은 순열이 모두 연결되는지 확인
        for i in range(1, len(permutation)):
            if matrix[permutation[i-1]][permutation[i]] != 0:
                sum += matrix[permutation[i-1]][permutation[i]]
            else:
                no_way = True
                break

        # 순열이 모두 연결되고 다시 출발점으로 돌아갈 수 있는지 확인
        if no_way == False and matrix[permutation[-1]][0] != 0:
            sum += matrix[permutation[-1]][0]
            if sum < min_cost:
                min_cost = sum
        else:
            continue

    print(min_cost)
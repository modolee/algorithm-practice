from sys import stdin

def next_permutation(arr):
    i = len(arr) - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(arr) - 1
    while arr[j] <= arr[i-1]:
        j -= 1

    arr[j], arr[i-1] = arr[i-1], arr[j]

    j = len(arr) - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True

if __name__ == '__main__':
    n = int(stdin.readline())
    cost_matrix = []

    for i in range(n):
        cost = list(map(int, stdin.readline().rstrip().split()))
        cost_matrix.append(cost)

    route = list(range(1, n))
    min_cost = 10 ** 7 + 1

    while True:
        no_way = False
        cost_sum = 0

        for i in range(1, n-1):
            if cost_matrix[route[i-1]][route[i]] == 0:
                no_way = True
                break
            else:
                cost_sum += cost_matrix[route[i-1]][route[i]]

        if no_way is False and cost_matrix[0][route[0]] != 0 and cost_matrix[route[-1]][0] != 0:
            cost_sum = cost_sum + cost_matrix[0][route[0]] + cost_matrix[route[-1]][0]
            if min_cost > cost_sum:
                min_cost = cost_sum

        if next_permutation(route) is False:
            break

    print(min_cost)
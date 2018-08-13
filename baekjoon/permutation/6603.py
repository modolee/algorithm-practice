from sys import stdin

def next_permutation(arr):
    length = len(arr)

    i = length - 1
    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1

    if i == 0:
        return False

    j = length - 1
    while arr[i-1] >= arr[j]:
        j -= 1

    arr[j], arr[i-1] = arr[i-1], arr[j]

    j = length - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return True


if __name__ == '__main__':
    while True:
        line = list(map(int, stdin.readline().rstrip().split()))

        if line[0] == 0:
            break
        else:
            arr = line[1:]
            length = line[0]
            permutation = [0] * (length - 6) + [1] * 6
            result = []

            while True:
                combination = []
                for idx, val in enumerate(permutation):
                    if val == 1:
                        combination.append(arr[idx])
                result.append(combination)
                result.sort()

                if next_permutation(permutation) is False:
                    for comb in result:
                        for val in comb:
                            print(val, end=' ')
                        print('')
                    print('')
                    break

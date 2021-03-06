from sys import stdin

def nextPermutation(arr):
    length = len(arr)
    i = length - 1

    while i > 0 and arr[i-1] >= arr[i]:
        i -= 1

    if i <= 0:
        return True

    j = length - 1

    while arr[j] <= arr[i-1]:
        j -= 1

    arr[i-1], arr[j] = arr[j], arr[i-1]

    j = length - 1
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

    return False

if __name__ == '__main__':
    n = int(stdin.readline())
    arr = list(range(1, n+1))

    while True:
        for val in arr:
            print(val, end=' ')
        print('')
        if nextPermutation(arr):
            break
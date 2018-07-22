def solution(L, x):
    left = 0
    right = len(L) - 1
    while left <= right:
        index = (right + left) // 2
        if L[index] > x:
            right = index - 1
            continue
        elif L[index] < x:
            left = index + 1
            continue
        elif L[index] == x:
            return index

    return -1
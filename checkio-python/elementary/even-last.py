def checkio(array):
    sum = 0
    for i in range(0, len(array), 2):
        sum += array[i] * array[-1]

    return sum
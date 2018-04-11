def index_power(array, n):
    if len(array) < n + 1:
        return -1

    return array[n] ** n
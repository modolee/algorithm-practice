def solution(x):
    fibonacciArray = [0, 1]

    for i in range(2, x + 1):
        fibonacciArray.append(fibonacciArray[i - 1] + fibonacciArray[i - 2])

    return fibonacciArray[x]
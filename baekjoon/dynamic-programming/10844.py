from sys import stdin


if __name__ == '__main__':
    n = int(stdin.readline().strip())
    dp = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1], []]

    for i in range(1, n):
        temp = list()
        temp.append(dp[(i - 1) % 2][1])
        for j in range(1, 9):
            temp.append(dp[(i-1) % 2][j-1] + dp[(i-1) % 2][j+1])
        temp.append(dp[(i - 1) % 2][8])

        dp[i % 2] = temp.copy()

    print(sum(dp[(n-1) % 2]) % 1000000000)

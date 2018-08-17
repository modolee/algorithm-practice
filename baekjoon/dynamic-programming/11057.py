from sys import stdin

# 시간 복잡도 : O(N)
if __name__ == '__main__':
    mod = 10007
    n = int(stdin.readline().strip())
    dp = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], []]

    for i in range(1, n):
        temp = []
        for j in range(10):
            temp.append(sum(dp[(i-1) % 2][j:]) % mod)
        dp[i % 2] = temp.copy()

    print(sum(dp[(n-1) % 2]) % mod)
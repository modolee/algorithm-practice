from sys import stdin


# 시간 복잡도
# N개의 배열를 채워야 됨
# 1개의 배열을 채우는 시간 복잡도 : O(1)
# N개의 배열을 채우는 시간 복잡도 : O(N)
if __name__ == '__main__':
    n = int(stdin.readline().strip())
    dp = [0, 1, 1]

    for i in range(3, n+1):
        dp.append(dp[i-2] + dp[i-1])

    print(dp[n])
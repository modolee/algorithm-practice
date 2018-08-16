from sys import stdin


# 시간 복잡도
# DP를 이용해서 문제를 해결하였고,
# dp 배열을 채우는데 걸리는 시간 N 만큼에
# 각 한칸 마다 3번의 연산이 필요한데 O(1)이다.
# 그래서 O(N*1) = O(N) 이다.
if __name__ == '__main__':
    dp = [0] * 1000001
    start_number = int(stdin.readline().rstrip())
    dp[1] = 0

    for i in range(2, start_number+1):
        dp[i] = dp[i - 1] + 1
        if i % 3 == 0 and dp[i] > dp[i // 3] + 1:
            dp[i] = dp[i // 3] + 1
        if i % 2 == 0 and dp[i] > dp[i // 2] + 1:
            dp[i] = dp[i // 2] + 1

    print(dp[start_number])
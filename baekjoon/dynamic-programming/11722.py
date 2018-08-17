from sys import stdin


if __name__ == '__main__':
    num_of_digits = int(stdin.readline().strip())
    digits = list(map(int, stdin.readline().strip().split()))
    dp = [1] + [0] * (num_of_digits - 1)

    for i in range(1, num_of_digits):
        for j in range(i):
            if digits[i] < digits[j] and dp[i] < dp[j]:
                dp[i] = dp[j]
        dp[i] += 1

    print(max(dp))

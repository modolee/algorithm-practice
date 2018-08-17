from sys import stdin


if __name__ == '__main__':
    num_of_digits = int(stdin.readline().strip())
    digits = list(map(int, stdin.readline().strip().split()))
    dp = [digits[0]] + [0] * (num_of_digits - 1)

    for i in range(1, num_of_digits):
        dp[i] = max(dp[i - 1] + digits[i], digits[i])

    print(max(dp))
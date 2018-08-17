from sys import stdin


if __name__ == '__main__':
    num_of_digits = int(stdin.readline().strip())
    digits = list()
    for _ in range(num_of_digits):
        digits.append(int(stdin.readline().strip()))

    dp = [[0] * 2 for i in range(num_of_digits)]
    dp[0] = [digits[0]] * 2
    dp[1] = [digits[1], digits[0] + digits[1]]

    for i in range(1, num_of_digits):
        dp[i][0] = max(dp[i-2][0] + digits[i], dp[i-2][1] + digits[i])
        dp[i][1] = dp[i-1][0] + digits[i]

    print(max(dp[num_of_digits - 1]))
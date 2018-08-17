from sys import stdin


if __name__ == '__main__':
    num_of_wines = int(stdin.readline().strip())
    wines = list()

    for _ in range(num_of_wines):
        wines.append(int(stdin.readline().strip()))

    dp = [[0] + [wines[0]] * 2, []]

    for i in range(1, num_of_wines):
        prev_index = (i-1) % 2
        current_index = i % 2

        dp[current_index] = [max(dp[prev_index][0], dp[prev_index][1], dp[prev_index][2]),
                             dp[prev_index][0] + wines[i],
                             dp[prev_index][1] + wines[i]]

    print(max(dp[(num_of_wines - 1) % 2]))
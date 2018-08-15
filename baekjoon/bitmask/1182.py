from sys import stdin


if __name__ == '__main__':
    num_of_digits, goal = list(map(int, stdin.readline().rstrip().split()))
    digits_list = list(map(int, stdin.readline().rstrip().split()))
    count = 0

    # 시간 복잡도
    # 1 ~ 2^n - 1 까지 모든 경우의 수를 확인하며
    # n 개의 숫자라 포함되어 있는지 체크하기 때문에
    # O(n * 2^n) => n의 최대는 20이므로 20 * 2^20 = 20 * 1M 이다.
    # 0.1G는 넘기 않으므로 충분히 동작가능한 알고리즘이다.
    for i in range(1, 2 ** num_of_digits):
        sub_sum = 0
        for j in range(num_of_digits):
            if i & (1 << j) > 0:
                sub_sum += digits_list[j]

        if goal == sub_sum:
            count += 1

    print(count)
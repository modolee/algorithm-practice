from sys import stdin


if __name__ == '__main__':
    num_of_digits, goal = list(map(int, stdin.readline().rstrip().split()))
    digits = list(map(int, stdin.readline().rstrip().split()))
    left, right = 0, 0
    count = 0

    total = digits[0]
    while left <= right < len(digits):
        if total <= goal:
            if total == goal:
                count += 1

            if right + 1 < len(digits):
                right += 1
                total += digits[right]
            else:
                break
        else:
            total -= digits[left]
            left += 1
            if right < left < len(digits):
                right = left
                total = digits[left]

    print(count)
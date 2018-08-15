from sys import stdin


if __name__ == '__main__':
    num_of_digits, goal = list(map(int, stdin.readline().rstrip().split()))
    digits = list(map(int, stdin.readline().rstrip().split()))

    left, right, min_length = 0, 0, 100001
    total = digits[0]

    while True:
        if total < goal:
            right += 1
            if right < len(digits):
                total += digits[right]
            else:
                break
        elif total >= goal:
            if right == left:
                min_length = 1
                break
            min_length = min(min_length, right - left + 1)
            total -= digits[left]
            left += 1

    if min_length == 100001:
        print(0)
    else:
        print(min_length)

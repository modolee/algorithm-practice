from sys import stdin

# 시간 복잡도
# 첫번째 반복문이 N회
# 두번째 반복문이 각각 1 + 2 + ... + N/2 - 1 + N/2
# 총 반복 횟수는 N(N+1)/4 => O(N^2)

if __name__ == '__main__':
    num_of_digits = int(stdin.readline().strip())
    digits = list(map(int, stdin.readline().strip().split()))
    digits = [0] + digits

    for i in range(2, num_of_digits + 1):
        for j in range(1, i//2 + 1):
            if digits[i] < digits[i - j] + digits[j]:
                digits[i] = digits[i - j] + digits[j]

    print(digits[num_of_digits])
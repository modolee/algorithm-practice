from sys import stdin

if __name__ == '__main__':
    num_of_case = int(stdin.readline())

    num_of_methods = [0] * 11
    num_of_methods[1] = 1
    num_of_methods[2] = 2
    num_of_methods[3] = 4

    for i in range(4, 11):
        num_of_methods[i] = num_of_methods[i-3] + num_of_methods[i-2] + num_of_methods[i-1]

    for i in range(num_of_case):
        digit = int(stdin.readline())
        print(num_of_methods[digit])
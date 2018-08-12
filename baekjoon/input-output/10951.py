from sys import stdin

if __name__ == '__main__':
    for line in stdin:
        a, b = list(map(int, line.rstrip().split()))
        print(a + b)
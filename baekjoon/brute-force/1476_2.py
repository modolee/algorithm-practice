from sys import stdin

if __name__ == '__main__':
    earth, sun, moon = list(map(int, stdin.readline().strip().split()))
    e, s, m, year = 0, 0, 0, 1
    earth -= 1
    sun -= 1
    moon -= 1

    while True:
        if e == earth and s == sun and m == moon:
            print(year)
            break

        year += 1
        e = (e + 1) % 15
        s = (s + 1) % 28
        m = (m + 1) % 19
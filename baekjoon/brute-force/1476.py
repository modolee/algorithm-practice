from sys import stdin

if __name__ == '__main__':
    earth, sun, moon = list(map(int, stdin.readline().strip().split()))
    e, s, m, year = 1, 1, 1, 1
    while True:
        if e == earth and s == sun and m == moon:
            print(year)
            break

        year += 1
        e += 1
        s += 1
        m += 1

        if e == 16:
            e = 1
        if s == 29:
            s = 1
        if m == 20:
            m = 1
from sys import stdin

if __name__ == '__main__':
    data = 0
    n = int(stdin.readline())

    for i in range(n):
        line = stdin.readline().rstrip().split()
        cmd = line[0]

        if cmd != 'all' and cmd != 'empty':
            val = int(line[1]) - 1

        if cmd == 'add':
            data |= (1 << val)
        elif cmd == 'remove':
            data &= ~(1 << val)
        elif cmd == 'check':
            if data & (1 << val):
                print('1')
            else:
                print('0')
        elif cmd == 'toggle':
            data ^= (1 << val)
        elif cmd == 'all':
            data = 2 ** 20 - 1
        elif cmd == 'empty':
            data = 0
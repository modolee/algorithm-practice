from sys import stdin

if __name__ == '__main__':
    n = int(stdin.readline())
    visited = [False] * (n+1)
    fac = [0] * (n+1)
    line = list(map(int, stdin.readline().rstrip().split()))
    cmd = line[0]

    fac[0] = 1
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i

    if cmd == 1:
        idx = line[1]
        output_arr = []
        sum = 0

        for i in range(n):
            for j in range(1, n+1):
                if visited[j] is False:
                    if sum + fac[n - i - 1] >= idx:
                        output_arr.append(j)
                        visited[j] = True
                        break
                    else:
                        sum += fac[n - i - 1]

        for val in output_arr:
            print(val, end=' ')

    elif cmd == 2:
        input_arr = line[1:]
        idx = 0
        for i in range(n):
            for j in range(1, input_arr[i]):
                if visited[j] is False:
                    idx += fac[n - i - 1]
            visited[input_arr[i]] = True

        print(idx + 1)
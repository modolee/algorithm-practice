from sys import stdin
import itertools

if __name__ == '__main__':
    while True:
        line = list(map(int, stdin.readline().rstrip().split()))

        if line[0] == 0:
            break
        else:
            arr = line[1:]
            all_combinations = list(itertools.combinations(arr, 6))

            for combination in all_combinations:
                for val in combination:
                    print(val, end=' ')
                print('')
            print('')
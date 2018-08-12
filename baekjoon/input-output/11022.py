if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        input_val = list(map(int, input().rstrip().split()))
        print('Case #{}: {} + {} = {}'.format(i+1, input_val[0], input_val[1], input_val[0] + input_val[1]))
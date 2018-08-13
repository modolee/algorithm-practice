def eratosthenes(n):
    prime = [False] + [False] + [True] * (n - 1)
    sqrt_n = int(n**0.5)

    for i in range(2, sqrt_n+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False

    return prime

if __name__ == '__main__':
    is_prime = eratosthenes(10000)
    print(is_prime[10000])
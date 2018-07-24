import itertools

pool = ['A', 'B', 'C']
print(list(map(''.join, itertools.permutations(pool)))) # 3개의 원소로 수열 만들기
print(list(map(''.join, itertools.permutations(pool, 2)))) # 2개의 원소로 수열 만들기

print(list(map(''.join, itertools.combinations(pool, 3)))) # 3개의 원소로 조합 만들기
print(list(map(''.join, itertools.combinations(pool, 2)))) # 2개의 원소로 조합 만들기
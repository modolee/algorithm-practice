import itertools

input_str = 'ABC'

per = list(itertools.permutations(input_str))
print(per)

per2 = list(itertools.permutations(input_str, 2))
print(per2)

com = list(itertools.combinations(input_str, 3))
print(com)

com2 = list(itertools.combinations(input_str, 2))
print(com2)


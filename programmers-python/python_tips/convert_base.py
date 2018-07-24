num = '3212'
base = 5

answer = 0
for idx, i in enumerate(num[::-1]):
    answer += int(i) * ( base ** idx )

print(answer)

answer = int(num, base)

print(answer)
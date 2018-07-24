### 우측 정렬 예
s = 'abc'
n = 7

answer = ''
for i in range(n-len(s)): # 문자열의 앞을 빈 문자열로 채우는 for 문
    answer += ' '
answer += s

print(answer)

s = 'abc'
n = 7
print(s.ljust(n)) # 좌측 정렬
print(s.center(n)) # 우측 정렬
print(s.rjust(n)) # 가운데 정렬
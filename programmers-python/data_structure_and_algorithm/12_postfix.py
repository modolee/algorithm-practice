class ArrayStack:

    def __init__(self):
        self.data = []

    def size(self):
        return len(self.data)

    def isEmpty(self):
        return self.size() == 0

    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def peek(self):
        return self.data[-1]

prec = {
    '*': 3, '/': 3,
    '+': 2, '-': 2,
    '(': 1
}

def solution(S):
    opStack = ArrayStack()
    answer = ''
    # 한 문자씩 읽기
    for c in S :
        # 연산 부호인 경우
        if c in prec:
            # 스택이 비어 있지 않거나, (가 아닌 경우 우선 순위 비교가 필요
            if (not opStack.isEmpty()) and (c != '('):
                top = opStack.peek()
                if prec[c] <= prec[top]:
                    answer += opStack.pop()
            opStack.push(c)
        # )인 경우 (가 나올 때 까지 pop
        elif c == ')':
            while True:
                top = opStack.pop()
                if top == '(':
                    break
                else:
                    answer += top
        # 괄호, 연산 부호가 아닌 경우
        else:
            answer += c
    # 스택에 남아 있는 모든 연산 부호 pop
    while not opStack.isEmpty():
        answer += opStack.pop()

    return answer
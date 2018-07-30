class MyQueue(object):
    def __init__(self):
        self.pushStack = []
        self.popStack = []

    def peek(self):
        self.migration()
        return self.popStack[-1]

    def pop(self):
        self.migration()
        return self.popStack.pop()

    def put(self, value):
        self.pushStack.append(value)

    def migration(self):
        if len(self.popStack) == 0:
            while len(self.pushStack) > 0:
                self.popStack.append(self.pushStack.pop())


queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
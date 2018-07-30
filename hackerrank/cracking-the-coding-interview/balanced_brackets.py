#!/bin/python3

import math
import os
import random
import re
import sys


class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self):
        return self.data.pop()

    def peek(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return 'F'

    def isEmpty(self):
        return (True if len(self.data) == 0 else False)


if __name__ == '__main__':
    t = int(input())

    openBracket = '[{('
    closeBracket = ')}]'
    pairBracket = {']': '[',
                   '}': '{',
                   ')': '('}

    for t_itr in range(t):
        expression = input()

        bracketStack = Stack()

        for bracket in expression:
            if bracket in openBracket:
                bracketStack.push(bracket)
            elif bracket in closeBracket:
                if bracketStack.peek() == pairBracket[bracket]:
                    bracketStack.pop()
                else:
                    bracketStack.push(bracket)

        if bracketStack.isEmpty():
            print("YES")
        else:
            print("NO")
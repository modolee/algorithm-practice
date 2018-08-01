#!/bin/python3

import math
import os
import random
import re
import sys


class MinHeap:
    def __init__(self):
        self.data = []

    def getHeapSize(self):
        return len(self.data)

    def getLeftChildIdx(self, idx):
        return 2 * idx + 1

    def getRightChildIdx(self, idx):
        return 2 * idx + 2

    def getParentIdx(self, idx):
        return (idx - 1) // 2

    def hasLeftChild(self, idx):
        return self.getLeftChildIdx(idx) < self.getHeapSize()

    def hasRightChild(self, idx):
        return self.getRightChildIdx(idx) < self.getHeapSize()

    def hasParent(self, idx):
        return self.getParentIdx(idx) >= 0

    def leftChild(self, idx):
        return self.data[self.getLeftChildIdx(idx)]

    def rightChild(self, idx):
        return self.data[self.getRightChildIdx(idx)]

    def parent(self, idx):
        return self.data[self.getParentIdx(idx)]

    def peek(self):
        if self.getHeapSize() == 0:
            pass

        return self.data[0]

    def push(self, val):
        self.data.append(val)
        self.heapifyUp()

    def pop(self):
        if self.getHeapSize() == 0:
            pass

        minVal = self.data[0]
        self.data[0] = self.data[-1]
        del (self.data[-1])
        self.heapifyDown()
        return minVal

    def swap(self, idx1, idx2):
        self.data[idx1], self.data[idx2] = self.data[idx2], self.data[idx1]

    def heapifyDown(self):
        idx = 0
        while self.hasLeftChild(idx):
            smallerChildIdx = self.getLeftChildIdx(idx)
            if self.hasRightChild(idx) and (self.leftChild(idx) > self.rightChild(idx)):
                smallerChildIdx = self.getRightChildIdx(idx)

            if self.data[idx] < self.data[smallerChildIdx]:
                break
            else:
                self.swap(idx, smallerChildIdx)
                idx = smallerChildIdx

    def heapifyUp(self):
        idx = self.getHeapSize() - 1
        while self.hasParent(idx) and self.parent(idx) > self.data[idx]:
            self.swap(idx, self.getParentIdx(idx))
            idx = self.getParentIdx(idx)


if __name__ == '__main__':
    n = int(input())

    min_heap_for_bigger = MinHeap()
    max_heap_for_smaller = MinHeap()

    input_number = 0

    for _ in range(n):
        a_item = int(input())
        input_number += 1

        max_heap_for_smaller.push(-a_item)

        mid = 0
        if input_number % 2 == 0:
            while max_heap_for_smaller.getHeapSize() != min_heap_for_bigger.getHeapSize():
                min_heap_for_bigger.push(-max_heap_for_smaller.pop())
            mid = (min_heap_for_bigger.peek() - max_heap_for_smaller.peek()) / 2
        else:
            if input_number > 1 and -max_heap_for_smaller.peek() > min_heap_for_bigger.peek():
                min_heap_for_bigger.push(-max_heap_for_smaller.pop())
                max_heap_for_smaller.push(-min_heap_for_bigger.pop())
            mid = -max_heap_for_smaller.peek()

        print('%.1f' % mid)
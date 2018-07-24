class MaxHeap:

    def __init__(self):
        self.data = [None]

    def insert(self, item):
        self.data.append(item)
        index = len(self.data) - 1
        parent = index // 2

        while parent > 0 and self.data[parent] < self.data[index]:
            self.data[parent], self.data[index] = self.data[index], self.data[parent]
            index = parent
            parent = index // 2


def solution(x):
    return 0
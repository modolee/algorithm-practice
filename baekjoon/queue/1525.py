from sys import stdin


class Node:
    def __init__(self, data, height):
        self.data = data
        self.height = height

    def move(self, direction):
        if direction == 'u':
            if self.zero_index() >= 3:
                index = self.zero_index() - 3
            else:
                return -1
        elif direction == 'd':
            if self.zero_index() <= 5:
                index = self.zero_index() + 3
            else:
                return -1
        elif direction == 'l':
            if self.zero_index() % 3 != 0:
                index = self.zero_index() - 1
            else:
                return -1
        elif direction == 'r':
            if self.zero_index() % 3 != 2:
                index = self.zero_index() + 1
            else:
                return -1

        return index if 0 <= index <= 8 else -1

    def swap_with_zero(self, index):
        data_str = list(self.data)
        data_str[self.zero_index()], data_str[index] \
            = data_str[index], data_str[self.zero_index()]
        return ''.join(data_str)

    def zero_index(self):
        return self.data.index('0')


class BfsTree:
    def __init__(self, root_data):
        self.bfs_queue = []
        self.is_in_queue = set()
        self.enqueue(root_data, 0)

    def enqueue(self, data, height):
        node = Node(data, height)
        self.bfs_queue.append(node)
        self.is_in_queue.add(data)

    def dequeue(self):
        return self.bfs_queue.pop(0)

    def is_empty(self):
        return True if len(self.bfs_queue) == 0 else False


if __name__ == '__main__':
    dest = '123456780'
    input_arr = []
    for _ in range(3):
        input_arr += list(map(str, stdin.readline().rstrip().split()))

    src = ''.join(input_arr)
    bfs_tree = BfsTree(src)

    while True:
        current = bfs_tree.dequeue()

        if current.data == dest:
            print(current.height)
            break
        else:
            for direction in ['u', 'd', 'l', 'r']:
                move_index = current.move(direction)
                if move_index != -1:
                    next_str = current.swap_with_zero(move_index)
                    if next_str not in bfs_tree.is_in_queue:
                        bfs_tree.enqueue(next_str, current.height + 1)

        if bfs_tree.is_empty():
            print('-1')
            break

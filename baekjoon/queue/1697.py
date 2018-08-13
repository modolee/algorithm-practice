from sys import stdin

class Node:
    def __init__(self, data, height):
        self.data = data
        self.height = height


class Tree:
    def __init__(self, data):
        self.bfs_queue = []
        self.enqueued = [False] * 100001
        self.enqueue(data, 0)

    def enqueue(self, data, height):
        node = Node(data, height)
        self.bfs_queue.append(node)
        self.enqueued[data] = True

    def dequeue(self):
        return self.bfs_queue.pop(0)

    def is_enqueued(self, data):
        return self.enqueued[data]


def is_in_bound(data):
    if 0 <= data <= 200000:
        return True
    else:
        return False


if __name__ == '__main__':
    soobin, sister = list(map(int, stdin.readline().rstrip().split()))
    bfs_tree = Tree(soobin)

    while True:
        current = bfs_tree.dequeue()

        if current.data == sister:
            print(current.height)
            break
        else:
            height = current.height + 1
            prev_data = current.data - 1
            if is_in_bound(prev_data) and bfs_tree.is_enqueued(prev_data) is False:
                bfs_tree.enqueue(prev_data, height)

            next_data = current.data + 1
            if is_in_bound(next_data) and bfs_tree.is_enqueued(next_data) is False:
                bfs_tree.enqueue(next_data, height)

            doubled_data = current.data * 2
            if is_in_bound(doubled_data) and bfs_tree.is_enqueued(doubled_data) is False:
                bfs_tree.enqueue(doubled_data, height)
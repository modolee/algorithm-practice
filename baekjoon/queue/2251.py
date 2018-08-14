from sys import stdin


class Node:
    def __init__(self, data):
        self.data = data
        self.data_int = list(map(int, self.data.split('-')))

    def is_first_zero(self):
        return True if self.data_int[0] == 0 else False


class BfsTree:
    def __init__(self, root_data):
        self.bfs_queue = []
        self.used_set = set()
        self.enqueue(root_data)

    def enqueue(self, data):
        node = Node(data)
        self.bfs_queue.append(node)
        self.used_set.add(data)

    def dequeue(self):
        return self.bfs_queue.pop(0)

    def is_empty(self):
        return True if len(self.bfs_queue) == 0 else False


if __name__ == '__main__':
    cap = list(map(int, stdin.readline().rstrip().split()))
    bfs_tree = BfsTree('0-0-'+str(cap[2]))
    result = []

    while not bfs_tree.is_empty():
        current = bfs_tree.dequeue()

        if current.is_first_zero():
            result.append(current.data_int[2])

        for i in range(3):
            if current.data_int[i] != 0:
                for j in range(3):
                    if i != j:
                        next_state = current.data_int.copy()
                        next_state[j] = min(cap[j], current.data_int[j] + current.data_int[i])
                        next_state[i] = max(0, current.data_int[i] - (cap[j] - current.data_int[j]))
                        next_state_str = str(next_state[0]) + '-' + str(next_state[1]) + '-' + str(next_state[2])
                        if next_state_str not in bfs_tree.used_set:
                            bfs_tree.enqueue(next_state_str)

    result.sort()
    for val in result:
        print(val, end=' ')
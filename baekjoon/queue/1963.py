from sys import stdin

class Node:
    def __init__(self, data, height):
        self.data = data
        self.height = height


class BfsTree:
    def __init__(self, root_data):
        self.bfs_queue = []
        self.is_in_queue = [False] * 10000
        self.enqueue(root_data, 0)

    def enqueue(self, data, height):
        node = Node(data, height)
        self.bfs_queue.append(node)
        self.is_in_queue[data] = True

    def dequeue(self):
        return self.bfs_queue.pop(0)

    def is_empty(self):
        return True if len(self.bfs_queue) == 0 else False


def eratosthenes(n):
    prime = [False] + [False] + [True] * (n - 1)
    sqrt_n = int(n**0.5)

    for i in range(2, sqrt_n+1):
        if prime[i]:
            for j in range(i*i, n+1, i):
                prime[j] = False

    return prime


def is_possible(is_prime, data, idx, digit):
    data_str = list(str(data))
    data_str[idx] = str(digit)
    candidate_data = int(''.join(data_str))

    if candidate_data >= 1000 and is_prime[candidate_data]:
        return candidate_data
    else:
        return -1


if __name__ == '__main__':
    is_prime = eratosthenes(10000)
    n = int(stdin.readline())
    for i in range(n):
        src, dest = list(map(int, stdin.readline().strip().split()))

        bfs_tree = BfsTree(src)

        while True:
            current = bfs_tree.dequeue()

            if current.data == dest:
                print(current.height)
                break
            else:
                for idx in range(4):
                    for digit in range(10):
                        candidate = is_possible(is_prime, current.data, idx, digit)
                        if candidate != -1 and bfs_tree.is_in_queue[candidate] is False:
                            bfs_tree.enqueue(candidate, current.height+1)

            if bfs_tree.is_empty():
                print('Impossible')
                break

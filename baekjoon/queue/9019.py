from sys import stdin


class Node:
    def __init__(self, data, route):
        self.data = data
        self.route = route

    def cmd_d(self):
        return self.data*2 % 10000

    def cmd_s(self):
        return self.data - 1 if self.data != 0 else 9999

    def cmd_l(self):
        data_str = list(str(self.data))
        while len(data_str) < 4:
            data_str.insert(0, '0')
        data_str = data_str[1:] + [data_str[0]]
        data_int = int(''.join(data_str))
        return data_int

    def cmd_r(self):
        data_str = list(str(self.data))
        while len(data_str) < 4:
            data_str.insert(0, '0')
        data_str = [data_str[-1]] + data_str[:-2]
        data_int = int(''.join(data_str))
        return data_int


class BfsTree:
    def __init__(self, root_data):
        self.bfs_queue = []
        self.is_in_queue = [False] * 10000
        self.enqueue(root_data, '')

    def enqueue(self, data, route):
        node = Node(data, route)
        self.bfs_queue.append(node)
        self.is_in_queue[data] = True

    def dequeue(self):
        return self.bfs_queue.pop(0)

    def is_empty(self):
        return True if len(self.bfs_queue) == 0 else False


# BFS를 통한 최단거리 찾기
# 최대 0 ~ 9999까지 모두 검사하는 경우
# O(N)

if __name__ == '__main__':
    n = int(stdin.readline())
    for _ in range(n):
        src, dest = list(map(int, stdin.readline().rstrip().split()))
        bfs_tree = BfsTree(src)

        while True:
            current = bfs_tree.dequeue()
            if current.data == dest:
                print(current.route)
                break
            else:
                trans_data = current.cmd_d()
                if bfs_tree.is_in_queue[trans_data] is False:
                    bfs_tree.enqueue(trans_data, current.route + 'D')

                trans_data = current.cmd_s()
                if bfs_tree.is_in_queue[trans_data] is False:
                    bfs_tree.enqueue(trans_data, current.route + 'S')

                trans_data = current.cmd_l()
                if bfs_tree.is_in_queue[trans_data] is False:
                    bfs_tree.enqueue(trans_data, current.route + 'L')

                trans_data = current.cmd_r()
                if bfs_tree.is_in_queue[trans_data] is False:
                    bfs_tree.enqueue(trans_data, current.route + 'R')

            if bfs_tree.is_empty():
                break

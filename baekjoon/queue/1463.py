from sys import stdin


class Node:
    def __init__(self, data, height):
        self.data = data
        self.height = height


class BfsTree:
    def __init__(self, root_data):
        self.bfs_queue = []
        self.used_set = set()
        self.enqueue(root_data, 0)

    def enqueue(self, data, height):
        node = Node(data, height)
        self.bfs_queue.append(node)
        self.used_set.add(data)

    def dequeue(self):
        return self.bfs_queue.pop(0)

    def is_empty(self):
        return True if len(self.bfs_queue) == 0 else False


# 시간 복잡도
# 최대 입력으로 들어 오는 N개의 숫자를 모두 순회해야 되는 경우
# N번 반복문을 돌아야 되며, 각 반복문 마다 3세트의 연산과 비교(2번의 연산과 2번의 비교를 그리고 enqueue)를 해야 된다.
# 2번의 연산은 모두 O(1)이고, bfs_tree.used_set에 들어 있는지 비교하는 연산의 경우 set을 사용하여 역시 O(1)이다.
# enqueue의 경우에도 O(1)이므로 O(N * 1) 이므로 O(N)의 시간 복잡도를 갖는다.
if __name__ == '__main__':
    src_digit = int(stdin.readline().rstrip())

    bfs_tree = BfsTree(src_digit)
    min_count = 1000001

    while True:
        current = bfs_tree.dequeue()

        if current.data == 1:
            print(current.height)
            break
        else:
            check_data = current.data % 3
            input_data = current.data // 3
            if check_data == 0 and input_data not in bfs_tree.used_set:
                bfs_tree.enqueue(input_data, current.height + 1)

            check_data = current.data % 2
            input_data = current.data // 2
            if check_data == 0 and input_data not in bfs_tree.used_set:
                bfs_tree.enqueue(input_data, current.height + 1)

            check_data = current.data - 1
            if check_data >= 1 and check_data not in bfs_tree.used_set:
                bfs_tree.enqueue(check_data, current.height + 1)

        if bfs_tree.is_empty():
            break

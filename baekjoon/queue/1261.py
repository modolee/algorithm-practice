from sys import stdin


class Node:
    def __init__(self, row, col, destroyed):
        self.row = row
        self.col = col
        self.destroyed = destroyed


class BfsTree:
    def __init__(self, goal_row, goal_col):
        self.high_queue = []
        self.low_queue = []
        self.is_used = set()
        self.goal_row = goal_row
        self.goal_col = goal_col
        self.enqueue('H', 0, 0, 0)

    def enqueue(self, priority, row, col, destoryed):
        node = Node(row, col, destoryed)
        if priority == 'H':
            self.high_queue.append(node)
        elif priority == 'L':
            self.low_queue.append(node)
        self.is_used.add(str(row) + '-' + str(col))

    def dequeue(self):
        return self.high_queue.pop(0)

    def is_empty(self, priority):
        if priority == 'H':
            return True if len(self.high_queue) == 0 else False
        elif priority == 'L':
            return True if len(self.low_queue) == 0 else False

    def is_finished(self, node):
        if node.row == self.goal_row and node.col == self.goal_col:
            return True
        else:
            return False

    def swap_queues(self):
        self.high_queue, self.low_queue = self.low_queue, self.high_queue


def is_valid_pos(row, col, goal_row, goal_col):
    if 0 <= row <= goal_row and 0 <= col <= goal_col:
        return True
    else:
        return False


if __name__ == '__main__':
    # 상 하 좌 우 포지션별 행렬 좌표
    row_pos = [-1, 1, 0, 0]
    col_pos = [0, 0, -1, 1]

    goal_col, goal_row = list(map(int, stdin.readline().rstrip().split()))

    maze_map = []
    for _ in range(goal_row):
        maze_map.append(stdin.readline().rstrip())

    goal_col -= 1
    goal_row -= 1
    bfs_tree = BfsTree(goal_row, goal_col)

    while True:
        current = bfs_tree.dequeue()

        if bfs_tree.is_finished(current):
            print(current.destroyed)
            break

        for i in range(4):
            next_row = current.row + row_pos[i]
            next_col = current.col + col_pos[i]
            next_state = str(next_row) + '-' + str(next_col)

            if is_valid_pos(next_row, next_col, goal_row, goal_col) and next_state not in bfs_tree.is_used:
                if maze_map[next_row][next_col] == '1':
                    bfs_tree.enqueue('L', next_row, next_col, current.destroyed + 1)
                else:
                    bfs_tree.enqueue('H', next_row, next_col, current.destroyed)

        if bfs_tree.is_empty('H'):
            bfs_tree.swap_queues()

            if bfs_tree.is_empty('H'):
                break

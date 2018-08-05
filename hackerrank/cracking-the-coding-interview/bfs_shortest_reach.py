class Graph:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.edges = [[-1 for i in range(n)] for j in range(n)]

    def connect(self, x, y):
        self.edges[x][y] = 1
        self.edges[y][x] = 1

    def find_all_distances(self, start_node):
        distance = [-1] * self.num_of_nodes
        bfs_queue = [start_node]

        distance[start_node] = 0
        while len(bfs_queue) != 0:
            node = bfs_queue.pop()
            for i in range(self.num_of_nodes):
                if self.edges[node][i] == 1 and distance[i] == -1:
                    bfs_queue.insert(0, i)
                    distance[i] = distance[node] + 6

        for i in range(self.num_of_nodes):
            if i != start_node:
                print(distance[i], end=' ')

        print('')


t = int(input())
for i in range(t):
    n, m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x, y = [int(x) for x in input().split()]
        graph.connect(x - 1, y - 1)
    s = int(input())
    graph.find_all_distances(s - 1)
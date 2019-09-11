
import random
from collections import deque


class Graph(list):

    MAX_DIST = 100

    def __init__(self):
        super(Graph, self).__init__()
        self.n = 2

    def generate_matrix(self, sz):
        del self[:]
        self.n = sz
        line = []
        for i in range(self.n):
            line.append(0)
        for row in range(self.n):
            l0 = line[:]
            for col in range(row+1, self.n):
                if random.random() > .2:
                    l0[col] = 1 + int(random.random() * Graph.MAX_DIST)
                else:
                    l0[col] = None
            self.append(l0)
        for row in range(self.n):
            for col in range(self.n):
                if row != col:
                    self[col][row] = self[row][col]

    def edge(self, v1, v2):
        if v1 == v2:
            return None
        # use min and max python std funcs when fetching edge
        # to ensure we consistently pick edge from above main diagonal of graph matrix
        return self[min(v1, v2)][max(v1, v2)]

    def get_edges(self, v):
        edges = []
        for v1 in range(self.n):
            edge = self.edge(v1, v)
            if edge is not None:
                edges.append((v1, edge))
        return edges

    def find_paths_depth(self, v1, target):
        stack = []
        path = [v1]
        stack.append(path)
        paths = []
        while len(stack) > 0:
            path = stack.pop()
            if path[len(path)-1] == target:
                paths.append(path)
            #
            for edge in self.get_edges(path[len(path) - 1]):
                if edge[0] not in path:
                    new_path = path[:]                          # copy path as a new one
                    new_path.append(edge[0])                    # and add this edge to it
                    stack.append(new_path)                      # include new path in breadth search
        return paths

    def find_paths_breadth(self, v1, target):
        queue = deque([])
        path = [v1]
        queue.append(path)
        paths = []
        while len(queue) > 0:
            path = queue.popleft()
            if path[len(path)-1] == target:
                paths.append(path)
            #
            for edge in self.get_edges(path[len(path) - 1]):
                if edge[0] not in path:
                    new_path = path[:]                          # copy path as a new one
                    new_path.append(edge[0])                    # and add this edge to it
                    queue.append(new_path)                      # include new path in breadth search
        return paths

    def as_matrix(self):
        ret = ""
        for row in range(self.n):
            ret += ",\t".join([str(x) for x in self[row]]) + "\n"
        return "\n" + ret + "\n"

    def as_graph(self):
        s = "Edge notation: X:Y, where X = target vertex and Y = distance (weight of edge)\n"
        for v1 in range(self.n):
            s += "Vertex %d: edges = [" % (v1+1)
            edges = self.get_edges(v1)
            s += ", ".join(["%d:%d" % (v2+1, dist) for v2, dist in edges])
            s += "]\n"
        return s










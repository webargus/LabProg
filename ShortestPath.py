
"""
    UFRPE - BSI2019.2 - ILP - Homework 3
    Due date: 2019/09/13
    Description:
        Class to generate random matrix graph and apply DFS, BFS and recursive methods to
        find the shortest distance two different vertices
        HIGHLIGHTS:
        - Script takes advantage of idle matrix area below main diagonal to save shortest distance data
        - Search result reports include time in secs each search method takes for same search for comparison purposes
    Author:
        Edson Kropniczki - (c) sep/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you please;
        source code also publicly available at https://github.com/webargus/LabProg;
    Disclaimer:
        Use it at your own risk!

*******************************************************************************************************
"""

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
        # fill matrix nodes below main diagonal with None,
        # for we'll use this matrix area to save shortest distances between them
        for row in range(self.n):
            for col in range(row):
                self[row][col] = None

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

    def find_paths_recursive(self, v1, target, path=[]):
        path = path + [v1]
        # base case: we quit search when we hit our target
        if v1 == target:
            return [path]
        paths = []
        # scan through all edges to current vertex
        for edge in self.get_edges(v1):
            # if edge not in path then we didn't scan it yet
            if edge[0] not in path:
                pts = self.find_paths_recursive(edge[0], target, path)  # do search recursively until we hit our target
                for pt in pts:
                    paths.append(pt)
        return paths

    def calc_shortest(self, paths):
        d = self.calc_distance(paths[0])
        p = paths[0]
        for path in paths:
            dist = self.calc_distance(path)
            if dist < d:
                d = dist
                p = path
        return d, p

    def calc_distance(self, path):
        dist = 0
        for ix in range(len(path)-1):
            i = path[ix]
            j = path[ix+1]
            if i > j:
                (i, j) = (j, i)
            dist += self[i][j]
        # save shortest distance to matrix at position identified by first and last vertex of path,
        # which corresponds to origin and destination, respectively
        i = path[0]
        j = path[len(path) - 1]
        if i < j:                   # swap coords to ensure we save distance into matrix area below main diagonal
            (i, j) = (j, i)
        if (self[i][j] is None) or (self[i][j] > dist):
            self[i][j] = dist
        return dist

    def as_matrix(self):
        ret = ""
        for row in range(self.n):
            ret += ",\t".join([str(x) for x in self[row]]) + "\n"
        return ret

    def as_graph(self):
        s = ""
        for v1 in range(self.n):
            s += "Vertex %d: edges = [" % (v1+1)
            edges = self.get_edges(v1)
            s += ", ".join(["%d:%d" % (v2+1, dist) for v2, dist in edges])
            s += "]\n"
        return s










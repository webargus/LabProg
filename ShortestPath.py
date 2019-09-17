
"""
    UFRPE - BSI2019.2 - ILP - Homework 3
    Due date: 2019/09/20
    Description:
        Class to generate random matrix graph and apply Depth First Search (DFS), Breadth First Search (BFS)9+9
        Dijkstra algorithm and recursive methods to find the shortest distance between two different vertices
        HIGHLIGHTS:
        - Using matrices as a graph data structure should boost performance when handling large data sets
        - Script takes advantage of idle matrix area below main diagonal to save shortest distance data
        - Script uses matrix idle main diagonal to store distance values when finding shortest path with Dijkstra
        - Search result reports include elapsed time in secs each search method takes, for comparison
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

    MAX_DIST = 100                  # static max. distance between cities

    def __init__(self):
        super(Graph, self).__init__()
        self.n = 2

    # generate random square matrix of size sz
    def generate_matrix(self, sz):
        del self[:]
        self.n = sz
        line = []
        for i in range(self.n):
            line.append(None)
        for row in range(self.n):
            l0 = line[:]
            for col in range(row+1, self.n):
                if random.random() > .2:
                    l0[col] = 1 + int(random.random() * Graph.MAX_DIST)
                else:
                    l0[col] = None
            self.append(l0)
        # fill matrix nodes below main diagonal with None,
        # for we'll use this matrix area to save calculated shortest distances between cities
        # 'None' here stands for Dijkstra's algorithm infinity mark
        '''for row in range(self.n):
            for col in range(row):
                self[row][col] = None'''

    def edge(self, v1, v2):
        if v1 == v2:
            return None
        # use min and max python std funcs when fetching edge
        # to ensure we consistently pick edges exclusively from matrix area above main diagonal
        return self[min(v1, v2)][max(v1, v2)]

    def get_edges(self, v):
        edges = []
        for v1 in range(self.n):
            edge = self.edge(v1, v)
            if edge is not None:
                edges.append(v1)
        return edges

    def dijkstra(self, v1, target):
        # we'll save child-parent vertices as key-value pairs in the 'paths' dictionary as we move into the graph
        # in search of our target city, so that we'll be able to rebuild the full path from source to target later
        paths = {}
        # Fill in list with vertex ids, which is necessary to mark vertices as visited as we sift through graph;
        # we're going to mark visited nodes replacing them with 'None' instead of removing
        # them from list, which is a way more costly operation in python
        unvisited = [vertex for vertex in range(self.n)]
        # here we'll be saving Dijkstra's optimal distances along the matrix main diagonal,
        # so we make a proper use of that idle memory section
        for ix in range(self.n):
            self[ix][ix] = None         # a 'None' value here means infinity in our algorithm version
        # start by assigning 0 for the distance from start vertex
        self[v1][v1] = 0
        # set current city to start vertex
        current = v1
        while current is not None:
            # check each neighbor of current city
            for neighbor in self.get_edges(current):
                # update neighbor's distance from origin with the shortest distance to it so far
                # notice that None here stands for infinity
                dist_from_current = self[current][current] + self[min(neighbor, current)][max(neighbor, current)]
                if (self[neighbor][neighbor] is None) or (dist_from_current < self[neighbor][neighbor]):
                    self[neighbor][neighbor] = dist_from_current
                    paths[neighbor] = current
            # mark current node as visited (None) in unvisited list, for we won't visit it again
            unvisited[current] = None
            # abort when we hit the target city
            if current == target:
                break
            # before we loop back, take the next unvisited city with the shortest distance
            # so far from previous vertex, for our current city
            # break out if the shortest distance results infinite, which means that the city is unreachable
            shortest = None
            for x in unvisited:
                if x is None:               # city already visited
                    continue
                if self[x][x] is None:      # infinite distance
                    continue
                if (shortest is None) or (shortest > self[x][x]):
                    shortest = self[x][x]
                    current = x
            if shortest is None:
                break
        # redo shortest distance path from target to origin
        path = [target]
        if (len(paths) > 0) and (target in paths):
            parent = paths[target]
            while parent != v1:
                path.append(parent)
                parent = paths[parent]
            path.append(v1)
            path.reverse()              # reverse path so that it goes from source to target city
        return path

    # DFS, non-recursive method that returns all possible paths between 2 cities
    def find_paths_depth(self, v1, target):
        # create stack to accumulate search paths deeper into graph structure and initialize it with root city
        stack = []
        path = [v1]
        stack.append(path)
        paths = []                                              # list to accumulate paths to target
        while len(stack) > 0:                                   # repeat search until we visit all cities
            path = stack.pop()                                  # retrieve path on top of stack (deep search)
            if path[len(path)-1] == target:                     # save it if whenever we hit our target city
                paths.append(path)
            # move deeper into graph structure by adding paths to neighbor cities on top of search stack
            for edge in self.get_edges(path[len(path) - 1]):
                if edge not in path:
                    new_path = path[:]                          # copy path as a new one
                    new_path.append(edge)                    # and add this edge to it
                    stack.append(new_path)                      # add new path to the top of the depth search stack
        return paths

    def find_paths_breadth(self, v1, target):
        # create queue and initialize it with root city
        queue = deque([])
        path = [v1]
        queue.append(path)
        paths = []      # path accumulator
        # repeat search until there is no more cities to visit
        while len(queue) > 0:
            path = queue.popleft()                    # remove queue left-most path, as we're doing a breadth search
            if path[len(path)-1] == target:           # save path whenever we hit our target
                paths.append(path)
            # add new cities to visited paths and push them on top of queue for searching
            for edge in self.get_edges(path[len(path) - 1]):
                if edge not in path:
                    new_path = path[:]                          # copy path as a new one
                    new_path.append(edge)                    # and add this edge to it
                    queue.append(new_path)                      # include new path in breadth search
        return paths

    def find_paths_recursive(self, v1, target, path=[]):
        path = path + [v1]
        # base case: we quit searching when we hit our target
        if v1 == target:
            return [path]
        paths = []
        # scan through all edges to current vertex
        for edge in self.get_edges(v1):
            # if edge not in path then we didn't scan it yet
            if edge not in path:
                pts = self.find_paths_recursive(edge, target, path)  # do search recursively until we hit our target
                for pt in pts:
                    paths.append(pt)
        return paths

    def calc_shortest(self, paths):
        if len(paths) == 0:             # no paths found, abort
            return "Infinite", "No path available"
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
        # which corresponds to origin and destination cities, respectively
        i = path[0]
        j = path[len(path) - 1]
        if i < j:                   # swap coords to ensure we save distance into matrix area below main diagonal
            (i, j) = (j, i)
        if (self[i][j] is None) or (self[i][j] > dist):
            self[i][j] = dist
        return dist

    def as_matrix(self):                    # return graph in raw matrix format for printing
        s = ""
        for row in range(self.n):
            s += ",\t".join([str(x) for x in self[row]]) + "\n"
        return s

    # return graph in Vertex X: edges = [Y1:distance_, ..., Yn: distance_n] format for printing
    def as_graph(self):
        s = ""
        for v1 in range(self.n):
            edges = self.get_edges(v1)
            if len(edges) > 0:
                s += "Vertex %d: edges = [" % (v1+1)
                s += ", ".join(["%d:%d" % (v2+1, self[min(v1, v2)][max(v1, v2)]) for v2 in edges])
                s += "]\n"
        return s










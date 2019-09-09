
import random
"""
while 1:
    try:
        n = int(input("Enter number of cities:"))
        if (n < 2) or (n > 10000):
            raise ValueError
        else:
            break
    except ValueError:
        print("Invalid input")
"""

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

    # Recursive depth-first search of target vertex beginning at vertex v1
    def find_paths_depth(self, v1, target, path=[]):
        # print(v1, path)                   # debug
        path = path + [v1]
        # base case: we quit search when we hit our target
        if v1 == target:
            return [path]
        paths = []
        # print("paths=", paths)            # debug
        # scan through all edges to current vertex
        for edge in self.get_edges(v1):
            # if edge not in path then we didn't scan it yet
            if edge[0] not in path:
                pts = self.find_paths(edge[0], target, path)    # do search recursively until we hit our target
                for pt in pts:
                    paths.append(pt)
        return paths
    
    def find_paths_breadth(self, v1, target):
        for ix in range(self.n):
            self[ix][ix] = 0
        self[v1][v1] = 1
        stack = []
        path = [v1]
        stack.append(path)
        paths = []
        while len(stack) > 0:
            path = stack.pop()
            if path[len(path)-1] == target:
                paths.append(path)

            for edge in self.get_edges(path[len(path) - 1]):
                if edge[0] not in path:
                    new_path = path[:]
                    new_path.append(edge[0])
                    stack.append(new_path)
        return paths

    def __str__(self):
        ret = ""
        for row in range(self.n):
            ret += ", ".join(['{:<4}'.format(str(x)) for x in self[row]]) + "\n"
        return ret

    def as_graph(self):
        """s = ""
        for row in range(self.n-1):
            s += "vertex %d: edges = [" % (row+1)
            s += ", ".join([str(x) for x in
                            ["%d:%d" % (y+1, self[row][y]) for y in range(row+1, self.n) if self[row][y] is not None]])
            s += "]\n"

        s = ""
        for v1 in range(self.n):
            s += "Vertex %d: edges = [" % (v1+1)
            s += ", ".join(["%d:%d" % (v2+1, self[v1][v2]) for v2 in range(self.n) if self.edge(v1, v2) is not None])
            s += "]\n"
        """
        s = ""
        for v1 in range(self.n):
            s += "Vertex %d: edges = [" % (v1+1)
            edges = self.get_edges(v1)
            s += ", ".join(["%d:%d" % (v2+1, dist) for v2, dist in edges])
            s += "]\n"
        return s

"""
graph = Graph(n)
print(graph)
print(graph.as_graph())

while 1:
    try:
        source = int(input("Enter number of origin city (0=exit):"))
        if source == 0:
            exit(0)
        if (source < 1) or (source > n):
            raise ValueError
        dest = int(input("Enter number of destination city (0=exit):"))
        if dest == 0:
            exit(0)
        if dest == source:
            print("Destination city can't be the same as origin city")
            raise ValueError
        print("Depth first:")
        p = graph.find_paths(source - 1, dest - 1)
        s = "path: " + "\npath: ".join([" -> ".join([str(x+1) for x in pt]) for pt in p])
        print(s, "\n", "-"*30)
        print("Breadth first:")
        paths = graph.find_paths_breadth(source-1, dest-1)
        for path in paths:
            print(" -> ".join([str(x+1) for x in path]))
    except ValueError:
        print("Invalid input")
"""









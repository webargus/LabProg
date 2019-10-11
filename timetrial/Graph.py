"""
        Ancilary classes to resolve Graph problems
"""


class Node:

    def __init__(self, tag, data=None):
        self.tag = tag
        self.data = data
        self.visited = False
        self.edges = []

    def get_tag(self):
        return self.tag

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def is_visited(self):
        return self.visited

    def set_visited(self, flag=True):
        self.visited = flag

    def add_edge(self, other, weight):
        self.edges.append(self.Edge(other, weight))

    def get_edges(self):
        return self.edges

    def __eq__(self, other):
        return self.tag == other.get_tag()

    def __str__(self):
        s = "(Vertex: %s, Data: %s, " % (str(self.get_tag()), str(self.get_data()))
        s += "Edges: " + ", ".join([str(edge) for edge in self.edges]) + ")"
        return s

    class Edge:

        def __init__(self, node, weight=None):
            self.weight = weight
            self.other = node

        def __str__(self):
            return " -> %s, weight: %s" % (str(self.other.get_tag()), str(self.weight))

        def get_other(self):
            return self.other

        def get_weight(self):
            return self.weight

        def set_weight(self, weight):
            self.weight = weight


class Graph(list):

    INFINITE = float("inf")

    def __init__(self):
        super(Graph, self).__init__()

    def __str__(self):
        s = "V = {"
        s += ", ".join([str(v) for v in self])
        s += "}\n"
        return s

    def add_edge(self, n1, n2, weight=None):
        if n1 not in self:
            self.append(n1)
        if n2 not in self:
            self.append(n2)
        n1.add_edge(n2, weight)
        n2.add_edge(n1, weight)

    def dijkstra(self, v1, v2):
        for node in self:
            node.set_visited(False)                             # set all vertices as unvisited
            if node == v1:
                node.data = 0                                   # set min distance to start vertex = 0
            else:
                node.data = Graph.INFINITE                      # and distances to other vertices as infinite
        current = v1                                            # set current vertex to start vertex
        # repeat until there are no more unvisited vertices assigned with minimum distance less than infinite
        while current.get_data() < Graph.INFINITE:
            # get edges leaving current edge
            edges = current.get_edges()
            # loop over vertices connected to current one
            for edge in edges:
                node = edge.get_other()
                if node.is_visited():               # skip if connected vertex already visited
                    continue
                # calculate a tentative distance between current vertex and vertex connected to it by edge
                tentative_dist = current.get_data() + edge.weight
                # replace previous distance with tentative distance if the latter is less than previous
                if tentative_dist < node.get_data():
                    node.set_data(tentative_dist)
            # mark current vertex as visited after having visited all of other vertices connected to it
            current.set_visited()
            # abort when we reach our goal
            if current == v2:
                break
            current = Node(0, Graph.INFINITE)
            for node in self:
                if node.is_visited():
                    continue
                if node.get_data() < current.get_data():
                    current = node







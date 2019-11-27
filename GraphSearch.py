"""

recursive_dfs(g, u):
    rotule u como visitado
    para toda aresta de u até v, faça:
        se o vértice v não estiver rotulado como visitado, então:
            recursive_dfs(g, v)

interactive_dfs(g, origin):
    be S a stack
    s.pile(origin)
    while s is not empty:
        v = s.pop()
        if v is not labeled as visited, do:
            label v as visited
            for each u adjacent to v:
                s.pile(u)

interactive_bfs(g, origin):
    be Q a queue
    q.insert(origin)
    while q is not empty:
        u = q.remove()
        for each adjacent vertex v of u:
            if v is not visited:
                label v as visited
                q.insert(v)
"""


class QueueNode:

    def __init__(self, item):
        self.item = item
        self.next = self.prev = None

    def get_data(self):
        return self.item

    def set_data(self, item):
        self.item = item

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def get_prev(self):
        return self.prev

    def set_prev(self, node):
        self.prev = node


class ProgLabQueue:

    def __init__(self):
        self.init = self.end = None
        self.n = 0

    def push(self, item):
        node = QueueNode(item)
        self.n += 1
        if self.init is None:
            self.init = self.end = node
            return
        self.end.set_next(node)
        node.set_prev(self.end)
        self.end = node

    def pop(self):
        if self.init is None:
            raise IndexError
        self.n -= 1
        ret = self.end.get_data()
        if self.init == self.end:
            self.init = self.end = None
            return ret
        self.end = self.end.get_prev()
        self.end.set_next(None)
        return ret

    def unshift(self, data):
        node = QueueNode(data)
        self.n += 1
        if self.init is None:
            self.init = self.end = node
            return
        self.init.set_prev(node)
        node.set_next(self.init)
        self.init = node

    def shift(self):
        if self.init is None:
            raise IndexError
        self.n -= 1
        ret = self.init.get_data()
        if self.init == self.end:
            self.init = self.end = None
            return ret
        self.init = self.init.get_next()
        self.init.set_prev(None)
        return ret

    def __get_node_at(self, ix):
        if (ix < 0) or (ix >= self.n):
            raise IndexError
        i = 0
        node = self.init
        while i <= ix:
            if i == ix:
                return node
            i += 1
            node = node.get_next()

    def __getitem__(self, key):
        return self.__get_node_at(key).get_data()

    def __setitem__(self, key, item):
        self.__get_node_at(key).set_data(item)

    def has_item(self, item):
        node = self.init
        while node is not None:
            if node.get_data() == item:
                return node
            node = node.get_next()
        return None

    def __len__(self):
        return self.n

    def __str__(self):
        s = "["
        i = 0
        node = self.init
        while i < self.n:
            s += str(node.get_data())
            if i < self.n - 1:
                s += ", "
            node = node.get_next()
            i += 1
        return s + "]"


class GraphNode:

    def __init__(self, node_id):
        self.node_id = node_id              # save node id (label)
        self.edges = ProgLabQueue()         # create blank list of edges
        self.color = None                   # assign no color to vertex as default color

    # find degree of node
    @staticmethod
    def degree(self):
        return len(self.edges)

    # check if this node edges another
    def has_edge_to(self, other):            # other must be obj of type Node
        for edge in self.edges:
            if edge.n2 == other:
                return True
        return False

    # add edge to node
    def add_edge(self, other):              # other must be of type Node
        edge = self.Edge(self, other)
        if not self.edges.has_item(edge):
            self.edges.push(edge)
            other.add_edge(self)

    def __eq__(self, other):                # other must be of type Node
        return self.node_id == other.node_id

    def __str__(self):
        s = "[node id: %s, " % self.node_id
        s += "edges: %s, " % self.edges
        s += "]"
        return s

    # Nested class Edge to construct (bidirectional) edge objects between Node instances
    class Edge:

        def __init__(self, n1, n2):     # n1, n2 are Node objects
            self.n1 = n1
            self.n2 = n2

        def __eq__(self, other):
            return (self.n1 == other.n1) and (self.n2 == other.n2)

        def __str__(self):
            return "%s -> %s" % (self.n1.node_id, self.n2.node_id)


class Graph:

    def __init__(self):
        self.nodes = ProgLabQueue()

    def add_node(self, node):
        self.nodes.push(node)


graph = Graph()
node1 = GraphNode(1)
node2 = GraphNode(2)
node3 = GraphNode(3)
node4 = GraphNode(4)

node1.add_edge(node2)
node2.add_edge(node3)
node3.add_edge(node1)
node3.add_edge(node4)

graph.add_node(node1)
graph.add_node(node2)
graph.add_node(node3)
graph.add_node(node4)

print(graph.nodes)

















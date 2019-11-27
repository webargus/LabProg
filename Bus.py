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

    def __iter__(self):
        node = self.init
        while node is not None:
            yield node.get_data()
            node = node.get_next()

    def push(self, item):
        node = QueueNode(item)
        if self.init is None:
            self.init = self.end = node
            return
        self.end.set_next(node)
        node.set_prev(self.end)
        self.end = node

    def pop(self):
        if self.init is None:
            raise IndexError
        ret = self.end.get_data()
        if self.init == self.end:
            self.init = self.end = None
            return ret
        self.end = self.end.get_prev()
        self.end.set_next(None)
        return ret

    def is_empty(self):
        return self.init is None

    def __str__(self):
        s = "["
        node = self.init
        while node is not None:
            s += str(node.get_data()) + ", "
            node = node.get_next()
        return s + "]"


"""
4 2 4
1 2
2 3
3 4

16 2 12
3 5
12 3
5 1
2 1
4 1
6 1
7 1
12 8
12 9
12 10
12 11
3 13
13 14
15 13
15 16
"""

INFINITE = float("inf")                     # set infinite as python's greatest integer (we'll be using dijkstra)

# input no. of cities (vertices), origin and destination (@dest) cities
n, origin, dest = (int(x) for x in input().split())

# create STATIC python list for graph:
edges = [0 for x in range(n)]
# create STATIC python list to track visited vertices
visited = [False for x in range(n)]
# create STATIC python list to save shortest distances from origin city to destination cities
distances = [INFINITE for x in range(n)]
# Input graph, where the i-th position in the list corresponds to vertex-i
# and its value (edges[i]) equals the vertex that vertex-i is edged to
# (we're assuming that two cities are always connected by only one edge, according to problem premises)
for i in range(n-1):
    c1, c2 = (int(x) for x in input().split())
    if edges[c1-1] == 0:
        edges[c1-1] = c2
    else:
        edges[c2-1] = c1


# ancillary function to get all vertices of graph that have an edge to edge @u
def get_edges(u):
    ret = []
    for v in range(n):
        if edges[v] == u:
            ret.append(v+1)
    if edges[u-1] != 0:
        ret.append(edges[u-1])
    return ret


# dijkstra algorithm implementation on graph (@edges):
u = origin                      # set start vertex to origin
distances[u-1] = 0              # and make the distance to itself zero
while 1:
    visited[u-1] = True                         # set vertex as visited
    edges_to_u = get_edges(u)            # get vertices that have an edge with u
    for v in edges_to_u:                        # loop over each adjacent vertex v of u
        # here we set the distance between any neighbor city of u and u as constant 1,
        # for we just want to count the no. of buses we'll take to reach next city
        dist_from_u = distances[u-1] + 1
        if dist_from_u < distances[v-1]:        # replace previous distance to v, if we found a shorter path
            distances[v-1] = dist_from_u
    if u == dest:                               # print out answer and abort when we reach our destination
        print(distances[u-1])
        break
    # set the next city to visit (u) as the one with the shortest distance to u so far
    # abort if we visited all cities or if remaining vertices unreachable
    shortest_distance = INFINITE
    for v in range(n):
        if visited[v]:
            continue
        if distances[v] < shortest_distance:
            shortest_distance = distances[v]
            u = v + 1
    if shortest_distance == INFINITE:
        break








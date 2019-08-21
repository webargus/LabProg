
"""
    UFRPE - BSI2019.1 - Matemática Discreta - Trabalho 2 - 2ª VA
    Dupla:
        Edson Kropniczki + Cristina Oliveira
    Descrição:
        classes para a implementação do algoritmo de Dijkstra,
        para cálculo da menor distância entre dois vértices de um grafo simples não-direcional

    Algoritmo:
        fonte: Wikipedia
        URL  : https://en.wikipedia.org/wiki/Dijkstra's_algorithm

    Pseudo-código para determinar a menor distância entre source e target:

    function Dijkstra(Graph, source, target):

        create vertex set Q

        for each vertex v in Graph:
            dist[v] ← INFINITY
            prev[v] ← UNDEFINED
            add v to Q
        dist[source] ← 0

        while Q is not empty:

            u ← vertex in Q with min dist[u]

            remove u from Q
            if u = target:
                break

            for each neighbor v of u:           // only v that are still in Q
                alt ← dist[u] + length(u, v)
                if alt < dist[v]:
                dist[v] ← alt
                prev[v] ← u

        return dist[], prev[]

    // pseudo-código p/ refazer o caminho reverso

    function reverse_path(prev, source, target):
        S ← empty sequence
        u ← target
        if prev[u] is defined or u = source:      // Do something only if the vertex is reachable
        while u is defined:                       // Construct the shortest path with a stack S
            insert u at the beginning of S        // Push the vertex onto the stack
            u ← prev[u]                           // Traverse from target to source
"""


#  Classes Node/Edge para a construção de grafos na GUI e para uso no algoritmo de Dijkstra
class Node:

    def __init__(self, node_id):
        self.node_id = node_id              # save node id (label)
        self.edges = []                     # create blank list of edges

    # check if edge exists in this node
    def _has_edge(self, edge):
        return edge in self.edges

    # add edge to node
    def add_edge(self, other, dist):
        edge = self.Edge(self, other, dist)
        if not self._has_edge(edge):
            self.edges.append(edge)
            other.add_edge(self, dist)

    # return Edge obj between this Node and @other, if any
    def get_edge(self, other):
        for edge in self.edges:
            if edge.n2 == other:
                return edge
        return None

    # minimum overload to make Node objects hashable, so that we can use them as dictionary keys
    # in Wikipedia Dijkstra algorithm
    def __hash__(self):
        return hash(self.node_id)

    def __eq__(self, other):
        return (self.node_id == other.node_id) and (self.edges == other.edges)

    def __ne__(self, other):
        return not(self == other)

    # Nested class Edge to construct tagged edge objects between Node instances
    class Edge:

        def __init__(self, n1, n2, dist):
            self.n1 = n1
            self.n2 = n2
            self.dist = dist

        def __eq__(self, other):
            return (self.n1 == other.n1) and (self.n2 == other.n2) and (self.dist == other.dist)

        def __lt__(self, other):
            return self.dist < other.dist















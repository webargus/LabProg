
"""
    UFRPE - BSI2019.2 - ILP - Homework 2
    Due date: 2019/09/06
    Description: Graph + Node + Edge classes to build and color user-defined map
    ***************************************************************************************************
             Core algorithm of exercise: please, refer to the Welsh-Powell coloring algorithm
             implemented in method 'assign_colors' of  class 'Graph' below!
    ***************************************************************************************************
    Author:
        Edson Kropniczki - (c) sep/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you please;
        source code also publicly available at https://github.com/webargus/LabProg;
    Disclaimer:
        Use it at your own risk!

*******************************************************************************************************
    Web resources:
        https://iq.opengenus.org/welsh-powell-algorithm
        https://www.slideshare.net/PriyankJain26/graph-coloring-48222920
        https://en.wikipedia.org/wiki/Four_color_theorem
        https://en.wikipedia.org/wiki/Graph_coloring#Algorithms
        https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
        http://www.dharwadker.org/vertex_coloring/
"""


class Graph(list):

    # static color palette to paint graph vertices (nodes)
    COLORS = ["yellow", "green", "blue", "orange", "red", "cyan", "magenta"]

    def __init__(self):
        super(Graph, self).__init__()

    ########################################################
    #
    #               Welsh-Powell algorithm
    #
    ########################################################
    def assign_colors(self):

        # sort graph nodes in descending order from highest to lowest degree
        self.sort(key=Node.degree, reverse=True)

        # assign colors to nodes
        color_ix = 0
        for node0 in self:
            # go fetch next node from ordered graph if current node (node0) already colored before
            if node0.color is not None:
                continue
            # select next color in palette and assign it to current node
            color = self.COLORS[color_ix]
            node0.color = color
            color_ix += 1
            # Welsh-Powell algorithm key premises:
            # Paint with current color all uncolored nodes that have no edge to current node
            # and which in turn have no edge to any other node colored with current color.
            # Scan graph for prospect nodes that might meet key premises above:
            for node1 in self:
                # skip this prospect node if node already colored before,
                # or when we happen to be scanning current node or when prospect node has edges to it,
                # or when there is some other node edging to prospect node, which has been
                # already colored with current color
                if (node1.color is not None) or (node1 == node0) or \
                        node0.has_edge_to(node1) or self._has_edge_to_node_with_color(node1, color):
                    continue
                # once our prospect node has met all premises, we can safely color it
                node1.color = color
        return color_ix         # return no. of colors used to color graph

    def _has_edge_to_node_with_color(self, node, color):
        for n in self:
            # check if color matches first and check edges only if color matches, for optimization in 'and' clause
            if n.color == color and n.has_edge_to(node):
                return True
        return False


class Node:

    def __init__(self, node_id):
        self.node_id = node_id              # save node id (label)
        self.edges = []                     # create blank list of edges
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
        if edge not in self.edges:
            self.edges.append(edge)
            other.add_edge(self)

    def __eq__(self, other):                # other must be of type Node
        return self.node_id == other.node_id

    # Nested class Edge to construct (bidirectional) edge objects between Node instances
    class Edge:

        def __init__(self, n1, n2):     # n1, n2 are Node objects
            self.n1 = n1
            self.n2 = n2

        def __eq__(self, other):
            return (self.n1 == other.n1) and (self.n2 == other.n2)


















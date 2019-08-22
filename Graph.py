
"""
    UFRPE - BSI2019.2 - ILP - Homework 1
    Due date: 2019/08/23
    Description: Graph + Node + Edge classes
    Author:
        Edson Kropniczki - (c) aug/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you please;
        source code also publicly available at https://github.com/webargus/LabProg;
        actually, accretions and improvements are more than welcome! :)
    Disclaimer:
        Use it at your own risk!

*******************************************************************************************************
    Web search references:
        https://en.wikipedia.org/wiki/Four_color_theorem
        https://en.wikipedia.org/wiki/Graph_coloring#Algorithms
        https://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
        http://www.dharwadker.org/vertex_coloring/
"""

import random


class Graph(list):

    def __init__(self):
        super(Graph, self).__init__()

    def assign_colors(self):

        # we need at least 2 nodes in graph if we want to paint them with different colors
        if len(self) < 2:
            return

        # assign colors to nodes
        for node in self:
            self._assign_color(node)

    def _assign_color(self, node):

        # shuffle colors just for fun
        random.shuffle(ColorNode.COLORS)

        # try to pick an available color from color list
        # available colors are colors which were not assigned to any node having an edge to this node
        for color in ColorNode.COLORS:
            available = True
            for edge in node.edges:
                if edge.n2.color == color:
                    available = False
                    break
            if available:
                node.color = color
                return


class Node:

    def __init__(self, node_id):
        self.node_id = node_id              # save node id (label)
        self.edges = []                     # create blank list of edges

    # check if edge exists in this node
    def _has_edge(self, edge):
        return edge in self.edges

    # add edge to node
    def add_edge(self, other):
        edge = self.Edge(self, other)
        if not self._has_edge(edge):
            self.edges.append(edge)
            other.add_edge(self)

    # Nested class Edge to construct edge objects between Node instances
    class Edge:

        def __init__(self, n1, n2):
            self.n1 = n1
            self.n2 = n2

        def __eq__(self, other):
            return (self.n1 == other.n1) and (self.n2 == other.n2)


#   class ColorNode just adds color member to class Node
class ColorNode(Node):

    COLORS = ["yellow", "green", "blue"]

    def __init__(self, node_id):
        super(ColorNode, self).__init__(node_id)
        self.color = None

    # std python overload to print node data for debugging
    def __str__(self):
        ret = "node id: %d; color: %s ; has edges to nodes: " % (self.node_id, self.color)
        ret += ", ".join([("%d" % edge.n2.node_id) for edge in self.edges])
        return ret
















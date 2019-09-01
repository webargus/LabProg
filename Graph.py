
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

    def get_node_by_id(self, node_id):
        for node in self:
            if node.node_id == node_id:
                return node
        return None

    def remove(self, node):
        node.remove_edges()
        super(Graph, self).remove(node)

    def assign_colors(self):

        # we need at least 2 nodes in graph if we want to paint them with different colors
        if len(self) < 2:
            return

        # shuffle colors just for fun
        # random.shuffle(ColorNode.COLORS)

        # assign colors to nodes
        for node in self:
            # try to pick an available color from color list
            # available colors are colors which were not assigned to any node having an edge to this node
            available_colors = [color for color in ColorNode.COLORS]
            for edge in node.edges:
                if edge.n2.color == available_colors[0]:
                    available_colors = available_colors[1:]
                if len(available_colors) == 0:
                    print("Can't color map: not enough colors available")
                    exit()
            node.color = available_colors[0]


class Node:

    def __init__(self, node_id):
        self.node_id = node_id              # save node id (label)
        self.edges = []                     # create blank list of edges

    # check if edge exists in this node
    def _has_edge(self, edge):
        return edge in self.edges

    # add edge to node
    def add_edge(self, other):              # other must be of type Node
        edge = self.Edge(self, other)
        if not self._has_edge(edge):
            self.edges.append(edge)
            other.add_edge(self)

    def remove_edges(self):
        for edge in self.edges:
            edge.n2.remove_edge(self)
            self.edges.remove(edge)
            self.remove_edges()

    def remove_edge(self, node):            # remove edge to node 'node'
        for edge in self.edges:
            if edge.n2 == node:
                self.edges.remove(edge)

    def __eq__(self, other):                # other must be of type Node
        return self.node_id == other.node_id

    # Nested class Edge to construct (bidirectional) edge objects between Node instances
    class Edge:

        def __init__(self, n1, n2):     # n1, n2 are Node objects
            self.n1 = n1
            self.n2 = n2

        def __eq__(self, other):
            return (self.n1 == other.n1) and (self.n2 == other.n2)


#   class ColorNode just adds color member to class Node
class ColorNode(Node):

    COLORS = ["yellow", "green", "blue", "orange", "red", "cyan", "white"]

    def __init__(self, node_id):
        super(ColorNode, self).__init__(node_id)
        self.color = None

    # std python overload to print node data for debugging
    def __str__(self):
        ret = "node id: %s; color: %s ; has edges to nodes: " % (self.node_id, self.color)
        ret += ", ".join([("%s" % edge.n2.node_id) for edge in self.edges])
        return ret
















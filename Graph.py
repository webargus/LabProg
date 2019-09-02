
"""
    UFRPE - BSI2019.2 - ILP - Homework 2
    Due date: 2019/09/06
    Description: Graph + Node + Edge classes to build and color user-defined map
                 *** Welsh-Powell coloring algorithm defined in method assign_colors of Graph class ***
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

    ########################################################
    #
    #               Welsh-Powell algorithm
    #
    ########################################################
    def assign_colors(self):

        # shuffle colors just for fun
        random.shuffle(ColorNode.COLORS)

        # sort graph nodes in descending order from highest to lowest degree
        self.sort(key=Node.degree, reverse=True)

        # assign colors to nodes
        color_ix = 0
        for node0 in self:
            # go fetch next node from ordered graph if current node (node0) colored before
            if node0.color is not None:
                continue
            # select next color in palette and assign it to current node
            color = ColorNode.COLORS[color_ix]
            node0.color = color
            color_ix += 1
            # Welsh-Powell algorithm key premise:
            # Color with current color all uncolored nodes that have no edge to current node
            # and in turn have no edge to any other node with current color.
            # Scan graph for prospect nodes that meet key premise above:
            for node1 in self:
                # skip this prospect node if node already colored before
                if node1.color is not None:
                    continue
                # skip current node or prospect nodes edging to it
                if node1 == node0 or node0.has_edge_to(node1):
                    continue
                # skip prospect node if there is some other node edging to it and already colored with current color
                if self._has_edge_to_node_with_color(node1, color):
                    continue
                node1.color = color

    def _has_edge_to_node_with_color(self, node, color):
        for n in self:
            if n.color == color and n.has_edge_to(node):
                return True
        return False


class Node:

    def __init__(self, node_id):
        self.node_id = node_id              # save node id (label)
        self.edges = []                     # create blank list of edges

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

    # check if edge exists in this node
    def _has_edge(self, edge):
        return edge in self.edges

    # add edge to node
    def add_edge(self, other):              # other must be of type Node
        edge = self.Edge(self, other)
        if not self._has_edge(edge):
            self.edges.append(edge)
            other.add_edge(self)

    # remove edges of this node; needed when undoing map
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


#   class 'ColorNode' inherits from 'Node', defines static color pallet
#   and conveniently includes handy member 'color'
class ColorNode(Node):

    COLORS = ["yellow", "green", "blue", "orange", "red", "cyan", "magenta"]

    def __init__(self, node_id):
        super(ColorNode, self).__init__(node_id)
        self.color = None

    # std python overload to print node data for debugging
    def __str__(self):
        ret = "node id: %s; color: %s ; has edges to nodes: " % (self.node_id, self.color)
        ret += ", ".join([("%s" % edge.n2.node_id) for edge in self.edges])
        return ret
















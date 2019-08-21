
"""
    UFRPE - BSI2019.2 - ILP - Homework 1
    Due date: 2019/08/23
    Description: Node + Edge ancillary classes for building graphs
    Author:
        Edson Kropniczki - (c) aug/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you please;
        source code also publicly available at https://github.com/webargus/LabProg;
        actually, accretions and improvements are more than welcome! :)
    Disclaimer:
        Use it at your own risk!
"""


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

    # return Edge obj between this Node and @other, if any
    def get_edge(self, other):
        for edge in self.edges:
            if edge.n2 == other:
                return edge
        return None

    # minimum overload to make Node objects hashable, so that we can use them as dictionary keys
    def __hash__(self):
        return hash(self.node_id)

    def __eq__(self, other):
        return (self.node_id == other.node_id) and (self.edges == other.edges)

    def __ne__(self, other):
        return not(self == other)

    # Nested class Edge to construct edge objects between Node instances
    class Edge:

        def __init__(self, n1, n2):
            self.n1 = n1
            self.n2 = n2

        def __eq__(self, other):
            return (self.n1 == other.n1) and (self.n2 == other.n2)


#   class ColorNode just adds color member to class Node
class ColorNode(Node):

    def __init__(self, node_id):
        super(ColorNode, self).__init__(node_id)
        self.color = None














import Graph


class CanvasGraph(Graph.Graph):

    def __init__(self):
        super(CanvasGraph, self).__init__()

    def get_node_by_id(self, node_id):
        for node in self:
            if node.node_id == node_id:
                return node
        return None

    def remove(self, node):
        node.remove_edges()
        super().remove(node)


class CanvasNode(Graph.Node):

    def __init__(self, node_id):
        super(CanvasNode, self).__init__(node_id)

    # remove edges of this node; needed only when undoing GUI map
    def remove_edges(self):
        for edge in self.edges:
            edge.n2.remove_edge(self)
            self.edges.remove(edge)
            self.remove_edges()

    # remove edge to node 'node'; needed only when undoing user GUI map input
    def remove_edge(self, node):
        for edge in self.edges:
            if edge.n2 == node:
                self.edges.remove(edge)

    # std python overload to print node data for debugging
    def __str__(self):
        ret = "vertex id: %s; edges: " % self.node_id
        ret += ", ".join([("%s" % edge.n2.node_id) for edge in self.edges])
        return ret










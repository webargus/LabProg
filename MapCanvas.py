
"""
    Description:
        GUI map (graph) coloring implementation
    Author:
        Edson Kropniczki - (c) aug/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you please;
        source code also publicly available at https://github.com/webargus/LabProg;
        actually, accretions and improvements are more than welcome! :)
    Disclaimer:
        Use it at your own risk!
"""

from tkinter import *
import Graph


class MapCanvas:

    def __init__(self, frame):

        self.graph = Graph.Graph()

        self.canvas = Canvas(frame, background="white", cursor="tcross")
        self.canvas.grid(row=0, column=0, sticky=NSEW)

        self.state_node = 1
        self.img_hair = PhotoImage(file="crosshair16.png")
        self.hair = self.canvas.create_image(0, 0, image=self.img_hair, state=HIDDEN)
        self.canvas.bind("<1>", self._handle_canvas_click)

    def _handle_canvas_click(self, event):
        # if cross-hair hidden and user clicked on canvas -> just put cross-hair img on clicked coords and show it
        if self.canvas.itemcget(self.hair, "state") == HIDDEN:
            self.canvas.coords(self.hair, event.x, event.y)
            self.canvas.itemconfigure(self.hair, state=NORMAL)
            self.canvas.tag_raise(self.hair)
        # if cross-hair shown -> create new retolandia state from cross-hair coords to clicked position
        # and hide cross-hair img
        else:
            self._create_state(event.x, event.y)
            self.canvas.itemconfigure(self.hair, state=HIDDEN)

    def _create_state(self, x, y):
        state_tag = "state_%d" % self.state_node
        state_id = self.canvas.create_rectangle(self.canvas.coords(self.hair),
                                                x,
                                                y,
                                                width=2,
                                                tags=(state_tag,))
        self.canvas.itemconfigure(state_id, fill="gray")
        # get ids of overlapped states
        ovl = self.canvas.find_overlapping(*self.canvas.coords(state_id))
        # split tags to get rid of eventual 'current' tag that tkinter sometimes appends to tags list
        ovl = [self.canvas.itemcget(sid, "tags").split(" ")[0] for sid in ovl]
        # sift through overlapped list one last time to pick state tags only, except current state
        ovl = [tag for tag in ovl if tag.startswith("state_") and tag != state_tag]
        # print(ovl)      # debug
        # create graph color node with ID equal to latest (current) state tag...
        node = Graph.ColorNode(state_tag)
        # ... and add edges to node created, corresponding to the nodes it overlaps (border states)
        for tag in ovl:
            node.add_edge(self.graph.get_node_by_id(tag))
        # add node to graph
        self.graph.append(node)
        # increment global node index
        self.state_node += 1

    def paint_map(self):
        self.graph.assign_colors()
        # debugging:
        for node in self.graph:
            print(node)
        for node in self.graph:
            self.canvas.itemconfigure(node.node_id, fill=node.color)

    def undo(self):
        if len(self.graph) == 0:
            return
        if self.state_node > 1:
            self.state_node -= 1
        node_id = "state_%d" % self.state_node
        self.canvas.delete(node_id)
        self.graph.remove(self.graph.get_node_by_id(node_id))
        '''for n in self.graph:         # debug
            print(n)'''

    def clear(self):
        # clear entire canvas drawing area and wipe out previous graph, if any
        self.canvas.delete("all")
        del self.graph[:]
        self.state_node = 1
        self.hair = self.canvas.create_image(0, 0, image=self.img_hair, state=HIDDEN)






















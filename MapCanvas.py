
"""
    Description:
        GUI map (graph) coloring implementation
    Author:
        Edson Kropniczki - (c) aug/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you please;
        source code also publicly available at https://github.com/webargus/LabProg;
    Disclaimer:
        Use it at your own risk!
"""

from tkinter import *
from tkinter import messagebox as mb
import datetime
import CanvasGraph


class MapCanvas:

    def __init__(self, frame, when_create_state=None):

        self.graph = CanvasGraph.CanvasGraph()

        self.canvas = Canvas(frame, background="white", cursor="tcross")
        self.canvas.grid(row=0, column=0, sticky=NSEW)

        self.when_create_state = when_create_state      # callback function called after vertex (State) creation
        self.state_node = 1                             # id of next graph state (vertex) to be created
        self.img_hair = PhotoImage(file="crosshair16.png")
        self.hair = self.canvas.create_image(0, 0, image=self.img_hair, state=HIDDEN)

        self.enabled = True
        self.canvas.bind("<1>", self._handle_canvas_click)

    def _handle_canvas_click(self, event):
        # abort if map colored
        if not self.enabled:
            return
        # if cross-hair hidden and user clicked on canvas -> just put cross-hair img on clicked coords and show it
        if self.canvas.itemcget(self.hair, "state") == HIDDEN:
            self.canvas.coords(self.hair, event.x, event.y)
            self.canvas.itemconfigure(self.hair, state=NORMAL)
            self.canvas.tag_raise(self.hair)
        # if cross-hair shown -> create new retonia state from cross-hair coords to clicked position
        # and hide cross-hair img
        else:
            self._create_state(event.x, event.y)
            self.canvas.itemconfigure(self.hair, state=HIDDEN)

    def _create_state(self, x, y):
        state_tag = "state_%d" % self.state_node
        (x0, y0) = self.canvas.coords(self.hair)
        state_id = self.canvas.create_rectangle(x0,
                                                y0,
                                                x,
                                                y,
                                                width=2,
                                                tags=(state_tag,))
        self.canvas.create_text((x0+x)/2,
                                (y0+y)/2,
                                text=("%d" % self.state_node),
                                font=("Arial", 8),
                                tags=(("tag_txt_%d" % self.state_node),))
        self.canvas.itemconfigure(state_id, fill="gray")
        # get ids of overlapped states
        ovl = self.canvas.find_overlapping(*self.canvas.coords(state_id))
        # split tags to get rid of eventual 'current' tag that tkinter sometimes appends to tags list
        ovl = [self.canvas.itemcget(sid, "tags").split(" ")[0] for sid in ovl]
        # sift through overlapped list one last time to pick state tags only, except current state
        ovl = [tag for tag in ovl if tag.startswith("state_") and tag != state_tag]
        # print(ovl)      # debug
        # create graph color node with ID equal to latest (current) state tag...
        node = CanvasGraph.CanvasNode(state_tag)
        # ... and add edges to node created, corresponding to the nodes it overlaps (border states)
        for tag in ovl:
            node.add_edge(self.graph.get_node_by_id(tag))
        # add node to graph
        self.graph.append(node)
        # notify caller on node created
        if self.when_create_state is not None:
            self.when_create_state(self.graph)
        # increment global vertex id
        self.state_node += 1

    def paint_map(self):
        self.enabled = False                            # disable map editing
        init = datetime.datetime.now()
        n_colors = self.graph.assign_colors()
        end = datetime.datetime.now()
        for node in self.graph:
            self.canvas.itemconfigure(node.node_id, fill=node.color)
        report = "%d vertices colored in " % len(self.graph)
        report += "%f seconds" % (end-init).total_seconds()
        report += " using %d colors" % n_colors
        mb.showwarning("Welsh-Powell Report", report)
        return

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
        self.canvas.delete(("tag_txt_%d" % self.state_node))

    def clear(self):
        # clear entire canvas drawing area and wipe out previous graph, if any
        self.canvas.delete("all")
        del self.graph[:]
        self.state_node = 1
        self.hair = self.canvas.create_image(0, 0, image=self.img_hair, state=HIDDEN)
        self.enabled = True                     # enable map editing






















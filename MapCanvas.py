
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
import random
import Graph


class MapCanvas:

    DOT_RADIUS = 4
    MIN_BOX_WIDTH = MIN_BOX_HEIGHT = 30

    def __init__(self, frame):

        self.graph = []

        self.canvas = Canvas(frame, background="white", cursor="tcross")
        self.canvas.grid(row=0, column=0, sticky=NSEW)

    def generate_random_map(self):
        self.clear()
        # get canvas width and height
        w = self.canvas.winfo_width() - 1
        h = self.canvas.winfo_height() - 1
        # draw background wrapping rectangle around drawing canvas and get its id
        rect = self.canvas.create_rectangle(1, 1, w - 1, h - 1)
        # create background node, which stands for the background rectangle and has edges to each node to be drawn
        bg_node = Graph.ColorNode(rect)
        self.graph.append(bg_node)
        x0 = 1
        yy0 = yy1 = prev_node = None
        while 1:
            x1 = x0 + MapCanvas.MIN_BOX_WIDTH + int(random.random()*w/8)
            y0 = int(1 + random.random() * (h - MapCanvas.MIN_BOX_HEIGHT - 1))
            y1 = y0 + MapCanvas.MIN_BOX_HEIGHT + int(random.random() * (h - y0 - MapCanvas.MIN_BOX_HEIGHT - 1))
            if yy0 is not None:
                if y1 < yy0:
                    y1 = yy0 + int(random.random()*(yy1-yy0))
                elif y0 > yy1:
                    y0 = yy0 + int(random.random()*(yy1-yy0))
            if x1 > w - MapCanvas.MIN_BOX_WIDTH:
                x1 = w - 1
            # draw random rectangle and bind graph node to it
            rect = self.canvas.create_rectangle(x0, y0, x1, y1)
            node = Graph.ColorNode(rect)
            # add edge to background node
            node.add_edge(bg_node)
            # save node to graph
            self.graph.append(node)
            if prev_node is not None:
                node.add_edge(prev_node)
            if x1 == w - 1:
                break
            x0 = x1
            yy0 = y0
            yy1 = y1
            prev_node = node

    def clear(self):
        # clear entire canvas drawing area and wipe out previous graph, if any
        self.canvas.delete("all")
        del self.graph[:]





















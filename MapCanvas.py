
"""
    Description:
        Elementary classes to draw simple undirected graphs on a tkinter Canvas
    Author:
        Edson Kropniczki - (c) jul/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you please;
        source code also publicly available at https://github.com/webargus/MatematicaDiscretaIII;
        actually, accretions and improvements are more than welcome! :)
    Disclaimer:
        Use it at your own risk!
"""

from tkinter import *
import random


class MapCanvas:

    DOT_RADIUS = 4
    MIN_BOX_WIDTH = MIN_BOX_HEIGHT = 30

    def __init__(self, frame):

        self.graph = []

        self.canvas = Canvas(frame, background="white", cursor="tcross")
        self.canvas.grid(row=0, column=0, sticky=NSEW)

    def clear(self):
        self.canvas.clear()

    def generate_random_map(self):
        self.clear()
        w = self.canvas.winfo_width() - 1
        h = self.canvas.winfo_height() - 1
        self.canvas.create_rectangle(1, 1, w - 1, h - 1)
        x0 = 1
        yy0 = yy1 = None
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
            self.canvas.create_rectangle(x0, y0, x1, y1)
            if x1 == w - 1:
                break
            x0 = x1
            yy0 = y0
            yy1 = y1

    def clear(self):
        self.canvas.delete("all")
        del self.graph[:]





















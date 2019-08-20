
"""
    Description:
        Elementary classes to draw simple undirected graphs on a tkinter Canvas
    Author:
        Edson Kropniczki - (c) jul/2019 - all rights reserved
    License:
        just keep this header in your copy and feel free to mess up with this code as you wish;
        source code also publicly available at https://github.com/webargus/MatematicaDiscretaIII;
        actually, accretions and improvements are more than welcome! :)
    Disclaimer:
        Use it at your own risk!
"""

from tkinter import *
import Regions
import random


class MapCanvas:

    def __init__(self, frame, callback):

        self.clicked = False                # Flag to toggle between rect 1st corner selection and rect drawing
        self.edit = True                    # Flag to toggle edit/processing mode

        self.canvas = CanvasRegions(frame)
        self.canvas.grid(row=0, column=0, sticky=NSEW)

        self.canvas.bind('<Button-1>', self._handle_click)

    def _handle_click(self, event, ctrl=False):
        # abort if canvas not in edit mode
        if not self.edit:
            return
        # create new corner if user 1st click on canvas
        if not self.clicked:
            self.canvas.draw_dot(Regions.Point(event.x, event.y))
            self.clicked = True
            return
        # user clicked for 2nd rect corner => now we can construct region
        self.canvas.draw_region(Regions.Point(event.x, event.y))
        self.clicked = False

    def generate_map(self):
        self.clear()
        self.canvas.generate_random_map()

    def clear(self):
        self.canvas.clear()
        self.edit = True
        self.clicked = False


class CanvasRegions(Canvas):

    DOT_RADIUS = 4
    MIN_BOX_WIDTH = MIN_BOX_HEIGHT = 30

    def __init__(self, frame):
        Canvas.__init__(self, frame, background="white", cursor="tcross")
        self.regions = Regions.Regions()    # Regions obj to retrieve regions created
        self.corner = None

    def generate_random_map(self):
        w = self.winfo_width() - 1
        h = self.winfo_height() - 1
        x0 = 1
        yy0 = yy1 = None
        while 1:
            x1 = x0 + CanvasRegions.MIN_BOX_WIDTH + int(random.random()*w/8)
            y0 = int(1 + random.random() * (h - CanvasRegions.MIN_BOX_HEIGHT))
            y1 = y0 + CanvasRegions.MIN_BOX_HEIGHT + int(random.random() * (h - y0 - CanvasRegions.MIN_BOX_HEIGHT - 1))
            if yy0 is not None:
                if y1 < yy0:
                    y1 = yy0 + int(random.random()*(yy1-yy0))
                elif y0 > yy1:
                    y0 = yy0 + int(random.random()*(yy1-yy0))
            if x1 > w - CanvasRegions.MIN_BOX_WIDTH:
                x1 = w - 1
            self.create_rectangle(x0, y0, x1, y1)
            if x1 == w - 1:
                break
            x0 = x1
            yy0 = y0
            yy1 = y1

    def draw_dot(self, point):
        self.corner = self.create_oval(point.x - CanvasRegions.DOT_RADIUS,
                                       point.y - CanvasRegions.DOT_RADIUS,
                                       point.x + CanvasRegions.DOT_RADIUS,
                                       point.y + CanvasRegions.DOT_RADIUS,
                                       fill="yellow")

    def draw_region(self, point):
        coords = self.coords(self.corner)
        p0 = Regions.Point(coords[0], coords[1])
        self._snap_to_closest(p0)
        self._snap_to_closest(point)

        self.regions.append(self.create_rectangle(p0.coords, point.coords))
        self.delete(self.corner)

    def _snap_to_closest(self, point):
        for rect in self.regions:
            coords = self.coords(rect)
            for i in range(2):
                if abs(coords[2*i] - point.x) <= CanvasRegions.DOT_RADIUS:
                    point.x = coords[2*i]
                if abs(coords[2*i+1] - point.y) <= CanvasRegions.DOT_RADIUS:
                    point.y = coords[2*i+1]

    def clear(self):
        self.delete("all")
        del self.regions[:]


class CanvasRegion(Regions.Region):

    canvas = None





















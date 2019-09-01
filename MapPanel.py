
"""
    UFRPE - BSI2019.2
    Author: Edson Kropniczki
    Description: GUI for drawing simple random maps
"""

from tkinter import *
import MapCanvas


class MapPanel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Map coloring based on the graph greedy coloring algorithm",
                            "font": ("Arial", 12)})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        form.grid_columnconfigure(0, weight=1)

        text = " How to build a Retolandia map with rectangles:\n"
        text += " 1. Click on the map area to stick a 1st State border vertex.\n"
        text += " 2. Click again on map area to build a State between both marks.\n"
        self.info_img = PhotoImage(file="info24.png")
        Label(form,
              relief=SUNKEN,
              text=text,
              font=("Arial, sans-serif", 8),
              image=self.info_img,
              compound=LEFT,
              justify=LEFT,
              anchor=W).grid(row=0, column=0, sticky=EW, pady=8, columnspan=3)

        canvasF = Frame(wrap, {"relief": SUNKEN, "border": 1})
        canvasF.grid({"pady": 8, "padx": 8, "row": 2, "column": 0, "sticky": NSEW})
        canvasF.grid_columnconfigure(0, weight=1)
        canvasF.grid_rowconfigure(0, weight=1)
        # create graph canvas
        self.canvas = MapCanvas.MapCanvas(canvasF)

        # btns
        self.clear_btn = Button(form,
                                width=10,
                                command=self._clear_map,
                                text="Clear map")
        self.clear_btn.grid(row=1, column=0, sticky=W, pady=8)
        self.undo_btn = Button(form,
                               width=10,
                               command=self.canvas.undo,
                               text="Undo last")
        self.undo_btn.grid(row=1, column=1, sticky=W, pady=8)
        self.colorize_btn = Button(form,
                                   width=10,
                                   command=self._colorize_map,
                                   text="Color map")
        self.colorize_btn.grid(row=1, column=2, stick=W)

    def _colorize_map(self):
        # we need at least 1 state to color map
        if len(self.canvas.graph) < 1:
            return
        self.canvas.paint_map()
        self.colorize_btn.configure(state="disabled")
        self.undo_btn.configure(state="disabled")

    def _clear_map(self):
        self.canvas.clear()
        self.colorize_btn.configure(state="normal")
        self.undo_btn.configure(state="normal")








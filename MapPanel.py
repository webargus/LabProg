
"""
    UFRPE - BSI2019.2
    Author: Edson Kropniczki
    Description: GUI for drawing very simple random maps
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

        text = " Instructions:\n"
        text += " 1. Click on the [Create map] button to create a random map.\n"
        text += " 2. Click on the [Color map] button to run coloring algorithm.\n"
        self.info_img = PhotoImage(file="info24.png")
        Label(form,
              relief=SUNKEN,
              text=text,
              font=("Arial, sans-serif", 9),
              image=self.info_img,
              compound=LEFT,
              justify=LEFT,
              anchor=W).grid(row=0, column=0, sticky=EW, pady=8, columnspan=2)

        # btns
        self.create = Button(form,
                             width=10,
                             command=self._generate_map,
                             text="Create map")
        self.create.grid(row=1, column=0, sticky=W, pady=8)
        self.color = Button(form,
                            width=10,
                            command=self._color_canvas,
                            text="Color map",
                            state="disabled")
        self.color.grid(row=1, column=1, stick=E)

        canvasF = Frame(wrap, {"relief": SUNKEN, "border": 1})
        canvasF.grid({"pady": 8, "padx": 8, "row": 2, "column": 0, "sticky": NSEW})
        canvasF.grid_columnconfigure(0, weight=1)
        canvasF.grid_rowconfigure(0, weight=1)
        # create graph canvas
        self.canvas = MapCanvas.MapCanvas(canvasF)

    def _generate_map(self):
        self.canvas.generate_random_map()
        self.color.config({"state": "normal"})

    def _color_canvas(self):
        self.canvas.paint_map()
        self.color.config({"state": "disabled"})











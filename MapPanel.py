
"""
    UFRPE - BSI2019.2
    Author: Edson Kropniczki
    Description: GUI for drawing simple random maps

"""

from tkinter import *
import MapCanvas
import ScrollableText


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
        l1 = Label(header, {"text": "Map coloring based on the Welsh-Powell algorithm",
                            "font": ("Arial", 12),
                            "pady": 4,
                            "padx": 4})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 4, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        form.grid_columnconfigure(0, weight=1)

        text = " Hints to build a proper Retônia map with rectangles:\n"
        text += " 1. Click on the map area to stick an initial State border 'landmark'.\n"
        text += " 2. Click on map area again to build a State (vertex) between marks.\n"
        text += " 3. Try to build maps by drawing intercepting adjacent rectangles.\n"
        text += " 4. Check corresponding updated graph input in bottom text area."
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
        # create map canvas
        self.canvas = MapCanvas.MapCanvas(canvasF, self._report_state_created)

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

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 3, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        # text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)
        self.text.configure(height=10)

    def _colorize_map(self):
        # we need at least 1 state to color map
        if len(self.canvas.graph) < 1:
            return
        self.colorize_btn.configure(state="disabled")
        self.undo_btn.configure(state="disabled")
        self.canvas.paint_map()

    def _clear_map(self):
        self.canvas.clear()
        self.colorize_btn.configure(state="normal")
        self.undo_btn.configure(state="normal")
        self.text.clear()

    def _report_state_created(self, graph):
        self.text.clear()
        self.text.append_text("Map graph input:\n")
        for vertex in graph:
            self.text.append_text(vertex)
            self.text.append_text("\n")






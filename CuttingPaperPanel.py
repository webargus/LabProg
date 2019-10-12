
from tkinter import *
import CuttingPaperCanvas


class CuttingPaperPanel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Maximization problem: cutting maximum number of paper pieces",
                            "font": ("Arial", 12),
                            "pady": 4,
                            "padx": 4})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 4, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        form.grid_columnconfigure(0, weight=1)

        # btns
        self.generate_paper = Button(form,
                                     width=20,
                                     command=self._generate_paper,
                                     text="Generate random shape")
        self.generate_paper.grid(row=1, column=0, sticky=W, pady=8)

        self.cut_paper = Button(form,
                                width=20,
                                command=self._cut_paper,
                                text="Cut paper",
                                state="disabled")
        self.cut_paper.grid(row=2, column=0, sticky=W, pady=8)

        canvasF = Frame(wrap, {"relief": SUNKEN, "border": 1})
        canvasF.grid({"pady": 8, "padx": 8, "row": 2, "column": 0, "sticky": NSEW})
        canvasF.grid_columnconfigure(0, weight=1)
        canvasF.grid_rowconfigure(0, weight=1)
        # create map canvas
        self.canvas = CuttingPaperCanvas.CuttingPaperCanvas(canvasF)

    def _generate_paper(self):
        self.canvas.draw_paper()
        self.cut_paper.configure(state="normal")

    def _cut_paper(self):
        self.cut_paper.configure(state="disabled")
        self.canvas.cut_paper()














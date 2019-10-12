
from tkinter import *
import CuttingPaper


class CuttingPaperCanvas:

    def __init__(self, frame):

        self.canvas = Canvas(frame, background="white", cursor="tcross")
        self.canvas.grid(row=0, column=0, sticky=NSEW)
        self.max_height = self.max_width = self.scale = 0
        self.cp = CuttingPaper.CuttingPaper()

    def draw_paper(self):
        self.max_height = self.canvas.winfo_height()
        self.max_width = self.canvas.winfo_width()
        self.scale = self.max_height/CuttingPaper.CuttingPaper.MAX_HEIGHT
        self.canvas.delete("all")

        rects = self.cp.gen_paper()

        self.canvas.create_rectangle(0, 0, self.max_width, self.max_height, fill="grey")
        width = (self.max_width - 48)//len(rects)

        x = 24
        for rect in rects:
            h = int(rect*self.scale)
            self.canvas.create_rectangle(x, self.max_height - h + 24, x + width, self.max_height - 24, fill="white")
            self.canvas.create_text(x + width/2, self.max_height - 32, text=str(rect), font=("Arial", 8))
            x += width

    def cut_paper(self):
        cuts = self.cp.cut_paper()
        for height, pieces in cuts.items():
            h = self.max_height - int(height*self.scale) + 22
            self.canvas.create_line(16, h, self.max_width - 16, h, fill="yellow", dash=(6, 2))
            self.canvas.create_text(64, h-12, text="Total: %d pieces" % pieces, fill="red", font=("Arial", 10, "bold"))










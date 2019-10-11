
"""
    UFRPE - BSI2019.2 - LP - Homework 1
    Due date: aug/23 2019
    Author: Edson Kropniczki
    Description: Homework main GUI
"""

from tkinter import *
from tkinter.ttk import *
import ScrollableText
import LinearRobotPanel
import MapPanel
import ShortestPathPanel
import CuttingPaperPanel
import Tools


class Gui(Frame):

    def __init__(self):
        Frame.__init__(self)
        Tools.Tools.root(self.master)
        Tools.Tools.center_window(self.master, 1280, 680)
        self.imgicon = PhotoImage(file='icon32.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, self.imgicon)

        self.master.resizable(0, 0)
        self.master.state('normal')
        self.master.title("Programming Lab' - SI2019.2")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.nb = Notebook(self)
        #   add tabs
        self.nb_files = [("Linear Robot", Frame(self.nb), "LinearRobot"),
                         ("Map Coloring", Frame(self.nb), "Graph",),
                         ("Shortest Path", Frame(self.nb), "ShortestPath"),
                         ("Cutting Paper", Frame(self.nb), "CuttingPaper")]
        for i in self.nb_files:
            self.nb.add(i[1], text="    " + i[0] + "    ")
        self.nb.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.nb.bind("<<NotebookTabChanged>>", self._tab_switch)

        LinearRobotPanel.LinearRobotPanel(self.nb_files[0][1])
        MapPanel.MapPanel(self.nb_files[1][1])
        ShortestPathPanel.ShortestPathPanel(self.nb_files[2][1])
        CuttingPaperPanel.CuttingPaperPanel(self.nb_files[3][1])

        frame = Frame(self)
        frame.grid({"row": 0, "column": 1, "sticky": NSEW, "pady": 4, "padx": 4})
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        ftop = Frame(frame)
        ftop.grid({"row": 0, "column": 0})
        text = "NOTICE: This is a rather simple, reusable hack of a standard tkinter Graphical User Interface template,"
        text += " geared towards facilitating user input in a graphical manner, when testing exercise assignments "
        text += "from the UFRPE Programming Lab subject program, as opposed to the otherwise cumbersome and "
        text += "far less efficient console-based input methods. All exercise source codes come in separated "
        text += "*.py package files which then again come listed in the "
        text += "text area section below just for the sake of easy reading and verification purposes.\n"
        text += "Therefore, having said that, please bear in mind that only source codes exclusively listed in "
        text += "the text area below "
        text += "should matter when analysing the solutions herein proposed for the exercise assignments, "
        text += "since the GUI code and the tkinter native code do not interfere in any ways or manners whatsoever "
        text += "neither with the solution proposed, its complexity level, nor with the code structure of the exercise."
        Label(ftop,
              text=text,
              wraplength=500,
              font=("Arial", 8),
              relief=RIDGE,
              padding=4).grid({"row": 0, "column": 0})
        fbottom = Frame(frame)
        fbottom.grid({"row": 1, "column": 0, "sticky": NSEW})
        self.text_widget = ScrollableText.ScrollableText(fbottom)

        self.mainloop()

    def _tab_switch(self, event):
        file = self.nb_files[self.nb.index(self.nb.select())][2] + ".py"
        try:
            handle = open(file, "r", encoding="utf-8")
        except OSError:
            print(OSError.args)
        self.text_widget.clear()
        self.text_widget.append_text("# Source file: %s\n" % file)
        for line in handle.readlines():
            self.text_widget.append_text(line)
        handle.close()


if __name__ == '__main__':
    gui = Gui()







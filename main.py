
"""
    UFRPE - BSI2019.2 - LP - Homework 1
    Due date: aug/23 2019
    Author: Edson Kropniczki
    Description: Homework main GUI
"""

from tkinter import *
from tkinter.ttk import *
import os
import ScrollableText
import LinearRobotPanel
import MapPanel
import Tools


class Gui(Frame):

    def __init__(self):
        Frame.__init__(self)
        Tools.Tools.root(self.master)
        Tools.Tools.center_window(self.master, 1120, 600)
        self.imgicon = PhotoImage(file='icon32.png')
        self.master.tk.call('wm', 'iconphoto', self.master._w, self.imgicon)

        self.master.resizable(0, 0)
        self.master.state('normal')
        self.master.title("Laboratório de Programação - Trabalho 1' - SI2019.2")
        self.master.grid_rowconfigure(0, weight=1)
        self.master.grid_columnconfigure(0, weight=1)
        self.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.nb = Notebook(self)
        #   add tabs
        self.nb_files = [("Linear Robot", Frame(self.nb), "LinearRobot"),
                         ("Map Coloring", Frame(self.nb), "Graph")]
        for i in self.nb_files:
            self.nb.add(i[1], text="    " + i[0] + "    ")
        self.nb.grid({"row": 0, "column": 0, "sticky": NSEW})
        self.nb.bind("<<NotebookTabChanged>>", self._tab_switch)

        LinearRobotPanel.LinearRobotPanel(self.nb_files[0][1])
        MapPanel.MapPanel(self.nb_files[1][1])

        frame = Frame(self)
        frame.grid({"row": 0, "column": 1, "sticky": NSEW, "pady": 4, "padx": 4})
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        self.text_widget = ScrollableText.ScrollableText(frame)

        self.mainloop()

    def _tab_switch(self, event):
        file = self.nb_files[self.nb.index(self.nb.select())][2] + ".py"
        try:
            handle = open(file, "r", encoding="utf-8")
        except OSError:
            print(OSError.args)
        self.text_widget.clear()
        for line in handle.readlines():
            self.text_widget.append_text(line)
        handle.close()


if __name__ == '__main__':
    gui = Gui()







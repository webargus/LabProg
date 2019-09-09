
from tkinter import *
from tkinter import messagebox
from threading import Thread
import ScrollableText
import ShortestPath


class ShortestPathPanel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Shortest path between two graph vertices",
                            "font": ("Arial", 12)})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        form.grid_columnconfigure(1, weight=1)

        Label(form, text="No. of cities (1 < N <= 100): ", font=("Arial", 9)).grid(row=0, column=0)
        self.no = StringVar()
        self.n_cities = Entry(form, width=4, textvar=self.no)
        self.n_cities.grid(row=0, column=1, sticky=W)
        Button(form, text="Generate graph", command=self.__gen_graph_matrix).grid(row=0, column=2)

        Label(form, text="Start city:", font=("Arial", 9)).grid(row=1, column=0, sticky=W)
        self.source = Entry(form, width=4)
        self.source.grid(row=1, column=1, columnspan=2, sticky=W)

        Label(form, text="Target city:", font=("Arial", 9)).grid(row=2, column=0, sticky=W)
        self.target = Entry(form, width=4)
        self.target.grid(row=2, column=1, columnspan=2, sticky=W)

        Button(form, text="Apply depth first", command=self.__apply_breadth_first).grid(row=3, column=0, sticky=W)
        Button(form, text="Apply breadth first", command=self.__apply_breadth_first)\
            .grid(row=3, column=1, sticky=E, columnspan=2, pady=32)

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 4, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)

        self.graph = ShortestPath.Graph()

    def __gen_graph_matrix(self):
        try:
            n = int(self.no.get())
            if (n < 2) or (n > 100):
                raise ValueError
        except ValueError:
            messagebox.showerror("Shortest path", "Entrada inválida:\nEntre um inteiro entre 2 e 100.")
            return
        self.graph.generate_matrix(n)
        self.text.clear()
        if n < 21:
            self.text.append_text(self.graph)

    def __apply_depth_first(self):
        pass

    def __apply_breadth_first(self):
        pass












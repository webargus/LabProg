
from tkinter import *
from tkinter import messagebox
from threading import Thread
import Tools
import ScrollableText
import ShortestPath


class ShortestPathPanel:

    MAX_ARRAY_SIZE = 10000

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Shortest path between two cities of a random graph",
                            "font": ("Arial", 12)})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})
        form.grid_columnconfigure(1, weight=1)

        Label(form,
              text="No. of cities (1 < N <= %d): " % ShortestPathPanel.MAX_ARRAY_SIZE,
              font=("Arial", 9)).grid(row=0, column=0)
        self.no = StringVar()
        self.n_cities = Entry(form, width=4, textvar=self.no)
        self.n_cities.grid(row=0, column=1, sticky=W)
        self.gen_graph = Button(form, text="Generate graph", command=self.__gen_graph_matrix)
        self.gen_graph.grid(row=0, column=2)

        Label(form, text="Start city:", font=("Arial", 9)).grid(row=1, column=0, sticky=W)
        self.start_city = StringVar()
        self.source = Entry(form, width=4, textvar=self.start_city)
        self.source.grid(row=1, column=1, columnspan=2, sticky=W)

        Label(form, text="Target city:", font=("Arial", 9)).grid(row=2, column=0, sticky=W)
        self.target_city = StringVar()
        self.target = Entry(form, width=4, textvar=self.target_city)
        self.target.grid(row=2, column=1, columnspan=2, sticky=W)

        self.verb = IntVar()
        self.verbose = Checkbutton(form, text="Show paths", variable=self.verb, font=("Arial", 9))
        self.verbose.grid(row=3, column=0, columnspan=3, sticky=W)

        self.btn_depth = Button(form,
                                text="Depth First Search",
                                command=self.__apply_depth_first,
                                state="disabled",
                                font=("Arial", 9))
        self.btn_depth.grid(row=4, column=0, sticky=W, pady=8)
        self.btn_breadth = Button(form,
                                  text="Breadth First Search",
                                  command=self.__apply_breadth_first,
                                  state="disabled",
                                  font=("Arial", 9))
        self.btn_breadth.grid(row=4, column=1, sticky=E, columnspan=2, pady=8)

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 4, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)

        self.graph = ShortestPath.Graph()

    def __gen_graph_matrix(self):
        try:
            n = int(self.no.get())
            if (n < 2) or (n > ShortestPathPanel.MAX_ARRAY_SIZE):
                raise ValueError
        except ValueError:
            messagebox.showerror("Shortest path",
                                 "Invalid input:\nEnter an integer between 2 and %d." % ShortestPathPanel.MAX_ARRAY_SIZE)
            return
        self.gen_graph.configure(state="disabled")
        self.btn_depth.configure(state="disabled")
        self.btn_breadth.configure(state="disabled")
        self.text.clear()
        self.text.append_text("Generating random %d X %d matrix...\n...this may take a while...\n" % (n, n))
        Tools.Tools.master.update_idletasks()
        thread = Thread(target=self.__gen_matrix_thread, args=(n,))
        thread.daemon = True
        thread.start()

    def __gen_matrix_thread(self, n):
        timer = Tools.Timer()
        timer.start()
        self.graph.generate_matrix(n)
        secs = timer.stop()
        self.text.append_text("Graph generated in %f seconds.\n" % secs)
        if n < 21:
            self.text.append_text(self.graph.as_matrix())
            self.text.append_text(self.graph.as_graph())
        self.gen_graph.configure(state="normal")
        self.btn_breadth.configure(state="normal")
        self.btn_depth.configure(state="normal")

    def __apply_depth_first(self):
        params = self.__validate_city_inputs()
        if params is None:
            return
        (source, target) = params
        self.btn_depth.configure(state="disabled")
        self.btn_breadth.configure(state="disabled")
        self.gen_graph.configure(state="disabled")

        thread = Thread(target=self.__thread_depth_first, args=(source, target))
        thread.daemon = True
        thread.start()

    def __apply_breadth_first(self):
        params = self.__validate_city_inputs()
        if params is None:
            return
        (source, target) = params
        self.btn_depth.configure(state="disabled")
        self.btn_breadth.configure(state="disabled")
        self.gen_graph.configure(state="disabled")

        thread = Thread(target=self.__thread_breadth_first, args=(source, target))
        thread.daemon = True
        thread.start()

    def __thread_depth_first(self, source, target):
        self.text.append_text("Searching depth first...\n")
        timer = Tools.Timer()
        timer.start()
        paths = self.graph.find_paths_depth(source, target)
        secs = timer.stop()
        self.text.append_text("DFS took %f seconds and returned %d possible paths\n" % (secs, len(paths)))
        if self.verb.get() == 1:
            self.text.append_text("Paths from city %d to city %d:\n" % (source+1, target+1))
            for path in paths:
                self.text.append_text(" -> ".join([str(x + 1) for x in path]) + "\n")
        self.btn_depth.configure(state="normal")
        self.btn_breadth.configure(state="normal")
        self.gen_graph.configure(state="normal")

    def __thread_breadth_first(self, source, target):
        self.text.append_text("Searching breadth first...\n")
        timer = Tools.Timer()
        timer.start()
        paths = self.graph.find_paths_breadth(source, target)
        secs = timer.stop()
        self.text.append_text("BFS took %f seconds and returned %d possible paths\n" % (secs, len(paths)))
        if self.verb.get() == 1:
            self.text.append_text("Paths from city %d to city %d:\n" % (source+1, target+1))
            for path in paths:
                self.text.append_text(" -> ".join([str(x + 1) for x in path]) + "\n")
        self.btn_depth.configure(state="normal")
        self.btn_breadth.configure(state="normal")
        self.gen_graph.configure(state="normal")

    def __validate_city_inputs(self):
        try:
            source = int(self.start_city.get())
            if (source < 1) or (source > self.graph.n):
                raise ValueError
            target = int(self.target_city.get())
            if (target < 1) or (target > self.graph.n):
                raise ValueError
        except ValueError:
            messagebox.showerror("Shortest path",
                                 "Invalid city:\nEnter an integer between 1 and %d." % self.graph.n)
            return None
        if source == target:
            messagebox.showerror("Shortest path",
                                 "Destination city can't be the same as origin city.")
            return None
        return source-1, target-1












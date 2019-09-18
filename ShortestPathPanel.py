
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

        Label(form,
              text="No. of cities (1 < N <= %d): " % ShortestPathPanel.MAX_ARRAY_SIZE,
              font=("Arial", 9)).grid(row=0, column=0)
        self.no = StringVar()
        self.n_cities = Entry(form, width=4, textvar=self.no)
        self.n_cities.grid(row=0, column=1, sticky=W)
        self.gen_graph = Button(form,
                                text="Generate graph",
                                command=self.__gen_graph_matrix,
                                font=("Arial", 9),
                                width=14)
        self.gen_graph.grid(row=0, column=2, columnspan=2, sticky=E)

        Label(form, text="Start city:", font=("Arial", 9)).grid(row=1, column=0, sticky=W)
        self.start_city = StringVar()
        self.source = Entry(form, width=4, textvar=self.start_city)
        self.source.grid(row=1, column=1, sticky=W)

        Label(form, text="Target city:", font=("Arial", 9)).grid(row=2, column=0, sticky=W)
        self.target_city = StringVar()
        self.target = Entry(form, width=4, textvar=self.target_city)
        self.target.grid(row=2, column=1, sticky=W)

        self.verb = IntVar()
        self.verbose = Checkbutton(form, text="Show paths", variable=self.verb, font=("Arial", 9))
        self.verbose.grid(row=3, column=0, sticky=W)

        self.btn_depth = Button(form,
                                text="Depth First",
                                command=self.__apply_depth_first,
                                state="disabled",
                                font=("Arial", 9),
                                width=14)
        self.btn_depth.grid(row=4, column=0, sticky=E, pady=8)
        self.btn_breadth = Button(form,
                                  text="Breadth First",
                                  command=self.__apply_breadth_first,
                                  state="disabled",
                                  font=("Arial", 9),
                                  width=14)
        self.btn_breadth.grid(row=4, column=1, sticky=W, pady=8)
        self.btn_recursive = Button(form,
                                    text="Recursive Search",
                                    command=self.__apply_recursive_search,
                                    state="disabled",
                                    font=("Arial", 9),
                                    width=14)
        self.btn_recursive.grid(row=4, column=2, sticky=W, pady=8)
        self.btn_dijkstra = Button(form,
                                   text="Dijkstra",
                                   command=self.__apply_dijkstra,
                                   state="disabled",
                                   font=("Arial", 9),
                                   width=14)
        self.btn_dijkstra.grid(row=4, column=3, sticky=W, pady=8)

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
        self.__set_btn_states("disabled")
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
        if n < 10:
            self.text.append_text("\n" + self.graph.as_matrix() + "\n")
            self.text.append_text("Edge notation: X:Y, where X = target vertex and Y = distance (weight of edge)\n")
            self.text.append_text(self.graph.as_graph() + "\n")
        self.__set_btn_states("normal")

    def __apply_depth_first(self):
        self.__apply_search(self.__thread_depth_first)

    def __apply_breadth_first(self):
        self.__apply_search(self.__thread_breadth_first)

    def __apply_recursive_search(self):
        self.__apply_search(self.__thread_recursive_search)

    def __apply_dijkstra(self):
        self.__apply_search(self.__thread_dijkstra)

    def __apply_search(self, callback):
        params = self.__validate_city_inputs()
        if params is None:
            return
        if self.graph.n > 12:
            msg = "This might cause your system to become unstable, depending on your computing power!\n"
            msg += "Be aware of potential stack overflow or memory out issues and continue at your own risk."
            if not messagebox.askokcancel("Warning!", msg, icon=messagebox.WARNING):
                return
        (source, target) = params
        self.__set_btn_states("disabled")

        thread = Thread(target=callback, args=(source, target))
        thread.daemon = True
        thread.start()

    def __thread_depth_first(self, source, target):
        self.__thread("DFS", source, target)

    def __thread_breadth_first(self, source, target):
        self.__thread("BFS", source, target)

    def __thread_recursive_search(self, source, target):
        self.__thread("Recursive search", source, target)

    def __thread_dijkstra(self, source, target):
        self.text.append_text("Starting Dijkstra thread...\n")
        Tools.Tools.master.update_idletasks()
        timer = Tools.Timer()
        timer.start()
        path = self.graph.dijkstra(source, target)
        secs = timer.stop()
        self.text.append_text("Dijkstra thread took %f seconds to complete\n" % secs)
        dist = self.graph[target][target]
        if dist is None:
            dist = "Infinite"
        else:
            dist = str(dist)
        weights = []
        for ix in range(len(path) - 1):
            weights.append("%d -> %d : %d" % (path[ix]+1, path[ix+1]+1, self.graph[min(path[ix], path[ix+1])][max(path[ix], path[ix+1])]))
        self.text.append_text(", ".join(s for s in weights) + "\n")
        self.text.append_text("Shortest path: %s %s\n" % (dist, "[" + " -> ".join(["%d" % (p+1) for p in path]) + "]\n"))
        # self.text.append_text(self.graph.as_matrix()+"\n")        # Debugging
        self.__set_btn_states("normal")

    def __thread(self, script, source, target):
        self.text.append_text("Starting %s thread...\n" % script)
        Tools.Tools.master.update_idletasks()
        timer = Tools.Timer()
        timer.start()
        if script == "DFS":
            paths = self.graph.find_paths_depth(source, target)
        elif script == "BFS":
            paths = self.graph.find_paths_breadth(source, target)
        else:
            paths = self.graph.find_paths_recursive(source, target)
        secs = timer.stop()
        self.text.append_text("%s thread took %f seconds and returned %d possible paths\n" % (script, secs, len(paths)))
        if self.verb.get() == 1:
            self.text.append_text("Paths from city %d to city %d:\n" % (source + 1, target + 1))
            if len(paths) > 0:
                for path in paths:
                    self.text.append_text(" -> ".join([str(x + 1) for x in path]) + "\n")
            else:
                self.text.append_text("No path found\n")
        (dist, path) = self.graph.calc_shortest(paths)
        try:
            self.text.append_text("Shortest path: %d %s\n" % (dist, "[" + " -> ".join([str(x + 1) for x in path]) + "]\n"))
        except:
            self.text.append_text("Distance: %s, path: %s\n" % (dist, path))
        self.__set_btn_states("normal")

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

    def __set_btn_states(self, state):
        self.gen_graph.configure(state=state)
        self.btn_breadth.configure(state=state)
        self.btn_depth.configure(state=state)
        self.btn_recursive.configure(state=state)
        self.btn_dijkstra.configure(state=state)










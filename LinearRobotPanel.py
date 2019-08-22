"""
    UFRPE - BSI2019.2
    Author: Edson Kropniczki
    Description: GUI to implement linear robot lazy algorithm
"""


from tkinter import *
from tkinter import messagebox
import ScrollableText
import LinearRobot


class LinearRobotPanel:

    def __init__(self, frame):

        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)

        wrap = Frame(frame)
        wrap.grid({"row": 0, "column": 0, "sticky": NSEW})
        wrap.grid_rowconfigure(2, weight=1)
        wrap.grid_columnconfigure(0, weight=1)

        header = Frame(wrap)
        header.grid({"row": 0, "column": 0, "sticky": NSEW})
        l1 = Label(header, {"text": "Algorithm to find robot position using regular expressions",
                            "font": ("Arial", 12)})
        l1.grid({"row": 0, "column": 0})

        form = Frame(wrap, {"pady": 8, "padx": 8})
        form.grid({"row": 1, "column": 0, "sticky": NSEW, "pady": 8, "padx": 8})

        # random string button
        params = {"text": "Generate random string",
                  "width": 20,
                  "font": ("Arial", 10),
                  "command": self._gen_string
                  }
        Button(form, params).grid({"row": 0, "column": 0, "sticky": W})

        # regular expression button
        params = {"text": "Apply regular expression",
                  "width": 20,
                  "font": ("Arial", 10),
                  "command": self._reg_exp
                  }
        Button(form, params).grid({"row": 2, "column": 0, "sticky": W})

        # robot position button
        params = {"text": "Determine robot position",
                  "width": 20,
                  "font": ("Arial", 10),
                  "command": self._calc_position
                  }
        Button(form, params).grid({"row": 3, "column": 0, "sticky": W})

        text = Frame(wrap, {"pady": 8, "padx": 8})
        text.grid({"row": 4, "column": 0, "sticky": NSEW})
        text.grid_columnconfigure(0, weight=1)
        text.grid_rowconfigure(0, weight=1)
        self.text = ScrollableText.ScrollableText(text)

    def _gen_string(self):
        pass

    def _reg_exp(self):
        pass

    def _calc_position(self):
        pass








import re
import random

MAX_STEP_BLOCKS = 100       # max. nr. of T or F blocks in command string
MAX_NUM_STEPS = 50          # max. nr. of in-tandem T or F commands in blocks


class LinearRobot:

    def __init__(self):
        self.command = self.result = self.position = None
        self.pattern = r"(F*)T*"                # regular expression pattern to filter out only Fs from an FT string

    # generate a MAX_NUM_STEPS X MAX_BLOCKS F-T command string
    def gen_rnd_str(self):
        self.command = ""
        for i in range(int(1 + random.random()*MAX_STEP_BLOCKS)):
            step = "F"
            if random.random() > .5:
                step = "T"
            self.command += step * int(1 + random.random() * MAX_NUM_STEPS)

    # use regular expression pattern to sift through F's in command string
    def apply_reg_exp(self):
        if self.command is None:
            return
        self.result = re.findall(self.pattern, self.command)
        # discard empty strings
        self.result = [x for x in self.result if len(x) > 0]

    # calculate robot final landing position
    def calc_robot_pos(self):
        if self.result is None:
            return
        f_count = len("".join(self.result))
        t_count = len(self.command) - f_count
        self.position = f_count - t_count








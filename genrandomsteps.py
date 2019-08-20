import random

MAX_STEP_BLOCKS = 100
MAX_NUM_STEPS = 50


def gen_rnd_str():
    ret = ""
    for i in range(int(1 + random.random()*MAX_STEP_BLOCKS)):
        step = "F"
        if random.random() > .5:
            step = "T"
        ret += step*int(1 + random.random()*MAX_NUM_STEPS)
    return ret


"""
    See https://olimpiada.ic.unicamp.br/pratique/pu/2017/f2/papel/ for details
"""

import random


class CuttingPaper(list):

    MAX_HEIGHT = 15
    MIN_HEIGHT = 5
    RECTS = 30

    def __init__(self):
        super(CuttingPaper, self).__init__()
        self.heights = []

    def __gen_random_height(self):
        return int(CuttingPaper.MIN_HEIGHT + random.random()*(CuttingPaper.MAX_HEIGHT - CuttingPaper.MIN_HEIGHT))

    def gen_paper(self):
        del self.heights[:]
        self.heights = [self.__gen_random_height() for x in range(CuttingPaper.RECTS)]
        return self.heights

    def cut_paper(self):
        print(self.heights)                     # debug
        # get unrepeated heights of rectangles
        tops = list(set(self.heights))
        cuts = {}
        for top in tops:
            cutting = False
            cuts[top] = 0
            for height in self.heights:
                if height > top:
                    if not cutting:
                        cutting = True
                        cuts[top] = cuts[top] + 1
                else:
                    cutting = False
        return {key: cuts[key] + 1 for key in cuts.keys() if cuts[key] == max(cuts.values())}











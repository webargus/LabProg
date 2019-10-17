"""
    UFRPE- BSI - 2009.2 - Programming Lab - Paper cutting exercise
    Author: Edson Kropniczki - kropniczki@gmail.com
    License: feel free to improve this code, but remember to keep this header
    Disclaimer: use it at your own risk!

    See https://olimpiada.ic.unicamp.br/pratique/pu/2017/f2/papel/ for details
    Overall script strategy detailed in method CuttingPaper.cut_paper down below
"""

import random                   # needed to generate random paper slips (rectangle heights)


class CuttingPaper(list):

    MAX_HEIGHT = 15             # max height of paper slips
    MIN_HEIGHT = 5              # min paper slip height
    RECTS = 30                  # max no. of paper slips displayed horizontally

    def __init__(self):
        super(CuttingPaper, self).__init__()
        self.peaks = []

    # ancillary private method to generate paper slip when creating random paper shape
    def __gen_random_height(self):
        return int(CuttingPaper.MIN_HEIGHT + random.random()*(CuttingPaper.MAX_HEIGHT - CuttingPaper.MIN_HEIGHT))

    # generate paper shape and save paper slip heights to self.heights member
    def gen_paper(self):
        del self.peaks[:]
        self.peaks = [self.__gen_random_height() for x in range(CuttingPaper.RECTS)]
        return self.peaks

    # walk along each paper valley and count a cut
    # whenever we cross one or more slips higher than current valley
    #  _     _
    # | |  _| |         peaks
    # | |_|   |_        valleys
    #
    def cut_paper(self):
        print(" ".join([str(x) for x in self.peaks]))                     # debug
        # get unrepeated valleys from shape
        valleys = list(set(self.peaks))
        # accumulate valley heights and their respective no. of cuts as key-value pairs in dict
        cuts = {}
        for valley in valleys:
            cutting = False             # bool flag raised when we're cutting through paper
            cuts[valley] = 0            # initialize valley cuts with zero, for we haven't cut any relative peak yet
            for height in self.peaks:   # check how all peaks compare with current valley
                if height > valley:     # if we hit a peak higher than current valley ...
                    if not cutting:     # ... while not cutting, then start doing it
                        cutting = True
                        cuts[valley] = cuts[valley] + 1     # add a cut through current valley
                else:
                    cutting = False     # we finish cutting when falling in a valley again
        # return valleys for which we got a maximum no. of cuts as dict key-value pairs
        return {key: cuts[key] + 1 for key in cuts.keys() if cuts[key] == max(cuts.values())}











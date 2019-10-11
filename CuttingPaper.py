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
        down = False
        pits = []
        top1 = []
        top2 = []
        top = None
        for i in range(len(self.heights) - 1):

            if self.heights[i] == self.heights[i + 1]:
                continue

            if self.heights[i] > self.heights[i + 1]:       # going down

                if not down:
                    print("top: %s" % str(top))
                    if top is None:
                        top = self.heights[i]
                    else:
                        top1.append(min(top, self.heights[i]))
                        top2.append(max(top, self.heights[i]))
                        top = self.heights[i]
                    down = True

            else:                                           # going up

                if down:                                    # if was going down, we found a pit
                    pits.append(self.heights[i])
                    down = False

        if not down:
            top1.append(min(top, self.heights[len(self.heights) - 1]))

        print("pits", pits)
        print("tops", top1)

        cuts = []
        for ix in range(len(pits)):
            cuts.append(0)
            for iy in range(len(pits)):
                if ix == iy:
                    continue
                if pits[iy] <= pits[ix]:
                    if top1[iy] > pits[ix]:
                        cuts[ix] += 1
                    elif top2[iy] > pits[ix]:
                        cuts[ix] += 1

        print("cuts: ", cuts)

        pieces = 1
        if len(cuts) > 0:
            pieces = 2 + max(cuts)
        return pieces, pits[cuts.index(max(cuts))]


"""

while 1:
    try:
        n = int(input("Enter no. of rectangles (1 ≤ N ≤ 10⁵, 0 = abort):"))
        if n == 0:
            exit(0)
        if (n > 10**5) or (n < 1):
            raise ValueError
    except ValueError:
        print("Invalid N, try again (0 = abort)")

    # generate random rectangles (== list of heights)
    print("Generating %d rectangles of random height 1 ≤ A(i) ≤ 10⁹, for 1 ≤ i ≤ %d..." % (n, n))
    rects = [gen_random_height() for x in range(n)]
    print(rects)

    pits = []
    history = [False, False, False]
    for i in range(len(rects) - 1):
        if rects[i] == rects[i + 1]:
            continue
        if rects[i] > rects[i + 1]:
            history[0] = True
        else:
            history[2] = True
            if history[0]:
                history[1] = True
        if history[0] and history[1] and history[2]:
            pits.append(rects[i])
            history = [False, False, False]
    print(pits)

    cuts = []
    for ix in range(len(pits)):
        cuts.append(0)
        for iy in range(len(pits)):
            if ix == iy:
                continue
            if pits[iy] <= pits[ix]:
                cuts[ix] += 1

    print("cuts: ", cuts)

    pieces = 1
    if len(cuts) > 0:
        pieces = 2 + max(cuts)
    print("\nMáximo de pedaços: %d\n" % (pieces + 1))

"""




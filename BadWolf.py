"""
    UFRPE- BSI - 2009.2 - Programming Lab - 'O lobo mau e as ovelhas do Juvenal'
    Due date: oct 1st 2019
    Author: Edson Kropniczki - kropniczki@gmail.com
    License: feel free to improve this code, but remember to keep this header
    Disclaimer: use it at your own risk!
"""


# custom implementation of queue class in Python
class QueueNode:

    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

    def get_data(self):
        return self.data

    def set_next(self, node):
        self.next = node

    def get_prev(self):
        return self.prev

    def set_prev(self, node):
        self.prev = node


class ProgLabQueue:

    def __init__(self):
        self.init = self.end = None
        self.n = 0

    def push(self, data):
        node = QueueNode(data)
        self.n += 1
        if self.init is None:
            self.init = self.end = node
            return
        self.end.set_next(node)
        node.set_prev(self.end)
        self.end = node

    def pop(self):
        if self.init is None:
            raise IndexError
        self.n -= 1
        ret = self.end.get_data()
        if self.init == self.end:
            self.init = self.end = None
            return ret
        self.end = self.end.get_prev()
        self.end.set_next(None)
        return ret

    def __len__(self):
        return self.n


class Farm:

    def __init__(self, n, m):
        # initialize n+2 X m+2 farm STATIC matrix, i.e., 2 lines and 2 rows larger than problem farm area;
        # we'll paste farm input into the center of this matrix and surround it with a fence;
        # notice that the script never appends or removes any element from matrix, just updates it;
        # fill matrix with '#', meaning fence
        self.mtx = [['#' for y in range(m+2)] for x in range(n+2)]

    # python print method overload to help with debugging
    """def __str__(self):
        s = ""
        for x in range(len(self.mtx)):
            for y in range(len(self.mtx[x])):
                s += "{:<2}".format(str(self.mtx[x][y]))
            s += "\n"
        return s"""

    # pasture lookup recursive call, works fine, but abandoned due to stack overflow issues
    def __seek_animal(self, pasture, sheep=0, wolves=0):
        if len(pasture) == 0:
            return sheep, wolves
        i, j = pasture.pop()
        if self.mtx[i][j] != '#':         # this spot hasn't been visited yet, so let's check it out
            spot = self.mtx[i][j]
            if spot == 'k':                    # that's a sheep
                sheep += 1
            elif spot == 'v':                  # that's a wolf
                wolves += 1
            self.mtx[i][j] = '#'          # set spot as visited (use same symbol for fence, since we skip it anyway)
            pasture.push((i, j-1))
            pasture.push((i, j+1))
            pasture.push((i-1, j))
            pasture.push((i+1, j))
        return self.__seek_animal(pasture, sheep, wolves)

    # main class public method: scan farm area looking for sheep and wolves within fences;
    # strategy: check adjacent farm spots breadth-first whenever we stumble across an unvisited farm spot;
    #           count sheep and wolves as we sift through spots
    def scan(self):
        # begin crawling through mtx starting from coords (1,1) all the way to (N,M)
        i = j = 1
        # using custom-made queue for breadth-first pasture lookup
        pasture = ProgLabQueue()
        total_sheep = total_wolves = 0
        while i <= len(self.mtx)-2:
            if self.mtx[i][j] != '#':        # that's not a fence spot, so we're in a pasture
                pasture.push((i, j))
                sheep = wolves = 0
                #
                # gave up calling recursive lookup calls, for exceeding maximum recursion depth consistently
                # when submitting script to run.codes cases;
                # sheep, wolves = self.__seek_animal(pasture)       # <= stack overflow in recursion
                # using iterative loop instead:
                while len(pasture) > 0:
                    i, j = pasture.pop()
                    if self.mtx[i][j] != '#':  # this spot hasn't been visited yet, so let's check it out
                        spot = self.mtx[i][j]
                        if spot == 'k':  # that's a sheep
                            sheep += 1
                        elif spot == 'v':  # that's a wolf
                            wolves += 1
                        # set spot as visited (use same symbol for fence, since we always skip it anyway)
                        self.mtx[i][j] = '#'
                        pasture.push((i, j - 1))
                        pasture.push((i, j + 1))
                        pasture.push((i - 1, j))
                        pasture.push((i + 1, j))
                if sheep > wolves:
                    total_sheep += sheep
                else:
                    total_wolves += wolves
            if j == len(self.mtx[i])-2:                 # update loop pointers
                j = 0
                i += 1
            j += 1
        return total_sheep, total_wolves


# get size of matrix (farm size)
n, m = (int(x) for x in input().split())

# create Farm obj and fill in with problem case inputs
farm = Farm(n, m)
for row in range(n):
    blocks = list(input())
    for col in range(len(blocks)):
        farm.mtx[row+1][col+1] = blocks[col]

# Workaround: for some unknown reason, run.codes is appending 1s to the right-most column of matrix!!
for i in range(len(farm.mtx)):
    farm.mtx[i][len(farm.mtx[i])-1] = '#'


# print(farm)                           # debugging
print("%d %d" % farm.scan())
# print(farm)                           # debugging















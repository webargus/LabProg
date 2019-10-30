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
        # fill matrix with binary 101, meaning fence (bit 0 raised) and visited (bit 2 raised)
        self.mtx = [[0b101 for y in range(m+2)] for x in range(n+2)]

    # all fence spots have been pre-set as visited
    def __seek_animal(self, pasture, sheep=0, wolves=0):
        if len(pasture) == 0:
            return sheep, wolves
        i, j = pasture.pop()
        if self.mtx[i][j] & 0b100 == 0:         # this spot hasn't been visited yet, so let's check it out
            self.mtx[i][j] |= 0b100             # set spot as visited
            spot = self.mtx[i][j] & 0b11
            if spot == 0b10:                    # that's a sheep
                sheep += 1
            elif spot == 0b11:                  # that's a wolf
                wolves += 1
            pasture.push((i, j-1))
            pasture.push((i, j+1))
            pasture.push((i-1, j))
            pasture.push((i+1, j))
        return self.__seek_animal(pasture, sheep, wolves)

    # main class public method: scan farm area looking for sheep and wolves within fences;
    # strategy: check adjacent farm spots breadth-first whenever we stumble across an unvisited farm spot;
    #           count sheep and wolves as we sift through spots
    # convention: 0b00 == empty pasture; 0b01 == fence; 0b10 == sheep; 0b11 == wolf
    def scan(self):
        # begin crawling through mtx starting from coords (1,1) all the way to (N,M)
        i = j = 1
        # using custom-made queue for breadth-first pasture lookup
        pasture = ProgLabQueue()
        total_sheep = total_wolves = 0
        while i <= len(self.mtx)-2:
            if self.mtx[i][j] & 0b111 != 0b101:        # that's NOT a fence spot, so let's check it out
                pasture.push((i, j))
                sheep, wolves = self.__seek_animal(pasture)
                if sheep > wolves:
                    total_sheep += sheep
                else:
                    total_wolves += wolves
            if j == len(self.mtx[i])-2:                 # update loop pointers
                j = 0
                i += 1
            j += 1
        return total_sheep, total_wolves


# get size of matrix (naval battle board size)
n, m = (int(x) for x in input().split())

# input nXm matrix filled with 0b00 (== empty pasture), 0b101 (== visited fence),
# 0b10 (== sheep) and 0b11 (== wolf), respectively
farm = Farm(n, m)
for row in range(n):
    blocks = list(input())
    for col in range(len(blocks)):
        block = 0b101                     # default == visited fence block
        if blocks[col] == '.':
            block = 0b00                  # just pasture
        elif blocks[col] == 'k':
            block = 0b10                  # that's a sheep
        elif blocks[col] == 'v':
            block = 0b11                  # that's a wolf
        farm.mtx[row+1][col+1] = block

print("%d %d" % farm.scan())
















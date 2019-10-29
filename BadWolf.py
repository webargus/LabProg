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

    # python print method overload to help with debugging
    def __str__(self):
        s = ""
        for x in range(len(self.mtx)):
            for y in range(len(self.mtx[x])):
                s += "{:<4}".format(str(self.mtx[x][y]))
            s += "\n"
        return s

    # ancillary private method to add a farm spot to adjacency list if farm spot not visited yet
    def __get_adjacent(self, adj, i, j):
        if self.mtx[i][j] & 0b111 == 0b101:       # that's a fence spot, so do not include it
            return
        self.mtx[i][j] |= 4                       # set farm spot to visited
        adj.push((i, j))                          # and add it to queue for analysis

    # ancillary private method to gather all farm spots surrounding a given (i, j) farm spot
    def __get_adjacents(self, adj, i, j):
        self.__get_adjacent(adj, i, j - 1)
        self.__get_adjacent(adj, i, j + 1)
        self.__get_adjacent(adj, i - 1, j)
        self.__get_adjacent(adj, i + 1, j)

    # main class public method: scan farm area looking for sheep and wolves within fences;
    # strategy: check adjacent farm spots breadth-first whenever we stumble across an unvisited farm spot;
    #           count sheep and wolves as we sift through spots
    def scan(self):
        # begin crawling through mtx starting from coords (1,1) all the way to (N,M)
        i = j = 1
        total_sheep = total_wolves = 0
        while i <= len(self.mtx)-2:
            if self.mtx[i][j] & 0b111 != 0b101:  # that's NOT a fence spot, so let's check it out
                self.mtx[i][j] |= 4                    # set spot as visited
                adj = ProgLabQueue()                   # using custom queue, since we're going to 'append' data
                adj.push((i, j))
                sheep_cnt = wolf_cnt = 0
                while len(adj) > 0:
                    i0, j0 = adj.pop()
                    self.__get_adjacents(adj, i0, j0)
                    flag = self.mtx[i0][j0] and 0b11
                    if flag == 0b10:                       # we found a sheep
                        sheep_cnt += 1
                    elif flag == 0b11:                     # we found a wolf
                        wolf_cnt += 1
                if wolf_cnt >= sheep_cnt:                  # wolves win
                    total_wolves += wolf_cnt
                else:                                      # sheep win
                    total_sheep += sheep_cnt

            if j == len(self.mtx[i])-2:                 # update loop pointers
                j = 0
                i += 1
            j += 1
        return total_sheep, total_wolves

# get size of matrix (naval battle board size)
n, m = (int(x) for x in input().split())

# input nXm matrix filled with 0s and 1s to retrieve water (".") and ship ("#") coordinates, respectively
y = ord(".")
mtx = [[1-ord(x)//y for x in list(input())] for x in range(n)]

# create and fill Board obj
board = Board(n, m)
x = y = 0
while x < len(mtx):
    board.mtx[x + 1][y + 1] = mtx[x][y]
    y += 1
    if y == len(mtx[x]):
        y = 0
        x += 1

# get shots
k = int(input())
for i in range(k):
    x, y = (int(x) for x in input().split())
    board.mtx[x][y] |= 2              # raise bit 2 to flag shot on coordinates (x, y)


print(board.scan())
















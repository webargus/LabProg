"""
    UFRPE- BSI - 2009.2 - Programming Lab - 'Juvenal não confia em ninguém'
    Due date: oct 1st 2019
    Author: Edson Kropniczki - kropniczki@gmail.com
    License: feel free to improve this code, but remember to keep this header
    Disclaimer: use it at your own risk!
"""


# self implementation of queue class in Python
class QueueNode:

    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

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

    def unshift(self, data):
        node = QueueNode(data)
        self.n += 1
        if self.init is None:
            self.init = self.end = node
            return
        self.init.set_prev(node)
        node.set_next(self.init)
        self.init = node

    def shift(self):
        if self.init is None:
            raise IndexError
        self.n -= 1
        ret = self.init.get_data()
        if self.init == self.end:
            self.init = self.end = None
            return ret
        self.init = self.init.get_next()
        self.init.set_prev(None)
        return ret

    def __get_node_at(self, ix):
        if (ix < 0) or (ix >= self.n):
            raise IndexError
        i = 0
        node = self.init
        while i <= ix:
            if i == ix:
                return node
            i += 1
            node = node.get_next()

    def __getitem__(self, key):
        return self.__get_node_at(key).get_data()

    def __setitem__(self, key, data):
        self.__get_node_at(key).set_data(data)

    def __len__(self):
        return self.n


class Board:

    def __init__(self, n, m):
        # initialize n+2 X m+2 battle board static matrix, i.e., 2 lines and 2 rows larger than problem board;
        # we'll copy input board into the center of this matrix and surround it with water;
        # notice that the script never appends or removes any element from matrix, but updates
        self.mtx = [[0 for y in range(m+2)] for x in range(n+2)]

    # python print method overload to help with debugging
    def __str__(self):
        s = ""
        for x in range(len(self.mtx)):
            for y in range(len(self.mtx[x])):
                s += "{:<4}".format(str(self.mtx[x][y]))
            s += "\n"
        return s

    # ancillary private method to add a ship block to adjacency list if ship block not visited yet
    def __get_adjacent(self, adj, i, j):
        if self.mtx[i][j] & 5 == 1:       # not visited and is ship part
            adj.push((i, j))

    # ancillary private method to gather all ship blocks surrounding a given (i, j) ship block
    def __get_adjacents(self, adj, i, j):
        self.__get_adjacent(adj, i, j - 1)
        self.__get_adjacent(adj, i, j + 1)
        self.__get_adjacent(adj, i - 1, j)
        self.__get_adjacent(adj, i - 1, j - 1)
        self.__get_adjacent(adj, i - 1, j + 1)
        self.__get_adjacent(adj, i + 1, j)
        self.__get_adjacent(adj, i + 1, j - 1)
        self.__get_adjacent(adj, i + 1, j + 1)

    # main class public method: scan board looking for sunken ships;
    def scan(self):
        i = j = 1
        total_cnt = 0
        while i <= len(self.mtx)-2:
            if self.mtx[i][j] & 5 == 1:                # ship part not visited yet
                adj = ProgLabQueue()
                adj.push((i, j))
                cnt = 1
                while len(adj) > 0:
                    i0, j0 = adj.pop()
                    self.mtx[i0][j0] |= 4  # set as visited
                    self.__get_adjacents(adj, i0, j0)
                    if self.mtx[i0][j0] & 2 == 0:  # ship part not shot
                        cnt = 0
                total_cnt += cnt

            if j == len(self.mtx[i])-2:
                j = 0
                i += 1
            j += 1
        return total_cnt


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

k = int(input())
for i in range(k):
    x, y = (int(x) for x in input().split())
    board.mtx[x][y] |= 2              # raise bit 2 to imply shot on board coordinates (x, y)

# print(board)        # debug

print(board.scan())

# print(board)        # debug














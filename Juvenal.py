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


class Board:

    def __init__(self, n, m):
        # initialize n+2 X m+2 STATIC battle board matrix, i.e., 2 lines and 2 rows larger than problem board;
        # we'll copy input board into the center of this matrix and surround it with water;
        # notice that the script never appends or removes elements from matrix, only updates them
        self.mtx = [[0 for y in range(m+2)] for x in range(n+2)]

    # class core recursive method: explore connected ship blocks seeking sunken ships;
    # strategy: check adjacent ship blocks breadth-first whenever we stumble across an unvisited block;
    #           we count a ship as sunken only if all ship blocks were hit (bit 2 raised)
    def __explore_ship(self, ship, cnt=1):
        if len(ship) == 0:                      # base case (queue empty => we visited all blocks)
            return cnt
        i, j = ship.pop()
        if self.mtx[i][j] & 0b101 == 1:         # not visited and is ship block
            self.mtx[i][j] |= 0b100             # set to visited
            if self.mtx[i][j] & 0b010 == 0:     # ship block not hit, ship still afloat
                cnt = 0
            # explore left, right, upper and lower matrix blocks for other possible ship blocks
            ship.push((i, j-1))
            ship.push((i, j+1))
            ship.push((i-1, j))
            ship.push((i+1, j))
        return self.__explore_ship(ship, cnt)

    def scan(self):
        # for some unknown reason, run.codes adds 1s to the right-most column of matrix;
        # it never happens either in URI judge, OBI, or in my own comp;
        # work-around: fill in right-most column back again with zeroes!
        # OBI: https://olimpiada.ic.unicamp.br/pratique/p2/2010/f1/batalha/
        # URI: https://www.urionlinejudge.com.br/judge/pt/problems/view/2371
        for i in range(len(self.mtx)):
            self.mtx[i][len(self.mtx[i])-1] = 0
        ship = ProgLabQueue()
        # begin crawling through mtx starting from coords (1,1) all the way to (N,M)
        i = j = 1
        total_cnt = 0                                   # var to accumulate global wrecked ship count
        while i <= len(self.mtx)-2:
            if self.mtx[i][j] & 0b101 == 1:             # ship part, not visited yet, so explore it
                ship.push((i, j))
                total_cnt += self.__explore_ship(ship)
            if j == len(self.mtx[i])-2:                 # update loop pointers
                j = 0
                i += 1
            j += 1
        return total_cnt

# ------------------------------------------------------------------------------------------
#   DATA INPUT SECTION

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

# shoot into board
k = int(input())
for i in range(k):
    x, y = (int(x) for x in input().split())
    board.mtx[x][y] |= 0b10              # raise bit 1 to flag shot on coordinates (x, y)

print(board.scan())

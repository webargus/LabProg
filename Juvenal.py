
class NavalBattle:

    def __init__(self, n, m):
        self.mtx = [[0 for y in range(m+2)] for x in range(n+2)]
        self.adj = []

    def __str__(self):
        s = ""
        for x in range(len(self.mtx)):
            for y in range(len(self.mtx[x])):
                s += "{:<4}".format(str(self.mtx[x][y]))
            s += "\n"
        return s

    def __get_adjacent(self, adj, i, j):
        if self.mtx[i][j] & 5 == 1:       # not visited and is ship part
            adj.append((i, j))

    def __get_adjacents(self, adj, i, j):
        self.__get_adjacent(adj, i, j - 1)
        self.__get_adjacent(adj, i, j + 1)
        self.__get_adjacent(adj, i - 1, j)
        self.__get_adjacent(adj, i - 1, j - 1)
        self.__get_adjacent(adj, i - 1, j + 1)
        self.__get_adjacent(adj, i + 1, j)
        self.__get_adjacent(adj, i + 1, j - 1)
        self.__get_adjacent(adj, i + 1, j + 1)

    def scan(self):
        i = j = 1
        total_cnt = 0
        while i <= len(self.mtx)-2:
            if self.mtx[i][j] & 5 == 1:                # ship part not visited yet
                adj = [(i, j)]
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


n, m = (int(x) for x in input().split())

y = ord(".")
nb = NavalBattle(n, m)
mtx = [[1-ord(x)//y for x in list(input())] for x in range(n)]
x = y = 0
while x < len(mtx):
    nb.mtx[x+1][y+1] = mtx[x][y]
    y += 1
    if y == len(mtx[x]):
        y = 0
        x += 1

k = int(input())
for i in range(k):
    x, y = (int(x) for x in input().split())
    nb.mtx[x][y] |= 2

print(nb)

print(nb.scan())

print(nb)
"""
5 5
..###
.....
#####
.....
#.##.
5
5 1
5 2
1 3
1 4
1 5

5 5
..#.#
#....
...#.
#....
...#.
5
1 3
1 4
1 5
2 1
3 4

7 7
.#....#
###..##
.#....#
....#.#
.#..#.#
.####.#
.......
8
1 1
1 2
2 1
2 2
2 3
3 2
5 2
6 2

"""

















class Point:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __getattr__(self, item):
        if item == "coords":
            return self.x, self.y


class Regions(list):

    def __init__(self):
        super(Regions, self).__init__()

    def exists(self, region):
        for r in self:
            if r == region:
                return True
        return False


class Region:

    def __init__(self, v0=Point(), v1=Point()):
        self.v0 = v0
        self.v1 = v1

    def __eq__(self, other):
        return (self.v0 == other.v0) and (self.v1 == other.v1)

    def width(self):
        return abs(self.v1.x - self.v0.x)

    def height(self):
        return abs(self.v1.y - self.v0.y)

    def size(self):
        return self.width()*self.height()

    def intersect(self, other):

        '''
       other.v0 +------+
                |  A   |
    self.v0 +---+------+----+
            | B |  C   |  D |
            +---+------+----+ self.v1
                |  E   |
                +------+ other.v1
        '''

        flag = (other.v0.x >= self.v0.x) and (other.v0.y <= self.v0.y) and (other.v1.x <= self.v1.x) and (other.v1.y >= self.v1.y)
        if flag:
            regs = [Region(other.v0, Point(other.v1.x, self.v0.y)),                         # region A
                    Region(self.v0, Point(other.v0.x, self.v1.y)),                          # region B
                    Region(Point(other.v0.x, self.v0.y), Point(other.v1.x, self.v1.y)),     # region C
                    Region(Point(other.v1.x, self.v0.y), self.v1),                          # region D
                    Region(Point(other.v0.x, self.v1.y), other.v1)]                         # region E
            # return only non zero size regions
            return [reg for reg in regs if reg.size() > 0]
        '''
        self.v0 +------+
                |   A  |
   other.v0 +---+------+----+
            | B |   C  |  D |
            +---+------+----+ other.v1
                |   E  |
                +------+ self.v1
        '''
        flag = (self.v0.x >= other.v0.x) and (self.v0.y <= other.v0.y) and (self.v1.x <= other.v1.x) and (self.v1.y >= other.v1.y)
        if flag:
            regs = [Region(self.v0, Point(self.v1.x, other.v0.y)),                          # region A
                    Region(other.v0, Point(self.v0.x, other.v1.y)),                         # region B
                    Region(Point(self.v0.x, other.v0.y), Point(self.v1.x, other.v1.y)),     # region C
                    Region(Point(self.v1.x, other.v0.y), Point(other.v1)),                  # region D
                    Region(Point(self.v0.x, other.v1.y), self.v1)]                          # region E
            return [reg for reg in regs if reg.size() > 0]











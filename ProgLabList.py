

class ProgLabListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class ProgLabList:

    def __init__(self):
        self.init = self.end = None
        self.n = 0

    def push(self, data):
        node = ProgLabListNode(data)
        if self.init is None:
            self.init = self.end = node
        self.end.set_next(node)
        self.end = node
        self.n += 1

    def __getitem__(self, ix):
        if 0 > ix >= self.n:
            raise IndexError
        i = 0
        node = self.init
        while i <= ix:
            if i == ix:
                return node
            i += 1
            node = node.get_next()

    def __setitem__(self, key, value):
        node = self.__getitem__(key)
        node.set_data(value)

    def __str__(self):
        s = "["
        i = 0
        node = self.init
        while i < self.n:
            s += str(node.get_data())
            if i < self.n - 1:
                s += ", "
            node = node.get_next()
            i += 1
        return s + "]"


l0 = ProgLabList()
l0.push(1)
l0.push(3)
l0.push(5)
l0[1] = 17
print(l0)









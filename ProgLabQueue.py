
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



queue = ProgLabQueue()
queue.push(1)
queue.push(5)
queue.push("test")
print(len(queue))
print(queue)
print(queue.pop())
print(queue.pop())
print(queue.pop())
print(len(queue))
queue.unshift("great")
queue.unshift("is")
queue.unshift("Edson")
queue[2] = "wonderful"
print(queue[0])
print(queue)
print(queue.shift())
print(queue.shift())
print(queue.shift())
print(queue)
print("len=", len(queue))
















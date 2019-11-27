

class StackNode:

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


class Stack:

    def __init__(self):
        self.init = self.end = None

    def push(self, data):
        node = StackNode(data)
        if self.init is None:
            self.init = self.end = node
            return
        self.end.set_next(node)
        node.set_prev(self.end)
        self.end = node

    def pop(self):
        if self.init is None:
            raise IndexError
        ret = self.end.get_data()
        if self.init == self.end:
            self.init = self.end = None
            return ret
        self.end = self.end.get_prev()
        self.end.set_next(None)
        return ret

    def is_empty(self):
        return self.init is None


t = int(input())

inp = 0                                         # input counter
while inp < t:
    a = input()                                 # get chain input
    stack = Stack()                             # create stack
    chain_ok = True                             # assume chain is well formed
    for character in a:
        # push chain opening chars {, [ or ( on top of stack
        if (character == '{') or (character == '[') or (character == '('):
            stack.push(character)
        else:
            # if char was not a chain opener, it must be a matching chain closing character
            if stack.is_empty():                # missing chain opener if stack is empty,
                chain_ok = False                # so abort with chain_ok indicating chain mal-formation
                break
            else:
                # retrieve last chain opener back from top of stack
                # and check if it matches chain closure char
                pop = stack.pop()
                if ((character == '}') and (pop == '{')) or ((character == ']') and (pop == '[')) or ((character == ')') and (pop == '(')):
                    continue
                else:
                    chain_ok = False        # abort if mal-formation detected
                    break
    # stack must always come out empty from loop, since the count of chain opening chars must
    # always match the count of closing ones
    if not stack.is_empty():
        chain_ok = False
    # print output
    if chain_ok:
        print("S")
    else:
        print("N")
    # go fetch next chain input
    inp += 1


"""
12
()
[]
{}
(]
}{
([{}])
{}()[]
()]
{[]
(
(([{}{}()[]])(){}){}
(((((((((({([])}])))))))))
"""








import math
from StacksAndQueues.Stack import StackNode,EmptyStackError

class StackNodeTrack(StackNode):
    def __init__(self, data, minimum):
        super().__init__(data)
        self.minimum = minimum


class StackMin():
    def __init__(self):
        self.top = None
        self.min_item = math.inf

    def push(self,data):
        node = StackNodeTrack(data,self.min_item)
        if data < self.min_item:
            self.min_item = data
        node.next = self.top
        self.top = node

    def pop(self):
        if self.top is None:
            raise EmptyStackError
        else:
            data = self.top.data
            self.min_item = self.top.minimum
            self.top = self.top.next
            return data

    def minf(self):
        return self.min_item

s = StackMin()

s.push(4)
s.push(5)
s.push(10)
s.push(1)
s.push(0)

print(s.minf())


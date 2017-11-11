from StacksAndQueues.Exceptions import EmptyStackError

class StackNode:
    # define __init__
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    # define __init__
    def __init__(self):
        self.top = None

    # define push operation
    def push(self,data):
        node = StackNode(data)
        node.next = self.top
        self.top = node

    # define pop operation
    def pop(self):
        if self.top is None:
            raise EmptyStackError
        else:
            data = self.top.data
            self.top = self.top.next
            return data

    # define peek function
    def seek(self):
        if self.top is None:
            raise EmptyStackError
        else:
            return self.top.data

    # define isEmpty fucntion
    def is_empty(self):
        return self.top is None





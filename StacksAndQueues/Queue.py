from StacksAndQueues.Exceptions import NoSuchElementError

class QueueNode:
    # implement init
    def __init__(self,data):
        self.data = data
        self.next = None

    #implement str
    def __str__(self):
        return str(self.data)

class Queue:
    #implement init
    def __init__(self):
        self.first = None
        self.last = None

    def __str__(self):
        string = ""
        head = self.first
        while head:
            string += str(head.data)
            if head.next is not None:
                string += " <= "
            head = head.next
        return string



    # define add
    def add(self, data):
        node = QueueNode(data)
        if self.last is not None:
            self.last.next = node
        self.last = node
        if self.first is None:
            self.first = self.last


    # define remove
    def remove(self):
        if self.first is None:
            raise NoSuchElementError
        data = self.first.data
        self.first = self.first.next

        if self.first is None:
            self.last = None

    # define peek
    def peek(self):
        if self.first is None:
            raise NoSuchElementError
        return self.first.data

    # define is_empty
    def is_empty(self):
        return self.first is None




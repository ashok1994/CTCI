from random import randint
class Node:
    def __init__(self, number, prev_node=None, next_node=None):
        self.prev = prev_node
        self.next = next_node
        self.data = number

    def __str__(self):
        return str(self.data)


class LinkedList:
    # Implement __init__ function take array of values and create a linked list
    def __init__(self, values=None):
        self.head = self.tail = None
        if values is not None:
            self.add_multiple(values)

    # Implement __iter__ function, look at generator functions
    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    # Implement __str__ function , values separated by ->
    def __str__(self):
        values = []
        curr = self.head
        while curr is not None:
            values.append(str(curr.data))
            curr = curr.next
        return ' -> '.join(values)

    # Implement __len__ function , Find the length of the linked list
    def __len__(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count

    # Implement add(self, value) function , add an element to the tail
    def add(self, value):
        node = Node(value)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = self.tail.next
        return node

    # Implement add_to_beginning(self, value) function, add an element to the head
    def add_to_beginning(self, value):
        if self.head is None:
            self.head = self.tail = Node(value)
        else:
            node = Node(value)
            node.next = self.head
            self.head = node
        return self

    # Implement add_multiple(self, values) function, add multiple values to the end
    def add_multiple(self, values):
        for v in values:
            self.add(v)
        return self
    # Implement generate(n, min_value, max_value) , generates n length linked list with random number, start with empty
    def generate(self, n, min_value, max_value):
        self.head = self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self


class DoublyLinkedList(LinkedList):

    # override add(value) method to link both ways
    def add(self, value):
        if self.head is None:
            self.tail = self.head = Node(value,None,self.tail)
        else:

            self.tail.next = Node(value)
            # Fix : Connect to prev node
            self.tail.next.prev = self.tail
            self.tail = self.tail.next

        return self



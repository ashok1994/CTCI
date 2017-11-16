"""
    Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
    Therefore, in real life we would likely start a new stack when the previous stack exceeds some threshold.
    Implement a data structure SetOfStacks that mimics this. SetOfStacks should be composed of several stacks
    and should create a new stack once the previous one exceeds capacity. SetOfStacks.push() and SetOfStacks.pop()
    should behave identically to a single stack (that is, pop() should return the same values as it would if there
    were just a single stack).

    FOLLOW UP
    Implement a function popAt(int index) which performs a pop operation on a specific sub stack.
"""


class StackLimited:
    def __init__(self, size):
        self.max_size = size
        self.elems = []
        self.curr_pos = 0

    def push(self, data):
        if len(self.elems) == self.max_size:
            return -1
        else:
            self.elems.append(data)
            self.curr_pos += 1

    def pop(self):
        if len(self.elems) == 0:
            return -1
        else:
            self.curr_pos -= 1
            return self.elems.pop()

    def is_empty(self):
        if self.curr_pos == 0:
            return True
        return False

    def is_full(self):
        if len(self.elems) == self.max_size:
            return True
        return False

class SetOfStacks:
    def __init__(self, max_size_per_stack):
        self.stacks = []
        self.max_size_per_stack = max_size_per_stack
        stack = StackLimited(max_size_per_stack)
        self.stacks.append(stack)
        self.currentStack = 0

    def inc_size(self):
        print("Incrementing")
        new_stack = StackLimited(self.max_size_per_stack)
        self.stacks.append(new_stack)
        self.currentStack += 1


    def dec_size(self):
        if len(self.stacks) == 1:
            return None
        print("Decrementing")
        self.stacks.pop()
        self.currentStack -= 1

    def is_current_stack_empty(self):
        return self.stacks[self.currentStack].is_empty()

    def is_current_stack_full(self):
        return self.stacks[self.currentStack].is_full()

    def push(self, data):
        if self.is_current_stack_full():
            self.inc_size()
        stack = self.stacks[self.currentStack]
        stack.push(data)

    def pop(self):
        if self.is_current_stack_empty():
            self.dec_size()
        val = self.stacks[self.currentStack].pop()
        if val == -1:
            raise Exception("Empty stack")
        else:
            return val



set1 = SetOfStacks(4)

set1.push(1)
set1.push(2)
set1.push(6)
set1.push(8)
set1.push(10)
print(set1.pop())


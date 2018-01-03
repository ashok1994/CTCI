from StacksAndQueues.Stack import Stack
from StacksAndQueues.Exceptions import EmptyStackError

class MyQueue:
    def __init__(self):
        self.inbox = Stack()
        self.outbox = Stack()

    def enqueue(self, item):
        self.inbox.push(item)

    def dequeue(self):
        if self.outbox.is_empty():
            if self.inbox.is_empty():
                raise Exception("Empty queue")
            else:
                while not self.inbox.is_empty():
                    try:
                        self.outbox.push(self.inbox.pop())
                    except EmptyStackError:
                        continue
                    except:
                        print("Error occured")

        return self.outbox.pop()



q = MyQueue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
q.enqueue(7)
print(q.dequeue())
print(q.dequeue())

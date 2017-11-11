
class ThreeStack:
    def __init__(self):
        self.arr = [None for x in range(12)]
        self.top1 = None
        self.top2 = None
        self.top3 = None

    def check_valid_pos(self, pos):
        return pos>=0 and pos < 12


    def pushOne(self,data):
        if self.top1 is None:
            self.arr[0] = data
            self.top1 = 0
        else:
            pos = self.top1 + 3
            if self.check_valid_pos(pos):
                self.arr[pos] = data
                self.top1 = pos
            else:
                raise Exception("Stack Overflow")


    def pushTwo(self,data):
        if self.top2 is None:
            self.arr[1] = data
            self.top2 = 1
        else:
            pos = self.top2 + 3
            if self.check_valid_pos(pos):
                self.arr[pos] = data
                self.top2 = pos
            else:
                raise Exception("Stack Overflow")

    def pushThree(self,data):
        if self.top3 is None:
            self.arr[2] = data
            self.top3 = 2
        else:
            pos = self.top3 + 3
            if self.check_valid_pos(pos):
                self.arr[pos] = data
                self.top3 = pos


    def popOne(self):
        if self.top1 is None:
            raise Exception("Stack underflow")
        else:
            data = self.arr[self.top1]
            pos = self.top1 - 3
            self.arr[self.top1] = None
            if self.check_valid_pos(pos):
                self.top1 = pos
            else:
                self.top1 = None

    def popTwo(self):
        if self.top2 is None:
            raise Exception("Stack underflow")
        else:
            data = self.arr[self.top2]
            pos = self.top2 - 3
            self.arr[self.top2] = None
            if self.check_valid_pos(pos):
                self.top2 = pos
            else:
                self.top2 = None

    def popThree(self):
        if self.top3 is None:
            raise Exception("Stack underflow")
        else:
            data = self.arr[self.top3]
            pos = self.top3 - 3
            self.arr[self.top3] = None
            if self.check_valid_pos(pos):
                self.top3 = pos
            else:
                self.top3 = None

    def seekOne(self):
        if self.top1 is None:
            raise Exception("No such element")
        else:
            return self.arr[self.top1]

    def seekTwo(self):
        if self.top2 is None:
            raise Exception("No such element")
        else:
            return self.arr[self.top2]

    def seekThree(self):
        if self.top3 is None:
            raise Exception("No such element")
        else:
            return self.arr[self.top3]


ts = ThreeStack()
ts.pushOne(1)
ts.pushOne(2)
ts.pushOne(2)
ts.pushOne(2)
ts.pushTwo(3)
print(ts.seekTwo())

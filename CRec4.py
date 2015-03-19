class CRec4:
    num = 0
    def __init__(self, num=0):
        self.overlap0 = [
            [4001,4001,4001,4001],
            [4002,4002,4002,4002],
            [4001,4001,4001,4001],
            [4002,4002,4002,4002]]
        self.overlap1 = None
        self.overlap2 = None
        self.overlap3 = None
        self.num = num

    def decrement(self):
        e = not self.empty()
        if e:
            self.num -= 1
        return e

    def increment(self):
        self.num += 1

    def empty(self):
        if self.num > 0:
            return False
        return True


    def isComposed(self):
        return True
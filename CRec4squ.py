class CRec4squ:
    num = 0
    def __init__(self, num=0):
        self.overlap0 = [
            [8001,8001,8002,8002],
            [8001,8001,8002,8002],
            [8002,8002,8001,8001],
            [8002,8002,8001,8001]]
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
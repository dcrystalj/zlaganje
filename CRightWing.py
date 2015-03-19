class CRightWing:
    def __init__(self, num=0):
        self.overlap0 = [
            [5,-1,-1,-1],
            [5,5,-1,-1],
            [-1,5,-1,-1],
            [-1,-1,-1,-1]]
        self.overlap1 = [
            [-1,5,5,-1],
            [5,5,-1,-1],
            [-1,-1,-1,-1],
            [-1,-1,-1,-1]]
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
        return False
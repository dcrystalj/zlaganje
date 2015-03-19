class CJ:
    def __init__(self, num=0):
        self.overlap0 = [
            [-1,3,-1,-1],
            [-1,3,-1,-1],
            [3,3,-1,-1],
            [-1,-1,-1,-1]]
        self.overlap1 = [
            [3,3,3,-1],
            [-1,-1,3,-1],
            [-1,-1,-1,-1],
            [-1,-1,-1,-1]]
        self.overlap2 = [
            [3,3,-1,-1],
            [3,-1,-1,-1],
            [3,-1,-1,-1],
            [-1,-1,-1,-1]]
        self.overlap3 = [
            [3,-1,-1,-1],
            [3,3,3,-1],
            [-1,-1,-1,-1],
            [-1,-1,-1,-1]]
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
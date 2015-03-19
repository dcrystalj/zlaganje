class CL:
    def __init__(self, num=0):
        self.overlap0 = [
            [2,-1,-1,-1],
            [2,-1,-1,-1],
            [2,2,-1,-1],
            [-1,-1,-1,-1]]
        self.overlap1 = [
            [-1,-1,2,-1],
            [2,2,2,-1],
            [-1,-1,-1,-1],
            [-1,-1,-1,-1]]
        self.overlap2 = [
            [2,2,2,-1],
            [2,-1,-1,-1],
            [-1,-1,-1,-1],
            [-1,-1,-1,-1]]
        self.overlap3 = [
            [2,2,-1,-1],
            [-1,2,-1,-1],
            [-1,2,-1,-1],
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
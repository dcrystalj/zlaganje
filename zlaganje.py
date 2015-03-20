from numpy import *
from CRec4 import *
from CRec4L import *
from CRec4J import *
from CRec4K import *
from CRec4squ import *
from CRectangle import *
from CL import *
from CJ import *
from CLeftWing import *
from CRightWing import *
from CK import *
from CSquare import *
from Zlaganje import *

class Zlaganje:
    #define properties
    n_rectangle = 0
    n_L = 0
    n_J = 0
    n_leftWing = 0
    n_rightWing = 0
    n_K = 0
    n_square = 0
    rectangle = 0
    L = 0
    J = 0
    leftWing = 0
    rightWing = 0
    K = 0
    square = 0
    grid = []
    allPossiblePlaces = []
    width = 0
    solutions = []
    cur_width = 9
    cur_height = 9
    rec4rec = 0
    rec4L = 0
    rec4J = 0
    rec4K = 0
    rec4squ = 0
    iteration = 0
    def __init__(self, rectangle, L=0, J=0, leftWing=0, rightWing=0, K=0, square=0, i=0):
        shapes = int(sqrt(rectangle*4 + L*4 + J*4 + leftWing*4 + rightWing*4 + K*4 + square*4)) + 15
        self.rec4rec = CRec4(0)
        self.rec4L = CRec4L(0)
        self.rec4J = CRec4J(0)
        self.rec4K = CRec4K(0)
        self.rec4squ = CRec4squ(0)

        rectangle = self.rec4num(rectangle, self.rec4rec)
        L = self.rec4num(L, self.rec4L)
        J = self.rec4num(J, self.rec4J)
        K = self.rec4num(K, self.rec4K)
        square = self.rec4num(square, self.rec4squ)

        self.n_rectangle = rectangle
        self.n_L = L
        self.n_J = J
        self.n_leftWing = leftWing
        self.n_rightWing = rightWing
        self.n_K = K
        self.n_square = square
        self.rectangle = CRectangle(rectangle)
        self.L = CL(L)
        self.J = CJ(J)
        self.leftWing = CLeftWing(leftWing)
        self.rightWing = CRightWing(rightWing)
        self.K = CK(K)
        self.square = CSquare(square)
        self.grid = zeros((shapes, shapes))
        self.width = shapes
        self.allPossiblePlaces = 0#self.getAllPossiblePlaces()
        self.iteration = i

    def line_prepender(self, filename, line):
        with open(filename, 'r+') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(line.rstrip('\r\n') + '\n' + content)

    def rec4num(self, rectangle, rec):
        if rectangle//4 >= 2:
            rec.num += rectangle//4-1
            rectangle -= (rectangle//4-1) * 4
        return rectangle

    def bestPossiblePlaces(self, shape):
        possible_places = self.possiblePlaces(shape)
        if possible_places == []: return []
        perimeters = []
        minimum = (0, inf)
        minimum1 = (0, inf)
        for i,j in enumerate(possible_places):
            self.placeShape(j[0], j[1], j[2], j[3], 1)
            perimeter = self.perimeter()
            if minimum[1] > perimeter:
                minimum = (i, perimeter)
            # elif minimum1[1] > perimeter and minimum[1] < perimeter:
            #     minimum1 = (i, perimeter)

            self.removeShape(j[0], j[1], j[2], j[3])

        #sort by perimeter
        #perimeters = sorted(perimeters, key=lambda x: x[1])
        return [possible_places[minimum[0]]] #, possible_places[minimum1[0]]]
        # return [possible_places[i[0]] for i in perimeters[:2]]

    #return array of arrays of all possible solutions
    def getAllPossiblePlaces(self):
        arr = [self.rectangle, self.L, self.J, self.leftWing, self.rightWing, self.K, self.square]
        return [self.bestPossiblePlaces(i) for i in arr]


    def solve(self, n=0, cnt=1):
        # while not self.recd():
        arr = [self.rec4rec, self.rec4L, self.rec4J, self.rec4K, self.rec4squ, \
        self.rectangle, self.square, self.L, self.J,  self.K, self.leftWing, self.rightWing]
        while (not arr[n].empty()):

            places = self.bestPossiblePlaces(arr[n])
            if places == []:
                return

            #for j in range(2):
            i = places[0]
            self.placeShape(i[0], i[1], i[2], i[3], cnt)
            s = places.pop(0)
            self.solve(n, cnt+5)
            places.append(0)
            self.removeShape(i[0], i[1], i[2], i[3])
            cnt += 1
        if (n < 11):
            self.solve(n+1, cnt+1)

        #self.plot()
        if self.solved():
            self.solutions.append(self.grid)
        else:
            return

        #if len(self.solutions) > 0:
            #self.getBestSolution()
        self.plotToFile()
        raise Exception("first plot")


    def filterPossiblePlaces(self, arr):
        return [i for i in arr if not self.overlaps(i[0], i[1], i[2], i[3])]


    def placeShape(self, i, j, shape, orientation, cnt=1):
        grid = self.grid
        shape_grid = self.shapeOrientation(shape, orientation)

        if shape_grid == None: return

        isComposed = shape.isComposed()

        for x in range(4):
            for y in range(4):
                if shape_grid[x][y] > 0:
                    grid[i+x][j+y] = cnt+shape_grid[x][y] if isComposed else cnt

                    #expand border
                    if i+x > self.cur_height:
                        self.cur_height = i+x+4
                    if j+y > self.cur_width:
                        self.cur_width = j+y+4

        if not shape.decrement(): raise Exception("cannot decrement !")

    def removeShape(self, i, j, shape, orientation):
        grid = self.grid
        shape_grid = self.shapeOrientation(shape, orientation)

        if shape_grid == None: return

        for x in range(4):
            for y in range(4):
                if shape_grid[x][y] > 0:
                    grid[i+x][j+y] = 0

        if  self.cur_height > 12 and self.cur_width > 12 and (grid[0:self.cur_height, self.cur_width-4:self.cur_width] <= 0).all() and \
            (grid[self.cur_height-4:self.cur_height,0: self.cur_width-4:self.cur_width] <= 0).all():
            self.cur_width -= 4
            self.cur_height -= 4

        shape.increment()

    def possiblePlaces(self, shape):
        if shape.empty(): return []

        width = min(self.cur_width, self.width-5)
        height = min(self.cur_height, self.width-5)
        places = []
        placesLen = 0
        isComposed = shape.isComposed()
        limit = 30 if isComposed else 500
        for i in range(5, height):
            for j in range(5, width):
                if not self.overlaps(i, j, shape, 0):
                    places.append([i,j,shape,0])
                    placesLen += 1
                if not self.overlaps(i, j, shape, 1):
                    places.append([i,j,shape,1])
                    placesLen += 1
                if not self.overlaps(i, j, shape, 2):
                    places.append([i,j,shape,2])
                    placesLen += 1
                if not self.overlaps(i, j, shape, 3):
                    places.append([i,j,shape,3])
                    placesLen += 1

            if placesLen > limit:
                return places

        return places

    def solved(self):
        return  self.rectangle.empty() and \
                self.L.empty() and \
                self.J.empty() and \
                self.leftWing.empty() and \
                self.rightWing.empty() and \
                self.K.empty() and \
                self.square.empty()

    def perimeter(self):
        p = 0
        width = self.width
        grid = self.grid
        for i in range(5, width-1):
            for j in range(5, width-1):
                if grid[i][j] > 0:
                    if grid[i][j+1] == 0: p += 1
                    if grid[i][j-1] == 0: p += 1
                    if grid[i+1][j] == 0: p += 1
                    if grid[i-1][j] == 0: p += 1
        return p

    def plot(self, grid = []):
        if grid == []:
            grid = self.grid

        width = self.width
        for i in range(5, width):
            print(grid[i][5:])

    def plotToFile(self):
        filename = 'out/' + str(self.iteration) + '.txt';
        savetxt(filename, self.grid[5:,5:], fmt='%4d')
        head = "800904\nZlaganje\n\n"+str(self.iteration)+"\n"+str(self.width) + " " + str(self.width) + "\n"
        self.line_prepender(filename, head)

    def overlaps(self, i, j, shape, orientation):
        o = self.shapeOrientation(shape, orientation)
        if o == None: return True
        width = self.width
        grid = self.grid

        for x in range(4):
            for y in range(4):
                if grid[i+x][j+y] > 0 and o[x][y] > 0:
                    return True
        return False

    def shapeOrientation(self, shape, orientation):
        o = []
        if orientation == 0:
            o = shape.overlap0
        elif orientation == 1:
            o = shape.overlap1
        elif orientation == 2:
            o = shape.overlap2
        else: #if orientation == 3:
            o = shape.overlap3
        return o

    def getBestSolution(self):
        solutions = self.solutions
        if len(solutions) == 0:
            print ("getbest == 0")
            return zeros((self.width, self.width))
        minimum = (0, 100000000)
        for i in range(len(solutions)):
            self.grid = solutions[i]
            perimeter = self.perimeter()
            if perimeter < minimum[1]:
                minimum = (i, perimeter)

        return solutions[minimum[0]]

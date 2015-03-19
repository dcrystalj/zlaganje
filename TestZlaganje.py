import unittest
from zlaganje import *
from numpy import *
class TestZlaganje(unittest.TestCase):



    # def test_bestPossiblePlaces(self):
    #     z = Zlaganje(3)
    #     self.assertListEqual(z.bestPossiblePlaces(z.square),[])

    #     self.assertTrue(len(z.bestPossiblePlaces(z.rectangle)) > 5)
    def test_rec4num(self):
        z = Zlaganje(3)
        self.assertEqual(z.rec4num(3, z.rec4rec), 3)
        z = Zlaganje(5)
        self.assertEqual(z.rec4num(5, z.rec4rec), 5)
        z = Zlaganje(8)
        self.assertEqual(z.rec4num(8, z.rec4rec), 4)
        z = Zlaganje(8)
        self.assertEqual(z.rec4num(9, z.rec4rec), 5)



    def test_solve(self):
        z = Zlaganje(3)
        try: z.solve()
        except:
            self.assertTrue(z.rectangle.empty())
            self.assertTrue(z.solved())

    def test_shapeOrientation(self):
        z = Zlaganje(3)
        self.assertEqual(z.shapeOrientation(z.rectangle, 3), None)
        self.assertEqual(z.shapeOrientation(z.rectangle, 2), None)
        self.assertEqual(z.shapeOrientation(z.rectangle, 0)[0], 4*[1])
        self.assertEqual(z.shapeOrientation(z.rectangle, 1)[0], [1]+3*[-1])

    def test_overlaps(self):
        z = Zlaganje(3)
        z.placeShape(0, 0, z.rectangle, 0)
        self.assertTrue(z.overlaps(0,0, z.rectangle, 1))
        self.assertTrue(z.overlaps(0,1, z.rectangle, 0))
        self.assertFalse(z.overlaps(1,0, z.rectangle, 1))
        self.assertFalse(z.overlaps(1,0, z.rectangle, 0))
        self.assertFalse(z.overlaps(1,1, z.rectangle, 1))

        z.placeShape(5, 5, z.rectangle, 0)
        self.assertTrue(z.overlaps(5, 2, z.rectangle, 0))
        self.assertFalse(z.overlaps(5, 1, z.rectangle, 0))

    def test_possiblePlaces(self):
        z = Zlaganje(0)
        self.assertEqual(z.possiblePlaces(z.rectangle), [])

        z = Zlaganje(2)
        z.placeShape(5, 5, z.rectangle, 0)
        d = z.possiblePlaces(z.rectangle)

        self.assertTrue([6,5, z.rectangle, 0] in d)
        self.assertTrue([6,5, z.rectangle, 1] in d)
        self.assertFalse([5,6, z.rectangle, 0] in d)
        self.assertFalse([5,6, z.rectangle, 1] in d)
        self.assertFalse([5,5, z.rectangle, 2] in d)
        self.assertFalse([6,6, z.rectangle, 2] in d)

    def test_removeShape(self):
        z = Zlaganje(3)
        d = [i for i in z.grid[0]]
        z.placeShape(0, 0, z.rectangle, 0)
        self.assertListNotEqual(z.grid[0], d)

        z.removeShape(0, 0, z.rectangle, 0)
        self.assertListEqual(list(z.grid[0]), d)

    def test_placeShape(self):
        z = Zlaganje(3)
        d = [i for i in z.grid[0]]
        z.placeShape(0, 0, z.rectangle, 0, 1)
        self.assertListNotEqual(z.grid[0], d)

    def assertListNotEqual(self, a, b):
        for i in range(len(a)):
            if a[i] != b[i]:
                return True
        raise Exception("They are equal")


    def test_perimeter(self):

        z = Zlaganje(3)
        z.placeShape(6,6, z.rectangle, 0)
        self.assertEqual(z.perimeter(), 10)

        z = Zlaganje(1)
        z.placeShape(5,5, z.rectangle, 1)
        self.assertEqual(z.perimeter(), 10)

        z = Zlaganje(3)
        try: z.solve()
        except:
            pass
            #self.assertEqual(len(z.solutions), )

        z = Zlaganje(3)
        try: z.solve()
        except:
            z.grid = z.getBestSolution()
            z.plot()
            self.assertEqual(z.perimeter(), 14)

        z = Zlaganje(1,1)
        try: z.solve()
        except:
            z.grid = z.getBestSolution()
            self.assertEqual(z.perimeter(), 14)

    def test_solved(self):
        z = Zlaganje(3)
        self.assertFalse(z.solved())
        try: z.solve()
        except: self.assertTrue(z.solved())

if __name__ == '__main__':
    unittest.main()
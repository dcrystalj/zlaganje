import unittest
from Pravokotnik import *
class TestPravokotnik(unittest.TestCase):

    def test_decrement(self):
        p = Pravokotnik(3)
        p.decrement()
        self.assertEqual(p.num, 2)
        p.decrement()
        p.decrement()
        self.assertEqual(p.num, 0)
        self.assertFalse(p.decrement())
        self.assertEqual(p.num, 0)

    def test_empty(self):
        p = Pravokotnik(1)
        self.assertFalse(p.empty())

        p = Pravokotnik(0)
        self.assertTrue(p.empty())

        p = Pravokotnik(-1)
        self.assertTrue(p.empty())

if __name__ == '__main__':
    unittest.main()
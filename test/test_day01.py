import unittest
from solutions.day01 import *

class TestDay01(unittest.TestCase):

    def setUp(self):
        with open("data/day01.txt") as f:
            self.data = f.read().strip()
            self.data = [ int(x) for x in self.data ]

    def test_day01a(self):
        self.assertEqual(3, day01a([ 1, 1, 2, 2 ]))
        self.assertEqual(4, day01a([ 1, 1, 1, 1 ]))
        self.assertEqual(0, day01a([ 1, 2, 3, 4 ]))
        self.assertEqual(9, day01a([ 9, 1, 2, 1, 2, 1, 2, 9 ]))
        self.assertEqual(1203, day01a(self.data))

    def test_day01b(self):
        self.assertEqual(6, day01b([ 1, 2, 1, 2 ]))
        self.assertEqual(0, day01b([ 1, 2, 2, 1 ]))
        self.assertEqual(4, day01b([ 1, 2, 3, 4, 2, 5 ]))
        self.assertEqual(12, day01b([ 1, 2, 3, 1, 2, 3 ]))
        self.assertEqual(4, day01b([ 1, 2, 1, 3, 1, 4, 1, 5 ]))
        self.assertEqual(1146, day01b(self.data))

if __name__ == "__main__":
    unittest.main()

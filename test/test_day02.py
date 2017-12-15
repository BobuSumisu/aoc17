import unittest
from solutions.day02 import *

class TestDay02(unittest.TestCase):

    def setUp(self):
        with open("data/day02.txt") as f:
            self.data = f.read().strip()
        self.data = [ [ int(x) for x in line.split("\t") ] for line in self.data.split("\n") ]

    def test_day02a(self):
        self.assertEqual(18, day02a([
            [ 5, 1, 9, 5 ],
            [ 7, 5, 3 ],
            [ 2, 4, 6, 8 ],
        ]))
        self.assertEqual(44887, day02a(self.data))

    def test_day02b(self):
        self.assertEqual(9, day02b([
            [ 5, 9, 2, 8 ],
            [ 9, 4, 7, 3 ],
            [ 3, 8, 6, 5 ],
        ]))
        self.assertEqual(242, day02b(self.data))

if __name__ == "__main__":
    unittest.main()

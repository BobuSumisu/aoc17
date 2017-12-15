import unittest
from solutions.day06 import *

class TestDay06(unittest.TestCase):
    def setUp(self):
        with open("data/day06.txt") as f:
            self.data = f.read()
        self.data = [ int(x) for x in self.data.strip().split("\t") ]

    def test_day06a(self):
        self.assertEqual(14029, day06a(self.data))

    def test_day06b(self):
        self.assertEqual(2765, day06b(self.data))

if __name__ == "__main__":
    unittest.main()

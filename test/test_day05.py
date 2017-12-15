import unittest
from solutions.day05 import *

class TestDay05(unittest.TestCase):
    def setUp(self):
        with open("data/day05.txt") as f:
            self.data = f.read()
        self.data = [ int(x) for x in self.data.strip().split("\n") ]

    def test_day05a(self):
        self.assertEqual(354121, day05a(self.data))

    def test_day05b(self):
        self.skipTest("too slow!")
        self.assertEqual(27283023, day05b(self.data))

if __name__ == "__main__":
    unittest.main()

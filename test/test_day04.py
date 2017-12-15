import unittest
from solutions.day04 import *

class TestDay04(unittest.TestCase):
    def setUp(self):
        with open("data/day04.txt") as f:
            self.data = f.read()
        self.data = self.data.strip().split("\n")

    def test_day04a(self):
        self.assertEqual(451, day04a(self.data))

    def test_day04b(self):
        self.assertEqual(223, day04b(self.data))

if __name__ == "__main__":
    unittest.main()

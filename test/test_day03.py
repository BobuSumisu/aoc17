import unittest
from solutions.day03 import *

class TestDay03(unittest.TestCase):

    def setUp(self):
        self.data = 368078

    def test_day03a(self):
        self.assertEqual(0, day03a(1))
        self.assertEqual(3, day03a(12))
        self.assertEqual(2, day03a(23))
        self.assertEqual(31, day03a(1024))
        self.assertEqual(371, day03a(self.data))

    def test_day03b(self):
        self.assertEqual(369601, day03b(self.data))

if __name__ == "__main__":
    unittest.main()

#
#   Advent of Code 2017
#   ===================
#
#   Day 2: Corruption Checksum
#   --------------------------
#
#   Input
#       A collection of n rows, s = [ r_1, r_2, …, r_n ],
#       where each row r contains len(r) numbers, r = [ a_1, a_2, …, a_len(n) ].
#   Notes
#       Assume each row contains at least one pair of divisable numbers.
#   Output A
#       The sum of the difference between the highest and lowest number in each row.
#   Output B
#       The sum of the quotient between the first two divisable numbers in each row.
#   Comments
#
from itertools import product

def day02a(data):
    return sum(max(r) - min(r) for r in data)

def day02b(data):
    return sum([int(x / y) for (x, y) in product(r, r) if x != y and x % y == 0][0] for r in data)

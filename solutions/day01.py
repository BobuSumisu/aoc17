#
#   Advent of Code 2017
#   ===================
#
#   Day 1: Inverse Captcha
#   ----------------------
#
#   Input
#       A list of n numbers, s = [ a_1, a_2, … , a_n ].
#   Notes
#       The sequence is circular and n is even.
#   Output A
#       The sum of each s[i] where s[i] == s[i + 1]
#   Output B
#       The sum of each s[i] where s[i] == s[i + n/2]
#   Comments
#

def rotate(s, n):
    """Rotate a list to the left."""
    return s[n:] + s[:n]

def day01a(data):
    return sum(x for x, y in zip(data, rotate(data, 1)) if x == y)

def day01b(data):
    hn = int(len(data) / 2)
    return sum(x for x, y in zip(data, rotate(data, hn)) if x == y)

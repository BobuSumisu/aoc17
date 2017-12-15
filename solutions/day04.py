#
#   Advent of Code 2017
#   ===================
#
#   Day 04: High-Entropy Passphrases
#   --------------------------------
#
#   Input
#       A collection of passphrases.
#   Notes
#
#   Output A
#       Count of passphrases with no duplicate words.
#   Output B
#       Count of passphrases with no duplicate words and no anagrams.
#   Comments
#

def has_duplicates(s):
    """Check is a list has duplicate entries."""
    seen = set()
    for x in s:
        if x in seen:
            return True
        seen.add(x)
    return False

def lexicographicalize(r):
    """Sort each word in the list alphabetically."""
    return [ "".join(sorted(x)) for x in r ]

def day04a(data):
    return len([r for r in data if not has_duplicates(r.split(" "))])

def day04b(data):
    return len([r for r in data if not has_duplicates(lexicographicalize(r.split(" ")))])

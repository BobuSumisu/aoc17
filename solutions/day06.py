#
#   Advent of Code 2017
#   ===================
#
#   Day 06: Memory Reallocation
#   ---------------------------
#
#   Input
#       16 memory banks.
#   Notes
#
#   Output A
#       How many reallocation cycles before a state has been seen before?
#   Output B
#       What is the size of the infinite loop?
#   Comments
#

def reallocate(state):
    s = list(state)
    highest = max(s)
    i = s.index(highest)
    s[i] = 0
    for j in range(highest):
        s[(i + 1 + j) % len(s)] += 1
    return tuple(s)

def day06a(data):
    state = tuple(data)
    seen = set()
    seen.add(state)
    count = 0

    while True:
        count += 1
        state = reallocate(state)
        if state in seen:
            break
        else:
            seen.add(state)

    return count

def day06b(data):
    state = tuple(data)
    seen = set()
    seen.add(state)
    count = 0
    loop_start = None

    while True:
        state = reallocate(state)
        if state in seen:
            if loop_start is None:
                loop_start = state
            else:
                count += 1
                if state == loop_start:
                    break
        else:
            seen.add(state)

    return count


#
#   Advent of Code 2017
#   ===================
#
#   Day 5: A Maze of Twisty Trampolines, All Alike
#   ----------------------------------------------
#
#   Input
#       A sequence of jump instructions.
#   Notes
#
#   Output A
#       The number of steps to reach the exit.
#   Output B
#       The number of steps to reach the exit.
#   Comments
#       These solutions are too slow. Running B takes about 4 seconds!
#

def day05a(data):
    memory = data[:]
    memory_len = len(memory)
    ip = 0
    steps = 0
    while ip >= 0 and ip < memory_len:
        steps += 1
        instr = memory[ip]
        memory[ip] = instr + 1
        ip += instr
    return steps

def day05b(data):
    memory = data[:]
    memory_len = len(memory)
    ip = 0
    steps = 0
    while ip >= 0 and ip < memory_len:
        steps += 1
        instr = memory[ip]
        if instr > 2:
            memory[ip] = instr - 1
        else:
            memory[ip] = instr + 1
        ip += instr
    return steps

from itertools import product
import copy

with open("aoc2.txt") as f:
    program = list(map(int, f.read().split(",")))

program2 = copy.copy(program)


def calc_output(program):
    position = 0
    while program[position] != 99:
        if program[position] == 1:
            program[program[position + 3]] = (
                program[program[position + 1]] + program[program[position + 2]]
            )
        elif program[position] == 2:
            program[program[position + 3]] = (
                program[program[position + 1]] * program[program[position + 2]]
            )
        position += 4
    return program[0]


program[1] = 12
program[2] = 2

print(calc_output(program))

### PART TWO
combinations = product(range(100), repeat=2)

for x, y in combinations:
    program = copy.copy(program2)
    program[1] = x
    program[2] = y
    if calc_output(program) == 19690720:
        print(100 * x + y)
        exit()
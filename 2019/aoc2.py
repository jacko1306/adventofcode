from itertools import product

with open("/home/florianjacke/vscode/private/jacko/adventofcode/2019/aoc2.txt") as f:
    program = list(map(int, f.read().split(",")))


def calcoutput(program):
    position = 0
    while program[position] != 99:
        output_pos = program[position + 3]
        input_pos1 = program[position + 1]
        input_pos2 = program[position + 2]
        input_1 = program[input_pos1]
        input_2 = program[input_pos2]
        if program[position] == 1:
            program[output_pos] = input_1 + input_2
        elif program[position] == 2:
            program[output_pos] = input_1 * input_2
        position += 4
    return program[0]


program[1] = 12
program[2] = 2

print(calcoutput(program))

### PART TWO
combinations = list(product(range(100), repeat=2))

for x, y in combinations:
    with open(
        "/home/florianjacke/vscode/private/jacko/adventofcode/2019/aoc2.txt"
    ) as f:
        program = list(map(int, f.read().split(",")))
    program[1] = x
    program[2] = y
    if calcoutput(program) == 19690720:
        print(100 * x + y)
        exit()
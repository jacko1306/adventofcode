from itertools import product
from itertools import permutations
import copy

with open("aoc7.txt") as f:
    program = list(map(int, f.read().split(",")))


def get_position(mode, position):
    if mode == 0:
        return program[position]
    else:
        return position


def add(A, B, C, position, input_value, output):
    program[get_position(A, position + 3)] = (
        program[get_position(C, position + 1)] + program[get_position(B, position + 2)]
    )
    return position + 4, output


def multiply(A, B, C, position, input_value, output):
    program[get_position(A, position + 3)] = (
        program[get_position(C, position + 1)] * program[get_position(B, position + 2)]
    )
    return position + 4, output


def write(A, B, C, position, input_value, output):
    if position == 0:
        program[program[position + 1]] = input_value[0]
    else:
        program[program[position + 1]] = input_value[1]
    return position + 2, output


def output(A, B, C, position, input_value, output):
    output = program[get_position(C, position + 1)]
    return position + 2, output


def jump_if_true(A, B, C, position, input_value, output):
    if program[get_position(C, position + 1)] != 0:
        return program[get_position(B, position + 2)], output
    else:
        return position + 3, output


def jump_if_false(A, B, C, position, input_value, output):
    if program[get_position(C, position + 1)] == 0:
        return program[get_position(B, position + 2)], output
    else:
        return position + 3, output


def less_than(A, B, C, position, input_value, output):
    if program[get_position(C, position + 1)] < program[get_position(B, position + 2)]:
        program[get_position(A, position + 3)] = 1
    else:
        program[get_position(A, position + 3)] = 0
    return position + 4, output


def equals(A, B, C, position, input_value, output):
    if program[get_position(C, position + 1)] == program[get_position(B, position + 2)]:
        program[get_position(A, position + 3)] = 1
    else:
        program[get_position(A, position + 3)] = 0
    return position + 4, output


def get_instruction(instruction):
    opcode = int(instruction[-2:])
    modes = instruction[:-2].zfill(3)
    return map(int, (list(modes))), opcode


instructions = {
    1: add,
    2: multiply,
    3: write,
    4: output,
    5: jump_if_true,
    6: jump_if_false,
    7: less_than,
    8: equals,
}


def calc_output(input_value):
    position = 0
    output = 0
    while program[position] != 99:
        instruction = str(program[position])
        [A, B, C], opcode = get_instruction(instruction)
        position, output = instructions[opcode](A, B, C, position, input_value, output)
    return output


max_output = 0
phases = range(5)[::-1]

for phases in permutations(range(5)):
    next_input = 0
    for phase in phases:
        next_input = calc_output([phase, next_input])
    if next_input > max_output:
        max_output = next_input

print(max_output)
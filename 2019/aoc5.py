from itertools import product
import copy

with open("aoc5.txt") as f:
    program = list(map(int, f.read().split(",")))


def get_position(mode, position):
    if mode == 0:
        return program[position]
    else:
        return position


def opcode1(A, B, C, position):
    program[get_position(A, position + 3)] = (
        program[get_position(C, position + 1)] + program[get_position(B, position + 2)]
    )


def opcode2(A, B, C, position):
    program[get_position(A, position + 3)] = (
        program[get_position(C, position + 1)] * program[get_position(B, position + 2)]
    )


def opcode5(B, C, position):
    if program[get_position(C, position + 1)] != 0:
        return program[get_position(B, position + 2)]
    else:
        return


def opcode6(B, C, position):
    if program[get_position(C, position + 1)] == 0:
        return program[get_position(B, position + 2)]
    else:
        return


def opcode7(A, B, C, position):
    if program[get_position(C, position + 1)] < program[get_position(B, position + 2)]:
        program[get_position(A, position + 3)] = 1
    else:
        program[get_position(A, position + 3)] = 0


def opcode8(A, B, C, position):
    if program[get_position(C, position + 1)] == program[get_position(B, position + 2)]:
        program[get_position(A, position + 3)] = 1
    else:
        program[get_position(A, position + 3)] = 0

def get_instruction(instruction):
    opcode = int(instruction[-2:])
    modes = instruction[:-2].zfill(3)
    return map(int,(list(modes))),opcode


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


def calc_output():
    position = 0
    while program[position] != 99:
        instruction = str(program[position])
        [A,B,C],opcode = get_instruction(instruction)
        
        if opcode == 1:
            opcode1(A, B, C, position)
            position += 4
        elif opcode == 2:
            opcode2(A, B, C, position)
            position += 4
        elif opcode == 3:
            program[program[position + 1]] = 5
            position += 2
        elif opcode == 4:
            print(program[get_position(C, position + 1)])
            position += 2
        elif opcode == 5:
            res = opcode5(B, C, position)
            if res:
                position = res
            else:
                position += 3
        elif opcode == 6:
            res = opcode6(B, C, position)
            if res:
                position = res
            else:
                position += 3
        elif opcode == 7:
            opcode7(A, B, C, position)
            position += 4
        elif opcode == 8:
            opcode8(A, B, C, position)
            position += 4
    return program

calc_output()

### Part 1 without opcodes 5,6,7,8 and input 1
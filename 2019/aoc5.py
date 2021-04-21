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


def calc_output():
    position = 0
    while program[position] != 99:
        instruction = str(program[position])
        instruction_length = len(instruction)
        A, B, C = 0, 0, 0
        opcode = int(instruction[-1])
        if instruction_length >= 3:
            C = int(instruction[-3])
            if instruction_length >= 4:
                B = int(instruction[-4])
                if instruction_length == 5:
                    A = int(instruction[-5])
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
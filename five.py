#!/usr/bin/python3

import math

def split_code(code):
    row = code[:7]
    column = code[7:]
    return row, column

def cut_half(res, dir):
    val_min = res[0]
    val_max = res[1]
    if dir == 0:
        val_max = math.floor((val_max-val_min)/2)+val_min
        res = [val_min,val_max]
    elif dir == 1:
        val = (val_max-val_min)/2+val_min
        val_min = math.ceil(val)
        res = [val_min,val_max]
    return res


def get_value(seq, res):
    val_min = res[0]
    val_max = res[1]
    for i in seq:
        if i == 'F' or i == 'L':
            dir = 0
        elif i == 'B' or i == 'R':
            dir = 1
        res = cut_half(res,dir)
        if res[0] == res[1]:
            return res[0]

def get_row(code):
    res = [0,127]
    res = get_value(code, res)
    return res

def get_column(code):
    res = [0,7]
    res = get_value(code, res)
    return res

with open('/vscode/adventofcode/five.txt') as file:
    report = file.read().split('\n')

max_id = 0
seat_ids = []
for code in report:
    row, column = split_code(code)
    row_int = get_row(row)
    column_int = get_column(column)
    seat_id = row_int * 8 + column_int
    seat_ids.append(seat_id)
    if seat_id > max_id:
        max_id = seat_id
print(max_id)
for i in range(0,max_id):
    if i+1 in seat_ids and i-1 in seat_ids and i not in seat_ids:
        print(i)
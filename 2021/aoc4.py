from collections import Counter
import numpy as np


with open("aoc4.txt") as f:
    puzzle_input = f.read().splitlines()

calls = [int(a) for a in puzzle_input[0].split(",")]

puzzles_pre = list(filter(lambda a: a != "", puzzle_input[2:]))
puzzles_pre = [puzzles_pre[x : x + 5] for x in range(0, len(puzzles_pre), 5)]
puzzles = []
for puzzle_pre in puzzles_pre:
    puzzle = []
    for line in puzzle_pre:
        numbers = line.split(" ")
        numbers = list(filter(lambda a: a != "", numbers))
        numbers = [int(a) for a in numbers]
        puzzle.append(numbers)
    puzzles.append(puzzle)

database = {}
already_called = []


def append_value(dict_obj, key, value):
    if key in dict_obj:
        dict_obj[key].append(value)
    else:
        dict_obj[key] = [value]


def check_bingo(puzzle_id):
    colums = Counter([item[0] for item in database[puzzle_id]])
    rows = Counter([item[1] for item in database[puzzle_id]])
    return colums.most_common(1)[0][1] == 5 or rows.most_common(1)[0][1] == 5


def result():
    acc = 0
    for row in puzzle:
        unmarked = list(set(row) - set(already_called))
        acc += int(np.sum(unmarked))
    return acc

puzzle_has_bingo = {}

for call in calls:
    already_called.append(call)
    for k, puzzle in enumerate(puzzles):
        for j, line in enumerate(puzzle):
            for i, number in enumerate(line):
                if call == number:
                    append_value(database, k, [i, j])
                    bingo = check_bingo(k)
                    if bingo:
                        if k not in puzzle_has_bingo and (len(puzzle_has_bingo) == 0 or len(puzzle_has_bingo) == len(puzzles)-1):
                            print(result() * call)
                        puzzle_has_bingo[k] = True
                        


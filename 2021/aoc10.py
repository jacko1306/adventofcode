import copy
import math

with open('aoc10.txt') as f:
    puzzle = f.read().splitlines()

open_brackets = ['{', '[', '(', '<']
closed_to_open = {'}': '{', ']': '[', ')': '(', '>': '<'}
open_to_closed = dict((v,k) for k,v in closed_to_open.items())
points_to_brackets = {')': 3, ']': 57, '}': 1197, '>': 25137}
second_points_to_brackets = {')': 1, ']': 2, '}': 3, '>': 4}
illegals = 0
legal_lines = copy.deepcopy(puzzle)
scores = []

for line in puzzle:
    last_opened_bracket = []
    for bracket in line:
        if bracket in open_brackets:
            last_opened_bracket.append(bracket)
        else:
            if last_opened_bracket[-1] != closed_to_open[bracket]:
                illegals +=  points_to_brackets[bracket]
                legal_lines.remove(line)
            last_opened_bracket.pop()
    if line in legal_lines:
        completers = list(reversed(list(open_to_closed[bracket] for bracket in last_opened_bracket)))
        score = 0
        for element in completers:
            score *= 5
            score += second_points_to_brackets[element]
        scores.append(score)
                
print(illegals)
scores = sorted(scores)
middle = math.floor(len(scores)/2)
print(scores[middle])
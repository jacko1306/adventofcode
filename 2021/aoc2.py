import numpy as np

with open('aoc2.txt') as f:
    lines = f.read().splitlines()

position = [0,0]

for x in lines:
    direction,value = x.split(' ')
    value = int(value)
    if direction == "forward":
        position[0] += value
    else:
        if direction == "up":
            position[1] -= value
        else:
            position[1] += value

print(np.product(position))

position = [0,0]
aim = 0

for x in lines:
    direction,value = x.split(' ')
    value = int(value)
    if direction == "forward":
        position[0] += value
        position[1] += value*aim
    else:
        if direction == "up":
            aim -= value
        else:
            aim += value

print(np.product(position))
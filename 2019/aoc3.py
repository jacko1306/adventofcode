import collections
import itertools

with open("aoc3.txt") as f:
    operations = f.read().splitlines()


def get_visits(construct):
    visited = {(0, 0): 0}
    x = 0
    y = 0
    instructions = construct.split(",")
    step_count = 0
    for instruction in instructions:
        direction, steps = instruction[0], instruction[1:]
        steps = int(steps)
        if direction == "R":
            new_pos = itertools.product(range(x, x + steps), [y])
            x += steps
        elif direction == "L":
            new_pos = itertools.product(range(x, x - steps, -1), [y])
            x -= steps
        elif direction == "U":
            new_pos = itertools.product([x], range(y, y + steps))
            y += steps
        elif direction == "D":
            new_pos = itertools.product([x], range(y, y - steps, -1))
            y -= steps

        for position in new_pos:
            if position not in visited:
                visited[position] = step_count
            step_count += 1
    return visited


def min_distance(wire1, wire2):
    crossings = set(wire1) & set(wire2)
    crossings.remove((0, 0))
    return min((abs(x) + abs(y) for x, y in crossings))


def min_steps(wire1, wire2):
    crossings = set(wire1) & set(wire2)
    crossings.remove((0, 0))
    return min(wire1[cross] + wire2[cross] for cross in crossings)


wire1 = get_visits(operations[0])
wire2 = get_visits(operations[1])

print(min_distance(wire1, wire2))
print(min_steps(wire1, wire2))

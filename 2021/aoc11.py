import numpy as np
import copy

with open("aoc11.txt") as f:
    puzzle = f.read().splitlines()

my_map = list(list(int(x) for x in line) for line in puzzle)
my_map_2 = copy.deepcopy(my_map)

total_flashes = 0
flashed = np.zeros((10, 10))


def is_inside(coordinates):
    if (
        coordinates[0] > -1
        and coordinates[1] > -1
        and coordinates[1] < 10
        and coordinates[0] < 10
    ):
        return True
    else:
        return False


def get_neighbors(x, y):
    normal_vectors = [
        np.array([0, 1]),
        np.array([1, 1]),
        np.array([1, 0]),
        np.array([1, -1]),
        np.array([0, -1]),
        np.array([-1, -1]),
        np.array([-1, 0]),
        np.array([-1, 1]),
    ]
    neighbors = []
    for vector in normal_vectors:
        if is_inside(vector + (x, y)) and flashed[vector[0] + x][vector[1] + y] != 1:
            neighbors.append(vector + (x, y))
    return neighbors


def update_adjacent(x, y, current_map):
    global total_flashes
    neighbors = get_neighbors(x, y)
    if current_map[x][y] > 9:
        for neighbor in neighbors:
            current_map[neighbor[0]][neighbor[1]] += 1
    current_map[x][y] = 0
    total_flashes += 1
    flashed[x][y] = 1


def update_all(current_map):
    for x, line in enumerate(current_map):
        for y, y_val in enumerate(line):
            current_map[x][y] += 1
    return current_map


def contains_value_greater_9(current_map):
    return any(x > 9 for sublist in current_map for x in sublist)


def contains_only_zeros(current_map):
    return all(x == 0 for sublist in current_map for x in sublist)


def calculation(phase, my_map_now, steps=500):
    global flashed
    for step in range(steps):
        flashed = np.zeros((10, 10))
        update_all(my_map_now)
        while contains_value_greater_9(my_map_now):
            for x, line in enumerate(my_map_now):
                for y, y_val in enumerate(line):
                    if y_val > 9:
                        update_adjacent(x, y, my_map_now)
        if phase == 2:
            if contains_only_zeros(my_map_now):
                print(step + 1)
                break


calculation(1, my_map, 100)
print(total_flashes)
calculation(2, my_map_2)

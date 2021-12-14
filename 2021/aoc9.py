import numpy as np
from itertools import combinations
import copy
from numpy.core.arrayprint import printoptions


with open("aoc9.txt") as f:
    puzzle_input = f.read().splitlines()

heightmap = []

for line in puzzle_input:
    heightmap.append([int(x) for x in line])

low_candidates = copy.deepcopy(heightmap)


def get_neighbors(coordinates: np.array):
    normal_vectors = [
        np.array([0, 1]),
        np.array([1, 0]),
        np.array([-1, 0]),
        np.array([0, -1]),
    ]
    neighbors = []
    for vector in normal_vectors:
        neighbors.append(vector + coordinates)
    return neighbors


for y, y_value in enumerate(heightmap):
    for x, x_value in enumerate(y_value):
        neighbors = get_neighbors((x, y))
        for neighbor in neighbors:
            if (
                neighbor[0] > -1
                and neighbor[1] > -1
                and neighbor[0] < len(heightmap[0])
                and neighbor[1] < len(heightmap)
            ):
                test_value = heightmap[neighbor[1]][neighbor[0]]
                if test_value < x_value:
                    low_candidates[y][x] = 9

res = 0
for line in low_candidates:
    for value in line:
        if value != 9:
            res += value + 1

print(res)

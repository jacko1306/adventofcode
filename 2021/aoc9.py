import numpy as np
from collections import defaultdict
import copy


with open("aoc9.txt") as f:
    puzzle_input = f.read().splitlines()

heightmap = []

for line in puzzle_input:
    heightmap.append([int(x) for x in line])

low_candidates = copy.deepcopy(heightmap)


def is_inside(coordinates):
    if (
        coordinates[0] > -1
        and coordinates[1] > -1
        and coordinates[1] < len(heightmap[0])
        and coordinates[0] < len(heightmap)
    ):
        return True
    else:
        return False


def get_neighbors(coordinates: np.array):
    normal_vectors = [
        np.array([0, 1]),
        np.array([1, 0]),
        np.array([-1, 0]),
        np.array([0, -1]),
    ]
    neighbors = []
    for vector in normal_vectors:
        if is_inside(vector + coordinates):
            neighbors.append(vector + coordinates)
    return neighbors


for y, y_value in enumerate(heightmap):
    for x, x_value in enumerate(y_value):
        neighbors = get_neighbors((y, x))
        for neighbor in neighbors:
            test_value = heightmap[neighbor[0]][neighbor[1]]
            if test_value < x_value:
                low_candidates[y][x] = 9


res = 0
for line in low_candidates:
    for value in line:
        if value != 9:
            res += value + 1
print(res)

visited = defaultdict(lambda: False)
basins = defaultdict()


def get_neighbors_2(coordinates):
    return_neighbors = []
    neighbors = get_neighbors(coordinates)
    for neighbor in neighbors:
        if (
            heightmap[neighbor[0]][neighbor[1]] != 9
            and not visited[(neighbor[0], neighbor[1])]
        ):
            return_neighbors.append(neighbor)
    return return_neighbors


def get_non_9_neighbors(coordinates, res=1):
    visited[coordinates] = True
    neighbors = get_neighbors_2(coordinates)
    for neighbor in neighbors:
        if not visited[(neighbor[0], neighbor[1])]:
            res += get_non_9_neighbors((neighbor[0], neighbor[1]), 1)
    return res


basin_counter = 0


for y, y_value in enumerate(heightmap):
    for x, x_value in enumerate(y_value):
        if not visited[(y, x)] and x_value != 9:
            basins[basin_counter] = get_non_9_neighbors((y, x))
            basin_counter += 1


max_3 = sorted(basins.items(), key=lambda pair: pair[1], reverse=True)[:3]

product_max_3 = 1
for k, v in max_3:
    product_max_3 *= v

print(product_max_3)

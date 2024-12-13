from collections import defaultdict
import itertools

with open("input8.txt") as f:
    antenna_map = f.read().splitlines()

antennas_positions = defaultdict()
possible_antinode = defaultdict()

for x, line in enumerate(antenna_map):
    for y, point in enumerate(line):
        if point != ".":
            antennas_positions[(x, y)] = point
        possible_antinode[(x, y)] = [0, point]

distinct_antennas = list(set(antennas_positions.values()))


def get_line(A, B, test):
    x1 = A[0]
    y1 = A[1]
    x2 = B[0]
    y2 = B[1]
    m = (y2 - y1) / (x2 - x1)
    b = y1 - (m * x1)

    for k,v in possible_antinode.items():
        x,y = k
        if v[1] == test:
            continue
        if float(y) == round(m * x + b, 1):
            distance_points_x = abs(x1 - x2)
            distance_points_y = abs(y1 - y2)

            if distance_points_x == abs(x - x1) and distance_points_y == abs(y - y1):
                possible_antinode[(x, y)][0] = 1
            elif distance_points_x == abs(x - x2) and distance_points_y == abs(y - y2):
                possible_antinode[(x, y)][0] = 1

    return


for test in distinct_antennas:
    all_positions = [k for k, v in antennas_positions.items() if v == test]
    all_combis = list(itertools.combinations(all_positions, r=2))

    for combi in all_combis:
        get_line(combi[0], combi[1], test)


print(sum([x for x, y in possible_antinode.values()]))

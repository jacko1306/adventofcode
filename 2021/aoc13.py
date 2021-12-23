with open("aoc13.txt") as f:
    puzzle = f.read().splitlines()

delimiter = puzzle.index("")
points = puzzle[:delimiter]
instructions = puzzle[delimiter:]
all_points = [(int(x), int(y)) for x, y in (p.split(",") for p in points)]
max_x = max(all_points, key=lambda x: x[0])[0] + 1
max_y = max(all_points, key=lambda x: x[1])[1] + 1
# use only first instruction for part 1
instructions = instructions[1]
print(max_x, " ", max_y)
fold_axis, fold_val = instructions.split(" ")[2].split("=")
fold_val = int(fold_val)
grid_original = [["." for _ in range(max_x)] for _ in range(max_y)]

for point in points:
    x, y = point.split(",")
    x = int(x)
    y = int(y)
    grid_original[y][x] = "#"


def print_grid(grid):
    for y in range(len(grid)):
        print("".join(grid[y]))


def split_y_for_folding(grid: list, fold_val) -> list:
    return [grid[:fold_val], grid[fold_val + 1 :]]


def split_x_for_folding(grid: list, fold_val) -> list:
    grid1 = [line[:fold_val] for line in grid]
    grid2 = [line[fold_val + 1 :] for line in grid]
    return [grid1, grid2]


def flip_second_half_at_y(grid) -> list:
    return list(reversed(grid))


def flip_second_halt_at_x(grid) -> list:
    new_grid = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for y, line in enumerate(grid):
        new_line = list(reversed(line))
        new_grid[y] = new_line
    return new_grid


if fold_axis == "y":
    halfes = split_y_for_folding(grid_original, fold_val)
    second_half = flip_second_half_at_y(halfes[1])
else:
    halfes = split_x_for_folding(grid_original, fold_val)
    second_half = flip_second_halt_at_x(halfes[1])


def combine_two_halfes(grid1, grid2):
    return_grid = [["." for _ in range(len(grid1[0]))] for _ in range(len(grid1))]
    for y, line in enumerate(grid1):
        for x, value in enumerate(line):
            x2 = grid2[y][x]
            if x2 == "#" or value == "#":
                return_grid[y][x] = "#"
    return return_grid


finished_grid = combine_two_halfes(halfes[0], second_half)
# print_grid(finished_grid)


def count_dots(grid):
    return sum(x.count("#") for x in grid)


print(count_dots(finished_grid))
with open("aoc13.txt") as f:
    puzzle = f.read().splitlines()

delimiter = puzzle.index("")
points = puzzle[:delimiter]
instructions = puzzle[delimiter + 1 :]
all_points = [(int(x), int(y)) for x, y in (p.split(",") for p in points)]
max_x = max(all_points, key=lambda x: x[0])[0] + 1
max_y = max(all_points, key=lambda x: x[1])[1] + 1


grid_original = [["." for _ in range(max_x)] for _ in range(max_y + 1)]

for point in points:
    x, y = point.split(",")
    x = int(x)
    y = int(y)
    grid_original[y][x] = "#"


def print_grid(grid):
    for y in range(len(grid)):
        print("".join(grid[y]))
    print()


def split_y_for_folding(grid: list, fold_val) -> list:
    return [grid[:fold_val], grid[fold_val + 1 :]]


def split_x_for_folding(grid: list, fold_val) -> list:
    grid1 = [line[:fold_val] for line in grid]
    grid2 = [line[fold_val + 1 :] for line in grid]
    return [grid1, grid2]


def flip_second_half_at_y(grid) -> list:
    return list(reversed(grid))


def flip_second_half_at_x(grid) -> list:
    new_grid = [["." for _ in range(len(grid[0]))] for _ in range(len(grid))]
    for y, line in enumerate(grid):
        new_line = list(reversed(line))
        new_grid[y] = new_line
    return new_grid


def combine_two_halfes(grid1, grid2):
    return_grid = [["." for _ in range(len(grid1[0]))] for _ in range(len(grid1))]
    for y, line in enumerate(grid1):
        for x, value in enumerate(line):
            x2 = grid2[y][x]
            if x2 == "#" or value == "#":
                return_grid[y][x] = "#"
    return return_grid


def count_dots(grid):
    return sum(x.count("#") for x in grid)


current_grid = grid_original
for i, instruction in enumerate(instructions):
    fold_axis, fold_val = instruction.split(" ")[2].split("=")
    fold_val = int(fold_val)
    if fold_axis == "y":
        halfes = split_y_for_folding(current_grid, fold_val)
        second_half = flip_second_half_at_y(halfes[1])
    else:
        halfes = split_x_for_folding(current_grid, fold_val)
        second_half = flip_second_half_at_x(halfes[1])
    current_grid = combine_two_halfes(halfes[0], second_half)
    if i == 0:
        print(count_dots(current_grid))


print_grid(current_grid)

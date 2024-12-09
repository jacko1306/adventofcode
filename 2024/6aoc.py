from collections import defaultdict

with open("input6.txt") as f:
    guard_map_input = f.read().splitlines()

guard_map = defaultdict(int)

guard_map = [list(x for x in g) for g in guard_map_input]
x_max = len(guard_map) - 1
y_max = len(guard_map[0]) - 1
obstacles = []
visited = []
visited_with_dir = []
current_dir = [-1, 0]
current_position = list()


for x, line in enumerate(guard_map):
    for y, point in enumerate(line):
        if point == "#":
            obstacles.append([x, y])
        if point == "^":
            visited.append([x, y])
            visited_with_dir.append([x, y, current_dir[0], current_dir[1]])

obstructions = obstacles.copy()


def reset_to_start():
    global current_position
    global visited
    global visited_with_dir
    global current_dir
    current_dir = [-1, 0]
    current_position.append(visited[0][0])
    current_position.append(visited[0][1])


def actual_move():
    global counter
    if current_position not in visited:
        visited.append([current_position[0], current_position[1]])
        visited_with_dir.append(
            [current_position[0], current_position[1], current_dir[0], current_dir[1]]
        )
    current_position[0] += current_dir[0]
    current_position[1] += current_dir[1]
    return


def test_move():
    test_position = current_position.copy()
    test_position[0] += current_dir[0]
    test_position[1] += current_dir[1]
    return test_position


def move():
    if no_obstacle():
        actual_move()
    else:
        turn()
    return


def no_obstacle():
    return test_move() not in obstacles


def turn():
    global current_dir
    new_dir = []
    if current_dir == [-1, 0]:
        new_dir = [0, 1]
    elif current_dir == [0, 1]:
        new_dir = [1, 0]
    elif current_dir == [1, 0]:
        new_dir = [0, -1]
    else:
        new_dir = [-1, 0]
    current_dir = new_dir
    return


def not_out_of_bounds():
    if (
        current_position[0] > x_max
        or current_position[1] > y_max
        or current_position[0] < 0
        or current_position[1] < 0
    ):
        return False

    return True


reset_to_start()

while not_out_of_bounds():
    move()

print(len(visited))


def test_obstruction():
    return


def no_loop():
    return


reset_to_start()

print(current_position)

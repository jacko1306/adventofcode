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
current_position = []
current_obstruction = []
max_step_counter = 0
final_max_step = 0


for x, line in enumerate(guard_map):
    for y, point in enumerate(line):
        if point == "#":
            obstacles.append([x, y])
        if point == "^":
            visited.append([x, y])
            visited_with_dir.append([x, y, [current_dir[0], current_dir[1]]])

obstructions = obstacles.copy()


def reset_to_start():
    global current_position
    global visited_with_dir
    global current_dir

    current_dir = [-1, 0]
    start_x = visited_with_dir[0][0]
    start_y = visited_with_dir[0][1]
    visited_with_dir = [[start_x, start_y, current_dir]]
    current_position = [start_x, start_y]


def actual_move():
    global max_step_counter
    max_step_counter += 1
    current_position[0] += current_dir[0]
    current_position[1] += current_dir[1]
    test = current_position + [current_dir]
    if current_position not in visited:
        visited.append([current_position[0], current_position[1]])
    if test not in visited_with_dir:
        visited_with_dir.append(
            [current_position[0], current_position[1], [current_dir[0], current_dir[1]]]
        )
    return


def test_move():
    return [current_position[0] + current_dir[0], current_position[1] + current_dir[1]]


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


def not_out_of_bounds(position):
    if position[0] > x_max:
        return False
    elif position[1] > y_max:
        return False
    elif position[0] < 0:
        return False
    elif position[1] < 0:
        return False
    else:
        return True


reset_to_start()

while not_out_of_bounds(test_move()):
    move()

print(len(visited))
final_max_step = max_step_counter


def add_obstruction():
    global current_obstruction
    test_current_obstruction = test_move()
    if not test_current_obstruction[0] > x_max:
        if not test_current_obstruction[1] > y_max:
            if not test_current_obstruction[0] < 0:
                if not test_current_obstruction[1] < 0:
                    current_obstruction = test_current_obstruction
                    obstructions.append(current_obstruction)

    return


def remove_obstruction():
    global current_obstruction
    if current_obstruction in obstructions:
        obstructions.remove(current_obstruction)
        current_obstruction = []
    return


def loop():
    test = test_move() + [current_dir]
    if test in visited_with_dir:
        return True
    else:
        return False


def no_obstacle2():
    testing_pos = test_move()
    if testing_pos not in obstructions:
        return True
    return False


turn_counter = 0


def move2():
    global turn_counter
    if no_obstacle2():
        actual_move()
    else:
        turn()
        turn_counter += 1
    return


reset_to_start()

loop_counter = 0
tests = 1


while tests <= (final_max_step + turn_counter):
    steps_moved = 0
    turn_counter = 0

    while not_out_of_bounds(current_position):
        if loop():
            break
        if tests == steps_moved:
            add_obstruction()
        move2()
        steps_moved += 1
    tests += 1
    if not_out_of_bounds(current_position):
        print(current_obstruction)
        loop_counter += 1
    remove_obstruction()
    reset_to_start()


print(loop_counter)

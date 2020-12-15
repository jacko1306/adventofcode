import re

with open('vscode/adventofcode/aoc12.txt') as f:
    orders = f.read().splitlines()
orders_split = []
for order in orders:
    dir = order[0]
    val = int(re.search(r'\d+', order).group())
    orders_split.append((dir, val))

coordinates = {'N':0,'S':0,'W':0,'E':0}
turn_right = {
    'N':'E',
    'E':'S',
    'S':'W',
    'W':'N'
}
turn_left = {
    'N':'W',
    'W':'S',
    'S':'E',
    'E':'N'
}
current_dir = 'E'
for dir, val in orders_split:
    if dir == 'N':
        coordinates['N'] += val
    if dir == 'E':
        coordinates['E'] += val
    if dir == 'S':
        coordinates['S'] += val
    if dir == 'W':
        coordinates['W'] += val
    if dir == 'F':
        coordinates[current_dir] += val
    if dir == 'R':
        if val == 90:
            current_dir = turn_right[current_dir]
        if val == 180:
            current_dir = turn_right[current_dir]
            current_dir = turn_right[current_dir]
        if val == 270:
            current_dir = turn_right[current_dir]
            current_dir = turn_right[current_dir]
            current_dir = turn_right[current_dir]
    if dir == 'L':
        if val == 90:
            current_dir = turn_left[current_dir]
        if val == 180:
            current_dir = turn_left[current_dir]
            current_dir = turn_left[current_dir]
        if val == 270:
            current_dir = turn_left[current_dir]
            current_dir = turn_left[current_dir]
            current_dir = turn_left[current_dir]
#print(coordinates)
manhatten = abs(coordinates['N']-coordinates['S'])+abs(coordinates['E']-coordinates['W'])
print(manhatten)

### PART 2 ###

coordinates = {'N':0,'S':0,'W':0,'E':0}
waypoint = {'N':1,'S':0,'W':0,'E':10}

def move_ship(multi):
    for dir, val in waypoint.items():
        coordinates[dir] += multi*val

def rotate_waypoint(val, dir):
    times = int(val/90)
    for i in range(times):
        if dir == 'R':
            help = waypoint['N']
            waypoint['N'] = waypoint['W']
            waypoint['W'] = waypoint['S']
            waypoint['S'] = waypoint['E']
            waypoint['E'] = help
        if dir == 'L':
            help = waypoint['N']
            waypoint['N'] = waypoint['E']
            waypoint['E'] = waypoint['S']
            waypoint['S'] = waypoint['W']
            waypoint['W'] = help

for dir, val in orders_split:
    if dir == 'F':
        move_ship(val)
    if dir in ['N','S','W','E']:
        waypoint[dir] += val
    if dir in ['R','L']:
        rotate_waypoint(val,dir)

manhatten = abs(coordinates['N']-coordinates['S'])+abs(coordinates['E']-coordinates['W'])
print(manhatten)       
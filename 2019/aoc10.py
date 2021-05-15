import itertools

with open('aoc10.txt') as f:
    map =  f.read().split()


def get_combinations(x,y):
    import itertools

    combs = []
    length = 5

    for i in range(length + 1):
        combs.append((length, i))
        combs.append((length * -1, i))
        combs.append((length, i * -1))
        combs.append((length * -1, i * -1))
        combs.append((i, length))
        combs.append((i, length * -1))
        combs.append((i * -1, length))
        combs.append((i * -1, length * -1))

    combs = set(combs)
    return combs

map_length = len(map[0])
map_height = len(map)

map_dict = {}
y = 0
for line in map:
    x = 0
    for el in line:
        if el == '.':
            val = 0
        else:
            val = 1
        map_dict[(x,y)] = val
        x += 1
    y += 1


def detect_aseroids(x,y):
    num = 0
    for x_dir, y_dir in get_combinations(x,y):
        for i in range(0-x,5-x):
            x_step = i*x_dir
            y_step = i*y_dir
            new_x = x+x_step
            new_y = y+y_step
            if new_x == x and new_y == y:
                continue
            test = map_dict.get(tuple((new_x, new_y)))
            if test == 1:
                num += 1
                break

    '''
    for x_adj in range(x,0,-1):
        if map_dict.get((x_adj,y)) != 0:
            num += 1
            break
    for x_adj in range(x,map_length):
        if map_dict.get((x_adj,y)) != 0:
            num += 1
            break      
    for y_adj in range(0,y):
        if map_dict.get((x,y_adj)) != 0:
            num += 1
            break
    for y_adj in range(y,map_height):
        if map_dict.get((x,y_adj)) != 0:
            num += 1
            break
    '''
    return num

y = 0

for line in map:
    newline = ''
    x = 0
    for el in line:
        num = 0
        if el == '#':
            num += detect_aseroids(x,y)
            newline += str(num)
        else:
            newline += '.'
        x += 1
    y += 1
    print(newline)
from collections import defaultdict

with open("input3.txt") as f:
    lift = f.read().splitlines()

lift_map = []

for i, line in enumerate(lift):
    lift_map += [(line)]
ext_map = defaultdict(int)
for y, line in enumerate(lift_map):
    for x, value in enumerate(line):
        ext_map[(y, x)] = lift_map[y][x]


def get_neighbors(x, y, length):
    neighbors = defaultdict(int)
    neighbors[(y, x - 1)] = ext_map[(y, x - 1)]
    neighbors[(y, x + length)] = ext_map[(y, x + length)]
    for n in range(-1, length + 1):
        neighbors[(y + 1, x + n)] = ext_map[(y + 1, x + n)]
        neighbors[(y - 1, x + n)] = ext_map[(y - 1, x + n)]
    return neighbors


def neighbors_have_symbol(x, y, length):
    SYMBOLS = ["+", "-", "*", "/", "&", "=", "$", "#", "%", "@"]
    neighbors = get_neighbors(x, y, length)
    if any(value in SYMBOLS for value in neighbors.values()):
        return True, neighbors
    else:
        return False, None


def get_length_and_number(x, y, value):
    length = 1
    if x + 1 <= len(lift_map[y]):
        if lift_map[y][x + 1].isdigit():
            length += 1
            value = value * 10 + int(lift_map[y][x + 1])
            if x + 2 <= len(lift_map[y]):
                if lift_map[y][x + 2].isdigit():
                    length += 1
                    value = value * 10 + int(lift_map[y][x + 2])
    return length, value


res = 0
current_number_length = 0
gears = defaultdict(lambda: 1)
gear_counter = defaultdict(int)

for y, line in enumerate(lift_map):
    for x, value in enumerate(line):
        if value.isdigit():
            if current_number_length < 1:
                length, number = get_length_and_number(x, y, int(value))
                current_number_length = length
                has_symbol, symbols = neighbors_have_symbol(x, y, length)
                if has_symbol:
                    res += number
                    for symbol in symbols.items():
                        if "*" == symbol[1]:
                            gears[symbol[0]] *= number
                            gear_counter[symbol[0]] += 1

            current_number_length -= 1

gear_sum = sum(gears[pos] for pos, i in gear_counter.items() if i ==2 )




print(res)
print(gear_sum)

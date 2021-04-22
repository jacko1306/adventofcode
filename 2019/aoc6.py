with open("aoc6.txt") as f:
    orbitMap = dict([list(reversed(x.split(")"))) for x in f.read().splitlines()])


def get_center_recursive(origin, acc=0):
    center = orbitMap.get(origin)
    if center == None:
        return acc
    return get_center_recursive(center, acc + 1)


print(sum(list(get_center_recursive(x) for x in orbitMap)))

with open("aoc6.txt") as f:
    orbit_map = dict([x.split(")")[::-1] for x in f.read().splitlines()])


def get_center(origin, acc=0):
    center = orbit_map.get(origin)
    if center is None:
        return acc
    return get_center(center, acc + 1)


print(sum([get_center(x) for x in orbit_map]))
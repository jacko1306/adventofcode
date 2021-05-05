import collections

with open("aoc6.txt") as f:
    orbit_map = dict([x.split(")")[::-1] for x in f.read().splitlines()])


def get_center_count(origin, acc=0):
    center = orbit_map.get(origin)
    if center is None:
        return acc
    return get_center_count(center, acc + 1)


print(sum([get_center_count(x) for x in orbit_map]))


def get_center(origin, acc_list=[]):
    center = orbit_map.get(origin)
    if center is None:
        return acc_list
    else:
        acc_list.append(center)
    return get_center(center, acc_list)


you_2_com = get_center("YOU", [])
san_2_com = get_center("SAN", [])

matching_paths = you_2_com + san_2_com
matching_paths = [
    item for item, count in collections.Counter(matching_paths).items() if count > 1
]

print(len(you_2_com) + len(san_2_com) - 2 * len(matching_paths))
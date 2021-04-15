import math

with open("aoc1.txt") as f:
    modules = list(map(int, f.read().splitlines()))

### PART ONE

res = 0

for module in modules:
    res += math.floor(module / 3) - 2

print(res)


### PART TWO


def calc_mass(module):
    return math.floor(module / 3) - 2


def calc_masses(module, acc=0):
    res = calc_mass(module)
    if res <= 0:
        return acc
    return calc_masses(res, acc + res)


res = 0
for module in modules:
    res += calc_masses(module)

print(res)
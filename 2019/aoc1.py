#!/usr/bin/python3

with open("/home/florianjacke/vscode/private/jacko/adventofcode/2019/aoc1.txt") as f:
    modules = map(int, f.read().splitlines())

### PART ONE

res = 0

for module in modules:
    res += int(module / 3) - 2

print(res)


### PART TWO

res = 0
with open("/home/florianjacke/vscode/private/jacko/adventofcode/2019/aoc1.txt") as f:
    modules = map(int, f.read().splitlines())

def calcMass(currentmodule):
    return int(currentmodule / 3) - 2
    
def calcMasses(currentmodule, sum = 0):
    res = calcMass(currentmodule)
    if res <= 0:
        return sum
    return calcMasses(res, sum + res)


for module in modules:
    res += calcMasses(module)

print(res)
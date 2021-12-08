import math

with open("aoc7.txt") as f:
    positions = [int(val) for val in f.read().split(",")]

min_fuel = 10000000000

def sum_to_zero(value):
    return sum(range(value,0,-1))


for x in range(1, max(positions) + 1):
    fuel = 0
    fuel = sum(sum_to_zero(abs(pos - x)) for pos in positions)
    if fuel < min_fuel:
        min_fuel = fuel


print(min_fuel)


#part 1 without sum_to_zero
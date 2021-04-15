import math

with open('vscode/adventofcode/aoc13.txt') as f:
    notes = f.read().splitlines()

earliest_dep = int(notes[0])
bus_list = notes[1].split(',')
bus_list = list(filter(lambda a: a != 'x', bus_list))
buses = list(map(int,bus_list))

possibilities = {}
bus_id = 0

for bus in buses:
    closeest_dep = earliest_dep%bus
    middle = bus/2
    if closeest_dep > middle:
        possibilities[bus] = bus-closeest_dep

#bus_id = min(possibilities, key=possibilities.get)
#res = bus_id*possibilities[bus_id]
#print(res)

### Part 2 ####

with open('vscode/adventofcode/aoc13.txt') as f:
    notes = f.read().splitlines()

bus_list = notes[1].split(',')
count_x = bus_list.count('x')
fin = len(bus_list)
start = int(bus_list[0])
dep = 0
found = 1
bus_list_num = bus_list.copy()
for i, bus in enumerate(bus_list):
    if bus != 'x':
        bus_list[i] = int(bus)
    if bus == 'x':
        bus_list_num[i] = bus_list_num[i-1]

bus_list_num = [int(x) for x in bus_list_num]

skip = []

for i, bus in enumerate(bus_list[1:]):
    if bus == 'x':
        continue
    while (dep+i+1)%bus!=0:
        dep += start
    print(dep, ' ', start, ' ', i, ' ', bus)
    start *= bus

print(dep)
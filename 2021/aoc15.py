from collections import defaultdict
from aoc9 import get_neighbors
import sys

with open('aoc15.txt') as f:
    puzzle = f.read().splitlines()

riskmap = [[int(x) for x in line] for line in puzzle]

path = []

def get_smallest_neighbor(x,y,visited):
    neighbors = get_neighbors((x,y),riskmap)
    test = defaultdict()
    for neighbor in neighbors:
        if (neighbor[0],neighbor[1]) not in visited:
            test[(neighbor[0],neighbor[1])] = riskmap[neighbor[0]][neighbor[1]]
    if not test:
        return None, None         
    smallest =  min(test.values())
    res = [key for key in test if test[key] == smallest]
    return test, smallest

def explore_map(x, y, map, path=[]):
    path = path + [(x,y)]
    paths = []
    next_nodes,val = get_smallest_neighbor(x,y,path)
    if x == len(map)-1 and y == len(map[0])-1:
        return [path]
    if next_nodes == None:
        return []
    for node in next_nodes:
        newpaths = explore_map(node[0],node[1], map, path)
        for newpath in newpaths:
                paths.append(newpath)
    return paths

paths = explore_map(0,0,riskmap)

def get_risk_to_path(path):
    risk = 0
    for point in path:
        risk += riskmap[point[0]][point[1]]
    return risk

lowest_risk = sys.maxsize
print(len(paths))

for path in paths:
    
    risk = get_risk_to_path(path)
    #print(path, ' ', risk)
    if risk < lowest_risk:
        lowest_risk = risk

print(lowest_risk)
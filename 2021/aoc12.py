import itertools
from collections import defaultdict
import copy

with open("aoc12.txt") as f:
    puzzle = f.read().splitlines()

connections_list1 = [line.split("-") for line in puzzle]
connections_list = copy.deepcopy(connections_list1)
caves = set(list(itertools.chain.from_iterable(connections_list)))
small_caves = list(filter(lambda x: x.islower(), caves))
big_caves = list(filter(lambda x: x.isupper(), caves))

for big in caves:
    for a, b in connections_list1:
        if a == big:
            if b != "end":
                connections_list.append([b, a])
connections = dict(list())
for s,e in connections_list:
    if s not in connections:
        connections[s] = list()
        connections[s].append(e)
    else:
        connections[s].append(e)

def check_max_one_small_cave_double(node, small_visited):
    if node == 'start':
        return False
    if any(value==3 for value in small_visited.values()):
        return False
    number = sum(value==2 for value in small_visited.values())
    if number <= 1:
        return True
    return False

def reset_small_cave_counter(small_cave_counter: dict):
    for k,v in small_cave_counter.items():
        if v >= 100:
            small_cave_counter[k] = 100
        else:
            small_cave_counter[k] = 0
    return small_cave_counter


def find_all_paths(graph, start, end, path=[], small_caves_visited={}):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                if node in small_caves:
                    small_caves_visited[node] += 1
                newpaths = find_all_paths(graph, node, end, path, small_caves_visited)
                for newpath in newpaths:
                    paths.append(newpath)
            elif check_max_one_small_cave_double(node,small_caves_visited):
                if node in small_caves:
                    small_caves_visited[node] += 1
                newpaths = find_all_paths(graph, node, end, path, small_caves_visited)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


paths = []
visited = {}
for cave in small_caves:
    visited[cave] = 0
visited['start'] = 100
visited['end'] = 100
test = find_all_paths(connections, 'start', 'end',[], visited)
for finding in test:
    paths.append(finding)

for path in paths:
    print(path)

print(len(paths))
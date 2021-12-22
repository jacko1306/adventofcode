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

for big in big_caves:
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


def find_all_paths(graph, start, end, path=[], small_caves_visited=[]):
        path = path + [start]
        if start == end:
            return [path]
        if start not in graph:
            return []
        paths = []
        for node in graph[start]:
            if node not in path:
                if node in small_caves:
                    small_caves_visited.append(node)
                newpaths = find_all_paths(graph, node, end, path, small_caves_visited)
                for newpath in newpaths:
                    paths.append(newpath)
            elif node not in small_caves_visited:
                newpaths = find_all_paths(graph, node, end, path, small_caves_visited)
                for newpath in newpaths:
                    paths.append(newpath)
        return paths


paths = []
test = find_all_paths(connections, 'start','end')
for finding in test:
    paths.append(finding)

for path in paths:
    print(path)

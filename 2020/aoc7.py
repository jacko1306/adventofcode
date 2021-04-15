#!/usr/bin/python3

import re
from string import digits

res = 0
res2 = 0
container = dict()
COLOR = 'shiny gold'

with open('/vscode/adventofcode/aoc7.txt') as f:
    report = f.read().split('\n')

for line in report:
    outer_color, inner_color_str = line.split('bags contain')
    outer_color = outer_color.rstrip()
    inner_color_str_split = inner_color_str.split(',')
    inner_colors = dict()
    for inner_color in inner_color_str_split:
        if inner_color == ' no other bags.':
            continue
        amount = re.search("\d+", inner_color).group()
        inner_color = ' '.join(inner_color.split(' ')[2:4])
        inner_color = inner_color.replace('bags', '').replace(' bag', '').replace('.', '').strip()
        inner_colors[inner_color] = amount

    container[outer_color] = inner_colors

def loop(current_color, color_values):
    list = []
    if not color_values:
        return False
    for c in color_values:
        if c == COLOR:
            return True
        else:
            ans = loop(c, container[c])
            if ans:
                break
    if ans: 
        return True
    else: 
        return False

for line in container.keys():
    col = container[line]
    result = loop(line, col)
    if result:
        res += 1

print(res)

def count(color_values):
    if not color_values:
        return 1
    else:
        ret_val = 1
        for k,v in color_values.items():
            number = int(count(container[k]))
            ret_val += int(v)*number
        return ret_val

num = count(container[COLOR])-1

print(num)
#print(container)
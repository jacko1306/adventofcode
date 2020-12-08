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

def count(color_values, color, num):
    if not color_values:
        return 1
    else:
        ret_val = 1
        for k,v in color_values.items():
            
            number = int(count(container[k],k,int(v)))

            ret_val += int(v)*number

        return ret_val

for line in container.keys():
    if line != COLOR:
        continue
    col = container[line]
    amnt = 0
    num = count(container[COLOR],COLOR,amnt)
    num-=1

print(num)
#print(container)

'''
violet = 1
blue = 2 * violet+1
green = 2 * blue+1
yellow = 2 * green+1
orange = 2 * yellow+1
red= 2*orange+1
shiny = 2*red

print(shiny)



for line in report:
    outer_color, keyword, inner_color_str = line.partition('bags contain')
    outer_color = outer_color.rstrip()
    inner_color_str_split = inner_color_str.split(',')
    inner_colors = []
    for inner_color in inner_color_str_split:
        if inner_color[:3] == ' no':
            continue
        num = re.search('\d+', inner_color).group()
        name = inner_color.replace(str(num),'').replace('bag', '').replace(' s', '').replace('.', '').lstrip().rstrip()

        inner_colors.append(name)

    container[outer_color] = inner_colors

output = ''

def rec_replace(old_color, old_inner, text):
    new_inner = []
    if len(old_inner)>=1:
        for inside in old_inner:
            new_color = inside.replace(inside,' '.join(container[inside])).split(' ')
            for inner_color in new_color:
                new_inner += container[inner_color]
                text += inner_color
            text += rec_replace(new_color, new_inner, text)
    return text

def return_children(parent_color):
    

for outer, inner in container.items():
    for color in inner:
        if color == __color__:
            res += 1
        new_color = rec_replace(color, inner, '')
        output += new_color + ' '
        print(output)
    output += '\n'

print(output)

def second():
    for line in report:
        outer_color, keyword, inner_color_str = line.partition('bags contain')
        outer_color = outer_color.rstrip()
        inner_color_str_split = inner_color_str.split(',')
        inner_colors = dict()
        for inner_color in inner_color_str_split:
            if inner_color[:3] == ' no':

                continue
            num = re.search('\d+', inner_color).group()
            name = inner_color.replace(str(num),'').replace('bag', '').replace(' s', '').lstrip().rstrip()

            inner_colors[num] = name

        container[outer_color] = inner_colors

    output = dict()
            
    for k, v in container:
        print(9)
    print(container)

'''
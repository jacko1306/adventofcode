#!/usr/bin/python3

import re


def item_check(item):
    res = False
    val = item[1]
    id = item[0]
    if id == 'byr':
        #return 1920 <= int(val) <= 2002
        val = int(val)
        if val >= 1920 and val <= 2002:
            res = True
            return res
    if id == 'iyr':
        val = int(val)
        if val >= 2010 and val <= 2020:
            res = True
            return res
    if id == 'eyr':
        val = int(val)
        if val >= 2020 and val <= 2030:
            res = True
            return res
    if id == 'hgt':
        unit = val[-2:]
        num = re.findall("\d+", val)
        type_1 = type(num)
        num = int(num[0])
        if unit == 'in':
            if num >= 59 and num <= 76:
                res = True
                return res
        elif unit == 'cm':
            if num >= 150 and num <= 193:
                res = True
                return res
    if id == 'hcl':
        if re.match('\#......',val):
            count = 0
            for i in val:
                if i == "#":
                    continue
                elif re.match('[a-f0-9]',i):
                    count+=1
            if count == 6:
                res = True
                return res
    if id == 'ecl':
        truth = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if val in truth:
            res = True
            return res
    if id == 'pid':
        length = len(val)
        if length == 9 and re.match('[0-9]',val):
            res = True
            return res
    return res

def validycheck(line):
    result = []
    valid_items = 0
    trigger = 0
    return_val = False
    for item in line:
        item = item.split(":")
        result.append(item)
        if item[0] == 'cid':
            valid_items += 1
            trigger = 1
        elif item_check(item):
            valid_items += 1
    
    if valid_items == 8 or (valid_items == 7 and trigger == 0):
        return_val = True
    return return_val

report = []
res = 0
with open('/vscode/adventofcode/aoc4.txt') as file:
    report = file.read().split('\n\n')
for line in report: 
    line = line.replace("\n", " ")
    line = line.split(" ")
    res += validycheck(line)

print(res)


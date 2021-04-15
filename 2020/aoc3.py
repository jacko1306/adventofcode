#!/usr/bin/python3

report = []

with open('/vscode/adventofcode/aoc3.txt') as file:
    for line in file:
        report.append(line.strip())

step = 3

i = 0
j = 0
while i < len(report)-1:
    i+=1
    line = report[i]
    
    if j+step < len(line):
        j+=step
    else:
        overflow = len(line)-j
        j=overflow-1
    print(line, ' ', j, ' ', line[j])
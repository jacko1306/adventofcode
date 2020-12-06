#!/usr/bin/python3

from collections import Counter

report = []
with open('/vscode/adventofcode/six.txt') as f:
    report = f.read().split('\n\n')
res_1 = 0
res_2 = 0
for line in report:
    length = line.count('\n') +1
    line = line.replace('\n', '')
    c = dict(Counter(line))
    for amnt in c.values():
        res_2 += amnt ==length
    for i in c:
        res_1 += 1
print(res_1)
print(res_2)
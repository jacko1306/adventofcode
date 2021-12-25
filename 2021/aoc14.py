from collections import defaultdict
from collections import Counter

with open('aoc14.txt') as f:
    puzzle = f.read().splitlines()

template = puzzle[0]
rules = puzzle[2:]
rulebook = defaultdict()
for rule in rules:
    k,v = rule.split(' -> ')
    rulebook[k] = v

def calc(template):
    for _ in range(5):
        insert_vals = []
        for i in range(len(template) - 1):
            start = template[i]
            end = template[i+1]
            lookup = start + end
            insert_val = rulebook[lookup]
            insert_vals.append(insert_val)
        template = ''.join(''.join(x) for x in zip(template,insert_vals))+template[-1]
        
        c = Counter(template)
        print(c)
        print(template)
    return c


c = calc(template)
min_occ = min(c.values())
max_occ = max(c.values())

print(max_occ-min_occ)

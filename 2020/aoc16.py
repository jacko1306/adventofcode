with open('/vscode/adventofcode/aoc16.txt') as f:
    input = f.read().split('\n\n')

fields = input[0].split('\n')
myticket = list(input[1].splitlines())
myticket.pop(0)
myticket = myticket[0].split(',')
nearbytickets = input[2].splitlines()
nearbytickets.pop(0)
fields_dict = {}
valid = list(nearbytickets.copy())
solution = {}

for field in fields:
    name, rule = field.split(':')
    rules = [x.strip() for x in rule.split(' or ')]
    rule_set = []
    for r in rules:
        range_low, range_high = r.split('-')
        s = range(int(range_low),int(range_high)+1)
        rule_set.extend(s)
    fields_dict[name] = rule_set

scanning_error = []

for i in range(0,len(nearbytickets)):
    for n in nearbytickets[i].split(','):
        num = int(n)
        count = 0
        for r in fields_dict.values():
            if num in r:
                count+=1
        if count == 0:
            scanning_error.append(num)
            valid.remove(nearbytickets[i])
            break
print(sum(scanning_error))

unknown_list = []
for i in range(0, len(list(valid[0].split(',')))):
    unknown_list.append([])

for line in valid:
    values = list(map(int,list(line.split(','))))
    for i, num in enumerate(values):
        unknown_list[i].append(num)

for i, pos in enumerate(unknown_list):
    for name, r in fields_dict.items():
        count = 0
        for num in pos:
            if num in r:
                count += 1
        if count == len(pos):
            if name not in solution.values():
                solution[i] = name

print(solution)
myticketdict = {}
for i, val in enumerate(list(map(int,myticket))):
    name = solution[i]
    myticketdict[name] = val

print(myticketdict)
from itertools import islice
from itertools import starmap
import operator
with open('vscode/adventofcode/aoc10.txt') as f:
    adapters = list(map(int,f.read().splitlines()))
    adapters.sort()
#with open('vscode/adventofcode/test.txt', 'w') as f:
#    for item in adapters:
#        f.write("%s\n" % item)

adapters.insert(0,0)
max_adapter = max(adapters)
built_in_adapter = max_adapter+3
adapters.append(built_in_adapter)

ones = 0
threes = 0

for i in range(0,len(adapters)-1):
    if adapters[i+1]-adapters[i] == 1:
        ones += 1
    else:
        threes += 1

print(ones*threes)

twos = 0
threes = 0
fours = 0
min_adapters = []
adapters.append(-10)
adapters.append(-10)
adapters.append(-10)
adapters.append(-10)
skips = []
steps = []
for i, adapter in enumerate(adapters):
    if adapters[i] == -10:
        continue
    steps.append(adapters[i+1]-adapter)
    if adapter in skips:
        continue
    if adapters[i+1]-adapters[i] == 1 and adapters[i+2]-adapters[i+1] == 1 and adapters[i+3]-adapters[i+2] == 1 and adapters[i+4]-adapters[i+3] == 1:
        fours+=1
        skips.append(adapter)
        skips.append(adapters[i+1])
        skips.append(adapters[i+2])
        skips.append(adapters[i+3])
    else:
        if adapters[i+1]-adapters[i] == 1 and adapters[i+2]-adapters[i+1] == 1 and adapters[i+3]-adapters[i+2] == 1:
            threes+=1
            skips.append(adapter)
            skips.append(adapters[i+1])
            skips.append(adapters[i+2])
        else:
            if adapters[i+1]-adapters[i] == 1 and adapters[i+2]-adapters[i+1] == 1:
                twos+=1
                skips.append(adapter)
                skips.append(adapters[i+1])

res = 7**fours*4**threes*2**twos
print(res)


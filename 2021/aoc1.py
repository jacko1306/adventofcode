with open('aoc1.txt') as f:
    depth = [int(x) for x in f.readlines()]

def gen_list(values):
    changes =  []
    for i,x in enumerate(values):
        if i == 0:
            continue
        changes.append(x>values[i-1])
    return sum(changes)

print(gen_list(depth))

###PART TWO###

res = 0
depth_acc = []

for i,x in enumerate(depth):
    if i == len(depth)-2:
        break
    depth_acc.append(x+depth[i+1]+depth[i+2])

print(gen_list(depth_acc))

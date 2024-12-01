import numpy as np

with open('input1.txt') as f:
    room_list = f.read().splitlines()
    
left = []
right = []

for i,j in [n.split ('  ') for n in room_list]:
    left.append(int(i))
    right.append(int(j))

result = [abs(x - y) for x, y in zip(sorted(right), sorted(left))]

print(sum(result))

second = 0
for n in left:
    second += n*right.count(n)

print(second)
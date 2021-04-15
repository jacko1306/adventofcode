with open('/home/florianjacke/vscode/adventofcode/aoc15.txt') as f:
    input = f.read().split(',')
input = list(map(int,input))
index_dict = {}
for i, value in enumerate(input):
    index_dict[value] = i+1
for i in range(6,30000000):
    if input[i-1] not in index_dict:
        input.append(0)
        index_dict[input[i-1]] = i
    else:
        last = input.pop()
        val = index_dict[last]
        index_dict[last] = i
        input.append(last)
        input.append(i-val)

print(input[-1])
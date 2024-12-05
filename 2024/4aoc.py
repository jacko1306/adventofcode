from collections import defaultdict

with open("input4.txt") as f:
    word_search = f.read().splitlines()

word_map = defaultdict(str)


def find_adjacent(x, y, dir=(None,None)):
    neighbors = {
        (1,0): word_map[x + 1, y],
        (-1,0): word_map[x - 1, y],
        (0,1): word_map[x, y + 1],
        (0,-1): word_map[x, y - 1],
        (1,1): word_map[x + 1, y + 1],
        (1,-1): word_map[x + 1, y - 1],
        (-1,1): word_map[x - 1, y + 1],
        (-1,-1): word_map[x - 1, y - 1],
    }
    if dir == (None,None):
        return neighbors 
    else:
        return {dir:neighbors[dir]}


for x, line in enumerate(word_search):
    for y, character in enumerate(line):
        word_map[x, y] = character

counter = 0
counter2 = 0

for x, line in enumerate(word_search):
    for y, character in enumerate(line):
        if character == "X":
            adjacents = find_adjacent(x, y)
            for k,v in adjacents.items():
                if v == 'M':
                    third = find_adjacent(x+k[0],y+k[1],k)
                    for k3,v3 in third.items():
                        if v3 == 'A':
                            fourth = find_adjacent(x+k[0]+k[0],y+k[1]+k[1],k)
                            for k4,v4 in fourth.items():
                                if v4 == 'S':
                                    counter +=1
        if character == 'A':
            corners = [find_adjacent(x,y, (-1,-1)),find_adjacent(x,y, (-1,1)), find_adjacent(x,y, (1,-1)), find_adjacent(x,y,(1,1) )]
            corner_values = []
            for c in corners:
                for kc,vc in c.items():
                    corner_values += vc 
            if len(corner_values) == 4:
                if corner_values == ['M', 'M', 'S', 'S'] or corner_values == ['M', 'S', 'M', 'S'] or corner_values == ['S', 'S', 'M', 'M'] or corner_values == ['S', 'M', 'S', 'M']:
                    counter2 += 1

print(counter)
print(counter2)
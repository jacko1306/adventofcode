from itertools import product

with open('/vscode/adventofcode/aoc17.txt') as f:
    input = f.read().splitlines()

z_init = 3
z_max = 2
x_max = 2
y_max = 2
slice = []

for i, line in enumerate(input):
    slice.append([])
    for char in line:
        slice[i].append(char)  

cube = [slice]

cube_new = cube.copy()

def pprint(list):
    for item in list:
        for line in item:
            print(*line)
        print()

def is_outside(x,y,z):
    return x < 0 or x >= x_max or y < 0 or y >= y_max or z < 0 or z >= z_max

def stencil(dim):
    stencils = list(product([-1,0,1], repeat=dim))
    zero = ((0,) * dim)
    stencils.remove(zero)
    return stencils

def neighbours(P):
    stencils = stencil(len(P))
    return [tuple([sum(x) for x in zip(P,s)]) for s in stencils]

def get_neighbors(x,y,z):
    P = (x,y,z)
    active = 0
    inactive = 0
    all_neighbours = neighbours(P)
    for location in all_neighbours:
        x1 = location[0]
        y1 = location[1]
        z1 = location[2]
        if is_outside(*location):
            try:
                some = cube_new[z1]
                try:
                    some =  cube_new[z1][x1]
                    cube_new[z1][x1].append('.')
                except:
                    cube_new[z1].append(['.'])
            except:
                cube_new.append([list('.')])
        test = cube_new[z1][x1][y1]
        if test == '.':
            inactive += 1
        else:
            active += 1
        
    return active, inactive

for z, slice in enumerate(cube):
    for x, line in enumerate(slice):
        for y, current in enumerate(line):
            print(x, y, z)
            active, inactive = get_neighbors(x,y,z)
            if current == '.':
                if active == 3:
                    print(cube_new[z][x][y])
            else:
                if 3 <= active <= 2:
                    print(cube_new[z][x][y])



import operator

matrix = dict()
line_length = 0

def get_input():
    global line_length
    with open('vscode/adventofcode/aoc11.txt') as f:
        input = f.read().splitlines()
    matrix = dict()
    line_length = len(input[0])
    count_L = 0
    for x, line in enumerate(input):
        for y in range(0,len(line)):
            if line[y] == 'L': count_L+=1
            point = (x,y)
            matrix[point] = line[y]
    return matrix
### part 1 ####

matrix = get_input()

def pretty_print():
    count = 0
    for point, seat in matrix.items():
        print(seat, end='')
        count+=1
        if count == line_length:
            print('')
            count = 0

def check(point, old_matrix):
    try:
        if old_matrix[point] == '#': return 1
        else: return 0
    except:
        return 0

def num_adjacent_seats_occ(point, old_matrix):
    x,y = point
    ret,l,r = 0,0,0
    u = 0
    d = 0
    lu = 0
    ld = 0
    ru = 0
    rd = 0
    l = check((x,y-1),old_matrix)
    lu = check((x-1,y-1),old_matrix)
    u = check((x-1,y),old_matrix)
    ru = check((x-1,y+1),old_matrix)
    r = check((x,y+1),old_matrix)
    rd = check((x+1,y+1),old_matrix)
    d = check((x+1,y),old_matrix)
    ld = check((x+1,y-1),old_matrix)
    return l+r+u+d+lu+ld+rd+ru

def empty_and_no_adjacent(matrix):
    old_matrix = matrix.copy()
    for point, seat in matrix.items():
        if seat == 'L' and num_adjacent_seats_occ(point, old_matrix) < 1:
            matrix[point] = '#'
    return matrix

def occupied_and_four_adjecent(matrix):
    old_matrix = matrix.copy()
    for point, seat in matrix.items():
        if seat == '#' and num_adjacent_seats_occ(point, old_matrix) >= 4:
            matrix[point] = 'L'
    return matrix

def populate_seats(matrix):
    matrix = empty_and_no_adjacent(matrix)
    matrix = occupied_and_four_adjecent(matrix)
    return matrix

new_matrix = dict()
old_matrix = matrix.copy()

while old_matrix != new_matrix:
    old_matrix = matrix.copy()
    new_matrix = populate_seats(matrix) 
    
def count_seats():
    return sum(map(lambda x: x == '#', matrix.values()))

print(count_seats())

#### PART 2 ####

matrix = get_input()

def check2(point, old_matrix, dir):
    try:
        new_point = tuple(map(operator.add, point, dir))
        if old_matrix[new_point] == '#': 
            return 1
        elif old_matrix[new_point] == '.': 
            return check2(new_point, old_matrix, dir)
        elif old_matrix[new_point] == 'L': 
            return 0
    except:
        return 0

def num_adjacent_seats_occ2(point, old_matrix):
    x,y = point
    ret = 0
    l,r,u,d,lu,ld,ru,rd = 0,0,0,0,0,0,0,0
    
    l = check2(point ,old_matrix, (0,-1))
    lu = check2(point ,old_matrix, (-1,-1))
    u = check2(point ,old_matrix, (-1,0))
    ru = check2(point ,old_matrix, (-1,1))
    r = check2(point ,old_matrix, (0,1))
    rd = check2(point ,old_matrix, (1,1))
    d = check2(point ,old_matrix, (1,0))
    ld = check2(point ,old_matrix, (1,-1))
    return l+r+u+d+lu+ld+rd+ru

def empty_and_no_adjacent_2(matrix):
    old_matrix = matrix.copy()
    for point, seat in matrix.items():
        num = num_adjacent_seats_occ2(point, old_matrix)
        if seat == 'L' and num < 1:
            matrix[point] = '#'
    return matrix

def occupied_and_five_adjecent_2(matrix):
    old_matrix = matrix.copy()
    for point, seat in matrix.items():
        num = num_adjacent_seats_occ2(point, old_matrix)
        if seat == '#' and num >= 5:
            matrix[point] = 'L'
    return matrix

def populate_seats_2(matrix):
    matrix = empty_and_no_adjacent_2(matrix)
    matrix = occupied_and_five_adjecent_2(matrix)
    return matrix

new_matrix = dict()
old_matrix = matrix.copy()
i = 0
while old_matrix != new_matrix:
    old_matrix = matrix.copy()
    new_matrix = populate_seats_2(matrix) 
    i+=1
print(count_seats())
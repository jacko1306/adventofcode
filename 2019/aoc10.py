import itertools
import copy

with open("aoc10.txt") as f:
    map = f.read().split()

map_length = len(map[0])
map_height = len(map)
all_astertoids = 0
for line in map:
    ast_in_line = line.count("#")
    all_astertoids += ast_in_line

map_dict = {}
y = 0
for line in map:
    x = 0
    for el in line:
        if el == ".":
            val = 0
        else:
            val = 1
        map_dict[(x, y)] = val
        x += 1
    y += 1


def list_rel_asteroids(x, y) -> dict:
    map_dict_trans = {}
    for key, value in map_dict.items():
        map_dict_trans[(x * -1 + key[0], y * -1 + key[1])] = value
    return map_dict_trans


def same_quad(vector1, vector2):
    if (
        vector1[0] < 0 and vector2[0] < 0 or vector1[0] >= 0 and vector2[0] >= 0
    ) and (vector1[1] < 0 and vector2[1] < 0 or vector1[1] >= 0 and vector2[1] >= 0):
        return True


def check_independency(vector1, vectors):
    for vector2 in vectors:
        if same_quad(vector1, vector2):
            if (vector1[0] * vector2[1]) - (vector1[1] * vector2[0]) == 0:
                return False
    return True


def eliminate_lin_dependent_vectors(vectors) -> list:
    vectors.remove((0, 0))
    independent_vectors = []
    for vector1 in vectors:
        if check_independency(vector1, independent_vectors):
            independent_vectors.append(vector1)
    return independent_vectors


def get_relative_asteroid_vectors(rel_ast_dict):
    vector_list = []
    for key, value in rel_ast_dict.items():
        if value == 1:
            vector_list.append(key)
    return vector_list


def detect_aseroids(x, y):
    rel_ast_dict = list_rel_asteroids(x, y)
    vector_list_all_asteroids = get_relative_asteroid_vectors(rel_ast_dict)
    independent_vectors = eliminate_lin_dependent_vectors(vector_list_all_asteroids)
    #print(x, y)
    #print(independent_vectors)
    return len(independent_vectors)


y = 0
max_num = 0
max_x = 0
max_y = 0

for line in map:
    newline = ""
    x = 0
    for el in line:
        num = 0
        if el == "#":
            num += detect_aseroids(x, y)
            if num > max_num:
                max_num = num
                max_x = x
                max_y = y
            newline += str(num)
        else:
            newline += "."
        x += 1
    y += 1
    #print(newline)


print(max_num)
print(max_x, max_y)
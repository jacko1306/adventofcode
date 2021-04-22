import math
from collections import Counter

with open("aoc4.txt") as f:
    minimum, maximum = map(int, f.read().split("-"))


def check_decrease(x):
    x_sorted = "".join(map(str,sorted(map(int,list(x)))))
    if x==x_sorted:
        return True


def check_adjacent(x):
    x_list = list(x)
    for i, element in enumerate(x_list[:-1]): 
        if element == x_list[i+1]:
            return True
    

def check_adjacent2(x):
    return 2 in Counter(x).values()


res = 0
res2 = 0

for x in range(minimum, maximum + 1):
    if check_decrease(str(x)):
        if check_adjacent(str(x)):
            res += 1
        if check_adjacent2(str(x)):
            res2 += 1

print(res)
print(res2)
print()
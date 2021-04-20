import math


with open("aoc4.txt") as f:
    minimum, maximum = map(int, f.read().split("-"))


def check_decrease(x):
    a = int(str(x)[0])
    b = int(str(x)[1])
    c = int(str(x)[2])
    d = int(str(x)[3])
    e = int(str(x)[4])
    f = int(str(x)[5])
    return a <= b <= c <= d <= e <= f


def check_adjacent(x):
    a = int(str(x)[0])
    b = int(str(x)[1])
    c = int(str(x)[2])
    d = int(str(x)[3])
    e = int(str(x)[4])
    f = int(str(x)[5])
    return a == b or b == c or c == d or d == e or e == f


def check_adjacent2(x):
    a = int(str(x)[0])
    b = int(str(x)[1])
    c = int(str(x)[2])
    d = int(str(x)[3])
    e = int(str(x)[4])
    f = int(str(x)[5])
    return (
        (a == b and b != c)
        or (b == c and c != d and a != b)
        or (c == d and d != e and b != c)
        or (d == e and e != f and d != c)
        or (e == f and d != e)
    )


res = 0
res2 = 0

for x in range(minimum, maximum + 1):
    if check_decrease(x):
        if check_adjacent(x):
            res += 1
        if check_adjacent2(x):
            res2 += 1

print(res)
print(res2)
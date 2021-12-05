from collections import Counter

with open("aoc5.txt") as f:
    puzzle_input = f.read().splitlines()


def get_intersections(part):
    points = []
    for line in puzzle_input:
        begin, end = line.split(" -> ")
        x1, y1 = [int(x) for x in begin.split(",")]
        x2, y2 = [int(y) for y in end.split(",")]
        if x1 == x2:
            for i in range(min(y1, y2), max(y1, y2) + 1):
                points.append((x1, i))
        elif y1 == y2:
            for j in range(min(x1, x2), max(x1, x2) + 1):
                points.append((j, y1))
        elif part == 2:
            if min(x1, x2) == x1 and min(y1, y2) == y1:
                step = 0
                for a in range(x1, x2 + 1):
                    points.append((a, y1 + step))
                    step += 1
            elif min(x1, x2) == x2 and min(y1, y2) == y2:
                step = 0
                for a in range(x2, x1 + 1):
                    points.append((a, y2 + step))
                    step += 1
            elif min(x1, x2) == x1 and min(y1, y2) == y2:
                step = 0
                for a in range(x1, x2 + 1):
                    points.append((a, y1 - step))
                    step += 1
            elif min(x1, x2) == x2 and min(y1, y2) == y1:
                step = 0
                for a in range(x2, x1 + 1):
                    points.append((a, y2 - step))
                    step += 1

    return [item for item, count in Counter(points).items() if count >= 2]


print(len(get_intersections(1)))
print(len(get_intersections(2)))

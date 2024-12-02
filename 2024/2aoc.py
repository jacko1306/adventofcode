with open("input2.txt") as f:
    reports = f.read().splitlines()


def isSafe(levels):
    diff_list = []
    for x, y in zip(levels[0::], levels[1::]):
        diff_list.append(y - x)
    if max(diff_list) < 0 and min(diff_list) >= -3:
        return 1
    elif min(diff_list) > 0 and max(diff_list) <= 3:
        return 1
    else:
        return 0


result = 0

for levels in reports:
    levels = map(int, levels.split(" "))
    result += isSafe(list(levels))

print(result)


def getSubLevel(levels):
    sublevels = []
    for x in range(len(levels)):
        sublevels.append(levels[: x - len(levels)] + levels[x + 1 :])
    return sublevels


result2 = 0
for levels in reports:
    for sublevel in getSubLevel(list(map(int, levels.split(" ")))):
        if isSafe(sublevel) == 1:
            result2 += 1
            break

print(result2)

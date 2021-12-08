from collections import defaultdict

with open("aoc6.txt") as f:
    fishes = f.read().split(",")


def mapping():
    global fishes
    global N
    fishes = [int(fish) for fish in fishes]
    N = defaultdict(int)
    for fish in fishes:
        N[fish] += 1


def calc(days):
    global N
    for _ in range(days):
        new_fishes = defaultdict(int)
        for x, cnt in N.items():
            if x == 0:
                new_fishes[6] += cnt
                new_fishes[8] += cnt
            else:
                new_fishes[x - 1] += cnt
        N = new_fishes

    print(sum(N.values()))


mapping()
calc(80)
mapping()
calc(256)

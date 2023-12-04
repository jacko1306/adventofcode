from collections import defaultdict
import math

with open("input2aoc.txt") as f:
    game_list = f.read().splitlines()

loaded = {"red": 12, "green": 13, "blue": 14}

possible_games_sum = 0

power = 1
power_sum = 0

for game in game_list:
    id = int(game.split(": ")[0].split(" ")[1])
    sets = game.split(": ")[1].split("; ")
    max_counter = defaultdict(int)
    for subset in sets:
        counters = []
        counters += subset.split(", ")
        subsubset = []
        for count in counters:
            subsubset += count.split(" ")
            for k, v in loaded.items():
                if k not in subsubset:
                    continue
                new_val = int(subsubset[subsubset.index(k) - 1])
                max_counter[k] = max(max_counter[k], new_val)

    compared_dict = {
        k: loaded[k] for k in loaded if k in max_counter and loaded[k] >= max_counter[k]
    }
    if (len(compared_dict)) >= 3:
        possible_games_sum += id

    power_sum += math.prod(max_counter.values())

print(possible_games_sum)
print(power_sum)
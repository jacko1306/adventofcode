from math import floor
from itertools import permutations

with open("input5.txt") as f:
    manual = f.read().split("\n\n")

rules = [list(int(i) for i in x.split("|")) for x in manual[0].splitlines()]
updates = [list(int(n) for n in y.split(",")) for y in manual[1].splitlines()]


def check_rule(number, sequence):
    new_sequence = []
    number_index_in_sequence = sequence.index(number)
    rule_counter = 0
    test_counter = 0
    for rule in rules:
        if number in rule:
            test_list = rule.copy()
            test_list.remove(number)
            if test_list[0] in sequence:
                test_counter += 1
                compare_index_in_sequence = sequence.index(test_list[0])
                number_index_in_rule = rule.index(number)
                compare_index_in_rule = rule.index(test_list[0])
                if number_index_in_rule < compare_index_in_rule:
                    if number_index_in_sequence < compare_index_in_sequence:
                        rule_counter += 1
                    

                elif number_index_in_rule > compare_index_in_rule:
                    if number_index_in_sequence > compare_index_in_sequence:
                        rule_counter += 1
                    else:
                        new_sequence = sequence.copy()
                        new_sequence.insert(compare_index_in_sequence + 1, number)
                        new_sequence.remove(number)
    if new_sequence:
        return rule_counter == test_counter, new_sequence
    else:
        return rule_counter == test_counter, sequence


result = 0
result2 = 0


for k, update in enumerate(updates):
    tested_updates = []
    update_counter = 0
    for u in update:
        n, new_update = check_rule(u, update)
        update_counter += n
        if new_update not in tested_updates:
            tested_updates.append(new_update)
    if update_counter == len(update):
        middle = floor(len(update) / 2)
        result += update[middle]
    else:
        k                            


print(result)
print(result2)

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


for update in updates:
    update_counter = 0
    update_counter2 = 0
    new_update = []
    error_in_update = False

    while new_update != update:
        if new_update:
            error_in_update = True
            update = new_update.copy()
            update_counter2 = 0
        for u in update:
            n, new_update = check_rule(u, update)
            if n:
                if error_in_update:
                    update_counter2 += n
                else:
                    update_counter += n
            else:
                break

    if update_counter == len(update):
        middle = floor(len(update) / 2)
        result += update[middle]
    if update_counter2 == len(update):
        middle = floor(len(update) / 2)
        result2 += update[middle]

print(result)
print(result2)

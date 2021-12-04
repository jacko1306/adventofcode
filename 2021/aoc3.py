with open("aoc3.txt") as f:
    report = f.read().splitlines()

bit_report = []

for line in report:
    bit_report.append([int(x) for x in line])

gamma = ""
epsilon = ""
oxy_candidates = bit_report.copy()
co2_candidates = bit_report.copy()


def get_most_and_least_common(basis, i):
    acc = sum(bit_row[i] for bit_row in basis)
    most_common = round(acc / len(basis))
    least_common = int(most_common != 1)

    return most_common, least_common, acc == len(basis) / 2


for i in range(len(bit_report[0])):
    most_common, least_common, equal = get_most_and_least_common(bit_report, i)
    gamma += str(most_common)
    epsilon += str(least_common)

print(int(gamma, 2) * int(epsilon, 2))

##PART TWO###
def removal(candidates, reference):
    for i in range(len(bit_report[0])):
        if len(candidates) > 1:
            most_common, least_common, equal = get_most_and_least_common(candidates, i)
            valuetocheck = least_common
            if reference == 1:
                valuetocheck = most_common
            for bit_row in bit_report:
                if not equal:
                    if bit_row[i] == valuetocheck:
                        try:
                            candidates.remove(bit_row)
                        except:
                            continue
                else:
                    for bit_row in candidates:
                        if bit_row[i] == reference:
                            candidates.remove(bit_row)
    return candidates

oxy_candidates = removal(oxy_candidates, 0)
co2_candidates = removal(co2_candidates, 1)
'''
for i in range(len(bit_report[0])):
    if len(oxy_candidates) > 1:
        most_common, least_common, equal = get_most_and_least_common(oxy_candidates, i)
        for bit_row in bit_report:
            if not equal:
                if bit_row[i] == least_common:
                    try:
                        oxy_candidates.remove(bit_row)
                    except:
                        continue
            else:
                for bit_row in oxy_candidates:
                    if bit_row[i] == 0:
                        oxy_candidates.remove(bit_row)
for i in range(len(bit_report[0])):
    if len(co2_candidates) > 1:
        most_common, least_common, equal = get_most_and_least_common(co2_candidates, i)
        for bit_row in bit_report:
            if not equal:
                if bit_row[i] == most_common:
                    try:
                        co2_candidates.remove(bit_row)
                    except:
                        continue
            else:
                for bit_row in co2_candidates:
                    if bit_row[i] == 1:
                        co2_candidates.remove(bit_row)

'''
print(
    int("".join([str(x) for x in oxy_candidates[0]]), 2)
    * int("".join([str(x) for x in co2_candidates[0]]), 2)
)

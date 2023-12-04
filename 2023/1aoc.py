with open("input1aoc.txt") as f:
    puzzle = f.readlines()

res = 0
spelled_numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]


def rreplace(s, old, new, occurrence):
    li = s.rsplit(old, occurrence)
    return new.join(li)


for line in puzzle:
    position_found_dict_low = {}
    for spelled in spelled_numbers:
        lowest_spot_where_substring_found = 10000
        if spelled in line and line.find(spelled) < lowest_spot_where_substring_found:
            lowest_spot_where_substring_found = line.find(spelled)
            position_found_dict_low[lowest_spot_where_substring_found] = spelled
    position_found_dict_high = {}
    for spelled in spelled_numbers:
        highest_spot_where_substring_found = 0
        if spelled in line and line.rfind(spelled) > highest_spot_where_substring_found:
            highest_spot_where_substring_found = line.rfind(spelled)
            position_found_dict_high[highest_spot_where_substring_found] = spelled
    if len(position_found_dict_low) > 0:
        first_spelled_number = position_found_dict_low[min(position_found_dict_low)]

        original_line = line
        if first_spelled_number in original_line:
            line = line.replace(
                first_spelled_number,
                str(spelled_numbers.index(first_spelled_number) + 1)
                + first_spelled_number,
                1,
            )
    if len(position_found_dict_high) > 0:
        last_spelled_number = position_found_dict_high[max(position_found_dict_high)]
        if last_spelled_number in original_line:
            line = rreplace(
                line,
                last_spelled_number,
                last_spelled_number
                + str(spelled_numbers.index(last_spelled_number) + 1),
                1,
            )
    only_numbers = [int(i) for i in line if i.isdigit()]
    if len(only_numbers) > 0:
        res += only_numbers[0]*10 + only_numbers[-1]

print(res)

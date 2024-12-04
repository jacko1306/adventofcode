import re

with open("input3.txt") as f:
    memory = f.read()


def get_result(memory):
    sequences = re.findall("mul\(\d+,\d+\)", memory)

    result = 0

    for seqeuce in sequences:
        x, y = [int(c) for c in re.findall("\d+", seqeuce)]
        result += x * y

    print(result)


get_result(memory)

test = ""


def run_memory(memory, test):
    condition_dont = re.search("don't\(\)", memory)
    test += memory[: condition_dont.start()]
    memory = memory[condition_dont.start() :]
    condition_do = re.search("do\(\)", memory)
    memory = memory[condition_do.start() :]
    return memory, test


while re.search("don't\(\)", memory):
    memory, test = run_memory(memory, test)

test += memory
get_result(test)

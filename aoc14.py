with open('vscode/adventofcode/aoc14.txt') as f:
    input = f.read().splitlines()

def write_to_mem(mask: str, memory, value):
    global memory_global
    value_bin = int(bin(value),2)
    print(int(value_bin,2))
    high = 2**35-1
    mask_one = int(mask.replace('X','0'),2)
    mask_zero_int = int(mask.replace('X','1'),2)
    mask_zero = high-mask_zero_int
    new_val = mask_one & value_bin
    print(new_val)


def extract_info(program):
    mask = program[0]
    memories = []
    values = []
    for i in range(1,len(program)):
        memories.append(program[i][0])
        values.append(program[i][1])
    for i in range(0,len(program)-1):
        write_to_mem(mask, memories[i], values[i])

program = []
memory_global = []
for line in input:
    if line[:4] == 'mask':
        program = []
        mask = line[8:]
        program.append(mask)
    if line[:3] == 'mem':
        memory = line[4]
        value = line[9:]
        program.append((memory, value))

extract_info(program)
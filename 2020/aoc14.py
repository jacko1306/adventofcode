import re
import pprint

with open('/home/florianjacke/vscode/adventofcode/aoc14.txt') as f:
    input = f.read().splitlines()

def write_to_mem(mask: str, memory, value):
    global memory_global
    mask_one = int(mask.replace('X','0'),2)
    mask_zero = int(mask.replace('X','1'),2)
    val = bin((value | int(bin(mask_one),2)) & int(bin(mask_zero),2))
    memory_global[memory] = int(val,2)

memory_global = dict()
for line in input:
    if line.startswith('mask'):
        mask = line[7:]
    if line.startswith('mem'):
        memory, value = line.split('=')
        value = int(value.strip())
        memory = re.findall("\d+", memory)[0]
        write_to_mem(mask, memory, value)
        
pp = pprint.PrettyPrinter(depth=6)

pp.pprint(memory_global.values())
print(sum(memory_global.values()))

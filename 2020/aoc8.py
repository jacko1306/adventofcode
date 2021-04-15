#//usr/bin/python3

accelerator = 0

with open('/vscode/adventofcode/aoc8.txt') as f:
    report = f.read().split('\n')

program = report

already_processed_lines = [False]*len(program)

def get_inputs(rule):
    action, val = rule.split(' ')
    val = int(val)
    return action, val

def go_to_next(index, rule):
    global accelerator
    if not already_processed_lines[index]:
        action,val = get_inputs(rule)
        already_processed_lines[index] = True
        step = 1
        if action == 'jmp':
            step = val
        next_index = index + step
        if action == 'acc':
            accelerator = accelerator + val
        if next_index >= len(report):
            return True
        
        
        return go_to_next(next_index, report[next_index])
    return False

go_to_next(0,report[0])
print(accelerator)

for i, line in enumerate(report):
    accelerator = 0
    already_processed_lines = [False]*len(report)
    action, val = line.split(' ')
    val = int(val)
    
    if action == 'acc':
        continue
    if action == 'nop':
        report[i] = 'jmp ' + str(val)
    if action == 'jmp':
        report[i] = 'nop ' + str(val)
    res=go_to_next(0,report[0])
    if action == 'nop':
        report[i] = 'nop ' + str(val)
    if action == 'jmp':
        report[i] = 'jmp ' + str(val)
    if res:
        print(accelerator)

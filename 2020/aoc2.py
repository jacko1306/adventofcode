import re

report = []

with open('/vscode/adventofcode/aoc2.txt') as file:
    for line in file:
        report.append(line.strip())

def part_one(report):
    result = 0
    for line in report:
        num = list(map(int,re.findall(r'\d+',line)))    
        key = str(re.findall(r'.:',line))
        k = str(''.join(x for x in key if x.isalpha()))
        p = str(re.findall(r':.*',line))
        pw = str(''.join(x for x in p if x.isalpha()))
        c = pw.count(k)
        if num[0] <= c <= num[1]:
            result += 1
    return result        

def part_two(report):
    result = 0
    for line in report:
        policy, letter, password = line.split(' ')
        #print(line)
        letter = letter[0]
        values = policy.split('-')
        min_val = int(values[0])-1
        max_val = int(values[1])-1
        #print(password[min_val], ' ', password[max_val], ' ', letter)
        if (password[min_val] == letter) ^ (password[max_val] == letter):
            result += 1
            #print(result)
    return result

result1 = part_one(report)
result = part_two(report)

print(result1)
print(result)






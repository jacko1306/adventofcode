with open('/vscode/adventofcode/aoc18.txt') as f:
    input = f.read().splitlines()

for line in input:
    numbers = []
    operators = []
    for element in line:
        if element == ' ':
            continue
        elif element == '+' or element == '*':
            operators.append(element)
        else:
            numbers.append(int(element))

res = numbers[0]

for i in range(0,len(numbers)-1):
    if operators[i] == '+':
        res += numbers[i+1]
    else:
        res *= numbers[i+1]

print(res)
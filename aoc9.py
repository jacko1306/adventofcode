
with open('vscode/adventofcode/aoc9.txt') as f:
    input = f.read().splitlines()

def get_preamble(index):
    return input[index-25:index]

def check(num, preamble):
    for x in preamble:
        if str(num-int(x)) in preamble:
            return False
    return True

for i, num in enumerate(input):
    if i<25:
        continue
    preamble = get_preamble(i)
    if check(int(num), preamble):
        res1=num
        print(num)
        break

res1=int(res1)
res2=0
input = list(map(int,input))
weakness = []
sum = 0

def add_set(start):
    global sum, res2
    for num in input[start:]:
        if sum<res1:
            weakness.append(num)
            sum +=num
        elif sum == res1:
            res2 = min(weakness) +  max(weakness)
            print(res2)
            return
        elif sum > res1:
            return
i=0
while res2 == 0:
    add_set(i)
    sum=0
    weakness=[]
    i += 1

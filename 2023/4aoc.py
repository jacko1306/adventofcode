with open("input4.txt") as f:
    lines = f.read().splitlines()

res = 0
    
for line in lines:
    card, numbers = line.split(':')
    txt, card_number = card.split()
    winning_numbers, my_numbers = (list(int(i) for i in x.split()) for x in numbers.split('|'))
    
    dupl = list(x for x in winning_numbers if x in my_numbers)
    if len(dupl) > 0:
        res += 2**(len(dupl)-1)

print(res)
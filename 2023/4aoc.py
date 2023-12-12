from collections import defaultdict

with open("input4.txt") as f:
    lines = f.read().splitlines()

res = 0
additional_cards = defaultdict(lambda: 1)

for line in lines:
    card, numbers = line.split(":")
    card_number = int(card.split()[-1])
    winning_numbers, my_numbers = (
        list(int(i) for i in x.split()) for x in numbers.split("|")
    )

    dupl = list(x for x in winning_numbers if x in my_numbers)
    if len(dupl) > 0:
        res += 2 ** (len(dupl) - 1)

    for n in range(additional_cards[card_number]):
        for m in range(card_number + 1, card_number + len(dupl) + 1):
            additional_cards[m] += 1

print(res)
print(sum(additional_cards.values()))

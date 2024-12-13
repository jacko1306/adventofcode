import itertools
from operator import mul
from functools import reduce

with open("input7.txt") as f:
    equations = f.read().splitlines()

final = 0
final2 = 0


def mul_sum(value_list, test_result, part):
    if part == 1:
        operators = ["*", "+"]
    else:
        operators = ["*", "+", '||']
    for operator_product in itertools.product(operators, repeat=len(value_list) - 1):
        test = [
            x
            for x in itertools.chain.from_iterable(
                itertools.zip_longest(value_list, operator_product)
            )
            if x
        ]
        calculated = int(test[0])
        current_operator = ""
        for x in test[1:]:
            if x == "+":
                current_operator = "+"
                continue
            elif x == "*":
                current_operator = "*"
                continue
            elif x == '||':
                current_operator = ''
                continue
            else:
                if current_operator == "*":
                    calculated *= int(x)
                elif current_operator == '+':
                    calculated += int(x)
                if current_operator == '':
                    calculated = int(str(calculated)+str(x))
        if calculated == test_result:
            return test_result
    return 0


for equation in equations:
    test_result, values_all = equation.split(": ")
    test_result = int(test_result)
    values = [a for a in values_all.split(" ")]
    final += mul_sum(values, test_result, 1)
    final2 += mul_sum(values, test_result, 2)
 

print(final)
print(final2)
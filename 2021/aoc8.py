from typing import final


with open('aoc8.txt') as f:
    puzzle = f.read().splitlines()

part_1 = 0

for line in puzzle:
    ten_sign_patterns, four_digit_output = [num.strip() for num in line.split('|')]
    ten_sign_patterns = ten_sign_patterns.split(' ')
    four_digit_output = four_digit_output.split(' ')
    part_1 += sum(len(z)<=4 or len(z)==7 for z in four_digit_output)
print(part_1)

final_res = 0

for line in puzzle:
    ten_sign_patterns, four_digit_output = [num.strip() for num in line.split('|')]
    ten_sign_patterns = ten_sign_patterns.split(' ')
    four_digit_output = four_digit_output.split(' ')
    positions =  {}
    num_to_char = {}
    char_count = {'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0} 
    for signal in ten_sign_patterns:
        for char in signal:
            char_count[char] += 1

    positions[1] = list(char_count.keys())[list(char_count.values()).index(6)]
    positions[4] = list(char_count.keys())[list(char_count.values()).index(4)]
    positions[5] = list(char_count.keys())[list(char_count.values()).index(9)]

    for signal in ten_sign_patterns:
        length = len(signal)    
        if length == 2:
            num_to_char[1] = signal
        elif length == 3:
            num_to_char[7] = signal
        elif length == 4:
            num_to_char[4] = signal
        elif length == 7:
            num_to_char[8] = signal
        
    positions[0] = list(set(num_to_char[7]) - set(num_to_char[1]))[0]
    positions[2] = list(set(num_to_char[1]) - set(positions[5]))[0]
    positions[3] = list(set(num_to_char[4]) - set(positions[1]) - set(positions[2]) - set(positions[5]))[0]
    positions[6] = list(set(num_to_char[8]) - set(positions[0]) - set(positions[1]) - set(positions[2]) - set(positions[3]) - set(positions[4]) - set(positions[5]))[0]

    reverted_positions =  dict((v,k) for k,v in positions.items())
    pos_to_real_number = {'012456':0, '25':1, '02346':2, '02356':3, '1235':4, '01356':5, '013456':6, '025':7, '0123456':8, '012356':9}
    res = ''
    for number in four_digit_output:
        number1 = ''
        for character in number:
            number1 += str(reverted_positions[character])
        a = sorted(number1, key=lambda x: float(x))
        b = ''.join(a)
        res += str(pos_to_real_number[b])
    final_res += int(res)

print(final_res)

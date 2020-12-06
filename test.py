#!/usr/bin/python3

with open('five.txt', 'r') as input_file: seat_codes = input_file.read().replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1').split('\n'); 
seat_ids = [int(i[:7], 2) * 8 + int(i[7:], 2) for i in seat_codes]; 

print(str((seat_ids[[(i + 1 not in seat_ids) and (i + 2 in seat_ids) for i in seat_ids].index(True)] + 1)))


max_id = max(seat_ids)
print(max_id)
for i in range(0,max_id):
    if i+1 in seat_ids and i-1 in seat_ids and i not in seat_ids:
        print(i)
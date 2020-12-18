"""Day 5. Binary Boarding."""
from pprint import pprint

def find_seat(line, row_min, row_max, col_min, col_max, number):
    # print(f"{line} {row_min} {row_max} {col_min} {col_max} {number}")
    a = line[:1]
    line = line[1:]
    number += 1
    if number == 10:
        if a == 'R':
            return row_min, col_max
        else:
            return row_min, col_min

    if number == 7:
        if a == 'F':
            row_max = row_min
        else:
            row_min = row_max
    elif number < 7:
        if a == 'F':
            row_max = row_max - round((row_max - row_min) / 2)
        else:
            row_min = row_min + round((row_max - row_min) / 2)
    else:
        if a == 'R':
            col_min = col_min + round((col_max - col_min) / 2)
        else:
            col_max = col_max - round((col_max - col_min) / 2)
        
    return find_seat(line, row_min, row_max, col_min, col_max, number)


with open("input.txt", "r") as f:
    lines = f.readlines()
rows_count = 127
cols_count = 7
number = 0
seats = []
i = 1

# Part onw
# for line in lines:
#     row, col = find_seat(line, 0, rows_count, 0, cols_count, number)
#     seat_id = row * 8 + col
#     seats.append(seat_id)

# seats.sort()
# seat_id_max = seats.pop()
# print(seat_id_max)

# Part two
a = []
for i in range(0,128):
    a.append([])
    for j in range(0,8):
        a[i].append(0)

# pprint(a)
# print(a[127][7])

for line in lines:
    row, col = find_seat(line, 0, rows_count, 0, cols_count, number)
    a[row][col] = 1
    # seat_id = row * 8 + col
    # seats.append(seat_id)
pprint(a)

for i in range(8, 120):
    if 0 in a[i]:
        b = a[i]
        col = b.index(0)
        row = i
        break
seat_id = row * 8 + col    
print(f"col = {col} row = {row} seat_id = {seat_id}")
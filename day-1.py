
inputs = []
start_pos = 50 # Where the dial starts
size = 100 # How many total numbers we have

with open('inputs/day-1-a.txt', 'r') as f:
    lines = f.readlines()
    for l in lines:
        inputs.append((l[0], int(l[1:])))

number_of_zeros = 0

result = start_pos
for [direction, amount] in inputs:
    rotation_amount = amount if direction == 'R' else -amount

    end_position = result + rotation_amount
    full_rotations = abs(end_position) // size
    crossovers = 1 if end_position <= 0 and result != 0 else 0

    result = end_position % size
    number_of_zeros += full_rotations + crossovers

if result == 0:
    number_of_zeros += 1
print(result, number_of_zeros)

# 11:49
# 12:47. Hard part done in 15 mins, 45 mins of tedious data processing :death:

lines = []
with open('inputs/day-6.txt', 'r') as f:
    lines = [l.replace('\n','') for l in f.readlines()] # Remove trailing new line

max_line_len = max([len(l) for l in lines])
lines = [l + ' ' * (max_line_len - len(l)) for l in lines]

r = 0
max_range = 0
for s in lines[-1]:
    if s == '*' or s == '+':
        if r > max_range:
            max_range = r
        r = 1
    else:
        r += 1

padded_vals = ['' for l in range(len(lines))]

found_ops = 0
used_padding = 0
for i_str in range(max_line_len):
    if lines[-1][i_str] == '*' or lines[-1][i_str] == '+':
        found_ops += 1
        padding_needed = max_range - used_padding
        if found_ops > 1:
            for i_line in range(len(padded_vals)):
                padded_vals[i_line] += ' ' * padding_needed
        used_padding = 0
    for i_line in range(len(padded_vals)):
        padded_vals[i_line] += lines[i_line][i_str]
    used_padding += 1
padding_needed = max_range - used_padding
if found_ops > 1:
    for i_line in range(len(padded_vals)):
        padded_vals[i_line] += ' ' * padding_needed

for l in padded_vals:
    print(l)

lines = padded_vals

col_count = len([i for i in lines[-1] if i != ' ' and i != "\n"])
# padding is the length of the last line, remove the last operation (no trailing spaces)
# divide by number of columns, ignoring the last (no trailing spaces)
padding = (len(lines[-1])-1)//(col_count-1)
digit_length = len(lines) - 1

# Normalize line lengths
for i, line in enumerate(lines):
    difference = padding*col_count - len(line)
    line = line + (' ' * difference)
    lines[i] = line


sections = []

# Loop over each problem
result = 0
for col_index in range(0, col_count):
    # Loop over each value
    values = []
    for op_value in range(0, padding - 1): # Minus 1 because of space between columns
        parsed_val = ''
        op_value_str_index = col_index * padding + op_value
        for d in range(digit_length):
            parsed_val += lines[d][op_value_str_index]
        if parsed_val.strip() != '':
            values.append(int(parsed_val))
    col_operation = lines[-1][col_index*padding]

    total = 0
    if col_operation == '+':
        for j in values:
            total += j
    if col_operation == '*':
        total = 1
        for j in values:
            total *= j
    print(col_operation, values, total)
    result += total
print('Result: ', result)


# WHY ISN"T THE INPUT CONSISTENT WIDTHS
# Going to have to normalize it. Fun.
# Can't normalize easily. Death. The whitespace could be before or after, so we can't know how long it should be.
# SO HAVE TO BUILD THESE LINES ONE BY ONE BASED ON WHERE THE OPERATION IS. SO TEDIOUS.

# 9770311935122 too low
# Was stripping last char instead of replacing \n in input, so missed the last operation
# 9770311947567
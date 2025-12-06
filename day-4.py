inputs = []
with open('inputs/day-4-a.txt', 'r') as f:
    inputs = [l.strip() for l in f.readlines()]

def get_neighbors(x: int, y: int, board):
    x_vector = [-1, 0, 1]
    y_vector = [-1, 0, 1]

    neighbors = []
    for x_v in x_vector:
        for y_v in y_vector:
            test_x = x + x_v
            test_y = y + y_v
            if not(x_v == 0 and y_v == 0):
                if test_y >= 0 and test_y < len(board):
                    test_row = board[test_y]
                    if test_x >= 0 and test_x < len(test_row):
                        neighbors.append(test_row[test_x])
    return neighbors

def accessible(neighbors: list[str]):
    roll_count = len([n for n in neighbors if n == '@'])
    return roll_count < 4

def boards_equal(b1, b2):
    if len(b1) != len(b2):
        return False
    if len(b1[0]) != len(b2[0]):
        return False
    for y, row in enumerate(b1):
        for x, cell in enumerate(row):
            if y < len(b2) and x < len(b2[0]) and cell != b2[y][x]:
                return False
    return True

h = len(inputs)
w = len(inputs[0])

count = 0
for x in range(0, w):
    for y in range(0, h):
        if accessible(get_neighbors(x, y, inputs)) and inputs[y][x] == '@':
            count += 1

print(count)

# Part 2
b2 = []
prev = inputs
while not boards_equal(prev, b2):
    if len(b2) != 0:  # hate this conditional but how do you avoid resetting prev on first run?
        prev = b2
    b2 = [] # Reset the new board
    for y in range(0, h):
        b2.append([])
        for x in range(0, w):
            if accessible(get_neighbors(x, y, prev)):
                b2[-1].append('.')
            else:
                b2[-1].append(prev[y][x])

inputs_count = 0
for x in range(0, w):
    for y in range(0, h):
        if inputs[y][x] == '@':
            inputs_count += 1

count = 0
for x in range(0, w):
    for y in range(0, h):
        if b2[y][x] == '@':
            count += 1
print(inputs_count - count)
for row in b2:
    new_row = ''
    for cell in row:
        new_row += cell
    print(new_row)
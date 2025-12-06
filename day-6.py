# 11:40
# Part 1: 11:49

lines = []
vals = []
ops = []
with open('inputs/day-6.txt', 'r') as f:
    lines = f.readlines()
    vals = [[int(el.strip()) for el in l.split(' ') if el != ''] for l in lines[:-1]]
    ops = [(el.strip()) for el in lines[-1].split(' ') if el != '']

print(vals, ops)

result = 0
for i in range(0, len(vals[0])):
    total = 0
    if ops[i] == '+':
        for j in range(0, len(vals)):
            total += vals[j][i]
    if ops[i] == '*':
        total = 1
        for j in range(0, len(vals)):
            total *= vals[j][i]
    result += total

print('Result: ', result)

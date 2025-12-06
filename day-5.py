lines = []
with open('inputs/day-5-a.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]

fresh = []
avail = []

found_space = False

for line in lines:
    if line == '':
        found_space = True
        continue
    if found_space:
        avail.append(int(line))
    else:
        fresh.append([int(l) for l in line.split('-')])

fresh_noisy = sorted(fresh)
avail = sorted(avail)

# fresh_noisy = [
#     [3,5],
#     [6,15],
#     [12,20],
#     [6,8],
#     [21,25],
#     [27,27],
#     [29,29],
#     [29,35],
#     [29, 30],
#     [35, 35]
# ]
# 31

"""
3
15
5
1
7
"""

fresh = []
for i, f in enumerate(fresh_noisy):
    is_dup = False
    if not i == 0:
        prev = fresh[-1]
        if prev[1] >= f[0]:
            fresh[-1][1] = max(f[1], prev[1])
            is_dup = True
    if not is_dup:
        fresh.append(f)

count = 0
found = set()
for f in fresh:
    print(f)
    count += f[1]-f[0]+1
    if f[0] in found:
        print('duplicate of ', f[0])
    if f[1] in found:
        print('duplicate of ', f[1])
    found.add(f[0])
    found.add(f[1])

# 3-5
# 4 - 20
# 7-9
# 20-16

print('Number of Possible Fresh: ', count)
# 342572021918433 <- Too low
# Handle fully encompassed ranges 352662119010118 <- Too high
# Sorted by both numbers 352509891817901 <- Too high
# 352509891817882 <- Still wrong, unclear why, and unclear why the number doesn't match the previous. It's because 2 numbers were deleted out of input, unclear how.
# GOT IT! It's got a duplicate entry when the start is the same as the end of the previous.
# Very subtle cause. Was reading the previous fron the input instead of the built up list, which only caused a problem
# When a range was followed by a 1 element range of the same number.
# 352509891817881

count = 0
for ingredient in avail:
    # Check if the ingredient is fresh
    # Find the closest min
    closest = fresh[0]
    index = 0
    for f in fresh:
        if f[0] > ingredient:
            break
        closest = f
        index += 1

    if index == len(fresh):
        closest = fresh[-1]

    is_fresh = ingredient >= closest[0] and ingredient <= closest[1]
    if is_fresh:
        count += 1

count = 0
for ingredient in avail:
    is_fresh = False
    for f in fresh:
        if ingredient >= f[0] and ingredient <= f[1]:
            is_fresh = True
    if is_fresh:
        count +=1

print (count)

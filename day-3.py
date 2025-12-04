inputs = []
with open('inputs/day-3-a.txt', 'r') as f:
    inputs = [l.strip() for l in f.readlines()]

def get_largest_pair(n: str):
    max = 0
    # Loop through once to test every number
    for i, val in enumerate(n):
        # Loop through the rest of n
        for val2 in n[i+1:]:
            if int(str(val)+str(val2)) > max:
                max = int(str(val)+str(val2))
    return max

def get_largest_run(n: str, run: int):
    maxes = []
    # For each number, how many possible runs are there, and how big are they?
    for i, val in enumerate(n):
        obj = {}
        maxes.append(obj)
        maxes[-1][1] = int(val)  # For every value, we have a run of length 1, and max is current val

        if len(maxes) == 1:
            continue # Move on if first element

        prev_obj = maxes[-2]

        for key in prev_obj:
            if prev_obj[key] > obj[key]:
                obj[key] = prev_obj[key] # Take previous best if its better
            if key + 1 <= run:
                # Grow the run if we can
                if key+1 in prev_obj:
                    obj[key+1] = max(prev_obj[key+1], int(str(prev_obj[key]) + val))
                else:
                    obj[key+1] = int(str(prev_obj[key]) + val)
    return maxes[-1][run]


max_joltage = 0
for line in inputs:
    max_joltage += get_largest_run(line, 12)
print(max_joltage)

def tests():
    assert get_largest_pair('9876511111') == 98
    assert get_largest_pair('811111111111119') == 89
    assert get_largest_pair('234234234234278') == 78
    assert get_largest_pair('818181911112111') == 92
    assert get_largest_run('987654321111111', 12) == 987654321111
    assert get_largest_run('811111111111119', 12) == 811111111119
    assert get_largest_run('234234234234278', 12) == 434234234278
    assert get_largest_run('818181911112111', 12) == 888911112111
tests()


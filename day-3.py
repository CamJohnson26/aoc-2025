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

max_joltage = 0
for line in inputs:
    max_joltage += get_largest_pair(line)
print(max_joltage)

def tests():
    assert get_largest_pair('9876511111') == 98
    assert get_largest_pair('811111111111119') == 89
    assert get_largest_pair('234234234234278') == 78
    assert get_largest_pair('818181911112111') == 92
tests()
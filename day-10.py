lines = []
machines = []

with open('inputs/day-10-test.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        b_i = 1
        b_j = line.index(']')
        br_i = line.index('{') + 1
        br_j = line.index('}')
        indicators = line[b_i:b_j]
        joltage = [int(num) for num in line[br_i:br_j].split(',')]
        elements = line.split(' ')[1: -1]
        buttons = [[int(s) for s in el.replace('(', '').replace(')', '').split(',')] for el in elements]
        machines.append({
            "indicators": indicators,
            "joltage": joltage,
            "buttons": buttons
        })

def push_button(light_state_str, button):
    light_state = list(light_state_str)
    for l in button:
        light_state[l] = '#' if light_state[l] == '.' else '.'
    return ''.join(light_state)


def get_minimum_presses_r(machine, found, depth=1):
    new_states = []
    start_len = len(found)
    for old_state in found:
        for button in machine['buttons']:
            new_state = push_button(old_state, button)
            new_states.append(new_state)
            if (machine["indicators"] == new_state):
                return depth
    for s in new_states:
        found.add(s)
    end_len = len(found)
    if start_len == end_len:
        raise "No new presses found!"
    return get_minimum_presses_r(machine, found, depth + 1)

def get_minimum_presses(machine):
    ini = '.' * len(machine['indicators'])
    found = set([ini])
    return get_minimum_presses_r(machine, found)


total = 0
for m in machines:
    total += get_minimum_presses(m)
    print(total)
print(total)
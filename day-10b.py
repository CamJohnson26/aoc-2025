import math

lines = []
machines = []

from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

"""
For every joltage, there's a certain number of buttons that reference it, and we need to push them exactly the same number of times as the joltage
This creates a system of equations, where every group of buttons is a variable, and the end joltage is the answer

We would usually use least-squares, but since only integers are valid, we use milp instead, optimized for this.

a_i is just a matrix with one row per joltage, and a value for each button. if the button references the joltage,
we set it to 1, otherwise 0.

b_i is the right hand side for each of these equations.

So 
e+f=3
b+f=5
c+d+e=4
a+b+d=7

Would be:
[
    [0, 0, 0, 0, 1, 1],  # e + f = 3
    [0, 1, 0, 0, 0, 1],  # b + f = 5
    [0, 0, 1, 1, 1, 0],  # c + d + e = 4
    [1, 1, 0, 1, 0, 0],  # a + b + d = 7
]
and
[3, 5, 4, 7]

What a pain
"""
def solve(a_i, b_i):
    # variable order: [a, b, c, d, e, f]
    A_eq = np.array(a_i, dtype=float)

    b_eq = np.array(b_i, dtype=float)

    constraints = LinearConstraint(A_eq, b_eq, b_eq)

    # nonnegative bounds
    bounds = Bounds(lb=np.zeros(len(a_i[0])), ub=np.full(len(a_i[0]), np.inf))

    # all variables are integers
    integrality = np.ones(len(a_i[0]), dtype=int)

    # tie-breaker objective: minimize sum of variables
    c = np.ones(len(a_i[0]))

    return round(milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)["fun"])


with open('inputs/day-10a.txt', 'r') as f:
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

def push_button(light_state, button):
    for l in button:
        light_state[l] = light_state[l] - 1
    return light_state

def to_str(n):
    return ','.join([str(i) for i in n])

def to_list(n):
    return [int(s) for s in n.split(',')]

def get_minimum_presses_r(machine, target, depth=0):

    if all([i==0 for i in target]):
        return depth

    subproblems = []
    for b in machine["buttons"]:
        new_state = ''
        result = list(target)
        d = 0
        while result != new_state or result == '':
            new_state = list(result)
            result = push_button(result, b)
            d += 1
            if any([i for i in result if i < 0]):
                if not new_state == target:
                    subproblems.append((new_state, depth+d-1)) # -1 since we go one too far
                break

    minimum = -1
    for s in subproblems:
        result = get_minimum_presses_r(machine, s[0], s[1])
        if minimum == -1 or (result < minimum and result != -1):
            minimum = result
    return minimum

def get_minimum_presses(machine):
    return get_minimum_presses_r(machine, list(machine['joltage']))

print('Starting')
total = 0
for m in machines:
    b_eq = m["joltage"]
    a_eq = []
    for i, joltage in enumerate(b_eq):
        a_eq.append([])
        for button in m["buttons"]:
            contains_joltage = i in button
            a_eq[-1].append(1 if i in button else 0)
    solution = solve(a_eq, b_eq)
    print(solution)
    total += solution
print(total)


    # result = get_minimum_presses(m)
    # print(result)
    # total += result
# print(total)



"""
a
b
c
d
e
f

e+f=3
b+f=5
c+d+e=4
a+b+d=7

minimize sum(a+b+c+d+e+f)
"""

"""
Can we assume that for every subsolution, we'll need to press some button the maximum number of times?
"""

"""
18558 -> too low
18559
"""
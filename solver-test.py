
from scipy.optimize import milp, LinearConstraint, Bounds
import numpy as np

def solve(a_i, b_i):
    # variable order: [a, b, c, d, e, f]
    A_eq = np.array([
        [0, 0, 0, 0, 1, 1],  # e + f = 3
        [0, 1, 0, 0, 0, 1],  # b + f = 5
        [0, 0, 1, 1, 1, 0],  # c + d + e = 4
        [1, 1, 0, 1, 0, 0],  # a + b + d = 7
    ], dtype=float)

    b_eq = np.array([3, 5, 4, 7], dtype=float)

    constraints = LinearConstraint(A_eq, b_eq, b_eq)

    # nonnegative bounds
    bounds = Bounds(lb=np.zeros(6), ub=np.full(6, np.inf))

    # all variables are integers
    integrality = np.ones(6, dtype=int)

    # tie-breaker objective: minimize sum of variables
    c = np.ones(6)

    return milp(c=c, constraints=constraints, bounds=bounds, integrality=integrality)["x"]

# %%

from itertools import product
import re
import numpy as np

arr = []

with open("input") as fobj:
    parts = []
    for line in fobj.readlines():
        if digits := re.findall(r"(\d+)", line):
            parts += digits
        else:
            arr.append(parts)
            parts = []
    arr.append(parts)

arr = np.array(arr, int)


presses = np.array(tuple(product(range(0, 101), range(0, 101))))

# %%  part 1

cost = 0

for machine in arr:

    a = machine[:2]
    b = machine[2:4]
    prize = machine[4:]

    results = (
        presses[:, 0, np.newaxis] * a + presses[:, 1, np.newaxis] * b
    )

    solutions = np.argwhere((results == prize).all(axis=1))

    if solutions.any():
        cost += min(np.dot(presses[idx], [3, 1])[0] for idx in solutions)

print(int(cost))

# %%  part 2

cost = 0

for machine in arr:

    a = machine[:2]
    b = machine[2:4]
    prize = machine[4:] + 10000000000000

    X = np.stack([a, b]).T

    solution = np.linalg.solve(X, prize)

    if abs(solution[0] - np.round(solution[0])) < 0.0025:
        cost += np.dot(solution, [3, 1])

print(int(cost))

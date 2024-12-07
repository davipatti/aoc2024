# %%

from operator import mul, add
from itertools import product, repeat


# %%

calibrations = []

with open("input") as fobj:
    for line in fobj:
        parts = line.split()
        target = int(parts[0][:-1])
        values = [int(value) for value in parts[1:]]
        calibrations.append((target, values))

# %%


def evaluate(values, operators):
    current = values[0]
    for value, operator in zip(values[1:], operators):
        current = operator(current, value)
    return current


def operator_combinations(n, operators=(mul, add)):
    yield from product(*zip(*(repeat(op, n) for op in operators)))


def is_possible(target, values, operators):
    for operators in operator_combinations(len(values) - 1, operators):
        if evaluate(values, operators) == target:
            return True
    else:
        return False


def solve(operators):
    return sum(
        target
        for target, values in calibrations
        if is_possible(target, values, operators)
    )


# %% part 1


print(solve((mul, add)))

# %% part 2


def concat(a, b):
    return int(str(a) + str(b))


print(solve((mul, add, concat)))

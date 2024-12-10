# %%

import numpy as np

# %% part 1


def is_safe(row):
    diff = np.diff(row)
    all_monotonic = all(diff > 0) or all(diff < 0)
    all_diffs_eq_1_2_or_3 = all((0 < abs(diff)) & (abs(diff) < 4))
    return all_monotonic and all_diffs_eq_1_2_or_3


i = 0
with open("input") as fobj:
    for line in fobj:
        i += is_safe([int(v) for v in line.strip().split()])

print(i)


# %% part 2


def is_safe_2(row):
    return any(is_safe(np.delete(row, i)) for i in range(len(row)))


i = 0
with open("input") as fobj:
    for line in fobj:
        i += is_safe_2([int(v) for v in line.strip().split()])

print(i)

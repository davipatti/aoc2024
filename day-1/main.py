# %%

import numpy as np

arr = np.loadtxt("input")

# %% part 1

print(np.abs(np.subtract.reduce(np.sort(arr, axis=0), axis=1)).sum())

# %% part 2

print(sum(value * (arr[:, 1] == value).sum() for value in arr[:, 0]))

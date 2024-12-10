# %%

import numpy as np

with open("input") as fobj:
    grid = np.array([list(line.strip()) for line in fobj], int)

nrows, ncols = grid.shape


def neighbours(i, j):
    for m, n in (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1):
        if 0 <= m < nrows and 0 <= n < ncols:
            yield m, n


def visit(i, j):
    if grid[i, j] == 9:
        yield i, j
    else:
        for m, n in neighbours(i, j):
            if grid[i, j] + 1 == grid[m, n]:
                yield from visit(m, n)


# %% part 1

print(sum(len(set(visit(i, j))) for i, j in np.argwhere(grid == 0)))


# %% part 2

print(sum(len(list(visit(i, j))) for i, j in np.argwhere(grid == 0)))

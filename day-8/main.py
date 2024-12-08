# %%

from itertools import combinations

import numpy as np


with open("input") as fobj:
    grid = np.array([list(line.strip()) for line in fobj])


def in_grid(position):
    nrows, ncols = grid.shape
    i, j = position
    return i >= 0 and j >= 0 and i < nrows and j < ncols


# %%  part 1

antinodes = set()
for char in set(grid.ravel()) - {"."}:
    for a, b in combinations(np.argwhere(grid == char), 2):
        diff = b - a
        antinodes.add(tuple(a - diff))
        antinodes.add(tuple(b + diff))


print(sum(in_grid(pos) for pos in antinodes))

# %%  part 2

antinodes = set()
for char in set(grid.ravel()) - {"."}:
    for a, b in combinations(np.argwhere(grid == char), 2):
        diff = b - a

        antinodes.add(tuple(a))
        antinodes.add(tuple(b))

        antinode = a - diff
        while in_grid(antinode):
            antinodes.add(tuple(antinode))
            antinode -= diff

        antinode = b + diff
        while in_grid(antinode):
            antinodes.add(tuple(antinode))
            antinode += diff

print(len(antinodes))

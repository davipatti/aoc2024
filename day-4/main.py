# %%

import numpy as np

# %%

with open("input") as fobj:
    grid = np.array([tuple(line.strip()) for line in fobj])

# %% part 1


def rotations(grid):
    for _ in range(4):
        yield grid
        grid = np.rot90(grid)


def diagonals(grid):
    nrows, ncols = grid.shape
    assert nrows == ncols
    for offset in range(-(nrows - 1), nrows):
        yield np.diagonal(grid, offset)


def part1(grid):

    total = 0

    for rotation in rotations(grid):
        for row in rotation:
            total += "".join(row).count("XMAS")

        for diagonal in diagonals(rotation):
            total += "".join(diagonal).count("XMAS")

    return total


print(part1(grid))


# %% part 2


def part2(grid):

    # X-shaped mask
    row_mask = np.array([0, 0, 1, 2, 2])
    col_mask = np.array([0, 2, 1, 0, 2])

    target = np.array(list("MSAMS"))

    total = 0

    # Slide the X-shaped mask over all positions in all rotations of the grid
    nrows, ncols = grid.shape
    for rotation in rotations(grid):
        for row_shift in range(nrows - 2):
            for col_shift in range(ncols - 2):

                i = row_mask + row_shift
                j = col_mask + col_shift

                if (rotation[i, j] == target).all():
                    total += 1

    return total


print(part2(grid))

# %%

from itertools import product
import numpy as np

with open("input") as fobj:
    grid = np.array([list(line.strip()) for line in fobj])

nrows, ncols = grid.shape


def neighbours(i, j):
    for m, n in (i - 1, j), (i, j + 1), (i + 1, j), (i, j - 1):
        if 0 <= m < nrows and 0 <= n < ncols:
            yield m, n


def grow_patch(i: int, j: int, patch: set = None):
    patch = patch or set()
    yield i, j
    patch.add((i, j))

    # Iterate over all unvisited neighbours
    for m, n in set(neighbours(i, j)) - patch:

        # For matching plants, yield their coordinates, and grow
        if grid[m, n] == grid[i, j]:
            yield from grow_patch(m, n, patch)


def find_all_patches():
    coords = set(product(range(nrows), range(ncols)))
    while coords:
        patch = set(grow_patch(*coords.pop()))
        yield patch
        coords -= patch


def perimeter(patch):
    perimeter = 4 * len(patch)
    for i, j in patch:
        # If all 4 neighbours are in the patch, then subtract 4
        # If no neighbours are in the patch, then subtract 0
        perimeter -= len(set(neighbours(i, j)) & patch)
    return perimeter


# %% part 1

print(sum(perimeter(patch) * len(patch) for patch in find_all_patches()))


# %% part 2

masks = [
    [(-1, 0), (-1, 1), (0, 1)],
    [(0, 1), (1, 1), (1, 0)],
    [(1, 0), (1, -1), (0, -1)],
    [(0, -1), (-1, -1), (-1, 0)],
]


def n_corners(patch):
    """
    Number of corners == number of edges for any patch.

    Consider corners:

        ...
        .##
        .##

    Call positions left, above and above left of the corner a, b, and x:

        xb.
        a##
        .##

    Corners are characterised by x being absent (i.e. not in the patch) and a and b both being
    absent (for outer corners) or and and b both being present (for inner corners).

    There's another case that the problem flags specifically:

        ####
        ##.#
        #.##
        ####

    Here there is a single # patch that touches itself diagonally in the center. This bucks
    one of the rules above. So, x can be in the patch if a and b are both not in the patch.

    Finally, obviously corners could be any rotation, so there are 4 different sets of a, x and b.
    """
    n = 0
    for i, j in patch:
        for (a_i, a_j), (x_i, x_j), (b_i, b_j) in masks:

            # x element must be absent
            x_absent = not (i + x_i, j + x_j) in patch

            # a and b elements must either both be absent or both be present
            # i.e. they must match
            a_present = (i + a_i, j + a_j) in patch
            b_present = (i + b_i, j + b_j) in patch
            a_matches_b = a_present is b_present

            if x_absent and a_matches_b:
                n += 1

            elif not x_absent and not a_present and not b_present:
                n += 1

    return n


print(sum(n_corners(patch) * len(patch) for patch in find_all_patches()))

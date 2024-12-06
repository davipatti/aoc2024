# %%

from tqdm import tqdm
from itertools import cycle
import numpy as np

with open("input") as fobj:
    grid = np.array([list(line.strip()) for line in fobj])


class LoopError(Exception): ...


def do_patrol(grid):
    path = set()  # Keep track of position
    states = set()  # Keep track of position and direction

    nrows, ncols = grid.shape
    position = np.argwhere(grid == "^")[0]
    directions = cycle(([-1, 0], [0, 1], [1, 0], [0, -1]))
    direction = next(directions)

    while True:

        path.add(tuple(position))

        # If we've seen this position and direction then we're in a loop
        status = tuple(position), tuple(direction)

        if status in states:
            raise LoopError
        else:
            states.add(status)

        # Check whether the next position would take us off the grid
        next_i, next_j = position + direction
        if (
            next_i == -1
            or next_j == -1
            or next_i == nrows
            or next_j == ncols
        ):
            return path

        # Check if we'd need to turn, and if so update direction
        if grid[next_i, next_j] == "#":
            direction = next(directions)

        # Update position
        position += direction


def solve_part_1(grid):
    return len(do_patrol(grid))


def solve_part_2(grid):
    total = 0

    # new obstacle has to be somewhere on the existing path
    existing_path = do_patrol(grid)

    start = np.argwhere(grid == "^")[0]

    for i, j in tqdm(existing_path):
        visible = j == start[1] and i < start[0]
        if grid[i, j] == "." and not visible:
            # if grid[i, j] == ".":
            new_grid = grid.copy()
            new_grid[i, j] = "#"
            try:
                do_patrol(new_grid)
            except LoopError:
                total += 1
    return total


print(solve_part_1(grid))
print(solve_part_2(grid))

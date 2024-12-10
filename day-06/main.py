# %%

from itertools import cycle
import numpy as np

with open("input") as fobj:
    grid = np.array([list(line.strip()) for line in fobj])


class InLoop(Exception): ...


def do_patrol(grid):
    path = set()  # Keep track of position
    states = set()  # Keep track of position and direction

    nrows, ncols = grid.shape
    position = np.argwhere(grid == "^")[0]
    directions = cycle(((-1, 0), (0, 1), (1, 0), (0, -1)))
    direction = next(directions)

    while True:

        path.add(tuple(position))

        # If we've seen this position and direction then we're in a loop
        status = tuple(position), direction
        if status in states:
            raise InLoop
        else:
            states.add(status)

        # Check whether the current direction would take us off the grid
        i, j = position + direction
        if i == -1 or j == -1 or i == nrows or j == ncols:
            return path

        # Check if we need to turn
        while grid[i, j] == "#":
            direction = next(directions)
            i, j = position + direction

        # Update position
        position += direction


def solve_part_1(grid):
    return len(do_patrol(grid))


def solve_part_2(grid):
    total = 0

    # new obstacle has to be somewhere on the existing path
    existing_path = do_patrol(grid)

    for i, j in existing_path:
        if grid[i, j] == ".":
            new_grid = grid.copy()
            new_grid[i, j] = "#"
            try:
                do_patrol(new_grid)
            except InLoop:
                total += 1
    return total


print(solve_part_1(grid))
print(solve_part_2(grid))

# %%

from operator import mul, add
from main import calibrations, concat


def operate(current, values, operators):
    if values:
        for op in operators:
            new_current = op(current, values[0])
            yield from operate(new_current, values[1:], operators)
    else:
        yield current


def is_possible(target, values, operators):
    for result in operate(values[0], values[1:], operators):
        if result == target:
            return True
    else:
        return False


def solve(operators):
    return sum(
        target
        for target, values in calibrations
        if is_possible(target, values, operators)
    )


if __name__ == "__main__":
    print(solve((mul, add)))
    print(solve((mul, add, concat)))

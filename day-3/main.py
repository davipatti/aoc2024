# %%

import re


with open("input", "r") as fobj:
    text = "".join(line.strip() for line in fobj)


# %% part 1


def mul_sum(string):
    return sum(int(i) * int(j) for i, j in re.findall(r"mul\((\d+),(\d+)\)", string))


print(mul_sum(text))

# %% part 2

total = 0

first = True

for part in text.split("don't()"):

    if first:
        total += mul_sum(part)
        first = False

    elif "do()" in part:
        total += mul_sum(part[part.index("do()") :])


print(total)

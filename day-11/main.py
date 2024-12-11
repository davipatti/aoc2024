# %%

from collections import Counter

with open("input") as fobj:
    counts = Counter(tuple(map(int, fobj.read().strip().split())))


def rules(digit):
    if digit == 0:
        return 1

    digit_str = str(digit)

    if len(digit_str) % 2 == 0:
        i = len(digit_str) // 2
        return int(digit_str[:i]), int(digit_str[i:])

    return digit * 2024


# %%


def apply_rules(counts):

    new_counts = Counter()

    for digit, count in counts.items():

        result = rules(digit)

        if isinstance(result, int):
            new_counts[result] += count

        else:
            for digit in result:
                new_counts[digit] += count

    return new_counts


def apply_rules_n(counts, n):
    for _ in range(n):
        counts = apply_rules(counts)
    return counts


# %% part 1

print(sum(apply_rules_n(counts, n=25).values()))

# %% part 2

print(sum(apply_rules_n(counts, n=75).values()))

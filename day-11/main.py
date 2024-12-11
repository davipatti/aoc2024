# %%

from collections import Counter

with open("input") as fobj:
    counts = Counter(tuple(map(int, fobj.read().strip().split())))


def rules(digits):

    as_str = str(digits)

    if (l := len(as_str)) % 2 == 0:
        i = l >> 1
        return int(as_str[:i]), int(as_str[i:])

    elif digits == 0:
        return (1,)

    else:
        return (digits * 2024,)


# %%


def apply_rules(counts):

    new_counts = Counter()

    for digits, count in counts.items():
        for result in rules(digits):
            new_counts[result] += count

    return new_counts


def apply_rules_n(counts, n):
    for _ in range(n):
        counts = apply_rules(counts)
    return counts


# %% part 1

print(sum(apply_rules_n(counts, n=25).values()))

# %% part 2

print(sum(apply_rules_n(counts, n=75).values()))
# %%
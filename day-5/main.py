# %%

rules = []
updates = []

with open("input") as fobj:
    for line in fobj:

        if "|" in line:
            a, b = line.strip().split("|")
            rules.append((int(a), int(b)))

        if "," in line:
            updates.append(
                [int(value) for value in line.strip().split(",")]
            )

rules = set(rules)


def find_unique_pages(rules) -> set[int]:
    pages = set()
    for rule in rules:
        for page in rule:
            pages.add(page)
    return pages


class Page:

    def __init__(self, n, rules):
        self.n = n

    def __gt__(self, other):
        return (other.n, self.n) in rules

    def __lt__(self, other):
        return (self.n, other.n) in rules


def sort_pages(rules: set[tuple[int, int]]) -> list[int]:
    """
    Sort pages based on some rules
    """
    unique_pages = find_unique_pages(rules)
    order = sorted(Page(n, rules) for n in unique_pages)
    return [page.n for page in order]


def filter_rules(rules: set[tuple[int, int]], update: list[int]):
    """
    Keep only rules that have pages appearing in this update.
    """
    update = set(update)
    for a, b in rules:
        if a in update and b in update:
            yield (a, b)


# %%


def solve(rules, updates, part):

    score = 0

    for update in updates:

        # THE ORDERING RULES THAT INVOLVE MISSING PAGE NUMBERS ARE NOT USED
        rules_subset = set(filter_rules(rules, update))

        order = sort_pages(rules_subset)

        if part == 1 and update == order:
            score += update[len(update) // 2]

        elif part == 2 and update != order:
            score += order[len(update) // 2]

    return score


print(solve(rules, updates, part=1))
print(solve(rules, updates, part=2))

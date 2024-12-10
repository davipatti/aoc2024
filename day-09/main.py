# %%

from collections import deque

with open("input") as fobj:
    disk_map = fobj.read().strip()


def make_queue(disk_map: str, method: str = "extend") -> deque:
    """
    Args:
        disk_map
        method: "extend" to make a flat deque or "append"
    """

    is_file = True
    id = 0

    queue = deque()

    grow = getattr(queue, method)

    for digit in disk_map:

        if is_file:
            grow([id] * int(digit))
            id += 1

        else:
            grow([None] * int(digit))

        is_file = not is_file

    return queue


# %%


def defrag(disk_map):

    queue = make_queue(disk_map)

    compacted = []
    append = compacted.append

    while queue:

        if (left_slot := queue.popleft()) is not None:
            append(left_slot)

        else:
            right_slot = queue.pop()
            while right_slot is None:
                right_slot = queue.pop()

            append(right_slot)

    return compacted


def checksum(disk_map):
    return sum(i * id for i, id in enumerate(disk_map))


def part_1(disk_map):
    compacted = defrag(disk_map)
    return checksum(compacted)


print(part_1(disk_map))

# %%


class NoUpdate(Exception): ...


def update(queue):
    """
    Update the queue, moving a file to a new position if possible.
    """

    if queue:
        file = queue[-1]
    else:
        return []

    if file[0] is not None:

        for i, slots in enumerate(queue):

            if slots[0] is None:

                if len(file) == len(slots):
                    queue[i] = queue.pop()
                    queue.append([None] * len(file))
                    return queue

                elif len(file) <= len(slots):
                    queue.insert(i, queue.pop())
                    queue.insert(
                        i + 1, [None] * (len(slots) - len(file))
                    )
                    del queue[i + 2]
                    queue.append([None] * len(file))
                    return queue

        else:
            raise NoUpdate

    else:
        raise NoUpdate


def group_nones(queue):
    """
    Combine multiple blocks that just contain None into single blocks.
    """
    cleaned = []
    append = cleaned.append
    n = 0
    for block in queue:
        if block and block[0] is not None:
            if n != 0:
                append([None] * n)
                n = 0
            append(block)
        else:
            n += len(block)
    if n != 0:
        append([None] * n)
    return cleaned


def checksum_queue(queue):
    total = 0
    i = 0
    for block in queue:
        for id in block:
            if id is not None:
                total += id * i
            i += 1
    return total


def part_2(disk_map):
    queue = make_queue(disk_map, "append")

    # collect blocks from the end of the queue that don't get updated
    from_right = []

    while queue:

        try:
            new = group_nones(update(queue))
        except NoUpdate:
            from_right.append(new.pop())

        queue = new

    return checksum_queue(reversed(group_nones(from_right)))


print(part_2(disk_map))

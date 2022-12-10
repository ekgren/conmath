from collections import deque


def op0(a, ix):
    return a[:ix] + "0" + a[ix:]


def op1(a, ix):
    return a[:ix] + "1" + a[ix:]


def op2(a, ix):
    return a[:ix] + "2" + a[ix:]


def op3(a, ix):
    return a[:ix] + a[ix + 1 :]


ops = [op0, op1, op2, op3]


mapping = {}
mapping_inv = []

init = ""
processed = {}
unprocessed = deque()

unprocessed.append(init)
for _ in range(10000):
    item = unprocessed.popleft()
    if item not in mapping:
        mapping[item] = len(mapping)
        mapping_inv.append(item)
    item_children = []
    for op in ops:
        for ix in range(len(item) + 1):
            child = op(item, ix)
            if child not in mapping:
                mapping[child] = len(mapping)
                mapping_inv.append(child)
            item_children.append(child)
            unprocessed.append(child)

    if mapping[item] not in processed:
        processed[mapping[item]] = [mapping[child] for child in item_children]

for k, v in processed.items():
    out = f"{k:>4}: "
    for e in sorted(set(v)):
        out += f"{e:>4},"
    print(out)
# print(unprocessed)

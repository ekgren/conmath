"""Fixed-size data memory and an explicit copy-round budget for the opening."""

class Failure(Exception):
    pass


class Budget:
    def __init__(self, limit, trace):
        self.limit = limit
        self.used = 0
        self.trace = trace

    def step(self):
        if self.used == self.limit:
            raise Failure("out-of-steps")
        self.used += 1
        self.trace.append({"op": "step", "step": self.used})


class Memory:
    def __init__(self, cells, budget):
        self.cells = cells.copy()
        self.budget = budget

    def address(self, address):
        if type(address) is not int or not 0 <= address < len(self.cells):
            raise Failure("out-of-memory")

    def read(self, address):
        self.address(address)
        value = self.cells[address]
        self.budget.trace.append({"op": "read", "address": address,
                                  "value": value, "step": self.budget.used})
        return value

    def write(self, address, value):
        self.address(address)
        if type(value) is not int or value not in (0, 1):
            raise Failure("invalid-value")
        self.cells[address] = value
        self.budget.trace.append({"op": "write", "address": address,
                                  "value": value, "step": self.budget.used})


def run_example(length, limit):
    if type(length) is not int or not 0 <= length <= 8:
        return {"ok": False, "reason": "invalid-input"}
    if type(limit) is not int or not 0 <= limit <= 9:
        return {"ok": False, "reason": "invalid-input"}
    initial = [1] * length + [0] * (16 - length)
    trace = []
    budget = Budget(limit, trace)
    memory = Memory(initial, budget)
    reason = "completed"
    try:
        successor(memory, 0, 8, length, budget)
    except Failure as failure:
        reason = str(failure)
    return {"ok": reason == "completed", "reason": reason,
            "length": length, "limit": limit, "steps": budget.used,
            "before": initial, "after": memory.cells, "trace": trace}

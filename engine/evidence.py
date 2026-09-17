"""Check this example's finite access record independently of its implementation."""

def check_execution(result, rules=32):
    failed = {"ok": False, "reason": "invalid-evidence"}
    if type(result) is not dict or result.get("ok") is not True:
        return failed
    length, limit = result.get("length"), result.get("limit")
    if type(length) is not int or not 0 <= length < 8:
        return failed
    if type(limit) is not int or not length + 1 <= limit <= 9:
        return failed
    if type(rules) is not int or not 0 <= rules <= 32:
        return failed
    trace = result.get("trace")
    if type(trace) is not list or len(trace) > 27:
        return failed
    for name in ("before", "after"):
        cells = result.get(name)
        if type(cells) is not list or len(cells) != 16:
            return failed
        if any(type(value) is not int or value not in (0, 1) for value in cells):
            return failed
    for event in trace:
        if type(event) is not dict or len(event) > 4:
            return failed
        if any(type(value) is not int for key, value in event.items() if key != "op"):
            return failed
    if rules < len(trace) + 2:
        return {"ok": False, "reason": "out-of-checking-steps"}
    if type(result.get("steps")) is not int or result.get("reason") != "completed" or result.get("steps") != length + 1:
        return failed
    before = [1] * length + [0] * (16 - length)
    after = before.copy()
    expected = []
    for i in range(length):
        expected.append({"op": "step", "step": i + 1})
        expected.append({"op": "read", "address": i, "value": 1, "step": i + 1})
        expected.append({"op": "write", "address": 8 + i, "value": 1, "step": i + 1})
        after[8 + i] = 1
    expected.append({"op": "step", "step": length + 1})
    expected.append({"op": "write", "address": 8 + length, "value": 1, "step": length + 1})
    after[8 + length] = 1
    if result.get("before") != before or result.get("after") != after or trace != expected:
        return failed
    return {"ok": True, "reason": "checked-execution", "rulesUsed": len(trace) + 2}

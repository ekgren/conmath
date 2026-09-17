# Resource bounds

The example reserves sixteen data cells before it runs. Addresses 0–7 hold the input; addresses 8–15 hold the output. Reads and writes check their addresses. Writing past address 15 fails rather than growing memory.

The input length is an integer from zero to eight. The step allowance is an integer from zero to nine. One charged step covers one loop round or the final write. Copying three marks and appending one therefore requires four charged steps. Returning normally does not consume an additional charged step in this model.

An eight-mark input fits the source, but its successor cannot fit the target. More steps cannot repair that lack of space. Exhaustion and an out-of-bounds access are failures: negative results for the attempt under its constraints.

This is a **data-capacity and program-work account**, not total memory or CPU accounting. Indices, the budget object, interpreter, supporting code, validation, initialization, and traces also require resources. Their costs are excluded explicitly; a complete machine-level resource proof remains future work.

The helper methods do not enforce a budget on arbitrary Python code. The fixed program has a bounded loop and checks its budget before each round. Its display trace is bounded by 25 events. The checker accepts at most 27 events and uses a separate check budget.

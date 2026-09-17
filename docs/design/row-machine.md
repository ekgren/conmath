# Copy-successor example

Status: implemented review revision. Replaces the SEEK/MARK/HALT candidate.
The user prioritized minimal, readable programs with explicit reads and writes.

## Reader program

`engine/successor.py` is seven lines of actual Python. Copy `length` marks from
`source + i` to `target + i`, then append a mark. Each copy round and final write
explicitly charges `budget.step()`. The browser executes this exact source via a
locally bundled Pyodide runtime in a worker. No Python-to-JavaScript imitation or
hand-written translator is involved. It remains static and requires no backend.

## Entry and memory contract

The admitted input is 0–8 marks with a 0–9 step budget. Integers exclude booleans.
The harness reserves sixteen initialized cells. Source starts at 0; target at 8.
Input is a prefix of marks, and all remaining cells are blank. The regions are
disjoint. They cannot grow. Access outside 0–15 raises a failure before access.
Each value is 0 or 1. This public example has fixed addresses; it is not a generic
copy routine with defined overlap semantics.

Memory.read returns one addressed value. Memory.write changes one addressed value.
Budget.step increments a bounded counter, or fails before the next round.
Trace emission belongs to the host account. Returning normally is success; an
exhausted budget or invalid address is failure, even if part of the target was
written. No rollback or automatic retry occurs.

## Work and storage

A step covers one bounded copy round (index arithmetic, read, write, and loop
control) or the final append. This model is defined for this fixed program, not
arbitrary Python. Source length bounds the loop. Three marks require four steps.
Eight marks need a ninth cell in the target, so cannot succeed with this capacity.

The sixteen-cell figure counts reserved data capacity, not interpreter RAM.
Python integers, lists, stack, budget, code, initialization, validation, worker,
and trace storage are explicitly outside that account. This revision deliberately
removes the former 26-bit machine-memory claim. A complete implementation cost
model remains open. Readability must not be confused with zero-cost helpers.

## Evidence

`engine/evidence.py` checks admitted metadata, initial/final memory, and the exact
ordered access record against an independent expected sequence. It accepts at
most 27 events (runs produce at most 25); rule budget is bounded by 32. Arrays
have sixteen entries. Repeated verification is deterministic. Truncated traces,
forged writes, changed results, failure outcomes, and inadequate check budgets
fail. This is a checker for individual execution evidence, not general induction.

## Implementation boundary

JavaScript only loads Python and presents controls/results. Source comes from
`.py` files at build time and the worker fetches those identical files. Worker
messages carry bounded configurations, never editable code. Browser tests verify
that runtime/code requests stay local and failed initialization is reported.
Pyodide adds roughly 13 MB of uncompressed runtime assets; reading and source
remain available without loading that runtime successfully. There is no CDN
requirement. A different runtime can replace this host without changing the
pedagogical program's contract.

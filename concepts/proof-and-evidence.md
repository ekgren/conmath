# Proof and evidence

The opening records the charged rounds and the addresses and values of every read and write. It also records the initial and final data memory, input length, budget, and success or failure.

The checker accepts a completed execution only if:

1. The input and budget are within the declared bounds, and the recorded initial memory is the specified input followed by blank cells.
2. Each copied mark is read from address `i` and written to address `8 + i`, with a charged step before it.
3. The final charged step writes one additional mark after the copies.
4. The final memory preserves the source and contains exactly the expected target. The recorded charged work is within the supplied budget.

The checker derives the expected access record independently of the program's implementation. It checks this single finite witness; it does not establish a general theorem or prove its own correctness.

The record is bounded: sixteen initial and final cells and at most 27 events. Checking charges two admission/conclusion checks plus one per event, with a maximum allowance of 32. Those units each cover bounded comparisons. The checker implementation and Python runtime remain trusted. No total checker-memory claim is made.

{{source:engine/evidence.py}}

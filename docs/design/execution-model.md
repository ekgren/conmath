# Execution model brief

Status: general requirements agreed. [Row machine v1](row-machine.md) is the
implemented candidate for the opening; a general machine remains unselected.

## Purpose

Give the book a concrete substrate for construction, proof, and resource claims.
The user accepts a simplified computer. A step may be an instruction transition;
it need not represent a physical clock cycle. Nothing may hide infinite work.
Choose for mathematical clarity and teachability, not hardware spectacle.

A small deterministic machine with finite memory and a short instruction set is
the current direction. A bounded register or tape design is a candidate, not a
settled axiom. C/Wasm or TypeScript alone would not settle the cost semantics.
JavaScript may implement the simulator without defining the mathematics.

## Before the first executable claim

Write down:

- Cell and value encodings; address and register widths; valid states.
- Storage for inputs, output, scratch work, program, and control information.
- Instruction syntax, validity, transitions, and charged work.
- Initial states, halting, invalid input, and resource exhaustion.
- Whether setup and validation belong to execution or are charged separately.
- Which storage is allocated in advance and which operations may allocate.
- Evidence format and the separate resources used to check it.
- A precise claim and the finite rules used to justify it.

Do not count arbitrary-size integer arithmetic or a whole array copy as one
unexplained step. A fixed-width primitive can be elementary if its bound and
meaning are explicit. Do not implement addition as an unexplained primitive and
then claim to have constructed it.

## Failure

Resource exhaustion means failure: a negative result because the requested
computation did not complete within the envelope. Debug snapshots are optional.
Partial output is not successful output.
There is no initial requirement for rollback or resumable computation.

## Future generalizable claims

A target theorem relates valid inputs and initial state, program behavior, output,
and sufficient resources. Resource bounds can depend on input representation.
Fitting the input is not sufficient if working or output storage exceeds capacity.

Choose and justify a finite reasoning rule for repeated execution before using it
in a checked general claim. Success on many configurations is supporting software
evidence, not a replacement for that rule or its justification.

# Foundation charter

Status: normative draft 0.2

## Commitments

1. Conmath claims only explicitly constructed values.
2. Every value has a finite representation under a declared resource envelope.
3. No type silently denotes a completed infinity.
4. Operations expose overflow, partiality, or widening explicitly.
5. Proofs are finite evidence checked by an executable kernel.
6. Quantification ranges over a declared domain; finite enumeration and an extensible theory are distinct.
7. Resource exhaustion never establishes falsity or absence of an inhabitant.
8. Mathematical cost and host-simulator cost are different measurements.
9. Conventional mathematics is explained before Conmath departs from it.
10. The trusted system stays small enough to inspect.
11. State changes are explicit. A stateful reference must identify the state or snapshot it describes.
12. Finite memory does not imply termination; a finite step budget bounds an execution attempt.
13. Bounded hardware and mutable state do not establish consistency or invalidate incompleteness theorems.

## Implemented domains and accounts

- Bit: low/high, displayed as 0/1; double negation checked by finite cases.
- Ideal digital logic: CMOS inverter switch state, NAND, edge-triggered storage.
- Word machine: four 4-bit data words, four 4-bit ROM instructions, 4-bit A,
  2-bit PC, 4-bit IR, 8-bit fuel, and four control states encoded in 2 bits.
  Model storage: 52 bits. UI history and host step count are excluded.
- One instruction step fetches, decodes, and executes atomically. PC remains at
  HALT; other instructions advance it modulo four. Exhaustion does not execute
  an instruction. HALT consumes one step. No analog timing claims.
- Allocator: bounded payload slots. Metadata/code storage is excluded explicitly.
  Failed append preserves the previous collection.
- Checked 4-bit addition: exact result in 0..15 or overflow; commutativity compares
  the full tagged result, including overflow.
- Dyadic enclosure of sqrt(2): exact integer comparisons, with a limit on the bit
  length of each arithmetic integer, including squared intermediates. This is
  not a total RAM budget. Host preflight may compute beyond that model limit;
  no over-limit result is admitted as a successful refinement. Failure preserves
  the last valid enclosure. Geometric rendering is approximate.

## Proposed foundation; not implemented as a general calculus

A construction may have the interface:

```
construct(input, state, budget)
  -> ok(value, newState, remainingBudget)
   | rejected(reason)
   | exhausted(resource)
```

A type describes representations and validity evidence. A constructor and its
resource-dependent outcome do not alone define a type or a set. Set-like
collections need equality, membership, duplicate, and snapshot semantics.
A general stateful type system still requires formation, typing, operational
rules, and soundness proofs.

A fixed finite structure is not a model of all Peano arithmetic axioms.
We do not claim to resolve the barber specification by changing its meaning over
time, nor to evade Gödel by running a formal theory on finite hardware.

## Route toward analysis

Floating-point arithmetic is a finite approximation with rounding laws to audit.
The binary64 example is host arithmetic, outside the tiny instruction set.
A candidate computable-real representation must include a convergence guarantee
and precision-indexed rational evidence under sufficient finite resources.
A permanently failing refiner does not establish an arbitrary-precision real.
General computable-real equality is not assumed decidable.

Open obligations: bounded rational arithmetic, compatible refinements, error
propagation, resource semantics for composition, algebraic proofs, and
constructive witnesses for analytic claims. The book labels these as research
rather than presenting the interval demonstration as completed real analysis.

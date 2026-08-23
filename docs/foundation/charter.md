# Foundation charter

Status: normative draft 0.1

## Commitments

1. Conmath claims only explicitly constructed values.
2. Every value has a finite representation under a declared resource envelope.
3. No type silently denotes a completed infinity.
4. Operations expose overflow, partiality, or widening explicitly.
5. Proofs are finite evidence checked by an executable kernel.
6. Quantification ranges over a declared constructible domain.
7. Resource exhaustion never establishes falsity.
8. Mathematical cost and host-simulator cost are different measurements.
9. Conventional mathematics is explained before Conmath departs from it.
10. The trusted system stays small enough to inspect.

## First constructed domain

Chapter 1 introduces `Bit`, with exactly two constructors:

```text
Bit : Type
low  : Bit
high : Bit
```

It defines equality and negation by cases, implements a one-cell machine, and
checks:

```text
∀ b : Bit, not(not(b)) = b
```

No natural numbers, general sets, induction, or unbounded structures are assumed.

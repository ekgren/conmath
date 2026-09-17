# Foundation charter

Status: accepted project commitments, 17 September 2026.
This is not yet a formal calculus or a soundness theorem.

## Constructions and state

1. Objects admitted by the system have finite, explicit representations.
2. A collection is constructed; a predicate alone does not populate it.
3. Explicitly constructed finite collections are allowed. Completed infinite
   collections and silently performed infinite work are not.
4. Computation transforms a specified state through defined operations.
5. Claims about mutable objects or membership identify the relevant state.
6. The substrate must explain storage, access, instructions, and their costs.
   A physical hardware tour is not a prerequisite for learning the mathematics.

## Resource constraints

Every execution has a declared finite step and memory envelope. Each elementary
instruction does bounded work. Operations must not hide iteration, arbitrary-size
arithmetic, bulk copying, or allocation inside an unexplained unit-cost step.

Success produces a specified completed result. Exhaustion and non-completion are
failure: a negative result for the computation under those constraints.
An implementation may expose `None`, an
error, or a tagged exhaustion result. A boolean `false` used to report operational
failure must not be confused with a proof of the proposition's negation.

A stopped state may be retained for debugging. It is not a completed construction
or a proof. Resume, rollback, and transactional semantics are not requirements for
the initial foundation; introduce them only if needed and account for their work.

Model memory and model steps are distinct from Python interpreter and browser overhead.
Both may be measured, but only the specified model supports formal cost claims.

## Proof and prediction

Proofs are finite evidence checked against explicit inference rules by a small
kernel. Checking is itself a resource-bounded computation. It succeeds with
accepted evidence or fails with a reason, such as invalid evidence or resource
exhaustion. Preserve that reason without treating exhaustion as a third outcome
outside success/failure.

The intended destination includes generalizable proofs: under stated input,
state, and resource conditions, a program is guaranteed by the model to perform
a stated construction without executing every variation in advance. This is a
goal for the proof system, not an already established result.

Such arguments must justify the rule that covers repeated steps, establish needed
memory and step bounds, and expose all assumptions. Examples alone are not a
proof of a general claim. No induction principle is silently imported.

Start with explicit trusted rules. Their mathematical justification, the kernel's
implementation correctness, and the UI's faithful reporting are separate
obligations. We do not attempt self-justification of the entire checker at launch.

## Stateful examples and deeper questions

The user's barber example uses a queue of people who have not yet shaved
themselves. The barber is eligible before his first self-shave; afterward he no
longer qualifies and is removed. This describes state-dependent eligibility and
an update rule. It does not assert that a time-independent contradictory
specification has acquired a solution. A full example must define the finite
population, evidence of past actions, updates, and their resource costs.

Investigate self-reference, incompleteness, and the foundations of analysis as the
system develops. Finite computation alone is not a demonstrated refutation of
Gödel's theorems. Determine which hypotheses and conclusions apply to our actual
formal system rather than announcing an outcome in advance.

## Mathematical route

Foundations → arithmetic → algebra → abstract algebra → mathematics for physics.
Numbers, equality, operations, and proofs must be built carefully. Conventional
real numbers are not admitted as magically available exact data; any later
approximation or constructive alternative needs its own representation,
guarantees, resource semantics, and proofs. The exact route remains research.

## First implementation under review

[Row machine v1](../design/row-machine.md) implements a single finite successor
construction and a bounded checker for its execution certificate. This is a
review draft, not the general calculus. Its certificate-memory budget excludes
checker working storage and code; it does not yet fulfill the eventual goal of
a complete proof-computer resource account.

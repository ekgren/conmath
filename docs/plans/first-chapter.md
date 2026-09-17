# First chapter: active plan

Status: planned. Scope approved in the 17 September 2026 interview.

## Outcome

One complete, short opening chapter with supporting concept pages, runnable
source, an explicit resource account, and a minimal checked claim. Establish the
voice, mathematical approach, and structure before expanding toward addition.

## Repository restart — completed

- [x] Commit all prior outstanding work, including ignored manuscript fragments.
- [x] Push preservation commit `df6b32b` before removing the old active tree.
- [x] Replace the previous book and engine with a clean repository harness.
- [x] Record the interview, accepted commitments, open choices, and content map.
- [x] Add executable repository checks and CI without new package dependencies.

## First chapter — not started

- [ ] Propose the smallest suitable finite execution model; specify encodings,
      instructions, storage, step charging, validation, and non-completion.
- [ ] Draft a foundations-led opening and linked concept explanations.
- [ ] Implement the construction and its deterministic, bounded execution.
- [ ] Define a minimal proof language and checker for the chapter's exact claim.
- [ ] Explain trusted rules and why they justify that claim.
- [ ] Display the actual runnable source alongside prose and evidence.
- [ ] Build separate static pages with a clear contents page and reading path.
- [ ] Add notation support and basic book typography without elaborate layouts.
- [ ] Add mathematical, boundary, content, build, and browser acceptance tests.
- [ ] Review the opening with the user before writing the remaining chapters.

## Acceptance evidence

- A reader can explain the object, its representation, the state change, the
  resource account, and what was actually proved.
- The example executes entirely in a browser with no computation backend.
- Both a successful run and constrained non-completion are demonstrated.
- Invalid proof evidence cannot earn a machine-checked label.
- Exhausted proof checking is reported as failure due to non-completion under the
  constraints, not as a proof of logical negation.
- Program and proof evidence reproduce deterministically.
- Published source and executed source agree.
- The build produces valid chapter/concept links; reading does not require JS.
- Browser checks cover keyboard access, narrow screens, execution, and failures.
- The chapter states its assumptions and limitations without inflated claims.

## Open implementation decisions

Exact machine, instruction encoding, inference rules, first theorem, publishing
format, font and notation tooling. The user delegated routine choices; make
concrete proposals based on this chapter rather than reopening the interview.

## Verification log

The repository restart is verified separately in [quality](../quality.md).
No first-chapter implementation, formal proof, or browser acceptance exists yet.

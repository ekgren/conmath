# First chapter: active plan

Status: implemented first reading draft; awaiting user review.

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

## First chapter — review draft

- [x] Propose the smallest suitable finite execution model; specify encodings,
      instructions, storage, step charging, validation, and non-completion.
- [x] Draft a foundations-led opening and linked concept explanations.
- [x] Implement the construction and its deterministic, bounded execution.
- [x] Define a minimal proof language and checker for the chapter's exact claim.
- [x] Explain trusted rules and why they justify that claim.
- [x] Display the actual runnable source alongside prose and evidence.
- [x] Build separate static pages with a clear contents page and reading path.
- [x] Add notation support and basic book typography without elaborate layouts.
- [x] Add mathematical, boundary, content, build, and browser acceptance tests.
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

The revised candidate is specified in [Copy successor](../design/row-machine.md).
It uses actual Python, sixteen data cells, a bounded execution-record checker, Markdown publishing,
local system typography, and native MathML. These remain reviewable choices, not
a commitment to use this exact machine for the whole book. General proof rules
and full checker-memory accounting remain open.

## Verification log

Local implementation and browser evidence is recorded in [quality](../quality.md).
The [QA inventory](../review-checklist.md) maps the reviewable controls and claims.
No deployment or remote CI result is claimed for this uncommitted review draft.

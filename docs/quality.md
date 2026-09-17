# Quality and known gaps

## Current implementation

One draft chapter and five supporting concept pages. A seven-line Python successor
program, sixteen-cell data memory, finite execution checker, deterministic static
publisher, and browser presentation are implemented. The [model specification](design/row-machine.md)
states costs, assumptions, and exclusions.

## Verification — 17 September 2026

- Local gate passed: 16 unit/harness tests, 7 browser scenarios, repository
  checks, and static build. Browser tests were rerun after the mobile wrapping fix.
- Unit checks cover editorial graphs, links, Python/JS dependency boundaries,
  deterministic publishing, source parity, all 90 input/budget configurations,
  deterministic access records, invalid inputs, forged evidence, and check budgets.
- Browser checks cover actual Python execution, local asset requests, source
  display, run/reset/check/export, step and memory failures, invalid inputs,
  keyboard use, no-JS reading, worker-load failure, and 390px/1280px layouts.
- Desktop figure and mobile program/checked-figure screenshots were inspected.
  Mobile code wrapping was corrected after inspection. The live in-app review
  verified Python readiness, execution, access record, and checker acceptance.
- Artifacts are under ignored `artifacts/`; the figure exports canonical evidence.
- No page overflow or uncaught errors appeared in successful browser acceptance.

These are local checks. The updated CI workflow runs the same gates, but this
review draft has not been pushed or verified by remote CI. No deployment claimed.

## Current review boundary

Stop before counting/addition until the user reviews the opening's voice, pace,
model, and typography. Content remains `draft` in the catalogue. A successful
certificate check proves only the specified individual execution relative to the
trusted rules. It is not a general theorem about all successor computations.

## Open obligations

- General reasoning rules, generalizable resource bounds, and a soundness argument.
- Complete resource accounting: sixteen cells count data only, excluding indices,
  interpreter, trace, checker scratch storage, JSON parsing, and browser objects.
- A general machine suitable for later arithmetic; this example has two eight-cell regions.
- Cross-browser acceptance beyond Chromium, richer notation, and a larger book.
- Bounded external certificate parsing if uploads or untrusted certificates are introduced.

## Harness limits

Source-boundary checks are conservative textual lint, not full program analysis.
Markdown checks cover ordinary inline links and supported anchors. External URLs
are not fetched by offline repository checks. Static links and actual browser
paths have separate tests. Structural tests do not establish mathematical truth.

The previous book remains at `df6b32b`; its old proof claims and tests are not
transferred to this implementation. See the [active plan](plans/first-chapter.md).

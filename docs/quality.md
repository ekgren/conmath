# Quality and known gaps

## Current evidence

- Historical book: 18 tests and its content/build checks passed before archival.
- Archive: commit `df6b32b` was pushed to `origin/main` before deletion.
- New harness: `npm run check` exercises catalogue, link, and boundary failure
  cases and validates this repository. Run it for current verification.
- Readiness: `npm run inventory` reports planned/authored content and source counts.

Local verification on 17 September 2026: all 10 harness tests passed;
structural checks passed for 17 Markdown documents and 7 planned content entries;
`git diff --check` passed. There are 0 engine modules and 0 authored/ready entries.
This receipt is local evidence; GitHub CI status must be checked separately.

## Not implemented or verified

- No new authored chapter or concept page.
- No formal machine specification or mathematical engine.
- No proof calculus, proof checker, soundness argument, or checked theorem.
- No static publisher, typography implementation, notation renderer, or browser UI.
- No browser tests, hosted deployment, or runtime performance evidence.

These are deliberate gaps, not regressions hidden by a green harness. The
[first chapter plan](plans/first-chapter.md) owns the next milestone.

## Harness limits

Source-boundary checks are conservative textual lint, not full program analysis.
Markdown link checks cover ordinary inline links and heading/explicit-ID anchors;
reference-style links and embedded HTML links need checker support before use.
External URLs are recorded but are not fetched by offline repository checks.
Structural checks do not decide whether mathematical prose is correct.

Keep evidence dated when adding manual or browser verification. Never transfer
the archived book's test or proof claims to the new implementation.

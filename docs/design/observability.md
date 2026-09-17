# Observability and verification

Status: repository, opening-machine, and browser checks implemented. The
[harness runbook](../harness.md) maps the current implementation and its limits.

Apply [Harness engineering](https://openai.com/index/harness-engineering/) through
small navigable documentation, executable constraints, reproducible behavior, and
evidence an agent can inspect. Do not copy a service observability stack into a
static book merely because the article used one.

## Repository today

- `AGENTS.md` is a short map into versioned repository knowledge.
- `npm run check` runs harness tests and structural gates.
- `npm run inventory` emits content status and source counts as JSON.
- The catalogue validates unique IDs, part ownership, prerequisites, cycles,
  source paths, and the distinction between planned and authored content.
- Markdown link checks reject missing local files and broken fragment anchors.
- Engine source checks reject external imports and recognized browser, storage,
  networking, clock, and randomness APIs. They are conservative lint rules.
- CI runs the same command as local verification.

Inventory is a readiness report, not proof or browser evidence. Passing checks
with an empty engine must not be represented as verified mathematics.

## First-chapter contract

- Expose reproducible program/input/model/budget descriptions.
- Emit structured transitions with sequence numbers, instruction/state changes,
  resource consumption, and final outcome. No timestamps in canonical evidence.
- Report proof success or failure, the rule checked, and a useful failure reason
  and location. Exhaustion is failure; its reason differs from invalid evidence.
- Keep trace/debug storage outside the model account only when that exclusion is
  stated; bound host trace retention so the browser remains responsive.
- Add deterministic fixtures and tests for exact resource boundaries, invalid
  programs/evidence, non-completion, and display/engine agreement.
- Add a static build and local preview with configurable ports.
- Exercise the served UI with browser automation. Check reading, navigation,
  source display, execution, failure reporting, keyboard use, and narrow screens.
- Capture browser exceptions, screenshots, and runtime evidence under ignored
  `artifacts/`, with a short dated verification receipt in the active plan.

Keep the UI responsive during execution; choose bounded execution slices or a
worker based on the first chapter's actual needs. Never allow uncontrolled code
execution or unbounded proof search to block the reader's page.

## Maintenance

Every behavior change updates its relevant spec and evidence. Record unfinished
work in the plan or quality page. Run the smallest meaningful tests plus the
required gates. Fix stale links and misleading status rather than accumulating
unverified claims. No scheduled automation or telemetry export is needed now.

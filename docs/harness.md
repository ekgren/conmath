# Harness runbook

The [harness-engineering article](https://openai.com/index/harness-engineering/)
is applied here as a feedback loop around a static book, not as a requirement for
a backend or a telemetry service.

## Find the relevant knowledge

Start at [AGENTS.md](../AGENTS.md). The [documentation map](index.md) leads to
commitments, implementation specifications, work plans, and quality evidence.
Do not infer that a draft mathematical proposal is a proved result.

## Reproduce a change

1. `npm ci` installs pinned authoring/testing dependencies.
2. `npx playwright install chromium` installs the browser used by the test suite.
3. `PORT=4173 npm run dev` builds and serves one isolated static preview.
4. `npm run check` runs the closeout gate. Set `TEST_PORT` for concurrent checkouts.
5. Inspect the generated browser JSON report and failure traces in `artifacts/`.

On Linux CI, install Chromium's system dependencies with
`npx playwright install --with-deps chromium`. A changed dependency requires a
freshness/health check; keep the lockfile committed. The reader needs no npm install.

## Inspect a computation

The figure exposes the current execution trace and a Download evidence control.
The download records model ID, input/resource configuration, visible states,
transitions, outcome, and proof result. Source details are generated from the same
engine modules served to the browser; unit tests enforce byte agreement.

Browser console: `window.conmath.inspect()` returns a detached snapshot of the
currently executed state, not future steps. It includes bounded diagnostic error
records. Sequence numbers belong to canonical traces; wall-clock timing does not.
The test harness captures uncaught errors and rejects unexpected network requests.

The maximum trace length is bounded by this model. The app exposes no editable
code, external certificate upload, or unbounded search. A more general machine
will need new responsiveness and bounded-decoding tests.

## Mechanical constraints

- Catalogue: valid IDs, part ownership, dependency order/cycles, source locations,
  and planned/draft/ready status.
- Documentation: repository-local links and supported fragment anchors.
- Engine: conservative forbidden-host-API and import-boundary lint.
- Publisher: deterministic output, valid static page/asset links, and source parity.
- Machine: all 9 valid input rows × all 10 step budgets, memory failure boundaries,
  deterministic replay, and valid cell values.
- Checker: altered transitions, false claimed outputs, truncated/extended evidence,
  exact checking budgets, and completed-run requirement.
- Browser: desktop/mobile reading, native math, run/reset, resource failures,
  checking, source display, trace inspection/export, no-JS reading, and keyboard use.

The engine checks are implementation evidence. Certificate acceptance is relative
to the model and checker rules. Neither establishes kernel soundness by itself.

## Keep the loop closed

After a behavior change, update its specification and add the smallest meaningful
regression check. After tests, inspect desktop and mobile screenshots; automated
fit checks do not establish typography quality. Record evidence and limitations in
[quality](quality.md), and update the [active plan](plans/first-chapter.md).

Stop after this opening for user review. Do not quietly expand into addition.
No scheduled agent, deployment, cloud logging, or background telemetry is enabled.

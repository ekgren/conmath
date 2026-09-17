# Conmath agent map

Static interactive mathematics book. The previous book is archived in Git;
its code, layout, and mathematical choices are not requirements.

## Read first

1. [README](README.md) — current implementation status and commands
2. [Architecture](ARCHITECTURE.md) — ownership, boundaries, trust
3. [Foundation charter](docs/foundation/charter.md) — accepted commitments
4. [Book design](docs/design/book.md) — audience, writing, content structure
5. [Active plan](docs/plans/first-chapter.md) — next deliverable and acceptance

## Commands

- `npm run check`: unit/harness tests, repository gates, static build, browser acceptance
- `npm run inventory`: JSON readiness report
- `npm run dev`: build and serve at port 4173; set `PORT` to isolate a checkout.
- `npm run build`: publish into disposable `dist/`; never edit generated output.
- `npm run test:browser`: browser tests; set `TEST_PORT` to isolate the test server.
- See [harness runbook](docs/harness.md) and [QA inventory](docs/review-checklist.md).

## Hard rules

- No backwards compatibility with either archived implementation.
- Finite representations, explicit state, bounded memory, bounded execution.
- An instruction must not conceal unbounded work.
- Exhaustion/non-completion is failure, a negative computation result; it does not by itself prove logical negation.
- Keep the formal model's costs separate from JavaScript/browser overhead.
- Keep `engine/` independent of browser code, clocks, network, and storage APIs.
- Canonical execution and proof evidence must be deterministic.
- Show the source actually executed; do not maintain a second illustrative copy.
- Label proposed rules, prose arguments, experiments, and checked claims honestly.
- Only a successful proof-checker result can earn a machine-checked label.
- Update foundation documents when semantics change.
- Use stable content IDs; put reading order in `book/catalog.json`.
- Do not invent chapters, proved results, or performance evidence to fill the map.
- Keep project knowledge and execution plans in this repository.

## Navigation

- [Documentation index](docs/index.md)
- [Restart interview](docs/decisions/2026-09-17-restart.md)
- [Quality and gaps](docs/quality.md)
- [Observability contract](docs/design/observability.md)

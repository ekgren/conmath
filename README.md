# Conmath

An interactive book about mathematics built from finite constructions, explicit
computation, and checked evidence. The published book is static; all reader
computation runs in the browser.

## Current review

**Chapter 1: Objects and constructions** is the first reading draft. It introduces
rows of marks, a seven-line Python program with explicit memory access and failure,
and a checker for individual execution certificates. Five concept pages support
it. Counting, addition, and generalizable proofs await review of this opening.

The machine is a deliberately small candidate, not a completed general foundation.
The data account reserves sixteen cells; interpreter and checker RAM are separate.
The exact displayed Python runs locally through a bundled Pyodide WebAssembly runtime.

## Run locally

Use Node.js 22+ and npm.

```sh
npm ci
npx playwright install chromium
npm run dev
```

Open <http://127.0.0.1:4173>. `PORT=4200 npm run dev` gives an isolated preview for
another checkout. The preview serves generated static files; rerun the build after
editing sources. No runtime API keys, external fonts, or services are required.

```sh
npm run check
npm run inventory
```

`check` runs unit/harness tests, repository checks, the static build, and browser
acceptance. Browser tests use port 4174 by default; set `TEST_PORT` to isolate a
second run. Browser reports, screenshots, and failure traces are in ignored
`artifacts/`. CI runs the same gate. `inventory` reports structural readiness only.

## Review and source map

- [Opening manuscript](book/parts/foundations/objects-and-constructions.md)
- [First-chapter plan and review boundary](docs/plans/first-chapter.md)
- [Book design](docs/design/book.md) and [foundation charter](docs/foundation/charter.md)
- [Machine and certificate specification](docs/design/row-machine.md)
- [Harness runbook](docs/harness.md) and [quality evidence](docs/quality.md)
- [Documentation index](docs/index.md) and [architecture](ARCHITECTURE.md)

`book/` owns reading order and manuscript; `concepts/` owns reference prose;
`engine/` owns executable rules; `web/` owns presentation; `scripts/` owns publishing
and checks. `dist/` is disposable static output. Never edit it as source.

## Earlier work

The previous book is preserved at
[df6b32b](https://github.com/ekgren/conmath/commit/df6b32baa4977354af9765cc4b5e73c63bc7f9bf).
The earlier Python prototype also remains in Git history. Neither is a
compatibility requirement or authority for the new foundations.

The agreed restart is recorded in the [interview](docs/decisions/2026-09-17-restart.md).

# Conmath

An executable, finite mathematics book, read as one continuous page.

Build a tiny computer from ideal switches and logic. Observe its memory,
registers, instructions, and finite budgets; then develop constructive
mathematics with explicit evidence and resource limits.

## Current surface

- Anchored sections, persistent contents, marginal notes, responsive inline figures
- Interactive CMOS inverter, NAND table, and clocked bit
- Four-bit register machine with colored memory grids and deterministic trace export
- Bounded allocation and checked finite proofs
- Floating-point grouping example and exact bounded refinement of a sqrt(2) enclosure
- Explicit research direction for stateful constructions and analysis

This is not yet a general type theory, real-number library, or proof assistant.

## Run and verify

Node.js 20 or newer. No dependencies to install.

```sh
npm run dev
```

Open <http://127.0.0.1:4173>. Manuscript edits rebuild automatically; refresh to see
changes. Other assets are served directly.

```sh
npm run build
npm run check
```

The check rejects stale assembled HTML and broken anchors/assets, and runs
engine behavior, resource-boundary, and determinism tests.

## Repository map

- `book/README.md` — manuscript map for readers of the source
- `book/parts/` — independent HTML fragments in reading order
- `site/index.html` — generated, committed single-page book; do not edit directly
- `site/assets/book.js` — browser interaction controllers
- `site/assets/engine/` — pure executable models and checkers
- `tests/` — behavioral checks
- `docs/foundation/charter.md` — normative commitments and proposed semantics
- `docs/design/` — editorial and observability records
- `ARCHITECTURE.md` — dependency and trust boundaries

The archived Python prototype is not a compatibility target. It remains at
`archive/python-prototype-2026-08-23`.

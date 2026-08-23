# Conmath

An executable, finite mathematics book.

Conmath develops constructive mathematics alongside an explicitly implementable
computer. Definitions, programs, proofs, and resource accounts are read
together. The archived Python prototype is not part of the new system.

## First version

- Static home page and book navigation
- Chapter 1, **The First Distinction**
- Executable one-bit machine
- Minimal proof checker for double negation on `Bit`
- Deterministic structured traces and JSON export
- Build-time content and engine checks

## Run

Requires Node.js 20 or newer. No dependency installation is required.

```sh
npm run dev
```

Open <http://127.0.0.1:4173>.

## Verify

```sh
npm run check
```

## Repository map

- `site/` — static book and interactive laboratory
- `site/assets/engine/` — pure executable foundation
- `tests/` — behavioral and determinism checks
- `docs/` — normative foundation and design records
- `ARCHITECTURE.md` — dependency and trust boundaries
- `AGENTS.md` — short navigation map for coding agents

The previous repository is preserved by the Git tag
`archive/python-prototype-2026-08-23`. It imposes no compatibility requirements.

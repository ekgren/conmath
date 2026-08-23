# Conmath agent map

Clean-slate executable mathematics book. The archived Python prototype is not
an API or source of truth.

## Read first

- `ARCHITECTURE.md` — boundaries, commands, trust model
- `docs/foundation/charter.md` — normative mathematical commitments
- `README.md` — current product surface

## Commands

- `npm run dev` — serve at `127.0.0.1:4173`
- `npm run check` — engine tests plus content/link checks

## Hard rules

- No backwards compatibility with the archived Python project.
- Keep formal engine modules independent of the DOM.
- Deterministic execution: no timestamps or randomness in canonical traces.
- Distinguish logical resource cost from JavaScript host overhead.
- Resource exhaustion is not logical rejection.
- Published proof claims must come from the checked engine.
- Update foundation documents when semantics change.
- Prefer explicit small modules and structured events.

## Active vertical slice

`Bit` → operations → finite machine → proof by cases → resource account →
browser visualization.

# Conmath architecture

## Product

Conmath is a static, executable mathematics book rendered as one continuous
page. `book/parts/` holds ordered manuscript fragments; `scripts/build-book.mjs`
assembles the committed `site/index.html`. Reading works without JavaScript;
construction, execution, and proof tools progressively enhance it.

## Trust boundary

The current trusted executable surface is:

1. `site/assets/engine/bit-machine.js`
2. `site/assets/engine/bit-proof.js`
3. `site/assets/engine/computer.js` — ideal logic, word machine, allocation, finite addition
4. `site/assets/engine/approximation.js` — exact dyadic enclosure and its resource envelope
5. Tests covering their behavior and deterministic traces

Browser rendering is outside the mathematical trust boundary. The UI must not
claim a theorem is checked unless the engine returns an accepted result.

## Dependency direction

```text
foundation values
      ↓
machine and proof rules
      ↓
structured traces
      ↓
browser presentation
```

Engine modules must not access the DOM, timers, local storage, randomness, or
the network. Canonical traces use sequence numbers, not wall-clock time.

## Resource semantics

Three accounts stay distinct:

- Logical representation: bits required by the defined object
- Conmath machine: instructions, words, stack depth, and proof nodes
- Host simulation: browser and JavaScript overhead

Only the first two are formal claims. Host overhead is implementation telemetry.

## Validation

`npm run check` is the complete local closeout command. It verifies machine
transitions and bounds, proof acceptance and rejection, trace determinism,
required pages, fragment links, assets, assembly freshness, and agent-facing metadata.

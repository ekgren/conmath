# Manuscript map

One scrollable page; independently editable source parts. Stable section IDs
are public links. Keep all reading content in this page.

- `parts/00-opening.html`: document shell, contents, introduction
- `parts/01-transistors.html`: CMOS inverter
- `parts/02-logic.html`: Bit, NAND, Boolean composition
- `parts/03-memory.html`: stored state, clocked register
- `parts/04-computer.html`: word machine, registers, memory, trace
- `parts/05-bounds.html`: allocation and proposed type interface
- `parts/06-proof.html`: checked Bit proof, paradox and incompleteness boundaries
- `parts/07-numbers.html`: bounded arithmetic, rounding, exact enclosures
- `parts/08-references.html`: sources and editorial influences
- `parts/09-closing.html`: document footer

`npm run build` assembles the fragments into committed `site/index.html`.
`npm run dev` builds first and rebuilds manuscript edits while serving.
`npm run check` rejects stale output and broken section/asset links.

Diagrams and controllers: `site/assets/book.js`, `site/assets/styles.css`.
Mathematical behavior: pure `site/assets/engine/` modules, with `tests/` coverage.
Proof status must follow an engine result. Label proposed semantics explicitly.

# Conmath

An interactive book about mathematics built from finite constructions, explicit
computation, and checked proofs.

The book will develop foundations, arithmetic, algebra, and eventually the
mathematics needed for physics. Readers will see and run the code behind the
examples and proofs in their browser. The published book will be entirely static;
no computation backend is required.

## Current state

**Design and repository harness. No new chapters, execution model, or proof
checker have been implemented yet.** The previous book was deliberately removed.
The first task is one carefully developed opening chapter, not a replacement
computer tour or a complete arithmetic textbook.

- [Agreed design](docs/design/book.md)
- [Foundation commitments](docs/foundation/charter.md)
- [Interview and decisions](docs/decisions/2026-09-17-restart.md)
- [First chapter plan](docs/plans/first-chapter.md)
- [Evidence and known gaps](docs/quality.md)
- [Architecture](ARCHITECTURE.md)
- [Documentation index](docs/index.md)

## Work locally

Use Node.js 22 or newer and npm. There are no package dependencies to install.

```sh
npm run check
npm run inventory
```

`check` runs harness regression tests, validates documentation links and the book
catalogue, and checks source boundaries. `inventory` emits a JSON readiness report
for agents and maintainers. These commands do not prove any mathematical claims.

There is no site to serve yet. Build, preview, and browser checks belong to the
first chapter milestone. Its delivery must include them before the milestone can
be called complete.

## Repository map

- [book/](book/README.md): reading order, parts, chapters, and sections
- [concepts/](concepts/README.md): separately addressable concept references
- [engine/](engine/README.md): future mathematical execution and proof modules
- [web/](web/README.md): future browser presentation and static publishing
- [docs/](docs/index.md): decisions, specifications, plans, and evidence
- `scripts/`: executable repository checks
- `tests/`: regression tests for those checks; later, engine and browser tests

## Previous work

The complete pre-reset book, including previously ignored manuscript fragments,
was committed and pushed as
[df6b32b](https://github.com/ekgren/conmath/commit/df6b32baa4977354af9765cc4b5e73c63bc7f9bf).
The earlier Python prototype remains in Git history. Neither is a compatibility
requirement or an authority for the new foundations.

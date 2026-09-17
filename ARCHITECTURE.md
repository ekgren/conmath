# Architecture

Status: accepted boundaries; mathematical engine and publisher not implemented.

## Ownership

- `book/catalog.json` owns stable part, chapter, and concept IDs, reading order,
  prerequisites, implementation status, and source locations.
- `book/parts/<part-id>/<chapter-id>.md` will own chapter prose and sections.
- `concepts/<concept-id>.md` will own precise supporting explanations. Chapters
  introduce concepts in context and link to their reference pages.
- `engine/` will own representations, machine transitions, resource accounting,
  proof syntax, and proof checking. It must run without a browser.
- `web/` will own rendering, controls, typography, and static publication.
- `tests/` owns executable evidence about harness and implementation behavior.
- `docs/` owns commitments, technical specifications, decisions, and plans.

No empty mathematical implementation is presented as a kernel. Directory README
files mark boundaries, not completed features.

## Dependency direction

```text
representations and rules → execution / proof checking → structured evidence
                                                            ↓
manuscript + catalogue ──────────────────────────────→ browser presentation
```

The engine may import only relative modules within `engine/`. It must not import
host packages or `web/`. Presentation consumes engine results; it cannot declare
proof acceptance itself. A static publisher may read manuscript and engine source
at build time. The reader's browser needs no server-side execution or API keys.

## Trust

There are separate obligations:

1. State the primitive representations, operations, and inference rules.
2. Justify why accepted derivations support their stated claims.
3. Test that the implementation follows those rules.
4. Verify that the presentation reports the engine result faithfully.

Passing software tests does not establish mathematical soundness. Kernel
acceptance is relative to the specified rules and trusted implementation.

## Resources

The eventual model must account for inputs, outputs, working storage, program and
control state, and proof-checker storage. State exclusions explicitly. Browser
objects, rendering, and debugging history belong to a separate host account.

Memory sizes and step counts must themselves have bounded representations. A
single JavaScript expression is not automatically one elementary model step.
Details are open in the [execution model brief](docs/design/execution-model.md).

## Enforcement today

`npm run check` validates the catalogue, local Markdown links, required repository
entry points, and conservative source-boundary rules. Boundary checks reject
recognized forbidden engine APIs and imports; they are a lint gate, not a
JavaScript sandbox or a soundness proof. Regression tests exercise failure cases.

[Observability](docs/design/observability.md) specifies the runtime and browser
checks that must be added with executable chapters. [Quality](docs/quality.md)
separates these future obligations from current evidence.

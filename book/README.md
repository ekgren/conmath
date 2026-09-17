# Manuscript

The new book has no authored chapters yet. [catalog.json](catalog.json) is the
single map of planned parts, chapters, concepts, reading order, and prerequisites.

Future chapter path: `book/parts/<part-id>/<chapter-id>.md`.
Use headings for sections and stable explicit IDs when publication begins.
Each chapter is a separate published page; do not reassemble a continuous book.

The catalogue's `parts` order and each part's `chapters` order define the main
reading path. Planned entries have `source: null`. Draft or ready entries need an
existing source file. A ready entry may only depend on other ready entries.

Concept references live in [concepts/](../concepts/README.md). Engine behavior
lives in [engine/](../engine/README.md). Code excerpts must eventually be sourced
from executable modules rather than copied into the manuscript.

Read the [book design](../docs/design/book.md) before adding content.

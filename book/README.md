# Manuscript

[catalog.json](catalog.json) owns the book's stable IDs, reading order, prerequisites,
source paths, and editorial status. The opening chapter is a draft awaiting review.

Chapter path: `book/parts/<part-id>/<chapter-id>.md`. Headings define sections and
published anchors. Each chapter is a separate page. Concepts live in
[concepts/](../concepts/README.md); behavior lives in [engine/](../engine/README.md).

Planned entries have `source: null` and are not published as empty pages. Draft
entries are published for review. Ready entries may only depend on ready content.
Keep IDs stable when changing a title or chapter order.

Publishing supports ordinary Markdown, native MathML/semantic HTML, and two
explicit directives: `{{experiment:row}}` inserts the opening figure;
`{{source:engine/successor.py}}` embeds the exact runnable module. Source links
to published chapter/concept Markdown files become static page links.

Run `npm run build`; never edit `dist/`. Read the
[book design](../docs/design/book.md) before expanding content.

# Browser presentation

The publisher builds chapter and concept pages from Markdown and the catalogue.
`book.css` supplies the basic book typography. `row-figure.html` and
`row-figure.mjs` present the opening construction and consume engine results.

Engine modules are copied without modification; displayed code is generated from
the same source. The UI never declares a proof accepted without checker success.
The output in `dist/` contains all assets, including native MathML notation and
the pinned Pyodide runtime. `python-worker.mjs` runs the actual Python sources.
The runtime adds roughly 13 MB before transport compression; no CDN is needed.

Use `npm run dev`; see the [harness runbook](../docs/harness.md) for isolated
preview ports, verification, diagnostics, and evidence capture.

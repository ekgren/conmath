import fs from 'node:fs';
import path from 'node:path';
import { marked } from 'marked';

export const escape = (text) => String(text).replace(/[&<>"']/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]));
export const slug = (text) => text.toLowerCase().replace(/[^a-z0-9\s-]/g, '').trim().replace(/\s+/g, '-');
export const route = (entry) => `${entry.source.startsWith('concepts/') ? 'concepts' : 'book'}/${entry.id}.html`;

export function renderManuscript(root, entry, entries) {
  const source = fs.readFileSync(path.join(root, entry.source), 'utf8');
  let html = marked.parse(source);
  html = html.replace(/<h([1-6])>(.*?)<\/h\1>/g, (_, level, title) => `<h${level} id="${slug(title)}">${title}</h${level}>`);
  html = html.replace(/href="([^"]+\.md)(#[^"]*)?"/g, (_, link, fragment = '') => {
    const target = path.posix.normalize(path.posix.join(path.posix.dirname(entry.source), link));
    const destination = entries.find((item) => item.source === target);
    if (!destination) throw new Error(`Unpublished manuscript link: ${target}`);
    return `href="../${route(destination)}${fragment}"`;
  });
  html = html.replace(/<p>\{\{experiment:row\}\}<\/p>/g, fs.readFileSync(path.join(root, 'web/row-figure.html'), 'utf8'));
  html = html.replace(/<p>\{\{source:([^}]+)\}\}<\/p>/g, (_, name) => {
    if (!/^engine\/[a-z-]+\.(?:mjs|py)$/.test(name)) throw new Error(`Invalid source include ${name}`);
    const code = fs.readFileSync(path.join(root, name), 'utf8');
    const block = `<pre class="program"><code data-source="${escape(name)}">${escape(code)}</code></pre>`;
    return name.endsWith("successor.py") ? block : `<details class="source"><summary>Read ${escape(path.basename(name))}</summary>${block}</details>`;
  });
  if (/\{\{/.test(html)) throw new Error(`Unknown manuscript directive in ${entry.source}`);
  const sections = [...source.matchAll(/^## (.+)$/gm)].map((match) => ({ title: match[1], id: slug(match[1]) }));
  return { html, sections };
}

export function page({ title, body, sidebar, prefix = '../', experiment = false, chapter = false }) {
  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>${escape(title)} · Conmath</title><meta name="description" content="A constructive mathematics book with finite computation and checked evidence.">
<link rel="icon" href="${prefix}assets/icon.svg" type="image/svg+xml"><link rel="stylesheet" href="${prefix}assets/book.css">${experiment ? `<script type="module" src="${prefix}assets/row-figure.mjs"></script>` : ''}</head>
<body><a class="skip" href="#main">Skip to content</a><header class="masthead"><a class="wordmark" href="${prefix}index.html">Conmath</a><span class="strapline">An executable mathematics book</span><nav aria-label="Book"><a href="${prefix}index.html">Contents</a><a href="${prefix}concepts/index.html">Concepts</a></nav></header>
<div class="page-grid"><aside>${sidebar}</aside><main id="main" tabindex="-1" class="${chapter ? 'chapter' : ''}">${body}</main></div>
<footer><span>Conmath</span><span>A work in progress · First reading draft</span></footer></body></html>`;
}

export function build(root) {
  const catalog = JSON.parse(fs.readFileSync(path.join(root, 'book/catalog.json'), 'utf8'));
  const entries = [...catalog.chapters, ...catalog.concepts].filter((entry) => entry.source);
  const output = new Map();
  for (const entry of entries) {
    const { html, sections } = renderManuscript(root, entry, entries);
    const chapter = catalog.chapters.includes(entry);
    const part = catalog.parts.find((item) => item.chapters.includes(entry.id));
    const chapterNumber = catalog.parts.flatMap((item) => item.chapters).indexOf(entry.id) + 1;
    const partLabel = part ? `Part ${catalog.parts.indexOf(part) + 1} · ${escape(part.title)}` : 'Concept reference';
    const sidebar = `<p class="eyebrow">${partLabel}</p><p class="side-title">${escape(entry.title)}</p><nav aria-label="On this page"><ol>${sections.map((section) => `<li><a href="#${section.id}">${escape(section.title)}</a></li>`).join('')}</ol></nav><a class="back-link" href="../index.html">← Book contents</a>`;
    const body = `<p class="eyebrow">${chapter ? `Chapter ${chapterNumber} · Reading draft` : 'Reference · Reading draft'}</p>${html}<div class="endnote">${chapter ? 'End of the first reading draft. Counting and addition come next, after review.' : '<a href="../book/objects-and-constructions.html">Return to the chapter →</a>'}</div>`;
    output.set(route(entry), page({ title: entry.title, body, sidebar, experiment: html.includes('id="row-experiment"'), chapter }));
  }
  const contents = catalog.parts.map((part, i) => `<section class="contents-part"><h2><span>${['I', 'II', 'III', 'IV'][i]}</span> ${escape(part.title)}</h2>${part.chapters.length ? `<ol>${part.chapters.map((id) => {
    const entry = catalog.chapters.find((chapter) => chapter.id === id);
    return `<li>${entry.source ? `<a href="${route(entry)}">${escape(entry.title)} <span aria-hidden="true">→</span></a><small>First reading draft</small>` : `<span>${escape(entry.title)}</span><small>To follow</small>`}</li>`;
  }).join('')}</ol>` : '<p class="planned">Later in the book</p>'}</section>`).join('');
  output.set('index.html', page({ title: 'Constructive mathematics', prefix: './', sidebar: '<p class="eyebrow">The book</p><p class="side-title">From constructions<br>to mathematics.</p>', body: `<p class="eyebrow">A book in development</p><h1>Constructive<br>mathematics</h1><p class="lede">Objects we can construct.<br>Work we can account for.<br>Claims we can check.</p><p>This book builds mathematics with finite memory and explicit steps. Read the definitions, run the code, and inspect the evidence.</p><p><a class="begin" href="book/objects-and-constructions.html">Begin with objects and constructions <span aria-hidden="true">→</span></a></p><div class="contents">${contents}</div>` }));
  output.set('concepts/index.html', page({ title: 'Concepts', sidebar: '<p class="eyebrow">Reference</p><p class="side-title">Definitions and<br>supporting material.</p>', body: `<p class="eyebrow">Read as needed</p><h1>Concepts</h1><p>These pages support the opening chapter. Follow the book in order, or return here to inspect a definition or assumption.</p><ol class="concept-list">${catalog.concepts.filter((entry) => entry.source).map((entry) => `<li><a href="${entry.id}.html">${escape(entry.title)} <span aria-hidden="true">→</span></a></li>`).join('')}</ol>` }));
  for (const name of ['book.css', 'row-figure.mjs', 'python-worker.mjs']) output.set(`assets/${name}`, fs.readFileSync(path.join(root, 'web', name), 'utf8'));
  output.set('assets/icon.svg', '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" fill="#faf8f2"/><text x="5" y="25" font-family="Georgia,serif" font-size="28" fill="#315b4b">C</text></svg>');
  for (const name of fs.readdirSync(path.join(root, 'engine')).filter((name) => /\.(mjs|py)$/.test(name))) output.set(`assets/engine/${name}`, fs.readFileSync(path.join(root, 'engine', name), 'utf8'));
  for (const name of ["pyodide.mjs", "pyodide.asm.mjs", "pyodide.asm.wasm", "python_stdlib.zip", "pyodide-lock.json"]) {
    output.set(`assets/python/${name}`, fs.readFileSync(path.join(root, "node_modules/pyodide", name)));
  }
  return output;
}

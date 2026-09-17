import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import { checkCatalog } from './catalog.mjs';
import { filesUnder, checkMarkdown, checkEngineSource } from './repository.mjs';

const root = fileURLToPath(new URL('../', import.meta.url));
const errors = [];
const files = filesUnder(root);
const required = [
  'AGENTS.md', 'ARCHITECTURE.md', 'README.md', 'CHANGELOG.md',
  'docs/index.md', 'docs/foundation/charter.md', 'docs/design/book.md',
  'docs/design/execution-model.md', 'docs/design/observability.md',
  'docs/decisions/2026-09-17-restart.md', 'docs/plans/first-chapter.md',
  'docs/quality.md', 'book/catalog.json', 'engine/README.md', 'web/README.md',
];
for (const name of required) if (!files.includes(name)) errors.push(`Missing required file: ${name}`);
const read = (name) => {
  const absolute = path.join(root, name);
  return fs.existsSync(absolute) && fs.statSync(absolute).isFile() ? fs.readFileSync(absolute, 'utf8') : null;
};
let catalog;
try {
  catalog = JSON.parse(read('book/catalog.json'));
  errors.push(...checkCatalog(catalog, read));
} catch (error) {
  errors.push(`Cannot read catalogue: ${error.message}`);
}
const markdown = files.filter((name) => name.endsWith('.md'));
const engine = files.filter((name) => /^engine\/.*\.(?:mjs|js|ts|py)$/.test(name));
for (const name of markdown) errors.push(...checkMarkdown(root, name));
for (const name of engine) errors.push(...checkEngineSource(name, read(name)));
const entries = ['chapters', 'concepts'].flatMap((group) => Array.isArray(catalog?.[group]) ? catalog[group] : []);
const registered = new Set(entries.map((entry) => entry?.source).filter(Boolean));
for (const name of markdown) {
  if ((name.startsWith('book/parts/') || (name.startsWith('concepts/') && name !== 'concepts/README.md')) && !registered.has(name)) {
    errors.push(`Unregistered content source: ${name}`);
  }
}
const report = {
  schemaVersion: 1,
  ok: errors.length === 0,
  scope: 'Repository structure only; not mathematical or browser verification',
  markdownFiles: markdown.length,
  engineModules: engine.length,
  content: Object.fromEntries(['planned', 'draft', 'ready'].map((status) => [status, entries.filter((entry) => entry?.status === status).length])),
  errors,
};
if (process.argv.includes('--json')) console.log(JSON.stringify(report, null, 2));
else if (errors.length) console.error(errors.join('\n'));
else console.log(`Repository checks passed: ${markdown.length} documents; ${engine.length} engine modules; ${report.content.ready} ready content entries (${report.content.planned} planned).\nNo mathematical or browser verification is implied.`);
process.exitCode = errors.length ? 1 : 0;

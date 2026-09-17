import assert from 'node:assert/strict';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { test } from 'node:test';
import { checkCatalog } from '../scripts/catalog.mjs';
import { checkMarkdown, checkEngineSource, filesUnder } from '../scripts/repository.mjs';

function fixture() {
  return {
    version: 1,
    parts: [{ id: 'foundations', title: 'Foundations', chapters: ['start', 'next'] }],
    chapters: [
      { id: 'start', title: 'Start', status: 'draft', source: 'book/parts/foundations/start.md', requires: [], concepts: ['state'] },
      { id: 'next', title: 'Next', status: 'planned', source: null, requires: ['start'], concepts: [] },
    ],
    concepts: [{ id: 'state', title: 'State', status: 'planned', source: null, requires: [] }],
  };
}
const source = (name) => name === 'book/parts/foundations/start.md' ? '# Start\nA draft.' : null;

test('a mixed draft/planned catalogue is valid without pretending content is ready', () => {
  assert.deepEqual(checkCatalog(fixture(), source), []);
});

test('broken graph edges, duplicate IDs, and multiple chapter owners fail', () => {
  const missing = fixture();
  missing.chapters[0].requires = ['missing'];
  assert.match(checkCatalog(missing, source).join('\n'), /unknown prerequisite/);
  const duplicate = fixture();
  duplicate.concepts[0].id = 'start';
  assert.match(checkCatalog(duplicate, source).join('\n'), /duplicate ID/);
  const owners = fixture();
  owners.parts.push({ id: 'second-part', title: 'Second', chapters: ['start'] });
  assert.match(checkCatalog(owners, source).join('\n'), /multiple positions or parts/);
});

test('cycles and impossible reading orders fail', () => {
  const catalog = fixture();
  catalog.chapters[0].requires = ['next'];
  const errors = checkCatalog(catalog, source).join('\n');
  assert.match(errors, /cycle/);
  assert.match(errors, /earlier in reading order/);
});

test('source paths cannot escape the content structure or be absent for authored pages', () => {
  const catalog = fixture();
  catalog.chapters[0].source = '../../outside.md';
  assert.match(checkCatalog(catalog, source).join('\n'), /source must be/);
  assert.match(checkCatalog(fixture(), () => null).join('\n'), /source missing or empty/);
  assert.match(checkCatalog(fixture(), () => '  ').join('\n'), /source missing or empty/);
});

test('ready content cannot depend on unfinished references', () => {
  const catalog = fixture();
  catalog.chapters[0].status = 'ready';
  assert.match(checkCatalog(catalog, source).join('\n'), /ready content depends on unfinished state/);
  catalog.concepts[0].status = 'ready';
  catalog.concepts[0].source = 'concepts/state.md';
  assert.deepEqual(checkCatalog(catalog, () => '# Authored content'), []);
});

test('invalid catalogue shape reports errors', () => {
  for (const value of [null, {}, { version: 1, parts: {}, chapters: [], concepts: [] }]) {
    assert.ok(checkCatalog(value, source).length > 0);
  }
});

function temporaryRepo(t) {
  const root = fs.mkdtempSync(path.join(os.tmpdir(), 'conmath-harness-'));
  t.after(() => fs.rmSync(root, { recursive: true, force: true }));
  return root;
}

test('Markdown links resolve relative paths and heading anchors, ignoring code examples', (t) => {
  const root = temporaryRepo(t);
  fs.mkdirSync(path.join(root, 'docs'));
  fs.writeFileSync(path.join(root, 'docs/topic.md'), '# A topic\n\n## More detail\n\n## More detail\n');
  fs.writeFileSync(path.join(root, 'README.md'), [
    '# Home', '[topic](docs/topic.md#more-detail)', '[duplicate](docs/topic.md#more-detail-1)',
    '[self](#home)', '[external](https://example.com)',
    '```md\n[example](nonexistent.md)\n```', '`[inline example](missing.md)`',
  ].join('\n\n'));
  assert.deepEqual(checkMarkdown(root, 'README.md'), []);
});

test('missing files, anchors, escaping paths, and malformed encoding fail links', (t) => {
  const root = temporaryRepo(t);
  fs.writeFileSync(path.join(root, 'README.md'), [
    '# Home', '[missing](none.md)', '[anchor](#absent)',
    '[escape](../outside.md)', '[malformed](%ZZ.md)',
  ].join('\n'));
  const errors = checkMarkdown(root, 'README.md').join('\n');
  assert.match(errors, /missing link target/);
  assert.match(errors, /missing anchor/);
  assert.match(errors, /escapes repository/);
  assert.match(errors, /malformed link/);
});

test('source inventory excludes generated output and refuses symlinks', (t) => {
  const root = temporaryRepo(t);
  fs.mkdirSync(path.join(root, 'dist'));
  fs.writeFileSync(path.join(root, 'dist/ignored.md'), 'generated');
  fs.writeFileSync(path.join(root, 'README.md'), 'source');
  assert.deepEqual(filesUnder(root), ['README.md']);
  fs.symlinkSync('README.md', path.join(root, 'alias.md'));
  assert.throws(() => filesUnder(root), /symlink/);
});

test('engine permits local dependencies and rejects host coupling and dynamic loading', () => {
  assert.deepEqual(checkEngineSource('engine/example.py', 'def identity(value):\n    return value'), []);
  for (const code of ['import os', 'from js import document', '__import__("os")', 'open("file")', 'exec("code")']) {
    assert.ok(checkEngineSource('engine/example.py', code).length > 0, code);
  }
  const name = 'engine/machine.mjs';
  assert.deepEqual(checkEngineSource(name, "import { bit } from './values.mjs';\nexport const flip = x => x ^ 1;"), []);
  for (const code of [
    "import { view } from '../web/view.mjs';", "import 'node:fs';",
    "export { x } from '../web/view.mjs';", "import('./values.mjs');",
    'document.title = "bad";', 'Math.random();', 'Date.now();', 'globalThis.fetch("/");',
  ]) assert.ok(checkEngineSource(name, code).length > 0, code);
});

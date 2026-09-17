import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { fileURLToPath } from 'node:url';
import { build, escape } from '../scripts/publish.mjs';
const root = fileURLToPath(new URL('../', import.meta.url));

test('static build is deterministic, links resolve, and unpublished content is not linked', () => {
  const output = build(root);
  assert.deepEqual(output, build(root));
  for (const [name, html] of output) {
    if (!name.endsWith('.html')) continue;
    for (const match of html.matchAll(/(?:href|src)="([^"#]+)(?:#[^"]*)?"/g)) {
      if (/^(?:https?:|data:)/.test(match[1])) continue;
      const destination = new URL(match[1], `https://book.invalid/${name}`).pathname.slice(1);
      assert.ok(output.has(destination), `${name} links to absent ${destination}`);
    }
  }
  assert.ok(!output.has('book/counting-and-addition.html'));
  assert.ok(output.get('book/objects-and-constructions.html').includes('<math display="block"'));
});

test('published source is byte-identical to the executed module', () => {
  const output = build(root);
  for (const filename of ['successor.py', 'evidence.py']) {
    const original = fs.readFileSync(new URL(`../engine/${filename}`, import.meta.url), 'utf8');
    assert.equal(output.get(`assets/engine/${filename}`), original);
    const html = output.get(filename === 'successor.py' ? 'book/objects-and-constructions.html' : 'concepts/proof-and-evidence.html');
    assert.ok(html.includes(`<code data-source="engine/${filename}">${escape(original)}</code>`));
  }
});

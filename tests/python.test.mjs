import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import { loadPyodide } from 'pyodide';
const python = await loadPyodide();
for (const name of ['successor.py', 'memory.py', 'evidence.py']) python.runPython(fs.readFileSync(new URL(`../engine/${name}`, import.meta.url), 'utf8'));
python.runPython('import json');
const run = (length, limit) => JSON.parse(python.runPython(`json.dumps(run_example(${length}, ${limit}))`));
function check(result, rules = 32) {
  python.globals.set('evidence_json', JSON.stringify(result));
  return JSON.parse(python.runPython(`json.dumps(check_execution(json.loads(evidence_json), ${rules}))`));
}

test('all 90 length/budget configurations follow copy-then-append semantics', () => {
  for (let length = 0; length <= 8; length++) for (let limit = 0; limit <= 9; limit++) {
    const result = run(length, limit);
    assert.equal(result.ok, length < 8 && limit >= length + 1);
    assert.equal(result.steps, Math.min(length + 1, limit));
    assert.deepEqual(result.after.slice(0, 8), result.before.slice(0, 8));
    assert.ok(result.trace.length <= 25);
    if (result.ok) {
      assert.deepEqual(result.after.slice(8), Array.from({ length: 8 }, (_, i) => i <= length ? 1 : 0));
      assert.equal(check(result).ok, true);
    } else {
      assert.equal(result.reason, length === 8 && limit === 9 ? 'out-of-memory' : 'out-of-steps');
      assert.equal(check(result).ok, false);
    }
  }
});

test('actual reads and writes identify disjoint source/target addresses', () => {
  const result = run(3, 4);
  assert.deepEqual(result.trace.filter(e => e.op === 'read').map(e => e.address), [0, 1, 2]);
  assert.deepEqual(result.trace.filter(e => e.op === 'write').map(e => e.address), [8, 9, 10, 11]);
  assert.deepEqual(run(3, 4), result);
  assert.deepEqual(run(3, 3).after.slice(8), [1, 1, 1, 0, 0, 0, 0, 0]);
});

test('checker rejects forged records and enforces the checking budget', () => {
  const result = run(3, 4);
  const needed = result.trace.length + 2;
  assert.equal(check(result, needed).ok, true);
  assert.equal(check(result, needed - 1).reason, 'out-of-checking-steps');
  const empty = run(0, 1); empty.steps = true;
  assert.equal(check(empty).ok, false);
  for (const mutate of [
    r => { r.trace[1].address = 7; },
    r => { r.trace.pop(); },
    r => { r.after[0] = 0; },
    r => { r.after[11] = 0; },
    r => { r.trace[1].value = true; },
    r => { r.before[0] = true; },
    r => { r.trace = Array(28).fill({}); },
    r => { r.ok = false; },
  ]) {
    const changed = structuredClone(result); mutate(changed); assert.equal(check(changed).ok, false);
  }
});

test('bounded input admission rejects invalid lengths and budgets', () => {
  for (const args of ['-1, 4', '9, 4', '3, -1', '3, 10', 'True, 4', '3, 1.5']) {
    assert.equal(JSON.parse(python.runPython(`json.dumps(run_example(${args}))`)).reason, 'invalid-input');
  }
  assert.equal(python.runPython('len(run_example(8, 9)["after"])'), 16);
});

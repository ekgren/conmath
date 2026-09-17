import test from 'node:test';
import assert from 'node:assert/strict';
import { inverter, nand, clockRegister, createComputer, stepComputer, allocate, addWord, checkCommutativity } from '../site/assets/engine/computer.js';
import { createApproximation, refine, checkEnclosure } from '../site/assets/engine/approximation.js';

test('complementary switches and NAND cover all Boolean inputs', () => {
  for (const a of [0, 1]) {
    const state = inverter(a);
    assert.notEqual(state.pmosOn, state.nmosOn);
    assert.equal(state.output, 1 - a);
    for (const b of [0, 1]) assert.equal(nand(a, b), a === 1 && b === 1 ? 0 : 1);
  }
  assert.throws(() => nand(2, 0), TypeError);
});
test('register preserves state without an edge and captures input on an edge', () => {
  for (const q of [0, 1]) for (const d of [0, 1]) {
    assert.equal(clockRegister(q, d, false), q);
    assert.equal(clockRegister(q, d, true), d);
  }
});
test('fetch/load/not/store/halt has deterministic register and memory transfers', () => {
  const run = () => {
    let state = createComputer(); const trace = [];
    for (let i = 0; i < 4; i++) { const result = stepComputer(state); state = result.state; trace.push(result); }
    return trace;
  };
  const trace = run();
  assert.equal(trace[0].state.a, 5); assert.equal(trace[0].state.ir, 4); assert.equal(trace[0].state.pc, 1);
  assert.equal(trace[1].state.a, 10);
  assert.deepEqual(trace[2].state.memory, [5, 10, 0, 0]);
  assert.equal(trace[3].state.status, 'halted'); assert.equal(trace[3].state.fuel, 0);
  assert.deepEqual(run(), trace);
  assert.equal(stepComputer(trace[3].state).event, null);
  assert.deepEqual(trace[0].event.before.memory, [5, 0, 0, 0]);
});
test('fuel exhaustion is non-mutating on the data path and does not execute STORE', () => {
  let state = createComputer(2);
  state = stepComputer(stepComputer(state).state).state;
  const result = stepComputer(state);
  assert.equal(result.state.status, 'exhausted');
  for (const key of ['a', 'pc', 'ir', 'steps', 'fuel']) assert.equal(result.state[key], state[key]);
  assert.deepEqual(result.state.memory, [5, 0, 0, 0]);
  assert.equal(stepComputer(createComputer(0)).state.steps, 0);
});
test('allocation success consumes capacity; failure leaves allocation unchanged', () => {
  assert.deepEqual(allocate(3, 4, 1), { outcome: 'ok', used: 4, capacity: 4 });
  assert.deepEqual(allocate(4, 4, 1), { outcome: 'out-of-memory', used: 4, capacity: 4 });
  assert.throws(() => allocate(5, 4, 1), RangeError);
});
test('four-bit addition distinguishes exact sums from overflow', () => {
  assert.deepEqual(addWord(8, 7), { outcome: 'ok', value: 15 });
  assert.deepEqual(addWord(8, 8), { outcome: 'overflow' });
  assert.deepEqual(checkCommutativity(), { accepted: true, cases: 256 });
});
test('exact enclosure narrows, contains sqrt(2), and preserves the last result on exhaustion', () => {
  for (const limit of [8, 12, 24]) {
    let state = createApproximation(limit);
    for (let i = 0; i < 40; i++) {
      const next = refine(state);
      assert.equal(checkEnclosure(next), true);
      if (next.status === 'exhausted') {
        for (const key of ['low', 'high', 'denominator', 'steps', 'peakBits']) assert.equal(next[key], state[key]);
        assert.equal(refine(next), next); break;
      }
      assert.equal(next.denominator, state.denominator * 2n);
      assert.equal(next.high - next.low, 1n);
      assert.ok(next.low * state.denominator >= state.low * next.denominator);
      assert.ok(next.high * state.denominator <= state.high * next.denominator);
      assert.ok(next.peakBits <= limit);
      state = next;
      assert.ok(i < 39, 'must reach the finite bound');
    }
  }
});

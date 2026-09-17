// Ideal digital model. No analog timing or electrical simulation.
function bit(value) {
  if (value !== 0 && value !== 1) throw new TypeError('Expected a bit');
  return value;
}
export function nand(a, b) { return 1 - bit(a) * bit(b); }
export function inverter(input) {
  bit(input);
  return Object.freeze({ input, pmosOn: input === 0, nmosOn: input === 1, output: nand(input, input) });
}
export function clockRegister(stored, input, edge) {
  bit(stored); bit(input);
  if (typeof edge !== 'boolean') throw new TypeError('Expected a clock edge flag');
  return edge ? input : stored;
}
export function bits(value, width) {
  if (!Number.isInteger(width) || width < 1 || width > 16 || !Number.isInteger(value) || value < 0 || value >= 2 ** width) throw new RangeError('Value does not fit');
  return value.toString(2).padStart(width, '0').split('').map(Number);
}
export const program = Object.freeze([0b0100, 0b1000, 0b1101, 0b0000]); // LOAD 0, NOT, STORE 1, HALT
const freeze = state => Object.freeze({ ...state, memory: Object.freeze([...state.memory]) });
export function createComputer(fuel = 4) {
  if (!Number.isInteger(fuel) || fuel < 0 || fuel > 255) throw new RangeError('Fuel must fit in 8 bits');
  return freeze({ memory: [5, 0, 0, 0], a: 0, pc: 0, ir: 0, fuel, steps: 0, status: 'ready' });
}
export function stepComputer(state) {
  if (!['ready', 'running'].includes(state.status)) return { state, event: null };
  if (state.fuel === 0) return { state: freeze({ ...state, status: 'exhausted' }), event: Object.freeze({ sequence: state.steps, type: 'resource.exhausted', resource: 'instructions' }) };
  const ir = program[state.pc];
  const opcode = ir >> 2;
  const address = ir & 3;
  const memory = [...state.memory];
  let a = state.a;
  let operation = 'HALT';
  if (opcode === 1) { a = memory[address]; operation = `LOAD ${address}`; }
  if (opcode === 2) { a ^= 15; operation = 'NOT'; }
  if (opcode === 3) { memory[address] = a; operation = `STORE ${address}`; }
  const next = freeze({ memory, a, ir, pc: opcode === 0 ? state.pc : (state.pc + 1) & 3, fuel: state.fuel - 1, steps: state.steps + 1, status: opcode === 0 ? 'halted' : 'running' });
  return { state: next, event: Object.freeze({ sequence: state.steps, type: 'instruction', operation, address: opcode === 1 || opcode === 3 ? address : null, before: state, after: next }) };
}
export function allocate(used, capacity, requested) {
  for (const n of [used, capacity, requested]) if (!Number.isInteger(n) || n < 0 || n > 16) throw new RangeError('Expected a capacity from 0 to 16');
  if (used > capacity) throw new RangeError('Invalid allocation state');
  return Object.freeze(requested > capacity - used ? { outcome: 'out-of-memory', used, capacity } : { outcome: 'ok', used: used + requested, capacity });
}
export function addWord(a, b) {
  bits(a, 4); bits(b, 4);
  return a + b > 15 ? Object.freeze({ outcome: 'overflow' }) : Object.freeze({ outcome: 'ok', value: a + b });
}
export function checkCommutativity() {
  let cases = 0;
  for (let a = 0; a < 16; a++) for (let b = 0; b < 16; b++) {
    const left = addWord(a, b), right = addWord(b, a);
    cases++;
    if (left.outcome !== right.outcome || left.value !== right.value) return Object.freeze({ accepted: false, cases });
  }
  return Object.freeze({ accepted: true, cases });
}

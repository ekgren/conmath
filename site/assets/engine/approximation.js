// Exact dyadic arithmetic with a declared bit limit on every arithmetic value.
// Browser allocation and BigInt overhead are outside this model account.
const length = n => n.toString(2).length;
export function createApproximation(limit = 12) {
  if (!Number.isInteger(limit) || limit < 4 || limit > 64) throw new RangeError('Bit limit must be 4–64');
  return Object.freeze({ low: 1n, high: 2n, denominator: 1n, steps: 0, limit, status: 'ready', peakBits: 3 });
}
export function refine(state) {
  if (state.status === 'exhausted') return state;
  // Preflight representational cost of the next exact comparison.
  const mid = state.low + state.high;
  const denominator = state.denominator * 2n;
  const square = mid * mid;
  const target = 2n * denominator * denominator;
  const peakBits = Math.max(length(square), length(target), length(state.high * 2n));
  if (peakBits > state.limit) return Object.freeze({ ...state, status: 'exhausted' });
  return Object.freeze({ ...state, low: square <= target ? mid : state.low * 2n, high: square <= target ? state.high * 2n : mid, denominator, steps: state.steps + 1, peakBits, status: 'ready' });
}
export function checkEnclosure(state) {
  return state.low >= 0n && state.low < state.high && state.low * state.low <= 2n * state.denominator * state.denominator && state.high * state.high >= 2n * state.denominator * state.denominator;
}

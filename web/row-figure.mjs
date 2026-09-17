const element = (id) => document.getElementById(id);
const form = element('configuration');
const worker = new Worker(new URL('./python-worker.mjs', import.meta.url), { type: 'module' });
let ready = false;
let busy = false;
let generation = 0;
let result = null;
let proof = null;
const errors = [];
const configuration = () => ({ length: Number(element('marks').value), limit: Number(element('fuel').value) });
const snapshot = () => ({ model: 'copy-successor-v1', input: configuration(), result, proof, errors: [...errors] });
window.conmath = Object.freeze({ inspect: () => structuredClone(snapshot()) });

function cells(id, values, offset) {
  const region = element(id);
  region.replaceChildren(...values.map((value, index) => {
    const cell = document.createElement('span');
    cell.textContent = value ? 'Ⅰ' : '·'; cell.className = value ? 'marked' : '';
    cell.title = `Address ${offset + index}: ${value}`; return cell;
  }));
  region.setAttribute('aria-label', `${offset ? 'Target' : 'Source'}: ${values.map((value) => value ? 'marked' : 'blank').join(', ')}`);
}
function draw() {
  const { length, limit } = configuration();
  const initial = Array.from({ length: 16 }, (_, i) => i < length ? 1 : 0);
  const memory = result?.after ?? initial;
  cells('source-cells', memory.slice(0, 8), 0); cells('cells', memory.slice(8), 8);
  const valid = form.checkValidity();
  element('run').disabled = !ready || busy || !valid;
  element('reset').disabled = !ready || busy;
  element('check-proof').disabled = busy || !result?.ok;
  element('export').disabled = busy || !result;
  const reasons = { 'out-of-steps': 'step budget exhausted', 'out-of-memory': 'target has no room for the final mark' };
  element('run-status').textContent = !valid ? 'Enter a whole step budget from 0 to 9.' : !ready ? 'Loading Python locally…' : busy ? 'Running…' : !result ? `Ready. ${length} input marks; ${limit} steps available.` : result.ok ? `Success. Copied ${length} marks and added one in ${result.steps} steps.` : `Failure: ${reasons[result.reason] ?? result.reason}. No completed result.`;
  element('run-status').dataset.outcome = result ? result.ok ? 'success' : 'failure' : 'ready';
  element('resource-use').textContent = `16 data cells reserved · ${result?.steps ?? 0} / ${limit} charged steps. Runtime and evidence storage are separate.`;
  element('proof-status').textContent = proof ? proof.ok ? `Checked: source preserved; target is its successor. ${proof.rulesUsed} checks.` : `Check failed: ${proof.reason}.` : result?.ok ? 'This run has not yet been checked.' : 'A successful run is needed before checking.';
  element('trace').replaceChildren(...(result?.trace?.length ? result.trace : [null]).map((event) => {
    const item = document.createElement('li');
    item.textContent = !event ? 'No operations recorded.' : event.op === 'step' ? `step ${event.step}` : `${event.op}(${event.address}) ${event.op === 'read' ? '→' : '←'} ${event.value}`;
    return item;
  }));
}
function reset() { generation += 1; result = null; proof = null; busy = false; draw(); }
function failed(message) {
  errors.push(String(message).slice(0, 500)); if (errors.length > 20) errors.shift();
  busy = false; ready = false; draw();
  element('run-status').textContent = 'Python could not run. Reload the page to retry; the program remains readable.';
}
worker.onerror = (event) => failed(event.message);
worker.onmessage = ({ data }) => {
  if (data.type === 'ready') { ready = true; draw(); return; }
  if (data.id !== undefined && data.id !== generation) return;
  if (data.type === 'error') { failed(data.message); return; }
  busy = false;
  if (data.type === 'result') { result = data.result; proof = null; }
  if (data.type === 'proof') proof = data.proof;
  draw();
};
form.addEventListener('submit', (event) => event.preventDefault());
form.addEventListener('input', reset);
element('reset').addEventListener('click', reset);
element('run').addEventListener('click', () => {
  if (!form.reportValidity()) return;
  generation += 1; busy = true; proof = null; draw();
  worker.postMessage({ type: 'run', id: generation, ...configuration() });
});
element('check-proof').addEventListener('click', () => {
  busy = true; draw(); worker.postMessage({ type: 'check', id: generation, result });
});
element('export').addEventListener('click', () => {
  const url = URL.createObjectURL(new Blob([JSON.stringify(snapshot(), null, 2)], { type: 'application/json' }));
  const link = document.createElement('a'); link.href = url; link.download = 'conmath-successor-evidence.json'; link.click();
  setTimeout(() => URL.revokeObjectURL(url), 1000);
});
draw();

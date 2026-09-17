import { inverter, nand, clockRegister, bits, createComputer, stepComputer, allocate, checkCommutativity } from './engine/computer.js';
import { createApproximation, refine, checkEnclosure } from './engine/approximation.js';
import { verifyDoubleNegation } from './engine/bit-proof.js';

const $ = id => document.getElementById(id);
const set = (id, text) => { $(id).textContent = text; };
const listen = (id, fn, event = 'click') => { $(id).addEventListener(event, fn); $(id).disabled = false; };
const signal = (id, active) => $(id).classList.toggle('active', Boolean(active));
let input = 0;
function drawInverter() {
  const state = inverter(input);
  set('inverter-input', `Input A = ${input}`);
  $('inverter-input').setAttribute('aria-pressed', String(Boolean(input)));
  set('inverter-value', state.output);
  set('pmos-state', state.pmosOn ? 'conducting' : 'open');
  set('nmos-state', state.nmosOn ? 'conducting' : 'open');
  signal('pull-up', state.pmosOn); signal('pull-down', state.nmosOn);
  signal('pmos-switch', state.pmosOn); signal('nmos-switch', state.nmosOn);
  signal('inverter-out', state.output);
  $('pmos-switch').setAttribute('d', state.pmosOn ? 'M305 80V140' : 'M305 80L331 130');
  $('nmos-switch').setAttribute('d', state.nmosOn ? 'M305 220V280' : 'M305 220L331 270');
  set('inverter-result', `A = ${input}: pMOS ${state.pmosOn ? 'conducts' : 'is open'}, nMOS ${state.nmosOn ? 'conducts' : 'is open'}. Output = ${state.output}.`);
}
listen('inverter-input', () => { input ^= 1; drawInverter(); });
drawInverter();
let a = 0, b = 0;
function drawNand() {
  const out = nand(a, b);
  for (const [name, value] of [['a', a], ['b', b]]) {
    set(`nand-${name}`, `${name.toUpperCase()} = ${value}`);
    $(`nand-${name}`).setAttribute('aria-pressed', String(Boolean(value)));
    signal(`nand-wire-${name}`, value);
  }
  signal('nand-wire-out', out); set('nand-output', out);
  set('nand-result', `NAND(${a}, ${b}) = ${out}.`);
  document.querySelectorAll('[data-case]').forEach(row => row.classList.toggle('selected', row.dataset.case === `${a}${b}`));
}
listen('nand-a', () => { a ^= 1; drawNand(); });
listen('nand-b', () => { b ^= 1; drawNand(); });
drawNand();
let d = 0, q = 0;
function drawRegister(captured = false) {
  set('register-input', `D = ${d}`); $('register-input').setAttribute('aria-pressed', String(Boolean(d)));
  for (const [name, value] of [['d', d], ['q', q]]) { set(`register-${name}`, value); $(`register-${name}`).dataset.value = value; }
  set('register-result', `D = ${d}, Q = ${q}. ${captured ? 'Clock edge: input captured.' : 'No clock edge: stored Q is unchanged.'}`);
}
listen('register-input', () => { d ^= 1; q = clockRegister(q, d, false); drawRegister(); });
listen('register-clock', () => { q = clockRegister(q, d, true); drawRegister(true); });
function bitRow(label, value, width) {
  const row = document.createElement('div'); row.className = 'bit-row';
  row.setAttribute('aria-label', `${label}: ${bits(value, width).join('')}`);
  const name = document.createElement('span'); name.className = 'row-label'; name.textContent = label; row.append(name);
  for (const valueBit of bits(value, width)) {
    const cell = document.createElement('span'); cell.className = 'bit-cell'; cell.dataset.value = valueBit; cell.textContent = valueBit; cell.setAttribute('aria-hidden', 'true'); row.append(cell);
  }
  return row;
}
let computer = createComputer(), events = [];
function drawComputer(lastEvent = null) {
  const lastAddress = events.filter(event => event.address != null).at(-1)?.address;
  $('computer-registers').replaceChildren(bitRow('A', computer.a, 4), bitRow('PC', computer.pc, 2), bitRow('IR', computer.ir, 4));
  $('computer-memory').replaceChildren(...computer.memory.map((word, index) => {
    const row = bitRow(bits(index, 2).join(''), word, 4);
    row.classList.toggle('accessed', index === lastAddress); return row;
  }));
  [...$('computer-program').children].forEach((row, index) => row.classList.toggle('selected', index === computer.pc && ['ready', 'running'].includes(computer.status)));
  $('computer-step').disabled = ['halted', 'exhausted'].includes(computer.status);
  set('computer-status', `${computer.status} · ${computer.steps} executed · ${computer.fuel} steps remaining`);
  if (!lastEvent) set('computer-transfer', 'Next: LOAD memory[0] into A.');
  else if (lastEvent.type === 'resource.exhausted') set('computer-transfer', 'Out of steps. No instruction executed; registers and memory preserved.');
  else set('computer-transfer', `${lastEvent.operation}: ${lastEvent.operation.startsWith('LOAD') ? 'memory[0] → A' : lastEvent.operation.startsWith('STORE') ? 'A → memory[1]' : lastEvent.operation === 'NOT' ? 'all four bits of A flipped' : 'execution stopped'}.`);
  $('computer-trace').replaceChildren(...events.map(e => {
    const li = document.createElement('li'); li.textContent = `${e.sequence}: ${e.operation ?? e.type}`; return li;
  }));
}
function resetComputer() { computer = createComputer(Number($('computer-budget').value)); events = []; drawComputer(); }
listen('computer-step', () => { const result = stepComputer(computer); computer = result.state; if (result.event) events.push(result.event); drawComputer(result.event); });
listen('computer-reset', resetComputer);
listen('computer-budget', resetComputer, 'change');
listen('computer-export', () => {
  const artifact = { format: 'conmath.computer-trace.v1', state: computer, events };
  const url = URL.createObjectURL(new Blob([JSON.stringify(artifact, null, 2)], { type: 'application/json' }));
  const link = document.createElement('a'); link.href = url; link.download = 'conmath-computer-trace.json'; link.click(); URL.revokeObjectURL(url);
});
drawComputer();
let used = 0;
function drawAllocation(outcome = 'ok') {
  const capacity = Number($('allocation-capacity').value);
  $('allocation-grid').replaceChildren(...Array.from({ length: capacity }, (_, i) => {
    const cell = document.createElement('span'); cell.className = 'allocation-cell'; cell.dataset.value = Number(i < used); cell.textContent = i < used ? '0 · stored' : 'free'; return cell;
  }));
  set('allocation-result', outcome === 'ok' ? `${used} of ${capacity} cells occupied.` : `Out of memory. ${used} of ${capacity} cells occupied; collection unchanged.`);
}
listen('allocate', () => { const result = allocate(used, Number($('allocation-capacity').value), 1); used = result.used; drawAllocation(result.outcome); });
listen('allocation-reset', () => { used = 0; drawAllocation(); });
listen('allocation-capacity', () => { used = 0; drawAllocation(); }, 'change');
drawAllocation();
listen('bit-check', () => {
  const result = verifyDoubleNegation();
  set('bit-proof-result', result.accepted ? `Accepted · ${result.resources.casesChecked} cases · ${result.resources.proofNodes} proof nodes` : result.exhausted ? 'Out of resources' : 'Rejected');
  set('bit-proof-trace', result.events.map(e => `${e.sequence}: ${e.rule ?? e.type}${e.case ? ` · ${e.case}` : ''}${e.outcome ? ` · ${e.outcome}` : ''}`).join('\n'));
});
listen('addition-check', () => { const result = checkCommutativity(); set('addition-result', `${result.accepted ? 'Accepted' : 'Rejected'} · ${result.cases} input pairs checked`); });
listen('rounding-check', () => { const a = 1e16, b = -1e16, c = 1; set('rounding-result', `(a + b) + c = ${(a + b) + c}\na + (b + c) = ${a + (b + c)}`); });
let approximation = createApproximation();
function drawInterval() {
  const s = approximation;
  const left = 40 + 540 * (Number(s.low) / Number(s.denominator) - 1);
  const right = 40 + 540 * (Number(s.high) / Number(s.denominator) - 1);
  $('interval-band').setAttribute('x', left); $('interval-band').setAttribute('width', right - left);
  $('interval-ends').setAttribute('d', `M${left} 42V88 M${right} 42V88`);
  set('interval-fractions', `[${s.low}/${s.denominator}, ${s.high}/${s.denominator}] · width ${s.high - s.low}/${s.denominator}`);
  set('interval-result', `${s.status === 'exhausted' ? 'Out of arithmetic bits. Last enclosure preserved.' : `${s.steps} refinements · peak integer width ${s.peakBits}/${s.limit} bits.`} Enclosure inequalities: ${checkEnclosure(s) ? 'checked' : 'failed'}.`);
  $('interval-refine').disabled = s.status === 'exhausted';
}
function resetInterval() { approximation = createApproximation(Number($('precision-budget').value)); drawInterval(); }
listen('interval-refine', () => { approximation = refine(approximation); drawInterval(); });
listen('interval-reset', resetInterval); listen('precision-budget', resetInterval, 'change');
drawInterval();
const links = [...document.querySelectorAll('.contents a')];
const sections = links.map(link => document.querySelector(link.getAttribute('href')));
function updateContents() {
  let index = 0;
  sections.forEach((section, i) => { if (section.getBoundingClientRect().top <= 180) index = i; });
  links.forEach((link, i) => { if (i === index) link.setAttribute('aria-current', 'location'); else link.removeAttribute('aria-current'); });
}
window.addEventListener('scroll', updateContents, { passive: true }); updateContents();

import {
  Bit,
  bitName,
  chapterProgram,
  createMachine,
  stepMachine
} from "./engine/bit-machine.js";
import { verifyDoubleNegation } from "./engine/bit-proof.js";

const elements = {
  cell: document.querySelector("[data-machine-cell]"),
  cellName: document.querySelector("[data-machine-cell-name]"),
  pc: document.querySelector("[data-machine-pc]"),
  status: document.querySelector("[data-machine-status]"),
  steps: document.querySelector("[data-machine-steps]"),
  trace: document.querySelector("[data-machine-trace]"),
  program: [...document.querySelectorAll("[data-program-instruction]")],
  step: document.querySelector("[data-action-step]"),
  run: document.querySelector("[data-action-run]"),
  reset: document.querySelector("[data-action-reset]"),
  export: document.querySelector("[data-action-export]"),
  verify: document.querySelector("[data-action-verify]"),
  proofStatus: document.querySelector("[data-proof-status]"),
  proofTrace: document.querySelector("[data-proof-trace]"),
  proofNodes: document.querySelector("[data-proof-nodes]"),
  normalizationSteps: document.querySelector("[data-normalization-steps]")
};

let machine = createMachine();
let trace = [];
let sequence = 0;
let running = false;

function renderMachine() {
  const name = bitName(machine.cell);
  elements.cell.dataset.value = name;
  elements.cell.textContent = machine.cell;
  elements.cellName.textContent = name;
  elements.pc.textContent = machine.pc;
  elements.status.textContent = machine.status;
  elements.status.dataset.status = machine.status;
  elements.steps.textContent = machine.steps;

  elements.program.forEach((row, index) => {
    row.classList.toggle("is-current", index === machine.pc && !["halted", "faulted", "exhausted"].includes(machine.status));
    row.classList.toggle("is-complete", index < machine.pc);
  });

  const terminal = ["halted", "faulted", "exhausted"].includes(machine.status);
  elements.step.disabled = terminal || running;
  elements.run.disabled = terminal || running;
}

function renderTrace() {
  elements.trace.replaceChildren();
  const visible = trace.slice(-10);
  if (!visible.length) {
    const empty = document.createElement("li");
    empty.className = "trace-empty";
    empty.textContent = "No events yet. Step the machine.";
    elements.trace.append(empty);
    return;
  }

  for (const item of visible) {
    const row = document.createElement("li");
    const sequenceLabel = document.createElement("span");
    const type = document.createElement("strong");
    const detail = document.createElement("span");
    sequenceLabel.textContent = String(item.sequence).padStart(2, "0");
    type.textContent = item.type.replace("machine.", "");
    detail.textContent = item.instruction ?? item.after?.cell ?? "";
    row.append(sequenceLabel, type, detail);
    elements.trace.append(row);
  }
}

function performStep() {
  const result = stepMachine(machine, chapterProgram, { sequence });
  machine = result.machine;
  sequence = result.nextSequence;
  trace.push(...result.events);
  renderMachine();
  renderTrace();
}

elements.step.addEventListener("click", performStep);

elements.run.addEventListener("click", async () => {
  running = true;
  renderMachine();
  while (!["halted", "faulted", "exhausted"].includes(machine.status)) {
    performStep();
    await new Promise((resolve) => window.setTimeout(resolve, 360));
  }
  running = false;
  renderMachine();
});

elements.reset.addEventListener("click", () => {
  machine = createMachine();
  trace = [];
  sequence = 0;
  running = false;
  renderMachine();
  renderTrace();
});

elements.export.addEventListener("click", () => {
  const artifact = {
    format: "conmath.trace.v1",
    chapter: "01-first-distinction",
    machine,
    events: trace
  };
  const blob = new Blob([JSON.stringify(artifact, null, 2)], { type: "application/json" });
  const link = document.createElement("a");
  link.href = URL.createObjectURL(blob);
  link.download = "conmath-chapter-01-trace.json";
  link.click();
  URL.revokeObjectURL(link.href);
});

elements.verify.addEventListener("click", () => {
  const result = verifyDoubleNegation();
  elements.proofStatus.textContent = result.accepted ? "accepted" : result.exhausted ? "out of resources" : "rejected";
  elements.proofStatus.dataset.accepted = String(result.accepted);
  elements.proofNodes.textContent = result.resources.proofNodes;
  elements.normalizationSteps.textContent = result.resources.normalizationSteps;
  elements.proofTrace.replaceChildren();

  for (const item of result.events) {
    const row = document.createElement("li");
    const rule = document.createElement("span");
    const detail = document.createElement("span");
    rule.textContent = item.rule ?? item.type.replace("proof.", "");
    detail.textContent = item.case ? `${item.case} → ${item.normalized ?? item.outcome ?? ""}` : item.outcome ?? item.theorem ?? "";
    row.append(rule, detail);
    elements.proofTrace.append(row);
  }
});

renderMachine();
renderTrace();

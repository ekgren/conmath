export const Bit = Object.freeze({ LOW: 0, HIGH: 1 });

export const Instruction = Object.freeze({
  SET_LOW: "SET_LOW",
  SET_HIGH: "SET_HIGH",
  FLIP: "FLIP",
  HALT: "HALT"
});

export const chapterProgram = Object.freeze([
  Instruction.SET_LOW,
  Instruction.FLIP,
  Instruction.FLIP,
  Instruction.HALT
]);

export function isBit(value) {
  return value === Bit.LOW || value === Bit.HIGH;
}

export function bitName(value) {
  if (!isBit(value)) throw new TypeError(`Expected Bit, received ${String(value)}`);
  return value === Bit.LOW ? "low" : "high";
}

export function negateBit(value) {
  if (!isBit(value)) throw new TypeError(`Expected Bit, received ${String(value)}`);
  return value === Bit.LOW ? Bit.HIGH : Bit.LOW;
}

export function equalBit(left, right) {
  if (!isBit(left) || !isBit(right)) throw new TypeError("Bit equality requires two Bit values");
  return left === right ? Bit.HIGH : Bit.LOW;
}

export function createMachine(cell = Bit.LOW) {
  if (!isBit(cell)) throw new TypeError("Machine cell must be a Bit");
  return Object.freeze({ cell, pc: 0, status: "ready", steps: 0 });
}

function traceEvent(sequence, type, payload) {
  return Object.freeze({ sequence, type, ...payload });
}

export function stepMachine(machine, program = chapterProgram, options = {}) {
  const runId = options.runId ?? "chapter-01-machine";
  const sequence = options.sequence ?? 0;

  if (["halted", "faulted", "exhausted"].includes(machine.status)) {
    return Object.freeze({ machine, events: Object.freeze([]), nextSequence: sequence });
  }

  const instruction = program[machine.pc];
  if (!instruction) {
    const faulted = Object.freeze({ ...machine, status: "faulted" });
    return Object.freeze({
      machine: faulted,
      events: Object.freeze([
        traceEvent(sequence, "machine.faulted", {
          runId,
          pc: machine.pc,
          reason: "instruction address outside program"
        })
      ]),
      nextSequence: sequence + 1
    });
  }

  const before = Object.freeze({ cell: bitName(machine.cell), pc: machine.pc, status: machine.status });
  let cell = machine.cell;
  let status = "running";

  if (instruction === Instruction.SET_LOW) cell = Bit.LOW;
  else if (instruction === Instruction.SET_HIGH) cell = Bit.HIGH;
  else if (instruction === Instruction.FLIP) cell = negateBit(cell);
  else if (instruction === Instruction.HALT) status = "halted";
  else throw new TypeError(`Unknown instruction: ${String(instruction)}`);

  const next = Object.freeze({
    cell,
    pc: machine.pc + 1,
    status,
    steps: machine.steps + 1
  });
  const after = Object.freeze({ cell: bitName(next.cell), pc: next.pc, status: next.status });

  return Object.freeze({
    machine: next,
    events: Object.freeze([
      traceEvent(sequence, "machine.instruction", {
        runId,
        pc: machine.pc,
        instruction,
        before
      }),
      traceEvent(sequence + 1, "machine.state.changed", {
        runId,
        instruction,
        after,
        resources: Object.freeze({ instructions: next.steps, stateWords: 3 })
      })
    ]),
    nextSequence: sequence + 2
  });
}

export function runMachine(program = chapterProgram, options = {}) {
  const runId = options.runId ?? "chapter-01-machine";
  const maximumSteps = options.maximumSteps ?? program.length;
  let machine = createMachine(options.initialCell ?? Bit.LOW);
  let sequence = 1;
  const events = [
    traceEvent(0, "machine.run.started", {
      runId,
      initial: Object.freeze({ cell: bitName(machine.cell), pc: machine.pc }),
      limits: Object.freeze({ maximumSteps })
    })
  ];

  while (!['halted', 'faulted'].includes(machine.status) && machine.steps < maximumSteps) {
    const result = stepMachine(machine, program, { runId, sequence });
    machine = result.machine;
    sequence = result.nextSequence;
    events.push(...result.events);
  }

  if (!['halted', 'faulted'].includes(machine.status)) {
    machine = Object.freeze({ ...machine, status: "exhausted" });
    events.push(
      traceEvent(sequence++, "resource.exhausted", {
        runId,
        resource: "instructions",
        limit: maximumSteps
      })
    );
  }

  events.push(
    traceEvent(sequence, "machine.run.completed", {
      runId,
      outcome: machine.status,
      final: Object.freeze({ cell: bitName(machine.cell), pc: machine.pc }),
      resources: Object.freeze({
        instructions: machine.steps,
        stateWords: 3,
        programWords: program.length
      })
    })
  );

  return Object.freeze({ machine, events: Object.freeze(events) });
}

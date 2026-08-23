import assert from "node:assert/strict";
import test from "node:test";

import {
  Bit,
  Instruction,
  bitName,
  chapterProgram,
  createMachine,
  equalBit,
  negateBit,
  runMachine,
  stepMachine
} from "../site/assets/engine/bit-machine.js";

test("Bit has two distinct, closed values", () => {
  assert.equal(bitName(Bit.LOW), "low");
  assert.equal(bitName(Bit.HIGH), "high");
  assert.throws(() => bitName(2), /Expected Bit/);
});

test("negation exchanges both constructed values", () => {
  assert.equal(negateBit(Bit.LOW), Bit.HIGH);
  assert.equal(negateBit(Bit.HIGH), Bit.LOW);
});

test("equality is total over Bit", () => {
  assert.equal(equalBit(Bit.LOW, Bit.LOW), Bit.HIGH);
  assert.equal(equalBit(Bit.HIGH, Bit.HIGH), Bit.HIGH);
  assert.equal(equalBit(Bit.LOW, Bit.HIGH), Bit.LOW);
  assert.equal(equalBit(Bit.HIGH, Bit.LOW), Bit.LOW);
});

test("the chapter program returns low after two flips and halts", () => {
  const result = runMachine(chapterProgram);
  assert.deepEqual(result.machine, {
    cell: Bit.LOW,
    pc: 4,
    status: "halted",
    steps: 4
  });
  assert.equal(result.events.at(-1).type, "machine.run.completed");
  assert.equal(result.events.at(-1).outcome, "halted");
});

test("a bounded run reports exhaustion rather than rejection", () => {
  const result = runMachine(chapterProgram, { maximumSteps: 2 });
  assert.equal(result.machine.status, "exhausted");
  assert.ok(result.events.some((event) => event.type === "resource.exhausted"));
});

test("execution traces are deterministic", () => {
  assert.deepEqual(runMachine(chapterProgram), runMachine(chapterProgram));
});

test("stepping an unknown instruction fails explicitly", () => {
  assert.throws(
    () => stepMachine(createMachine(), ["INVENTED"]),
    /Unknown instruction/
  );
  assert.ok(Object.values(Instruction).includes("FLIP"));
});

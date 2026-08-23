import assert from "node:assert/strict";
import test from "node:test";

import {
  doubleNegationProof,
  doubleNegationTheorem,
  verifyByCases,
  verifyDoubleNegation
} from "../site/assets/engine/bit-proof.js";

test("double negation is accepted by cases", () => {
  const result = verifyDoubleNegation();
  assert.equal(result.accepted, true);
  assert.deepEqual(result.resources, {
    proofNodes: 3,
    normalizationSteps: 4,
    casesChecked: 2
  });
  assert.equal(result.events.at(-1).outcome, "accepted");
});

test("a missing branch is rejected", () => {
  const proof = {
    ...doubleNegationProof,
    branches: { low: { kind: "reflexivity" } }
  };
  const result = verifyByCases(doubleNegationTheorem, proof);
  assert.equal(result.accepted, false);
  assert.equal(result.events.at(-1).type, "kernel.rule.rejected");
});

test("insufficient proof resources are reported separately", () => {
  const result = verifyDoubleNegation({ maximumProofNodes: 2 });
  assert.equal(result.accepted, false);
  assert.equal(result.exhausted, true);
  assert.equal(result.events.at(-1).type, "resource.exhausted");
});

test("proof traces are deterministic", () => {
  assert.deepEqual(verifyDoubleNegation(), verifyDoubleNegation());
});

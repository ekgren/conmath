import { Bit, bitName, isBit, negateBit } from "./bit-machine.js";

export const variable = (name) => Object.freeze({ kind: "variable", name });
export const negate = (value) => Object.freeze({ kind: "negate", value });

export const doubleNegationTheorem = Object.freeze({
  name: "bit.double-negation.v1",
  variable: "b",
  domain: Object.freeze([Bit.LOW, Bit.HIGH]),
  left: negate(negate(variable("b"))),
  right: variable("b")
});

export const doubleNegationProof = Object.freeze({
  kind: "cases",
  variable: "b",
  branches: Object.freeze({
    low: Object.freeze({ kind: "reflexivity" }),
    high: Object.freeze({ kind: "reflexivity" })
  })
});

function event(sequence, type, payload) {
  return Object.freeze({ sequence, type, ...payload });
}

function normalize(expression, environment, account) {
  if (expression.kind === "variable") {
    const value = environment[expression.name];
    if (!isBit(value)) throw new TypeError(`Unbound Bit variable: ${expression.name}`);
    return value;
  }
  if (expression.kind === "negate") {
    account.normalizationSteps += 1;
    return negateBit(normalize(expression.value, environment, account));
  }
  throw new TypeError(`Unknown expression: ${String(expression.kind)}`);
}

export function verifyByCases(theorem, proof, options = {}) {
  const runId = options.runId ?? "chapter-01-proof";
  const maximumProofNodes = options.maximumProofNodes ?? 3;
  const events = [];
  let sequence = 0;
  const account = { proofNodes: 1, normalizationSteps: 0, casesChecked: 0 };

  events.push(event(sequence++, "proof.check.started", {
    runId,
    theorem: theorem.name,
    limits: Object.freeze({ maximumProofNodes })
  }));

  if (proof.kind !== "cases" || proof.variable !== theorem.variable) {
    events.push(event(sequence, "kernel.rule.rejected", {
      runId,
      rule: "cases",
      reason: "proof does not eliminate the theorem variable"
    }));
    return Object.freeze({ accepted: false, events: Object.freeze(events), resources: Object.freeze(account) });
  }

  for (const value of theorem.domain) {
    const branchName = bitName(value);
    const branch = proof.branches[branchName];
    account.proofNodes += 1;

    if (account.proofNodes > maximumProofNodes) {
      events.push(event(sequence, "resource.exhausted", {
        runId,
        resource: "proofNodes",
        limit: maximumProofNodes
      }));
      return Object.freeze({ accepted: false, exhausted: true, events: Object.freeze(events), resources: Object.freeze(account) });
    }

    events.push(event(sequence++, "kernel.rule.entered", {
      runId,
      rule: "cases",
      case: branchName
    }));

    if (!branch || branch.kind !== "reflexivity") {
      events.push(event(sequence, "kernel.rule.rejected", {
        runId,
        rule: "reflexivity",
        case: branchName,
        reason: "missing reflexivity evidence"
      }));
      return Object.freeze({ accepted: false, events: Object.freeze(events), resources: Object.freeze(account) });
    }

    const environment = { [theorem.variable]: value };
    const left = normalize(theorem.left, environment, account);
    const right = normalize(theorem.right, environment, account);
    account.casesChecked += 1;

    if (left !== right) {
      events.push(event(sequence, "kernel.rule.rejected", {
        runId,
        rule: "reflexivity",
        case: branchName,
        normalized: Object.freeze({ left: bitName(left), right: bitName(right) })
      }));
      return Object.freeze({ accepted: false, events: Object.freeze(events), resources: Object.freeze(account) });
    }

    events.push(event(sequence++, "kernel.rule.accepted", {
      runId,
      rule: "reflexivity",
      case: branchName,
      normalized: bitName(left)
    }));
  }

  events.push(event(sequence, "proof.check.completed", {
    runId,
    theorem: theorem.name,
    outcome: "accepted",
    resources: Object.freeze({ ...account })
  }));

  return Object.freeze({
    accepted: true,
    events: Object.freeze(events),
    resources: Object.freeze({ ...account })
  });
}

export function verifyDoubleNegation(options = {}) {
  return verifyByCases(doubleNegationTheorem, doubleNegationProof, options);
}

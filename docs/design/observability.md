# Observability contract

Status: active draft 0.1

## Purpose

Make mathematical execution, proof checking, browser behavior, and build state
directly legible to readers and coding agents.

## Canonical events

Current event families:

```text
machine.run.started
machine.instruction
machine.state.changed
machine.faulted
machine.run.completed
proof.check.started
kernel.rule.entered
kernel.rule.accepted
kernel.rule.rejected
proof.check.completed
resource.exhausted
```

## Determinism

Canonical events contain ordered sequence numbers and stable run identifiers.
They contain no timestamps, randomness, DOM state, or browser-specific values.
The same input must produce deeply equal traces.

## Resource separation

- Logical: representation implied by the formal object
- Machine: explicit state words, program words, steps, proof nodes
- Host: JavaScript, DOM, browser, and operating-system overhead

The first two are part of Conmath claims. Host metrics may diagnose the site but
must not be presented as mathematical cost.

## Agent feedback loop

- `npm run check` emits concise local proof.
- Engine errors name the violated boundary.
- Browser trace export is structured JSON.
- UI warnings and errors are inspectable through browser developer logs.
- New recurring failure modes should become tests, lints, or documentation.

Harness inspiration:
https://openai.com/index/harness-engineering/

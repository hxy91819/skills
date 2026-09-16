---
name: diagnosing-bugs
description: Diagnose complex, intermittent, or performance bugs when the cause is unclear; not a default workflow for every simple fix.
---

# Diagnosing Bugs

Use evidence to narrow a hard bug. Adapt the investigation to the symptom rather than completing a fixed sequence. Read relevant `CONTEXT.md` and ADRs when they help interpret the affected code.

## Protect evidence

Redact secrets before showing commands, output, or captured artifacts. Keep credentials in the environment; quote only signal-bearing lines from traces that may contain auth headers. Use local fixtures or authorized environments, and obtain permission before production instrumentation or external mutations.

## Establish the symptom

Capture the exact wrong output, error, timing, or intermittent pattern. Seek a repeatable check that exercises the real call path and can distinguish this bug from setup failures. A focused test, fixture-driven CLI, isolated replay, or local browser check may fit. Minimise the scenario where that helps isolate the cause.

For intermittent failures, record attempts, failure frequency, seeds, timing, and relevant conditions; improve reproduction rate without pretending the result is deterministic. Keep stress runs bounded by the environment and task.

If automated reproduction is infeasible, report what was tried, the evidence gap, and the smallest safe repeatable check available. Ask for redacted artifacts or access only when needed. Lack of a running repro does not prohibit reading source and forming hypotheses; label them unverified and avoid claiming a confirmed cause or fix.

For human-driven reproduction, [scripts/hitl-loop.template.sh](scripts/hitl-loop.template.sh) is an optional structured capture template. Use it only when a human loop is needed, not as a mandatory fallback.

## Test hypotheses

Read the relevant code and evidence to propose falsifiable explanations. Use as many alternatives as the uncertainty warrants, not a fixed count. For each, name the predicted observation and a discriminating check. Share important assumptions and findings without blocking on a routine checkpoint.

Use a debugger or targeted instrumentation where helpful. Change one relevant variable at a time. Tag temporary logs so they can be removed; never log secrets or indiscriminately capture data.

For performance regressions, measure the baseline before changing code. Record workload, environment, timing distribution or profiler/query-plan evidence, then compare under the same conditions after the fix.

## Fix and verify

For an automatically reproducible bug, run a regression test before changing the implementation. Confirm it fails on the user's actual symptom, not test setup. Choose a test boundary that reaches the real bug pattern, including multiple callers when necessary. Apply the fix and rerun the same test and the original scenario.

If no suitable automated test is feasible, explicitly report the coverage gap and the alternative evidence. Do not replace a meaningful symptom assertion with a shallow test that merely passes.

Before declaring completion, remove temporary instrumentation and throwaway harnesses unless deliberately retained, report the observed outcome and remaining uncertainty, and explain the evidence for the cause. A missing test boundary may justify proposing architectural work, not starting it automatically.

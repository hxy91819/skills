## What it does

`diagnosing-bugs` narrows complex, intermittent, or performance failures through symptom evidence and testable hypotheses. It can read source and reason before a running reproduction exists, but unverified explanations remain labelled as such.

## When to reach for it

Type `/diagnosing-bugs`, or let it match a genuinely complex diagnostic task. Ordinary simple fixes and quick explanations should not enter this workflow automatically.

## Evidence before confidence

- For reproducible bugs, run a regression test that fails on the actual symptom before changing the implementation, then rerun it after the fix.
- For intermittent failures, report conditions and failure frequency rather than pretending one pass proves a fix.
- For performance regressions, establish a baseline workload and measurements, then compare like for like after the change.
- When automated reproduction is infeasible, report the gap and use the smallest safe repeatable check available.

Commands, logs, and captured traces must be redacted before sharing. Production instrumentation or external mutations require authorization. Temporary instrumentation is removed before completion.

## Common questions

**Why did it used to take over simple bug questions?**
The trigger covered almost anything broken or slow. It is now limited to hard diagnosis, and there is no required six-phase ceremony or fixed hypothesis count.

**Can it reason without a repro?**
Yes. Reading source can suggest falsifiable hypotheses and help construct a repro. That is not the same as claiming a confirmed cause or a verified fix.

**Does redaction happen automatically?**
It is a required handling rule, not a sanitizer. Review captured evidence before sharing it, especially outside the project.

## It's working if

- The failure being checked is your symptom, not test setup.
- You see before/after evidence or an explicit reproduction gap.
- Performance claims have a baseline, and secret values are absent from shared output.

## Where it fits

A standalone diagnostic capability. [implement](https://aihero.dev/skills-implement) keeps the regression-test loop for normal bug fixes; [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) may be proposed separately when test boundaries are the problem. For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).

# Engineering

Skills I use daily for code work.

## User-invoked

Explicit independent entry (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[ask-matt](./ask-matt/SKILL.md)**: Ask which skill or flow fits your situation. A router over the user-invoked skills in this repo.
- **[grill-with-docs](./grill-with-docs/SKILL.md)**: Grilling session that also builds your project's domain model, sharpening terminology and updating `CONTEXT.md` and ADRs inline.
- **[triage](./triage/SKILL.md)**: Move issues through a state machine of triage roles.
- **[improve-codebase-architecture](./improve-codebase-architecture/SKILL.md)**: Scan a codebase for deepening opportunities, present them as a visual HTML report, then grill through whichever one you pick.
- **[setup-matt-pocock-skills](./setup-matt-pocock-skills/SKILL.md)**: Configure this repo for the engineering skills (issue tracker, triage labels, domain doc layout). Run once per repo.
- **[to-spec](./to-spec/SKILL.md)**: Turn the current conversation into a spec and publish it to the issue tracker.
- **[to-tickets](./to-tickets/SKILL.md)**: Break any plan, spec, or conversation into a set of tracer-bullet tickets, each declaring its blocking edges, whether as text in a local file or as native blocking links on a real tracker.
- **[implement](./implement/SKILL.md)**: Build the requested work, verify reproducible bugs with a failing regression test before the fix, and apply two-axis review before committing.
- **[wayfinder](./wayfinder/SKILL.md)**: Plan a huge chunk of work (more than one agent session can hold) as a shared map of decision tickets on the issue tracker, resolved one at a time until the way to the destination is clear.
- **[codebase-design](./codebase-design/SKILL.md)**: Explicit design reference for interface depth, locality, and seams; consult only when a design choice needs it.
- **[code-review](./code-review/SKILL.md)**: Explicit Standards and Spec review of selected commits, branches, staged changes, or WIP, scaled to the task.
- **[wizard](./wizard/SKILL.md)**: Generate a human-run Bash wizard only on explicit request, scoped from non-secret configuration.

## Model-invoked

Model- or user-reachable (rich trigger phrasing so the model can reach for them).

- **[prototype](./prototype/SKILL.md)**: Build a requested local interactive logic demo or UI prototype, without automatic production changes or publication.
- **[diagnosing-bugs](./diagnosing-bugs/SKILL.md)**: Diagnose complex, intermittent, or performance bugs with symptom evidence, testable hypotheses, regression checks, and performance baselines.
- **[domain-modeling](./domain-modeling/SKILL.md)**: Maintain domain terminology, CONTEXT.md, and ADRs within an authorized model or documentation task.

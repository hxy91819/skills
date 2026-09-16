# Productivity

General workflow tools, not code-specific.

## User-invoked

Explicit independent entry (Claude Code: `disable-model-invocation: true`; Codex: `policy.allow_implicit_invocation: false` in `agents/openai.yaml`).

- **[grill-me](./grill-me/SKILL.md)**: Interview about a plan or design until the current task's decisions are clear, without writing files.
- **[handoff](./handoff/SKILL.md)**: Compact the current conversation into a handoff document so another agent can continue the work.
- **[teach](./teach/SKILL.md)**: Teach the user a new skill or concept over multiple sessions, using the current directory as a stateful teaching workspace.
- **[to-questionnaire](./to-questionnaire/SKILL.md)**: Turn a decision you can't answer alone into a Markdown questionnaire for the one person who can (filled in async, or together over a meeting).
- **[wait-what](./wait-what/SKILL.md)**: Fire this the moment a message doesn't land. The agent re-pitches it with the context you're missing, in plain English, using your `CONTEXT.md` vocabulary.
- **[grilling](./grilling/SKILL.md)**: Explicit rounds of questions until the current task has enough decisions; also read as reference by started interview flows.
- **[writing-for-agents](./writing-for-agents/SKILL.md)**: Explicit writing reference for scoped instructions and conditional disclosure, not a prerequisite to every edit.

## Model-invoked

None currently.

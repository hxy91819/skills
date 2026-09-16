# Model-invoked vs user-invoked

Every `SKILL.md` in this repo has an explicit invocation policy:

- **User-invoked**: independently started by the user. Set `disable-model-invocation: true`, `triggers: [user]` for Devin, and `policy.allow_implicit_invocation: false` in `agents/openai.yaml`. The description is a concise human-facing summary.
- **Model-invoked**: model- or user-reachable for a matching task. Omit the disabling fields and use a precise model-facing description. Preserve existing policies unless the task requires changing them.

Every skill carries `agents/openai.yaml` with `interface.display_name` and `interface.short_description`, plus the disabling policy for user-invoked entries. Keep frontmatter, Codex metadata, README grouping, and docs consistent. These are configuration contracts for supporting hosts, not a guarantee of identical discovery or enforcement across hosts.

## Dependencies and reference reading

Use the host's skill tool for an available model-invoked capability, one skill per call. An explicit-only entry is not an automatic tool dependency. Instead, an already-started workflow may link and read its relevant instructions as reference within the current scope. Name the purpose and condition at the link; do not start an independent workflow or add a confirmation gate to every step.

Shared references can remain with the skill that owns them. A relative link is sufficient for reference consumption; reading a file does not grant permission to implement, publish, or write elsewhere. Router recommendations remain human-facing choices.

## Passive vs active domain work

Reading `CONTEXT.md` or explaining a term is not permission to maintain domain documents. Select `domain-modeling` only within an authorized domain-model or documentation maintenance task.

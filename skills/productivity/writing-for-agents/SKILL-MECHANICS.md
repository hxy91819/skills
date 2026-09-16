# Skill mechanics

Consult this branch of [writing-for-agents](SKILL.md) when changing discovery policy or routing, not for every skill edit.

## Invocation and reading are different

- **Model-invoked** skills permit automatic selection for a precise task match. Keep the description short and discriminating.
- **User-invoked** skills require explicit selection for their independent workflow. In this repo, pair `disable-model-invocation: true` with `policy.allow_implicit_invocation: false` in `agents/openai.yaml`, and `triggers: [user]` for Devin.

These fields express policy to supporting hosts. Hosts differ in listing, context injection, tools, and enforcement; do not promise that a description is always loaded, always hidden, or that every host prevents the same calls.

Disabling automatic selection does not make the files unreadable. An already-started workflow can explicitly link relevant reference instructions without invoking a new independent workflow or asking the user to restart each step. Such a pointer must name the condition, purpose, and scope. Reading reference material never expands authorization.

## Dependencies and routers

For an automatic capability, use the host's skill tool where available. For explicit-only reference material, use a relative link to the needed file and read it within the caller's scope. Do not require a tool invocation the host may reject.

Split a new entry only when it needs independent discovery or human selection. Shared references may stay with their owner and be linked by callers; they do not need a new automatic skill.

A router maps user needs to available entries and invocation modes. Update its map, README grouping, metadata, and human docs together. It recommends independent workflows rather than silently starting them.

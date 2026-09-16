---
name: writing-for-agents
description: Reference for scoped agent instructions and conditional disclosure, consulted explicitly when needed.
disable-model-invocation: true
triggers:
  - user
---

# Writing for Agents

A writing reference, not a workflow to run on every document edit. Keep instructions that change decisions: local conventions, runtime contracts, scope, and stopping conditions. Leave basic teaching to the model's existing capabilities.

## Context pointers

A **context pointer** names material and the condition for reading it. Link a reference where the relevant branch needs it, rather than requiring every caller to read every guide. Keep enough purpose and constraints at the entrypoint that each branch is usable on its own.

## Information hierarchy

Keep shared constraints inline. Put substantial branch-specific detail in a linked reference; co-locate a concept's rules and caveats. A short, single-purpose document needs no extra reference layer. Check links and update callers when moving material.

## Completion and scope

Describe an observable completion condition proportional to the task. Preserve authorization boundaries and distinguish a decision from permission to implement or publish it. Do not turn a narrow edit into an interview, exhaustive audit, or parallel workflow by default.

## Pruning

Use one source of truth per rule. Prefer real project terminology over mandatory invented vocabulary. Remove repeated explanations and facts cheaply discoverable from the environment; preserve non-obvious reasons and operational constraints.

When changing skill discovery, invocation policy, or a router, consult [SKILL-MECHANICS.md](SKILL-MECHANICS.md). Ordinary prose edits do not need it.

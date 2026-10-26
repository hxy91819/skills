---
name: to-spec
description: "Turn the current conversation into a spec and publish it to the project issue tracker: no interview, just synthesis of what you've already discussed."
disable-model-invocation: true
triggers:
  - user
---

This skill takes the current conversation context and codebase understanding and produces a spec. Do NOT interview the user; just synthesize what you already know.

The issue tracker and triage label vocabulary should have been provided to you. If not, tell the user to run `/setup-matt-pocock-skills`.

Read `docs/agents/issue-tracker.md` for the configured tracker contract before any tracker operation.

## Process

1. Explore the repo to understand the current state of the codebase, if you haven't already. Use the project's domain glossary vocabulary throughout the spec, and respect any ADRs in the area you're touching.

2. Sketch out the test boundaries at which you're going to test the feature. Existing test boundaries should be preferred to new ones, and the fewer across the codebase the better - the ideal number is one. For each story, choose the boundary by its regression risk, below. If a new test boundary is needed, propose one at the layer that catches the risk.

Choose each story's boundary by its regression risk: ask who notices first when the story regresses, what is lost, and which layer catches it earliest and most stably. Take the highest boundary that catches that risk, but not higher than the risk needs. A story that changes a persisted side effect or an external contract usually takes an **API** test. Within a UI flow, only a few critical paths earn a **browser end-to-end** test: one main path and one denial path; the rest of the UI change can sit at a lower boundary or `none`. A story of pure internal logic takes whatever lower boundary the repo already tests at (unit, service or integration), named as the repo names it. Use `none` only with a stated reason. Unit tests stay the implementer's call unless the row declares a `unit` boundary.

Check with the user that these test boundaries and the risk each one catches match their expectations.

3. Write the spec using the template below, then publish it using only the commands and conventions in `docs/agents/issue-tracker.md`. Apply the `ready-for-agent` triage label through that same contract - no need for additional triage.

Keep the bar where the user set it. Audit trails, evidence chains, reconciliation, replay protection, extra approval steps and similar verification requirements go into the spec only when the user asked for them; when you include one, quote the user's words beside it. Every story, decision and test row downstream is built and checked to what the spec says, so a requirement added here costs the whole chain.

<spec-template>

## Problem Statement

The problem that the user is facing, from the user's perspective.

## Solution

The solution to the problem, from the user's perspective.

## User Stories

A numbered list of user stories covering the behaviour the user asked for. Each user story should be in the format of:

1. As an <actor>, I want a <feature>, so that <benefit>

<user-story-example>
1. As a mobile bank customer, I want to see balance on my accounts, so that I can make better informed decisions about my spending
</user-story-example>

Cover the core paths the user described, written so the first version runs and its result can be observed. Don't pad the list with edge cases, hardening or failure handling nobody raised; those become stories when the user asks for them or a real run shows they matter.

## Implementation Decisions

A list of implementation decisions that were made. This can include:

- The modules that will be built/modified
- The interfaces of those modules that will be modified
- Technical clarifications from the developer
- Architectural decisions
- Schema changes
- API contracts
- Specific interactions

Do NOT include specific file paths or code snippets. They may end up being outdated very quickly.

Exception: if a prototype produced a snippet that encodes a decision more precisely than prose can (state machine, reducer, schema, type shape), inline it within the relevant decision and note briefly that it came from a prototype. Trim to the decision-rich parts, not a working demo, just the important bits.

## Testing Decisions

A list of testing decisions that were made. Include:

- A description of what makes a good test (only test external behavior, not implementation details)
- Prior art for the tests (i.e. similar types of tests in the codebase)
- The regression contract: one row per user story, including the boundary, the risk it guards and what proves it. `/to-tickets`, `/implement` and `/code-review` read this table, so a story missing from it carries no test obligation.

| Story | Boundary | Risk | Proven by |
| --- | --- | --- | --- |
| 1 | browser e2e | checkout breaks on the main path | the suite or scenario, by name, not path |
| 2 | api | a rejected request leaves a partial record | ... |
| 3 | unit | fee rounding drifts | ... |
| 4 | none: reason | ... | |

`Boundary` is chosen by the story's regression risk: ask who notices first when it regresses, what is lost, and which layer catches it earliest and most stably, then take the highest boundary that catches the risk without going higher than it needs. Use `browser e2e`, `api`, a lower boundary the repo already tests at (unit, service or integration, named as the repo names it), or `none` with a reason. `Risk` is one sentence naming the regression the row exists to catch. Name a lower boundary when that layer is what catches the risk.

## Out of Scope

A description of the things that are out of scope for this spec.

## Further Notes

Any further notes about the feature.

</spec-template>

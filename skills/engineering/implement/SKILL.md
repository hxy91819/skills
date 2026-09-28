---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
triggers:
  - user
---

Implement the work described by the user in the spec or tickets.

Use /tdd where possible, at pre-agreed test boundaries.

The spec's Testing Decisions table (or the ticket's test criteria) is the completion list: a story is done when the test at its declared boundary exists and passes. Never substitute a lower boundary for a `browser e2e` or `api` row. Unit tests are yours to add or skip.

When an existing browser e2e or API test fails because of your change, decide whether the test or the code is wrong, then say which you changed and why in the commit message. That line is how the reviewer and the next agent tell a fixed regression from a silenced one.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

The work is done when every row of the completion list passes, the full suite passes, and CI passes where the repo has it. Validation the spec doesn't ask for (real-environment runs, extra gates, other tickets' acceptance) is out of scope: mention it in one line as out of scope, never report it as remaining or blocking.

Commit your work to the current branch, then review it.

## Review

Pick the tier from the change's risk. File count, test count and ticket length don't raise it; when torn between two tiers, take the lower.

| Tier | When | Review |
| --- | --- | --- |
| Skip | Only docs, config or tests changed; a CI or flaky-test fix; a small fix inside one module that touches no schema, migration, permission or credential | None. Tests and CI are the gate. |
| Self | Ordinary feature work inside one module | Reread the diff yourself against the spec lines and the completion list. No sub-agents. |
| Full | Cross-module change; schema or migration; permissions or credentials; a core state machine | Run /code-review against the commit you branched from. |

Review once. After fixing findings, rerun the affected tests and don't review again.

Fix only blocking findings in this change: a spec requirement missing or wrong, with the spec line quoted; a declared test missing or below its boundary; an existing browser e2e or API test weakened; a hard violation of a documented repo standard. List everything else (smells, suggestions, anything without a spec line) in the commit or MR description instead of fixing it.

Review doesn't hold up delivery. Push and open the MR as you normally would and let review run alongside CI. If a review axis can't run for provider reasons, say so and deliver without it.

## Deliver

Deliver the way the repo's `AGENTS.md` says (a merge request, a direct push, or whatever it documents), using the tools and skills the repo provides for its code host. When a tool, credential or entry point you need is missing, report the work as blocked and name exactly what is missing; don't improvise a different route.

When the spec relies on a capability that doesn't exist yet, report that as blocked too. Don't design a new subsystem to stand in for it; that is a new decision for the user, not part of this ticket.

Once the change has landed (merged, or pushed where the repo pushes directly), leave a one-line result on the ticket and close it, so tickets blocked by it become visibly ready.

## Report

Open the final report with three lines: the outcome, what the user needs to decide (or "nothing"), and the next step. Use plain words and the project's own terms, not shorthand you coined during the run. Details (changed files, tests, links) follow; keep the whole report short, roughly 400 words at most.

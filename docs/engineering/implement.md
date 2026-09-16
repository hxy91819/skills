## What it does

`implement` builds the work described by a spec or tickets. For automatically reproducible bugs it runs a regression test before the implementation change and confirms the test fails because of the reported symptom, then reruns the same test after the fix.

## When to reach for it

Invoke `/implement` explicitly when the requested work is ready to build. Use [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) for complex diagnostic uncertainty, not as a prerequisite to every fix.

## A bug-fix evidence loop

The test must reach the real symptom; a setup failure or a test that merely passes gives no evidence. If automated reproduction is infeasible, the result reports the coverage gap and the smallest safe repeatable check available.

The flow runs relevant checks during implementation and the full suite at the end, reads [code-review](https://aihero.dev/skills-code-review) to assess Standards and Spec over the task's changes including WIP, then commits to the current branch within the user's Git instructions. Reading the review reference is part of this started flow, not a new confirmation gate.

## Common questions

**Do I need to install a separate test-first skill?**
No. The regression requirement is part of `implement` itself. Testing still follows the task's agreed behaviour and the repository's conventions.

**What if the bug cannot be reproduced automatically?**
The report must say so, explain the evidence gap, and identify what was checked instead. A shallow passing test is not a substitute.

**Does the review always launch two agents?**
No. The two axes stay separate, but small reviews can run directly.

## It's working if

- A reproducible bug has an observed failing symptom test before the fix and a passing rerun after it.
- Unreproduced claims and test gaps are explicit.
- The final review includes this task's uncommitted changes, not only HEAD.

## Where it fits

A build step downstream of [to-spec](https://aihero.dev/skills-to-spec) and [to-tickets](https://aihero.dev/skills-to-tickets), with [code-review](https://aihero.dev/skills-code-review) as its closing reference. For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).

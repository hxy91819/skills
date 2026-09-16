---
name: implement
description: "Implement a piece of work based on a spec or set of tickets."
disable-model-invocation: true
triggers:
  - user
---

Implement the work described by the user in the spec or tickets.

For bug fixes that can be reproduced in an automated test, run a regression test before changing the implementation and confirm it fails because of the reported bug, not test setup. Apply the fix and rerun the same test. If automated reproduction is not feasible, report the coverage gap and use the smallest safe, repeatable check available.

Run typechecking regularly, single test files regularly, and the full test suite once at the end.

Once done, read [code-review](../code-review/SKILL.md) and apply its Standards and Spec review to this task's changes, including uncommitted work. This is part of the already-started implementation, not a new skill invocation or another confirmation gate.

Commit your work to the current branch.

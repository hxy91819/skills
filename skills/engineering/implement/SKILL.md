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

Once done, use /code-review to review the work.

Commit your work to the current branch.

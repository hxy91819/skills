---
"mattpocock-skills": patch
---

Choose each story's test boundary by its regression risk instead of fixing two. The Testing Decisions table gains a `Risk` column and each row names the boundary that catches that risk: `browser e2e`, `api`, an existing lower boundary, or `none` with a reason. `to-tickets`, `implement` and `code-review` read the declared boundary from the row, and derive rows by the same risk rule when no spec table exists.

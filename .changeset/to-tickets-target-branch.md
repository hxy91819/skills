---
"mattpocock-skills": patch
---

`to-tickets` defines a blocking edge as "start once the blocker has merged to the target branch": the trunk, or the spec's integration branch when `implement-spec` runs the tickets. This removes the clash with `implement-spec`, which merges every ticket onto one integration branch.

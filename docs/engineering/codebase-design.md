## What it does

`codebase-design` is a design reference for **depth**, **locality**, and **seams**. Reading it does not start a design session, codebase scan, refactor, or delegation.

## When to reach for it

Invoke `/codebase-design` explicitly, or read the relevant reference from a design task already underway. It no longer selects itself automatically for every interface discussion.

## Design choices, not vocabulary policing

Depth is useful behaviour behind a small interface; locality is related changes and verification concentrated in one place. A seam makes real variation or testing possible. These are lenses for evaluating a design, not reasons to rename an existing service, component, API, or boundary.

Read only the branch the decision needs:

- Deepening a chosen cluster: dependency categories and test boundaries.
- Comparing alternative interfaces: constraints, caller examples, and trade-offs. Parallel designs are optional and have no minimum reviewer count.

## Common questions

**Why did reading a reference used to start a long design process?**
The old alternative-design branch prescribed parallel work. It now explicitly stays within the chosen design question and stops at the decision unless implementation is authorized.

**Do all callers have to use these exact words?**
No. Existing domain and code names take priority. The terms should clarify a real choice, not impose a new vocabulary.

## It's working if

- The comparison explains what callers gain and what complexity remains.
- Reading the reference does not create an unexpected refactoring task.
- Only the relevant design branch is consulted.

## Where it fits

An explicit reference beneath [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture), which finds candidates, and alongside [domain-modeling](https://aihero.dev/skills-domain-modeling), which maintains authorized domain documentation. For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).

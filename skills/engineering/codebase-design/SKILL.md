---
name: codebase-design
description: Reference for deep-module design and interface trade-offs, consulted explicitly when needed.
disable-model-invocation: true
triggers:
  - user
---

# Codebase Design

A design reference, not a session driver. Read the relevant guidance when a task needs interface design; reading it does not start exploration, refactoring, or delegation. Keep the project's actual domain and code names, including service, component, API, or boundary where those are the right terms.

## Design preferences

- **Depth** means useful behaviour behind a small interface, not a ratio of code lines. Include invariants, ordering, errors, configuration, and performance in the interface cost a caller pays.
- **Locality** means related changes and verification concentrate in one place. Use the deletion test: would removing this abstraction remove complexity, or scatter it across callers?
- A **seam** is a point where behaviour can be replaced without editing its caller; an **adapter** fills that role. Introduce one for a real variation or testing need, not a hypothetical future use.
- Test observable behaviour at an appropriate interface. Internal seams can support focused tests without becoming part of the public API.

## Read only the relevant branch

- Deepening a chosen cluster with dependencies: [DEEPENING.md](DEEPENING.md).
- Comparing genuinely different interfaces for an unresolved design choice: [DESIGN-IT-TWICE.md](DESIGN-IT-TWICE.md).

Neither branch authorizes implementation or expands the current task.

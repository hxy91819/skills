# Design It Twice

Use this reference when alternative interfaces would resolve a real design uncertainty, not for every module change. See [SKILL.md](SKILL.md) for depth and locality and [DEEPENING.md](DEEPENING.md) for dependency trade-offs.

State the chosen problem, constraints, and caller needs. Compare a small number of meaningfully different designs, such as a minimal interface and one optimised for the common caller. For each, show the interface (including invariants and errors), a usage example, the hidden complexity, and the dependency strategy.

Work directly for small decisions. Independent parallel designs are optional when the task merits them and delegation is permitted; there is no minimum agent count. Give each delegate a bounded design question and require it to work directly, without further delegation.

Compare depth, locality, seam placement, and migration cost. Recommend a design with its trade-offs. Stop at the design decision unless implementation is already authorized.

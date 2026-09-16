---
name: grilling
description: Explicit interview to stress-test a plan, decision, or idea.
disable-model-invocation: true
triggers:
  - user
---

Interview until the decisions needed for the current task are sufficiently clear. Use a **design tree** to track dependencies, not as a requirement to explore every possible branch. An already-started interview workflow can read this reference and continue without another invocation or per-round permission gate.

Work the tree in **rounds**. The **frontier** is every decision whose prerequisites are already settled: the questions you can ask _now_ without guessing at answers you haven't heard yet. Ask the relevant, manageable part of the frontier in one round: number each question and give your recommended answer. Then wait for the user's answers before the next round.

Format a round like so:

```
❓ **Q1** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>

---

❓ **Q2** - **<question title>**: <question body, might be multiple paragraphs, including multiple choices>

➡️ <your recommended answer>
```

Each round the user answers reshapes the tree: settled decisions push the frontier outward and unblock questions that depended on them. Recompute the frontier and ask the next round. A question whose answer depends on another question still open in this round belongs to a _later_ round, not this one.

Look up available facts directly using permitted tools; delegation is optional when it would materially help and is allowed. Ask the user for inaccessible facts or decisions that require their judgement. Distinguish unknown facts from unsettled choices, and continue with independent questions where possible.

Stop when the current task's decisions are sufficient to proceed. Summarise settled choices, material assumptions, and any deferred questions. Do not exhaust unrelated branches. Continue within the already-authorized workflow; obtain approval only for genuinely new scope or unresolved decisions, not for each transition.

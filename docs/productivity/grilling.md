## What it does

`grilling` stress-tests a plan with numbered questions and recommended answers in rounds. It stops when the current task has enough decisions, not when every imaginable design branch has been visited.

## When to reach for it

Invoke `/grilling` explicitly for an interview. [grill-me](https://aihero.dev/skills-grill-me) and [grill-with-docs](https://aihero.dev/skills-grill-with-docs) also read it as reference inside their user-started flows, without asking you to invoke it again.

## Rounds and the frontier

The **frontier** contains questions whose prerequisites are settled. A round takes a manageable, relevant part of it; dependent questions wait for the answers they need. Each question has a recommendation, and you own the decisions.

Available facts are looked up directly. Delegation is optional when useful and permitted, not mandatory for a filesystem lookup. Inaccessible facts and material assumptions are made visible.

## Common questions

**How long should it run?**
Until you have the decisions required for the current task. State your time or scope limit. Unrelated branches can be deferred; a long session is not proof of a good one.

**Does it start building when questions run out?**
Only if building was already authorized. It summarises choices and unresolved gaps, then stays within the started workflow. A new objective requires approval, not a ritual confirmation at every step.

**Can I ask for one question at a time?**
Yes. The numbered format supports rounds, but your preferred pace takes priority.

## It's working if

- Questions have clear recommendations and do not depend on unanswered questions in the same round.
- The interview stops once the current decision is actionable.
- Facts are checked rather than delegated mechanically or guessed.

## Where it fits

An explicit interview mode and shared reference used by the planning flows, including [wayfinder](https://aihero.dev/skills-wayfinder). For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).

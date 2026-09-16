## What it does

`domain-modeling` builds and sharpens a project's **ubiquitous language** while you are designing: challenging a term that conflicts with the glossary, forcing a precise word where you used a vague one, and stress-testing a relationship with a concrete scenario until the boundaries are exact.

It is the **active** discipline, not the passive one. Reading `CONTEXT.md` to borrow its vocabulary is a one-line habit any skill can do; this skill is for when you are *changing* the model. That is what makes it interrupt. It writes a resolved term into `CONTEXT.md` at the moment it is resolved, in the middle of the conversation, rather than producing a tidy glossary at the end, because the batched version is a summary of a [session](https://www.aihero.dev/ai-coding-dictionary/session), and the inline version is the session's actual output.

It writes only within an authorized domain-model or documentation maintenance task. A terminology explanation alone stays a conversation, not a file edit.

## When to reach for it

Type `/domain-modeling`, or let it match an already-authorized model or documentation maintenance task. It is not triggered just because someone asks what a term means.

| The situation | The move |
| --- | --- |
| You asked to clarify and maintain conflicting glossary terms | Resolve the term and update the authorized glossary |
| You asked to record a durable architectural decision | Offer an ADR if it clears the three tests below |
| You only want a term explained | Read the glossary or code; do not write files |
| The module's shape is the question | Consult [codebase-design](https://aihero.dev/skills-codebase-design) as reference |
| You want an interview plus maintained documents | [grill-with-docs](https://aihero.dev/skills-grill-with-docs) |

## Prerequisites

An authorized workspace for domain documents is required. Existing files are not a prerequisite; within that scope, the skill writes into two places and creates both lazily:

- **`CONTEXT.md`** at the repo root, created by the first resolved term. In a repo with a `CONTEXT-MAP.md` at the root, terms go into the per-context `CONTEXT.md` the map points at instead.
- **`docs/adr/`**, created by the first ADR that clears the bar.

Nothing needs to exist before you start, and nothing is created speculatively.

## Two artifacts, two bars

The glossary and the ADR are held to different standards, and conflating them is where most of the trouble in this skill comes from.

| | `CONTEXT.md` | `docs/adr/NNNN-slug.md` |
| --- | --- | --- |
| Holds | Terms. What a thing **is**, in one or two sentences, with rejected synonyms under `_Avoid_` | One decision, in one to three sentences: context, choice, reason |
| Bar to write | A vague term became canonical | **All three**: hard to reverse, surprising without context, the result of a real trade-off |
| Written | Inline, the moment the term is settled | Offered, not assumed |
| Never holds | Implementation details, a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), a scratch pad, general programming concepts | A diary of every choice made this session |

Miss any one of the ADR's three tests and there is no ADR. An easily-reversed decision will just get reversed; an unsurprising one is nobody's question; one with no real alternative records that you did the obvious thing.

The `CONTEXT.md` rule is the one to actually hold onto, because it is the one that breaks in the field. **It is a glossary and nothing else.** Left unchecked, models treat "write to `CONTEXT.md`" as permission to persist every answer you give, and the file turns into a running spec. This is the most-reported problem with the skill, across several models.

## Cross-referencing, and where it stops

The move that makes the skill click: when you state how something works, it checks the code and surfaces the contradiction. *"Your code cancels entire Orders, but you just said partial cancellation is possible, which is right?"* The language and the code are made to agree, out loud, before either is changed.

The limit is worth knowing. It cross-references **code** and the committed `CONTEXT.md`/ADRs, and nothing else. It does not search your issue tracker, so a naming collision that was argued out and deliberately settled in a closed issue months ago gets surfaced as if it were new. There is [an open request](https://github.com/mattpocock/skills/issues/717) to fix this; until then, the workaround is to put the instruction in your own `docs/agents/domain.md`, which the skills already read.

## Common questions

**My `CONTEXT.md` is 500 lines. 1,000. 3,000. What do I do?**
The size is a symptom, not the disease: the file has absorbed implementation detail and decisions that were never glossary material. The fix is a direct instruction: `/grill-with-docs make my CONTEXT.md more concise and remove any implementation details from it`. Run it against a bloated file and most of it goes. Only reach for a `CONTEXT-MAP.md` split once the file is genuinely lean and still covers two domains that a reader would not want to hold at once; splitting a bloated file just gives you several bloated files. The skill's guidance here is not yet strong enough to prevent the growth in the first place, and the issue tracking that is still open.

**Why is it `CONTEXT.md` and not `GLOSSARY.md`?**
This is the most-argued naming question in the whole skill set and it has no settled answer. The case against the current name is good: if it is "a glossary and nothing else", `GLOSSARY.md` says so, and, as one reader put it, "with ai agents everything is [context](https://www.aihero.dev/ai-coding-dictionary/context)". The case for it is the map: `CONTEXT-MAP.md` pointing at several `CONTEXT.md` files reads naturally in a way `GLOSSARY-MAP.md` does not, and `context` is the standing DDD word for a bounded area of the model. At least one person maintains a local fork purely to rename the file. You can do the same, but every other skill in the set looks for `CONTEXT.md`, so a rename means patching all of them.

**Where did `/ubiquitous-language` go?**
It was removed, and it was not deprecated. Its job moved into `domain-modeling`, which maintains the whole model continuously rather than dumping a glossary out of one conversation. It can be used within document-maintaining flows; discussion or triage alone is not permission to write a glossary.

**How do I get a glossary for a codebase that has none?**
Ask for it explicitly rather than waiting for it to accumulate. `/grill-with-docs help me scaffold my existing repo with a CONTEXT.md` is the documented route; expect a long interrogation: one user reported 50+ questions before the file was in shape. Incidental use builds the glossary far too slowly on a brownfield repo.

**Can I keep the domain model and use my own ADR format?**
Not cleanly today. The glossary half and the ADR half ship in one skill, so a team with an established ADR convention (different template, different location, different naming) gets instructions that conflict with its house style. The current options are to copy the skill locally and edit it, or to override the ADR conventions in your repo's own agent docs. Splitting the two apart is [an open request](https://github.com/mattpocock/skills/issues/557).

**Does a glossary actually earn its keep? It is one more artifact to review, and it can go stale.**
Sometimes it does not, and it is worth being honest about where. DDD gets less useful the closer it gets to the implementation: the payoff is upstream, in naming and concept alignment, not in aggregates and layer ceremony. Synonym control matters at naming boundaries: module names, table names, status enums, issue titles, CLI commands. It matters much less in ordinary prose. There is also a live objection that domain terms compress communication *between humans* who already share them, and that an agent responds the same way to the plain-English description. On that reading, the glossary's value is keeping you and your reviewers aligned with what the agent is doing, not making the agent better. On a one-day build, skip it. And an unreviewed, agent-authored glossary is worse than none: it becomes confident-sounding lore that later sessions treat as truth.

**Can it turn my vague prompts into domain language for me?**
No, and there is no plan for a skill that does. A domain language you do not understand yourself becomes meaningless drivel once written down. This skill enforces precision once you have the understanding; it does not manufacture vocabulary you do not have. The related trap is using domain words without doing the modelling: right nouns over the wrong conceptual structure produce output that reads correct and is not.

## It's working if

- It stops you mid-sentence to ask which of two things you meant, instead of picking one and moving on.
- `CONTEXT.md` changes **during** the conversation, not in a burst at the end.
- It refuses to write an ADR for something you could undo tomorrow, and says which of the three tests failed.
- New entries define what a thing *is* in one or two sentences and name the words you are giving up under `_Avoid_`.
- It quotes your code back at you when your code and your sentence disagree.
- `CONTEXT.md` gets shorter as often as it gets longer.

## Where it fits

`domain-modeling` is a model-invoked capability within authorized domain maintenance. [grill-with-docs](https://aihero.dev/skills-grill-with-docs) includes that scope. Other flows such as [wayfinder](https://aihero.dev/skills-wayfinder) and [triage](https://aihero.dev/skills-triage) use it only when document maintenance is included. [codebase-design](https://aihero.dev/skills-codebase-design) is instead an explicit design reference, not a vocabulary mandate. [ask-matt](https://aihero.dev/skills-ask-matt) maps the available flows.

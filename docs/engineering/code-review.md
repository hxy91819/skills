## What it does

`code-review` reviews the diff between `HEAD` and a fixed point you name (a commit, a branch, a tag, `main`, `HEAD~5`) along three axes. **Standards** asks whether the code follows how this repo writes code. **Spec** asks whether the code does what the originating issue or [spec](https://www.aihero.dev/ai-coding-dictionary/spec) asked for. **Tests** asks whether every row of the spec's regression contract (the Testing Decisions table) has a test at the boundary it declared, and whether the diff touched existing browser e2e or API tests. Each axis runs in its own [sub-agent](https://www.aihero.dev/ai-coding-dictionary/subagent), dispatched through BB (Spec at medium difficulty, Standards and Tests at simple), so none sees another's reasoning. It runs once per change, marks each finding blocking or non-blocking, and treats anything it can't tie to a spec line or a documented standard as a suggestion rather than a gap.

The skill never merges or re-ranks the axes. The report ends with a worst issue *per axis* and declines to name a single winner across them. A change can pass one axis and fail the other. Code that follows every convention but implements the wrong thing passes Standards and fails Spec. Code that does exactly what the [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket) asked but breaks the repo's conventions does the reverse. Code that does the right thing with a pile of unit tests and nothing that would catch the feature regressing passes Spec and fails Tests. A blended verdict lets the passing axis hide the failing one.

## When to reach for it

Type `/code-review`, or the agent reaches for it automatically when you ask to review a branch, a PR, work in progress, or anything "since X".

| Your situation | Reach for |
| --- | --- |
| A diff exists and you want to know if it is built right *and* is the right thing | `code-review` |
| You want bugs hunted in the diff: null paths, races, off-by-one | Claude Code's own built-in review, not this one (see the name clash below) |
| Nothing is written yet and you want it written test-first | [tdd](https://aihero.dev/skills-tdd) |
| A whole spec needs building, review included | [implement](https://aihero.dev/skills-implement), which calls this skill itself |
| The whole codebase has drifted, not one diff | [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) |
| Something is broken and you do not know why | [diagnosing-bugs](https://aihero.dev/skills-diagnosing-bugs) |

You must supply the fixed point. If you do not, the skill asks for one rather than guessing. Before it spawns anything, it checks that the ref resolves and that the diff is not empty, so a mistyped branch name fails in front of you instead of inside two sub-agents.

## Prerequisites

BB and the `bb-model-routing` skill must be available to dispatch the review agents. Spec uses the configured medium difficulty route; Standards and Tests use simple.

The Standards axis needs nothing. It reads whatever the repo documents (`CODING_STANDARDS.md`, `CONTRIBUTING.md`, and the like) and falls back on a built-in baseline when the repo documents nothing.

The Spec axis needs a spec to exist and be findable. It looks in this order:

1. Issue references in the commit messages (`#123`, `Closes #45`, a GitLab `!67`), fetched through the tracker doc.
2. A path you pass in as an argument.
3. A spec file under `docs/`, `specs/`, or `.scratch/` matching the branch or feature name.
4. Asking you.

Step 1 depends on the tracker doc, which [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) writes. Without it the axis still works if you hand it a path. With no spec at all, the skill skips the Spec sub-agent and the report says "no spec available" rather than inventing requirements.

The Tests axis reads the spec's Testing Decisions table, or the tickets' test criteria. With neither, it derives one row per story by the same rule the spec would have used (browser e2e for a story that changes what a user sees or does, api for one that changes a request, response, or persisted side effect) and says it did so.

## The three axes

| | Standards | Spec | Tests |
| --- | --- | --- | --- |
| Question | Is it built right? | Is it the right thing? | Would it be caught if it regressed? |
| Reads | The repo's documented standards, plus the smell baseline | The originating issue or spec | The spec's Testing Decisions table |
| Reports | Documented breaches (can be hard), and smells (always judgement calls) | Missing or partial requirements, scope creep, requirements implemented wrongly | Rows with no test, rows delivered below their declared boundary, tests that don't assert the story, existing e2e or API tests weakened or removed without a spec line asking for it |
| Every finding cites | The standards file and the rule, or the named smell plus the hunk | The line of the spec | The row of the table, plus the hunk |

This design exists to avoid a generic review skill that does not know your standards. Such a skill flags what is deliberate in your codebase and misses the invariants your codebase depends on. So the repo's own documentation is the [primary source](https://www.aihero.dev/ai-coding-dictionary/primary-source) on the Standards axis, and **the repo always overrides**.

The **smell baseline** sits under the repo's standards. It is twelve code smells from chapter 3 of Fowler's _Refactoring_: Mysterious Name, Duplicated Code, Feature Envy, Data Clumps, Primitive Obsession, Repeated Switches, Shotgun Surgery, Divergent Change, Speculative Generality, Message Chains, Middle Man, Refused Bequest. Each is a labelled heuristic ("possible Feature Envy"), never a hard violation. Each states what the smell is and how to fix it, so a finding comes with a fix attached rather than only a complaint. Both axes skip anything your linter already enforces.

## Common questions

**It collides with Claude Code's own `/code-review`. What do I do?**

This is the most reported problem with the skill, and it is not fixed. Claude Code ships its own `/code-review`, which does something different: it hunts bugs in the diff, where this one checks spec compliance and repo standards. When you install this library, one of them wins, and which one depends on how you installed:

- **Plugin marketplace.** Every skill gets a `mattpocock-skills:` prefix, and the built-in becomes hard to reach at the unqualified name.
- **Plain skills install.** The local file wins, and this skill shadows the built-in.

One answer is to remove Claude Code's built-in skills entirely. That saves a lot of [context](https://www.aihero.dev/ai-coding-dictionary/context), and the collision stops mattering. The shadowing itself is arguably a Claude Code [harness](https://www.aihero.dev/ai-coding-dictionary/harness) bug (a skill author should be free to name a skill anything), so the other answer is to rename the local copy. `npx skills update` undoes an edit to the frontmatter or a renamed directory. The durable workaround users report is to fork the skill to a new name and drop `code-review` from the managed set. Keep a note of the commit you forked from so you can re-sync by hand.

**Can a review agent start another review agent?**

No. The coordinating agent dispatches one BB thread per available axis. Each review task tells its agent to complete that axis directly and return a report without invoking `code-review`, using `bb-model-routing`, or creating another agent. The skill also states this boundary for agents that load it while already assigned an axis. Earlier prompts omitted the boundary, allowing a review agent to mistake the coordinator's dispatch step for its own work.

**Should I run it in the same [session](https://www.aihero.dev/ai-coding-dictionary/session) that wrote the code?**

Prefer a fresh one. As one reader put it: "Same context reviewing itself isn't review, it's confirmation bias with a slash command." An agent that reviews in the authoring session has every assumption that shaped the code in its context. An independent reviewer would not have that context. This is also why people ask for [implement](https://aihero.dev/skills-implement) without its built-in review step, because that step runs the review inside the session that just wrote the diff. The independent version is to invoke `/code-review` yourself from a clean session.

**After every ticket, or once at the end?**

Both work, and the skill does not decide for you. Per-ticket keeps each diff small enough that the Spec axis has one clear spec to check against, which is the mode `implement` uses. Batching to the end of a branch catches interactions between tickets that the per-ticket passes each miss. If you are unsure, review per ticket and run one final pass against the branch point.

**Can I trust the findings?**

Not without checking. Sub-agent output is a hypothesis, not evidence. One team reported a dozen breaking changes that prose-based reviews had missed. The skill combines the reports as they are, or lightly cleaned. It does not re-verify each claim against the files, so a finding can cite the wrong location or overstate an impact. Read the citation on each finding before you act on it. The skill requires every finding to carry a citation (a standards rule, a smell plus its hunk, or a spec line), and that is what makes the findings checkable.

**Why does it find new problems every single time I run it?**

Each fix adds new code to review, and the judgement-call half of the Standards axis gives different results from run to run. One reader described the loop: "/code-review and /improve-code-architecture always find new stuff every time. I implement fixes, rerun these skills, and again and again." There is no convergence guarantee. Treat a pass as a list of leads. Act on the ones with a cited rule behind them, then stop. Do not run it in a loop until it comes back clean, because it never will.

**Does it review my uncommitted work?**

No. It diffs `<fixed-point>...HEAD`. The three-dot form measures from the merge-base and excludes staged and working-tree changes. If `implement` has not made an interim commit, the review cannot see the work that is about to go into the next commit. Commit first, then review, then amend or add a fixup.

## It's working if

- It refuses to start on a bad ref or an empty diff, before any sub-agent is spawned.
- Each available axis runs in its own BB thread: Spec at medium difficulty, Standards and Tests at simple.
- An axis that fails for provider reasons is retried once, then reported as "not run" while the other axes are aggregated.
- Every finding is marked blocking or non-blocking, and nothing without a quoted spec line or documented standard is blocking.
- The report arrives as three separate blocks under `## Standards`, `## Spec` and `## Tests`, not one merged list.
- Every Standards finding names either a rule in one of your repo's files or one of the twelve smells, with the hunk quoted; every Spec finding quotes a line of the spec; every Tests finding names the row of the table.
- The closing summary gives a worst issue per axis and declines to pick an overall winner.
- With no spec available, the Spec block says so instead of listing requirements it inferred from the code.

## Where it fits

`code-review` is the review step near the tail of the build chain: `grill-with-docs → to-spec → to-tickets → implement → code-review → retro`. It also stands alone on any branch or PR you point it at.

- [implement](https://aihero.dev/skills-implement) is the closest neighbour. It drives the build and calls this skill as its own closing review before committing. [implement-spec](https://aihero.dev/skills-implement-spec) does the same once, over the whole integration branch.
- [retro](https://aihero.dev/skills-retro) comes after it and tunes it. When a session shows the review missing a class of mistake, `retro` proposes the check or the `CODING_STANDARDS.md` rule the Standards axis then reads.
- [pr](https://aihero.dev/skills-pr) writes the pull request body once the reviewed work goes up.
- [to-spec](https://aihero.dev/skills-to-spec) and [to-tickets](https://aihero.dev/skills-to-tickets) produce the document the Spec axis checks against, so a vague spec makes that axis vague.
- [improve-codebase-architecture](https://aihero.dev/skills-improve-codebase-architecture) is the whole-codebase counterpart, because this skill only looks at one diff.

[ask-matt](https://aihero.dev/skills-ask-matt) routes across the whole set when you are unsure which skill the situation wants.

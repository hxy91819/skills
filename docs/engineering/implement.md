## What it does

`implement` builds work that has already been decided. You point it at a [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket), a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), or the plan you just agreed in the conversation, and it writes the code, drives [tdd](https://aihero.dev/skills-tdd) at the test boundaries, typechecks as it goes, commits to the current branch, and then reviews at a tier matched to the change's risk: none for docs, config, test-only and small single-module fixes, a self-review for ordinary feature work, and a full [code-review](https://aihero.dev/skills-code-review) for cross-module, schema, permission or core state-machine changes.

It never reopens the plan. There is no interview, no clarifying round, no proposal of a different approach. Whatever was settled upstream is the input, and the skill's whole job is to turn that into a commit. That is what separates it from typing "build this" at a fresh [agent](https://www.aihero.dev/ai-coding-dictionary/agent), which will happily redesign the work while it builds it.

## When to reach for it

You invoke this by typing `/implement` yourself: the agent won't reach for it on its own. It ships with `disable-model-invocation: true`, so no other skill can call it either. Wherever [ask-matt](https://aihero.dev/skills-ask-matt) or [to-tickets](https://aihero.dev/skills-to-tickets) says "then `/implement` per ticket", that is an instruction to you, not something the agent will do unprompted.

Where the work currently lives decides whether this is the right skill:

| The work is… | Reach for |
| --- | --- |
| A ticket on the tracker | `/implement #42`, one ticket per [session](https://www.aihero.dev/ai-coding-dictionary/session), [clearing](https://www.aihero.dev/ai-coding-dictionary/clearing) context between tickets |
| A spec, not yet split up, and the build spans sessions | [to-tickets](https://aihero.dev/skills-to-tickets) first, then `/implement` per ticket |
| A spec, and the build is small | `/implement` directly against the spec |
| Only in the conversation you just had, and it's still small | `/implement` right there, in the same window |
| Not written down anywhere yet | [grill-with-docs](https://aihero.dev/skills-grill-with-docs), or [grill-me](https://aihero.dev/skills-grill-me) if there's no codebase |
| One concrete behaviour you want test-first, with no spec | [tdd](https://aihero.dev/skills-tdd) directly |
| Already built, and you want it checked | [code-review](https://aihero.dev/skills-code-review) directly |

The same-session case is worth naming because the skill's own first line doesn't cover it. `SKILL.md` says "the spec or tickets", which nudges the [model](https://www.aihero.dev/ai-coding-dictionary/model) to go hunting for a file that doesn't exist. If the plan lives only in the thread, say so when you invoke it.

## Prerequisites

`implement` commits to the branch you are on. It does not create one, and it does not ask. Check you are on the branch you want the work on before you start.

If the tickets came from [to-tickets](https://aihero.dev/skills-to-tickets), the tracker they live on was configured by [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills). `code-review` reads the same configuration to find the originating spec at close-out.

## What one run does

A run is seven beats, in order:

1. Read the ticket or spec and work out the test boundaries.
2. Drive [tdd](https://aihero.dev/skills-tdd) at the pre-agreed test boundaries, one red-green slice at a time.
3. Typecheck often, run single test files as it goes.
4. Run the full test suite once, at the end.
5. Commit to the current branch, then review at the tier the change's risk calls for (skip, self, or full [code-review](https://aihero.dev/skills-code-review)). Review runs once; only blocking findings are fixed.
6. Deliver the way the repo's `AGENTS.md` says, using the repo's own tools for its code host, then leave a one-line result on the ticket and close it.
7. Report: three opening lines (outcome, what you need to decide, next step), then short details.

One run covers one ticket. The tickets [to-tickets](https://aihero.dev/skills-to-tickets) produces are tracer-bullet vertical slices sized to fit a single fresh [context window](https://www.aihero.dev/ai-coding-dictionary/context-window), so the intended rhythm is: clear context, implement one ticket, commit, clear again. Each ticket is self-contained, which is what makes the previous ticket's context disposable.

## Pre-agreed test boundaries

The idea the skill runs on is the **test boundary**: the public boundary you observe behaviour at, without reaching inside. Tests live at test boundaries. Working at a test boundary agreed before any code is written is what keeps the tests durable, because the implementation underneath can be rewritten without the tests moving.

The word "pre-agreed" is doing real work, and it is also the skill's weakest joint. Nothing inside `implement` agrees the test boundaries. `tdd` is the skill that asks, and it refuses to write a test at an unconfirmed test boundary. So in practice the agreement happens either upstream in the spec, or in the first exchange of the run. If it happens nowhere, the precondition never fires and the run quietly becomes "just write the code". Naming the test boundaries in the spec is what stops that.

The spec's Testing Decisions table is also the run's completion list. A story whose row says `browser e2e` or `api` is not done until a test at that boundary exists and passes, and the skill is told not to substitute a lower one. When an existing browser e2e or API test breaks under the change, the skill decides whether the test or the code is wrong and records which it changed, and why, in the commit message. That one line is what lets a reviewer or the next agent tell a fixed regression from a silenced one without anyone having to gate the decision.

## Common questions

**It finished, but my ticket is still open.**

It closes the ticket only after the change has landed: merged, or pushed where the repo pushes directly. If the merge request is still waiting on CI or a human merge, the ticket stays open until then. If delivery was blocked (a missing tool, credential or entry point), the report names what is missing and the ticket stays open on purpose.

**It stopped and said a capability is missing instead of building it.**

That is intended. When the spec relies on something that doesn't exist yet, designing a stand-in subsystem is a new decision, so the skill reports it as blocked rather than inventing one inside a ticket.

**Can I point it at all my tickets at once, or run several in parallel?**

Not with `/implement`: one invocation, one ticket. For a whole spec in one run, use [implement-spec](https://aihero.dev/skills-implement-spec), which fans the tickets out to [subagents](https://www.aihero.dev/ai-coding-dictionary/subagent), each in its own worktree, across the ready frontier, and merges them onto one integration branch. Running several `/implement` sessions side by side in one checkout is worse than unsupported: one field report describes a `git commit --amend` in one session landing on another session's commit, a stash vanishing from `refs/stash`, and commits landing on the wrong branch, all in a single afternoon across three issues. The sessions share one working directory, one index, and one HEAD. Git worktrees are the community workaround, and note that `refs/stash` is shared across worktrees too, so worktrees alone do not fix the stash case.

**Can it open a pull request instead of committing?**

It follows the repo. It commits on the current branch, then delivers the way the repo's `AGENTS.md` documents: a merge request, a direct push, or whatever the repo uses, with the repo's own tools for its code host. Document the convention in `AGENTS.md` and it will use it. When the delivery is a pull request, [pr](https://aihero.dev/skills-pr) shapes its body.

**`code-review` says it cannot see my changes.**

`code-review` reviews `git diff <fixed-point>...HEAD`, which excludes staged and working-tree changes. `implement` now commits before it reviews, so the diff is there. If you run `code-review` on your own, commit first, then review against the point you branched from.

Separately, some people deliberately do not want the review inside the run at all, because an agent reviewing the code it just wrote is biased toward its own solution. Running [code-review](https://aihero.dev/skills-code-review) in a fresh session against a fixed point is a legitimate alternative, and is the same reason that skill runs its three axes in separate sub-agents.

**One ticket burned 150k tokens. Am I using it wrong?**

Probably the ticket is too big rather than the skill being misused. A run does codebase exploration, a red-green loop per test boundary, a full suite, and a review, so a non-trivial ticket exceeding 100k [tokens](https://www.aihero.dev/ai-coding-dictionary/token) is normal rather than a sign something broke. The lever is upstream: right-size the tickets in [to-tickets](https://aihero.dev/skills-to-tickets) so each fits one fresh window. If a single ticket keeps blowing out, split it rather than raising the [effort](https://www.aihero.dev/ai-coding-dictionary/effort) level.

**`/implement #2` in a fresh session worked on something completely unrelated.**

`#2` is resolved against whatever numbered list the agent can see, which in a fresh session may be a todo file, a checklist, or another work list rather than the configured tracker. The resolution is confident rather than fail-closed, so the mistake is not obvious until it has started. Pass the full reference, the issue URL or `owner/repo#2`, and ask it to confirm the title back before it begins.

## It's working if

- The session opens by reading the ticket or spec and restating what it will build, rather than asking you what to build.
- You can see an actual `/tdd` invocation in the trace, not just tests appearing in the diff.
- Typechecks and single test files run repeatedly during the run, and the full suite runs once near the end.
- The run reaches a commit on your current branch without you prompting it to carry on.
- It delivers through the repo's documented route and closes the ticket once the change has landed.
- The final report opens with the outcome, what you need to decide, and the next step.
- The diff is one ticket's worth of change: a vertical slice through every layer, not several tickets swept together.

## Where it fits

`implement` is the build step of the main chain:

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

Its neighbours are [to-tickets](https://aihero.dev/skills-to-tickets), which produces the tickets it consumes and declares the blocking edges that decide their order; [tdd](https://aihero.dev/skills-tdd), which it drives internally at each test boundary; and [code-review](https://aihero.dev/skills-code-review), which it runs after committing when the change is risky enough to need it. It sits downstream of the planning skills and trusts them. It does not re-validate the shape of what it was handed, so a badly-structured map or a horizontally-layered ticket gets built as written.

That trust is why [wayfinder](https://aihero.dev/skills-wayfinder) merges onto the chain at [to-spec](https://aihero.dev/skills-to-spec) rather than looping its map straight into `implement`. Go straight to `implement` from a map only when the effort turned out genuinely small.

[ask-matt](https://aihero.dev/skills-ask-matt) is the router over the whole set when you are not sure which flow you are in.

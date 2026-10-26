## What it does

`implement` builds work that has already been decided. You point it at a [ticket](https://www.aihero.dev/ai-coding-dictionary/ticket), a [spec](https://www.aihero.dev/ai-coding-dictionary/spec), or the plan you just agreed in the conversation, and it writes the code, drives [tdd](https://aihero.dev/skills-tdd) at the test boundaries, typechecks as it goes, commits to the current branch, then reviews at a tier matched to risk and delivers through the repo's documented route.

It never reopens the plan. There is no interview, no clarifying round, no proposal of a different approach. Whatever was settled upstream is the input, and the skill's job is to build and deliver that work. That is what separates it from typing "build this" at a fresh [agent](https://www.aihero.dev/ai-coding-dictionary/agent), which often redesigns the work while it builds it.

## When to reach for it

You invoke this by typing `/implement` yourself, and the agent won't reach for it on its own. It ships with `disable-model-invocation: true`, so no other skill can call it either. Wherever [ask-matt](https://aihero.dev/skills-ask-matt) or [to-tickets](https://aihero.dev/skills-to-tickets) says "then `/implement` per ticket", that is an instruction to you, not something the agent will do unprompted.

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

The same-session case is worth naming because the skill's own first line doesn't cover it. `SKILL.md` says "the spec or tickets", which pushes the [model](https://www.aihero.dev/ai-coding-dictionary/model) to look for a file that doesn't exist. If the plan lives only in the thread, say so when you invoke it.

## Prerequisites

`implement` commits to the branch you are on. It does not create one, and it does not ask. Check you are on the branch you want the work on before you start.

If the tickets came from [to-tickets](https://aihero.dev/skills-to-tickets), [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills) configured the tracker they live on. `code-review` reads the same configuration to find the originating spec at close-out.

## What one run does

A run has seven steps, in order:

1. Fetch a passed ticket reference with the commands in `docs/agents/issue-tracker.md` and state its title, then read the work and its test boundaries. Ask if the reference is ambiguous. If that contract requires claiming, claim the ticket as documented before starting work.
2. Drive [tdd](https://aihero.dev/skills-tdd) at the pre-agreed test boundaries, one red-green slice at a time.
3. Typecheck often, run single test files as it goes.
4. Run the full test suite once, at the end.
5. Commit to the current branch, then review once at the tier the change calls for. Fix blocking findings and rerun the affected tests.
6. Deliver using the repo's own tools and `AGENTS.md` rules, with tracker and MR commands from `docs/agents/issue-tracker.md`. Once the change has landed, use that contract to leave a one-line result on the ticket and close it.
7. Report the outcome, what you need to decide, and the next step, followed by short details.

One run covers one ticket. The tickets [to-tickets](https://aihero.dev/skills-to-tickets) produces are tracer-bullet vertical slices sized to fit a single fresh [context window](https://www.aihero.dev/ai-coding-dictionary/context-window), so the intended rhythm is: clear context, implement one ticket, commit, clear again. Each ticket is self-contained, so you can discard the previous ticket's context.

## Review matched to risk

| Tier | Change | Review |
| --- | --- | --- |
| Skip | Docs, config, tests, CI or flaky-test fixes; a small single-module fix without schema, migration, permission or credential changes | Tests and CI |
| Self | Ordinary feature work inside one module | Reread the diff against the spec and completion list |
| Full | Cross-module work, schema or migration, permissions or credentials, a core state machine | Call [code-review](https://aihero.dev/skills-code-review) against the branch point |

File count does not raise the tier; when torn, take the lower. Review runs once. Missing or wrong spec requirements, missing or weaker declared tests, weakened existing browser e2e or API tests, and hard repo-standard violations block. Smells and suggestions go in the commit or MR description. Review can run alongside CI and delivery; a provider failure is reported rather than starting an endless review loop.

## Pre-agreed test boundaries

The skill's central idea is the **test boundary**, the public boundary you observe behaviour at without reaching inside. Tests live at test boundaries. When the test boundary is agreed before any code exists, the tests last, and you can rewrite the implementation underneath without changing them.

The "pre-agreed" part matters, and it is also the skill's weakest point. Nothing inside `implement` agrees the test boundaries. `tdd` is the skill that asks, and it refuses to write a test at an unconfirmed test boundary. So in practice the agreement happens either upstream in the spec, or in the first exchange of the run. If it happens nowhere, the run becomes "just write the code" and nothing warns you. Naming the test boundaries in the spec is what stops that.

The spec's Testing Decisions table (or the ticket's test criteria) is the completion list. Every declared test must exist and pass at its boundary; a unit test cannot replace a `browser e2e` or `api` row. When an existing browser e2e or API test fails because of the change, the commit message states whether the test or code changed and why. The full suite and CI must pass where the repo has them. Extra validation outside the spec is reported as out of scope.

## Common questions

**It finished, but my ticket is still open.**

The ticket closes only after the change has landed: merged, or pushed where the repo pushes directly. A merge request waiting for CI or human merge leaves it open. Missing delivery tools, credentials or entry points are reported as blockers. A capability the spec relies on but that does not exist is also a blocker, not permission to invent a replacement subsystem.

**Can I point it at all my tickets at once, or run several in parallel?**

Not with `/implement`: one invocation, one ticket. For a whole spec in one run, use [implement-spec](https://aihero.dev/skills-implement-spec), which gives each ticket on the ready frontier to a [subagent](https://www.aihero.dev/ai-coding-dictionary/subagent) in its own worktree, then merges the results onto one integration branch. Running several `/implement` sessions side by side in one checkout is worse than unsupported. One field report describes a `git commit --amend` in one session landing on another session's commit, a stash vanishing from `refs/stash`, and commits landing on the wrong branch, all in a single afternoon across three issues. The sessions share one working directory, one index, and one HEAD. Users work around this with git worktrees, but `refs/stash` is shared across worktrees too, so worktrees alone do not fix the stash case.

**Can it open a pull request instead of committing?**

It commits on the current branch, then follows the repo's `AGENTS.md`: a merge request, a direct push, or whatever the project documents, using its own code-host tools. When delivery uses a pull request, [pr](https://aihero.dev/skills-pr) shapes the body.

**`code-review` says it cannot see my changes.**

`code-review` reviews `git diff <fixed-point>...HEAD`, which excludes staged and working-tree changes. `implement` commits before review, so the diff is visible. When invoking `code-review` on its own, commit first and review against the branch point.

Separately, some people do not want the review inside the run at all, because an agent reviewing the code it just wrote is biased toward its own solution. Running [code-review](https://aihero.dev/skills-code-review) in a fresh session against a fixed point is a valid alternative. The same bias is why that skill runs its three axes in separate BB threads.

**One ticket burned 150k tokens. Am I using it wrong?**

Probably not. The ticket is more likely too big. A run does codebase exploration, a red-green loop per test boundary, a full suite, and a review, so a non-trivial ticket exceeding 100k [tokens](https://www.aihero.dev/ai-coding-dictionary/token) is normal rather than a sign something broke. The fix is upstream. Right-size the tickets in [to-tickets](https://aihero.dev/skills-to-tickets) so each fits one fresh window. If a single ticket keeps going over, split it rather than raising the [effort](https://www.aihero.dev/ai-coding-dictionary/effort) level.

**`/implement #2` in a fresh session worked on something completely unrelated.**

The agent resolved `#2` against another numbered list in context, such as a todo file or checklist, rather than the configured tracker. `implement` now fetches a passed reference from the issue tracker and states its title before starting, and asks when the reference is ambiguous. Check that title matches the ticket you meant; passing the issue URL or `owner/repo#2` removes the ambiguity entirely.

## It's working if

- The session opens by reading the ticket or spec and restating what it will build, rather than asking you what to build.
- You can see an actual `tdd` Skill tool call in the trace, not just tests appearing in the diff.
- Typechecks and single test files run repeatedly during the run, and the full suite runs once near the end.
- The run reaches a commit on your current branch without you prompting it to carry on.
- It delivers through the repo's documented route and closes the ticket after the change lands.
- The final report opens with the outcome, what you need to decide, and the next step.
- The diff is one ticket's worth of change: a vertical slice through every layer, not several tickets swept together.

## Where it fits

`implement` is the build step of the main chain:

```txt
grill-with-docs → to-spec → to-tickets → implement → code-review → retro
```

Its neighbours are [to-tickets](https://aihero.dev/skills-to-tickets), which produces the tickets it consumes and declares the blocking edges that decide their order; [tdd](https://aihero.dev/skills-tdd), which it drives internally at each test boundary; and [code-review](https://aihero.dev/skills-code-review), which it calls after committing when the change calls for Full review. It sits downstream of the planning skills and trusts them. It does not re-validate the shape of what it was handed, so a badly-structured map or a horizontally-layered ticket gets built as written.

That trust is why [wayfinder](https://aihero.dev/skills-wayfinder) merges onto the chain at [to-spec](https://aihero.dev/skills-to-spec) rather than looping its map straight into `implement`. Go straight to `implement` from a map only when the effort turned out small.

[ask-matt](https://aihero.dev/skills-ask-matt) is the router over the whole set when you are not sure which flow you are in.

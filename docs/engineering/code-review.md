## What it does

`code-review` reports **Standards** and **Spec** findings separately, so compliance with one cannot mask failure on the other. It reviews the requested Git state rather than assuming every request means a merge-base diff ending at HEAD.

## When to reach for it

Invoke `/code-review` explicitly. It does not independently auto-start. [implement](https://aihero.dev/skills-implement) can read its review instructions within an already-started build without another invocation. Use it for selected commits, branches, staged changes, or work in progress.

## Scope before findings

| Request | What is inspected |
| --- | --- |
| Since an exact commit or tag | Endpoint changes from that ref to HEAD |
| One commit | That commit's patch; a merge needs a parent choice |
| Branch or PR | Merge-base changes to the requested target, even if it is not checked out |
| Staged only | The index, excluding unstaged and untracked work |
| Unstaged only | Tracked working-tree changes against the index |
| WIP | Net tracked changes, staged/unstaged views, and in-scope untracked additions |
| Branch plus WIP | Merge-base through the working tree, with the separate index views and untracked additions |

The report names the scope and commands. An empty scope stays empty; unavailable inputs become limitations rather than silently disappearing. Review does not stage files or make fixes.

Small reviews run directly. Larger reviews may use independent reviewers when permitted, but there is no mandatory pair of [subagents](https://www.aihero.dev/ai-coding-dictionary/subagent).

## Common questions

**Must I supply a spec or base every time?**
No. The review uses your target, requirements, and conversation first. It asks only for ambiguity that affects the result. With no spec it still reviews Standards and explicitly marks Spec coverage unavailable; tracker setup is not required for a local review.

**Can reviewers recursively start more reviews?**
No. Optional delegates receive a bounded scope and must review directly without invoking this skill or delegating again.

**Does a clean report authorize a commit or fix?**
No. Those are separate actions. Findings are evidence to evaluate, not an instruction to keep refactoring until every heuristic is quiet.

## It's working if

- Staged-only findings do not include your unfinished working-tree edits.
- WIP includes in-scope untracked additions without staging them.
- Each finding cites a rule or requirement and file evidence; missing inputs are visible.

## Where it fits

A standalone explicit review mode and a reference used by [implement](https://aihero.dev/skills-implement) before its commit. For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).

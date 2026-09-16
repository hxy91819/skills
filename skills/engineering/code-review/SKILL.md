---
name: code-review
description: Explicit two-axis review of selected commits, branches, staged changes, or work in progress.
disable-model-invocation: true
triggers:
  - user
---

# Code Review

Review the requested changes along two separate axes: **Standards** (documented repo conventions and the smell baseline below) and **Spec** (the requested behaviour). This explicit review mode may also be read as reference inside an already-started implementation workflow, without a new invocation or confirmation gate. Review only; do not fix, stage, commit, or publish unless separately authorized.

## 1. Resolve the requested scope

Use the user's target and conversation context first. Ask only when an unresolved ambiguity would change the reviewed files or requirements. Inspect `git status --short` and resolve supplied refs with `git rev-parse --verify '<ref>^{commit}'`. Record the exact commands and resolved commits so the scope is reproducible. Do not silently substitute HEAD for a user-supplied target.

Choose the matching comparison (quote actual refs and paths in shell commands):

| Request | Review input |
| --- | --- |
| Changes since an exact commit or tag | `git diff <base> HEAD --` (endpoint comparison, not merge-base) |
| One named commit | `git show --format=fuller --patch <commit> --`; for a merge, identify the requested parent before comparing |
| Branch or PR changes | `git diff <base>...<target> --`; use the requested target branch, which need not be checked out |
| Explicit endpoint comparison | `git diff <base> <target> --` |
| Staged changes only | `git diff --cached --` (against HEAD, or the empty tree in an unborn repo) |
| Unstaged tracked changes only | `git diff --` (against the index) |
| All current WIP | `git diff HEAD --` for the net tracked changes, plus `git diff --cached --` and `git diff --` to inspect staged/unstaged states that can cancel out; include in-scope untracked additions below |
| Branch plus WIP | Resolve `git merge-base <base> HEAD`, then `git diff <merge-base> --` for the net tracked result, plus staged/unstaged views above and in-scope untracked additions below |
| Untracked files, or any WIP scope that includes them | Enumerate with `git ls-files --others --exclude-standard -z`; read the in-scope files directly as additions, without staging them |

Untracked files are not in any ordinary `git diff`. Use the NUL-delimited list safely for filenames with spaces or newlines; respect task paths and avoid reading unrelated secrets or ignored files. For WIP in an unborn repo, use the staged and unstaged views plus untracked files instead of HEAD-based commands. A staged-only request excludes unstaged/untracked work unless explicitly included.

For branch history, use `git log <base>..<target> --oneline`; for an exact since-commit request use `<base>..HEAD`. These logs supply context, not a substitute for the diff. Preserve requested path limits across every view. If the selected scope is empty, report that without inventing a different scope. Report unavailable refs or inputs rather than silently skipping them.

## 2. Identify the spec source

Use the user's supplied spec or requirements already in context. Otherwise inspect relevant local specs and issue references in the selected commits. Consult `docs/agents/issue-tracker.md` only if fetching an issue is necessary and permitted; a local review does not require tracker setup. Ask for missing requirements only when they block a useful finding. With no spec, still review Standards and mark Spec as unavailable, stating the coverage gap.

## 3. Identify the standards sources

Anything in the repo that documents how code should be written, such as `CODING_STANDARDS.md` or `CONTRIBUTING.md`.

On top of whatever the repo documents, the Standards axis always carries the **smell baseline** below: a fixed set of Fowler code smells (_Refactoring_, ch.3) that applies even when a repo documents nothing. Two rules bind it:

- **The repo overrides.** A documented repo standard always wins; where it endorses something the baseline would flag, suppress the smell.
- **Always a judgement call.** Each smell is a labelled heuristic ("possible Feature Envy"), never a hard violation. Like any standard here, skip anything tooling already enforces.

Each smell reads *what it is* → *how to fix*; match it against the diff:

- **Mysterious Name**: a function, variable, or type whose name doesn't reveal what it does or holds. → rename it; if no honest name comes, the design's murky.
- **Duplicated Code**: the same logic shape appears in more than one hunk or file in the change. → extract the shared shape, call it from both.
- **Feature Envy**: a method that reaches into another object's data more than its own. → move the method onto the data it envies.
- **Data Clumps**: the same few fields or params keep travelling together (a type wanting to be born). → bundle them into one type, pass that.
- **Primitive Obsession**: a primitive or string standing in for a domain concept that deserves its own type. → give the concept its own small type.
- **Repeated Switches**: the same `switch`/`if`-cascade on the same type recurs across the change. → replace with polymorphism, or one map both sites share.
- **Shotgun Surgery**: one logical change forces scattered edits across many files in the diff. → gather what changes together into one module.
- **Divergent Change**: one file or module is edited for several unrelated reasons. → split so each module changes for one reason.
- **Speculative Generality**: abstraction, parameters, or hooks added for needs the spec doesn't have. → delete it; inline back until a real need shows.
- **Message Chains**: long `a.b().c().d()` navigation the caller shouldn't depend on. → hide the walk behind one method on the first object.
- **Middle Man**: a class or function that mostly just delegates onward. → cut it, call the real target direct.
- **Refused Bequest**: a subclass or implementer that ignores or overrides most of what it inherits. → drop the inheritance, use composition.

## 4. Review at the appropriate scale

For a small diff, review both axes directly. Independent reviewers are optional for a larger or riskier change when delegation is available and permitted. Give each the exact scope, relevant file contents (including in-scope untracked additions), standards or spec, and this boundary: perform the assigned review directly; do not invoke this skill or delegate again.

Ground findings in file/line evidence and the relevant rule or requirement. Keep documented violations distinct from heuristic smells. Do not fabricate findings to fill either axis.

## 5. Report

Report the selected scope and commands, then separate `## Standards` and `## Spec` sections. Keep each axis's findings, severity, and coverage gaps separate; one passing axis does not cancel a failure in the other. End with findings counts and the worst issue within each axis. Missing specs or uninspected files are limitations, not passes.

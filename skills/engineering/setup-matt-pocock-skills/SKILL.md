---
name: setup-matt-pocock-skills
description: "Configure this repo for the engineering skills: derive the issue tracker, triage labels, and domain doc layout, write them, then report. Run once before first use of the other engineering skills."
disable-model-invocation: true
---

# Setup Matt Pocock's Skills

Scaffold the per-repo configuration that the engineering skills assume:

- **Issue tracker**: where issues live
- **Triage labels**: the strings used for the five canonical triage roles
- **Domain docs**: where `CONTEXT.md` and ADRs live, and the consumer rules for reading them

This skill runs **yolo**: explore the repo, derive the recommended defaults, write, then report. The user adjusts afterwards by editing `docs/agents/*.md`.

## Process

### 1. Explore

Look at the current repo to understand its starting state. Read whatever exists; don't assume. Done when every item below has been inspected:

- `git remote -v` and `.git/config`: which remotes exist, and what host each points at. Prefer `origin`, then any other remote.
- `AGENTS.md` and `CLAUDE.md` at the repo root: does either exist? Is there already an `## Agent skills` section in either?
- `CONTEXT.md` and `CONTEXT-MAP.md` at the repo root
- `docs/adr/` and any `src/*/docs/adr/` directories
- `docs/agents/`: does this skill's prior output already exist?
- `.scratch/`: a sign that a local-markdown issue tracker convention is already in use
- Is the `triage` skill installed? (a `triage` skill folder alongside this one, or `triage` in your available skills.) This decides whether `triage-labels.md` is written.
- Monorepo signals: a `pnpm-workspace.yaml`, a `workspaces` field in `package.json`, or a populated `packages/*` with its own `src/`. These are present only in a genuinely large multi-package repo; their absence means single-context, which is almost every repo.

### 2. Derive

Decide every value from what exploration found. Done when tracker, labels (or skip), domain layout, and instruction file each have a value.

**Issue tracker** is the remote's host, nothing else:

| Remote URL contains | Tracker |
| --- | --- |
| `github` | GitHub |
| `gitlab` | GitLab |
| neither, or no remotes | Local markdown |

Prefer `origin`. If `origin` matches a row, that is the tracker. Otherwise scan the remaining remotes. GitHub and GitLab templates carry a "PRs as a request surface" flag, defaulted **off**. Leave it off.

**Triage labels.** If `triage` is installed, use the five canonical role strings as-is: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. If it is not installed, skip labels entirely.

**Domain docs.** Single-context (one `CONTEXT.md` + `docs/adr/` at the repo root) unless exploration found monorepo signals, in which case multi-context (a root `CONTEXT-MAP.md` pointing to per-context `CONTEXT.md` files).

**Instruction file:**

- If `CLAUDE.md` exists, edit it.
- Else if `AGENTS.md` exists, edit it.
- If neither exists, create `AGENTS.md`.

Never create `AGENTS.md` when `CLAUDE.md` already exists (or vice versa); always edit the one that's already there.

### 3. Write

Write immediately after deriving. Done when the files below exist with the derived content, and the chosen instruction file has exactly one `## Agent skills` block.

If an `## Agent skills` block already exists in the chosen file, update its contents in-place rather than appending a duplicate. Leave user edits to the surrounding sections untouched.

The block:

```markdown
## Agent skills

### Issue tracker

[one-line summary of where issues are tracked]. See `docs/agents/issue-tracker.md`.

### Triage labels

[one-line summary of the label vocabulary]. See `docs/agents/triage-labels.md`.

### Domain docs

[one-line summary of layout: "single-context" or "multi-context"]. See `docs/agents/domain.md`.
```

Include the `### Triage labels` sub-block, and write `docs/agents/triage-labels.md`, only when `triage` is installed. When it isn't, both are omitted.

Then write the docs files using the seed templates in this skill folder as a starting point:

- [issue-tracker-github.md](./issue-tracker-github.md): GitHub issue tracker
- [issue-tracker-gitlab.md](./issue-tracker-gitlab.md): GitLab issue tracker
- [issue-tracker-local.md](./issue-tracker-local.md): local-markdown issue tracker
- [triage-labels.md](./triage-labels.md): label mapping (only if `triage` is installed)
- [domain.md](./domain.md): domain doc consumer rules + layout

A Jira, Linear, or other tracker is a later edit to `docs/agents/issue-tracker.md`, not a setup interview.

### 4. Report

Tell the user the setup is complete: every derived choice, every file written, and which engineering skills will now read from them. If a found convention disagrees with the derived default (`.scratch/` present but the remote is GitHub, `docs/agents/` already pointing at a different tracker), name the mismatch in the report.

They can edit `docs/agents/*.md` directly later; re-running this skill is only necessary if they want to switch issue trackers or restart from scratch.

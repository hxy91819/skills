---
"mattpocock-skills": patch
---

Follow the configured `docs/agents/issue-tracker.md` contract across the engineering flow:

- `to-tickets` uses declared parent-child, blocking, and claim conventions, falls back to `Part of #<parent>` and `Blocked by: #<n>` description lines when native operations are not declared, and reads relationships back through the same contract.
- `implement` fetches, claims when required, comments on, and closes tickets through the tracker contract, including MR commands during delivery.
- `code-review` distinguishes GitLab-style issue (`#n`) and MR (`!n`) references and follows their spec links using the tracker contract.
- `to-spec` publishes and labels specs using only the tracker contract.
- `setup-matt-pocock-skills` offers GitLab-style self-hosted platforms with their own CLI and a Gongfeng template using `gongfengcli`, a project ID placeholder, text relationships, and assignment before work starts.

The corresponding docs pages describe these contracts. Testing Decisions and regression contract rules are unchanged.

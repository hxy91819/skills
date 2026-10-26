# Issue tracker: Gongfeng

Issues and specs for this repo live as Gongfeng issues. Use `gongfengcli` for all operations. Replace `<project-id>` throughout this document with the project's numeric ID; commands use that ID rather than a repository path.

## Conventions

- **Create an issue**: `gongfengcli issues create <project-id> -f title='...' -f description='...'`. For multi-line descriptions, pass the complete JSON with `--data '<json>'`.
- **Read an issue**: `gongfengcli issues get <project-id> <iid> --by-iid`. For machine-readable output, put the global `--json` flag before the subcommand: `gongfengcli --json issues get <project-id> <iid> --by-iid`. Use `gongfengcli comments issue --help` to find supported comment-reading commands and their required ID form when reading the full discussion.
- **List issues**: `gongfengcli issues list <project-id> --state opened --labels <label>`. Add `--all` to fetch every page.
- **Update a description**: `gongfengcli issues edit <project-id> <iid> --by-iid -f description='...'`. For multi-line descriptions, use `--data '<json>'`.
- **Comment on an issue**: `gongfengcli comments issue create <project-id> <issueId> --body '...'`. This subcommand has no `--by-iid`; first use `gongfengcli comments issue --help` to check the required ID form and arguments, resolving the ID from the issue response as needed.
- **Set labels**: `gongfengcli issues edit <project-id> <iid> --by-iid -f labels=a,b`. Supply the complete final label list, preserving labels that should remain.
- **Close**: first comment with the result or reason, then run `gongfengcli issues edit <project-id> <iid> --by-iid -f state_event=close`.
- **Create a label**: `gongfengcli labels project create <project-id> --name <n> --color <c>`.
- **Merge requests**: use `gongfengcli mr create|get|list`. Use `gongfengcli mr --help` and the relevant subcommand's help for project and ID arguments. Comment with `gongfengcli comments mr create <project-id> <mrId> --body '...'`; first check `gongfengcli comments mr --help` for its required ID form and arguments. Issue references use `#<iid>` and MR references use `!<iid>`; they have separate number sequences. Read an MR's linked issues through the issue commands above.

## Merge requests as a triage surface

**MRs as a request surface: no.** _(Set to `yes` if this repo treats external merge requests as feature requests; `/triage` reads this flag.)_

When set to `yes`, MRs use the same labels and states as issues through `gongfengcli comments mr`, `mr edit -f labels=...`, and `mr edit -f state_event=close`. Follow the relevant subcommand's help for ID forms and arguments.

## When a skill says "publish to the issue tracker"

Create a Gongfeng issue using the conventions above.

## When a skill says "fetch the relevant ticket"

Run `gongfengcli issues get <project-id> <iid> --by-iid`, then read comments when needed using the conventions above.

## Ticket relationships and claiming

These conventions apply to all tickets, including those published by `/to-tickets` and worked by `/implement`.

- **Parent-child**: put `Part of #<parent>` on the first line of the child description. This contract uses text to group issues and does not assume a native sub-issue operation.
- **Blocking**: put `Blocked by: #<n>, #<n>` near the top of the description, or `Blocked by: None` for no blockers. Gongfeng has no native blocking link; use these text lines for both writing and reading relationships. A ticket is unblocked when every referenced blocker is closed.
- **Claim**: before starting work, assign the ticket to the driving developer using `gongfengcli issues edit <project-id> <iid> --by-iid` with the assignee field supported by the CLI. Check `gongfengcli issues edit --help` for that field and its ID form. Claiming is the session's first write.

## Wayfinding operations

Used by `/wayfinder`. The **map** is a single issue labelled `wayfinder:map`; child tickets follow the relationship and claim conventions above.

- **Map**: an issue whose body holds Notes / Decisions-so-far / Fog. Create with `gongfengcli issues create <project-id> -f title='...' -f labels=wayfinder:map`, passing a long body with `--data`.
- **Child ticket**: an issue with `Part of #<map>` on its first line and a `wayfinder:<type>` label (`research`/`prototype`/`grilling`/`task`).
- **Frontier query**: list opened issues with the appropriate `wayfinder:<type>` label and `--all`. Keep those whose first line is `Part of #<map>`, then exclude tickets with an open blocker or an assignee. Pick the first in map order.
- **Resolve**: comment with the answer, close the issue, then append a context pointer (gist + link) to the map's Decisions-so-far.

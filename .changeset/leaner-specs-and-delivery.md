---
"mattpocock-skills": patch
---

Keep specs lean and make `implement` finish the job. `to-spec` now writes user stories for the core paths only and adds verification requirements (audit trails, reconciliation, replay protection, extra approvals) only when the user asked for them, quoting the user's words. `to-tickets` defines a blocking edge as "start once the blocker has merged to the trunk", so tickets no longer stack on each other's branches. `implement` delivers through the route the repo's `AGENTS.md` documents, reports a missing tool or capability as blocked instead of improvising a route or a stand-in subsystem, closes the ticket once the change has landed, and opens its final report with the outcome, the decision needed and the next step.

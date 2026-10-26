---
"mattpocock-skills": patch
---

`code-review` now searches the repo for standards files and always hands `CODING_STANDARDS.md` / `CONTRIBUTING.md` to the Standards sub-agent (#1065), keeps the fork's three-axis BB dispatch and notification collection in place of upstream's foreground sub-agent calls (#1073), and resolves the issue tracker through the provided tracker doc instead of a hard-coded path (#937).

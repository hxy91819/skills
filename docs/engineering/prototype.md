## What it does

`prototype` builds local **throwaway code that answers a question**. It requires an explicit request for an interactive prototype; design advice alone does not authorize code, production integration, or publication.

## When to reach for it

Type `/prototype`, or explicitly request an interactive logic demo or UI prototype. Automatic selection is limited to that request, including within an authorized [wayfinder](https://aihero.dev/skills-wayfinder) task.

## Two artifacts

| Question | Artifact |
| --- | --- |
| Does this logic or state model work as expected? | A single shareable HTML file, with visible state, free-play buttons, and guided walkthroughs |
| Which UI direction works? | Structurally different variants on one local route, switched by a URL parameter and floating bar |

Use in-memory data or permitted read-only fixtures; mutations stay stubbed. The handoff names the question, answer, and limitations. Prototype code is not production-ready merely because part of it is portable.

## Common questions

**Does it publish a prototype branch or write an issue?**
Not automatically. It delivers the local artifact. Commits, published branches, issue updates, and production work need authorization for those actions.

**Should I prototype when the design is already settled?**
No. Use [implement](https://aihero.dev/skills-implement) for decided work. Prototyping earns its place by answering a specific unresolved question.

## It's working if

- You can run the local artifact and name the question it answers.
- A non-developer can drive the logic walkthrough.
- UI variants differ structurally, and no production or remote write appeared as an automatic follow-up.

## Where it fits

A standalone design aid, also available to explicitly requested prototype tasks inside planning flows. Its answer can feed [to-spec](https://aihero.dev/skills-to-spec), without starting implementation. For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).

## What it does

`wizard` generates a human-run Bash procedure from a reusable template. It only generates on explicit request; a missing credential alone does not warrant a script.

## When to reach for it

Invoke `/wizard` when you want an interactive script for a manual procedure. For a single missing value, concise instructions or the host's secure input mechanism are usually enough.

## Scope without reading secrets

The procedure is scoped from README guidance, non-secret examples, schemas, and workflow variable names. Secret-bearing environment files and credential values are not read to discover what the script needs.

The template retains staged progress, URL opening, hidden terminal input, environment-file writes, and optional GitHub secret/variable writes. The generated script is checked statically and handed to you; it is not run end to end by the authoring agent. Generation is not authorization for any remote write.

## Common questions

**Does the model need my key to generate the wizard?**
No. It needs the variable name and destination, not the value. Enter secrets locally at runtime using hidden input; do not paste them into chat or generated source.

**Will it run a migration or set remote secrets for me?**
It generates and explains the stages you asked for. You review and run them. Irreversible actions retain confirmation gates; generating a script does not expand execution permissions.

**Is the template still available?**
Yes. The template and its helpers are unchanged; only selection and safe scoping have changed.

## It's working if

- No script appears merely because a credential is missing.
- The handoff explains destinations and external writes without including secret values.
- You can review named stages before running the script yourself.

## Where it fits

A standalone explicit procedure generator, separate from [implement](https://aihero.dev/skills-implement) and [setup-matt-pocock-skills](https://aihero.dev/skills-setup-matt-pocock-skills). For the whole map, see [ask-matt](https://aihero.dev/skills-ask-matt).

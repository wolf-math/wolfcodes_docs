---
title: Shell Scripts Style
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Shell scripts style

Use this guide when writing or revising shell scripting pages and tutorials.

Shell scripting sits between command-line usage and full programming. It is narrower than a language like Python or JavaScript, but it still needs real teaching structure because beginners can easily copy commands they do not understand or write scripts that behave unsafely.

Shell scripting docs should help readers answer questions like:

- What problem is a shell script solving?
- Why use a script instead of typing commands manually?
- What does this script actually do line by line?
- What shell behavior is important to understand here?
- What habit is safe and reliable in real code?
- What fragile or dangerous pattern should the reader avoid?

The goal is not to turn every page into a complete Bash reference. The goal is to help readers write small, useful, safe scripts with a strong mental model.

## Frontmatter

Use the standard frontmatter on every page:

```md
---
title: Concept Name
sidebar_position: X
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
```

- `title` should be literal, specific, and easy to scan in the sidebar.
- `sidebar_position` controls ordering within the section.
- Keep author, license, and source metadata consistent.
- Do not add extra metadata unless the surrounding section already uses it.

If the section uses an `index.mdx` hub page, follow the same approach as other guide hubs in the repo: short welcome text, grouped links, and minimal teaching on the hub itself.

## Core principle

Write like a careful engineer teaching someone how to automate terminal work without causing surprises.

Shell scripting guides should be:

- Practical and concrete
- Strong on mental models
- Explicit about what the shell is doing
- Conservative about safety
- Honest about tradeoffs and portability

Prefer:

```md
Quote variables unless you specifically need word splitting or glob expansion.
```

Avoid:

```md
The shell performs several nuanced expansion phases that may occasionally necessitate defensive quoting practices.
```

The voice should feel approachable, but not casual about risk. Shell scripts often touch files, processes, permissions, and system state. The writing should reflect that.

## What belongs in shell scripting docs

Good shell scripting topics usually include:

- What shell scripts are for
- Creating and running scripts
- Shebangs and executable permissions
- Variables and positional arguments
- Exit codes and control flow
- Conditionals and loops
- Functions
- Pipes, redirection, and command substitution
- Reading input and prompting carefully
- Safe scripting habits
- Small automation tasks for files, logs, and system workflows

Topics that usually do not belong in beginner shell scripting guides:

- Exhaustive Bash grammar details
- Deep shell portability edge cases across every shell
- Advanced `sed`, `awk`, or `find` wizardry unless the page is specifically about them
- Full Linux administration guides unrelated to scripting
- Copy-paste deployment scripts with no explanation

Keep the scope focused on the scripting lesson. Bring in Unix tools when they help the reader understand the script, not to show off command-line fluency.

## Recommended scope

Treat shell scripting as a compact guide series, not a giant language curriculum.

Most shell scripting sections should be leaner than `docs/python/guides` or `docs/javascript/guides`. A small number of focused pages with strong examples is usually better than many thin pages.

Prefer:

- One page per core scripting concept
- A few subsections with clear examples
- Repeated emphasis on reading scripts top to bottom
- Real tasks over abstract syntax catalogs

Avoid inflating the section into a full Bash encyclopedia unless that is an explicit project goal.

## Page shapes

Most shell scripting pages should fit one of these patterns.

### Concept guides

Use for topics such as variables, exit codes, conditionals, loops, or command substitution.

Suggested shape:

1. `## What is/are [concept]?`
2. `## Why this matters` when motivation needs its own section
3. Smallest working example
4. Explanation of what the shell does
5. Common patterns
6. Common mistakes or gotchas
7. `## Safe habits` or `## Summary` when useful

### Script-building guides

Use for topics such as writing and running a script, adding arguments, or building a small task script.

Suggested shape:

1. Short framing paragraph
2. `## The smallest script`
3. `## Running the script`
4. `## Explaining each line`
5. `## Making it reusable`
6. `## Common mistakes`
7. `## Safer version` or `## Best practices`

### Task-based guides

Use for topics such as log rotation helpers, backup scripts, file cleanup scripts, or simple system tasks.

Suggested shape:

1. What task the script solves
2. Full script example early
3. `## How it works`
4. `## Why this version is safer`
5. `## Variations`
6. `## When shell is the wrong tool`

For shell scripting, task-based pages are often the most effective because they connect syntax directly to a real workflow.

## Default structure

There is no rigid template, but most shell scripting pages should move in this order:

1. Define the concept or task
2. Show the smallest useful script
3. Explain the script line by line
4. Clarify the shell behavior involved
5. Show a practical variation
6. Call out a mistake or risk
7. End with a rule of thumb or summary

Always prefer explanation tied to an actual script over abstract prose about syntax rules.

## Headings

Use direct, practical headings:

```md
## What are positional arguments?
## Writing your first script
## Checking exit codes
## Looping over files
## Why quoting matters
## Safer file deletion
## Summary
```

Use backticks in headings for exact syntax, variables, commands, and keywords:

```md
## The `#!` shebang
## `$1`, `$2`, and `"$@"`
## `if`, `then`, and `fi`
## `for` loops
## `$(...)` command substitution
```

Prefer specific headings over vague ones:

- Use `## Reading arguments with "$@"`, not `## Argument techniques`
- Use `## Redirecting output to a file`, not `## More features`
- Use `## Checking whether a file exists`, not `## Useful conditions`

## Openings and mental models

Start most pages with a plain-language definition.

Example shape:

````md
## What are shell variables?

**Shell variables** store string values that your script can reuse later. They let you avoid repetition, make scripts configurable, and pass data between commands.

```bash
name="Aaron"
echo "Hello, $name"
```
````

Shell scripting pages should teach mental models early and often:

- A shell script is a sequence of commands the shell reads and runs.
- The shell splits and expands text before many commands run.
- Exit codes communicate success or failure.
- Pipes connect one command's output to another command's input.
- Quoting changes how the shell interprets text.

These models matter more than memorizing every bit of syntax.

## Examples

Examples are the heart of the page.

Use:

- Short scripts that can be read in one pass
- Realistic names such as `backup_dir`, `log_file`, `source_dir`, and `target_dir`
- Comments only when they genuinely help the reader parse the script
- Output blocks when behavior matters

Use shell fences:

````md
```bash
#!/usr/bin/env bash
echo "Hello"
```
````

Use `text` for terminal output:

````md
**Output:**

```text
Hello
```
````

When showing a full script, prefer a complete runnable example over disconnected fragments. Then break it apart afterward.

## Explaining scripts

After a meaningful script example, explain it in order.

Useful explanation labels:

```md
**What this does:**
- Sets a variable for the log file path.
- Runs the command.
- Appends output to a file.
```

```md
**How the shell reads this:**
1. It expands `$log_file`.
2. It runs the command.
3. It redirects standard output.
```

```md
**Important:** Unquoted variables can split into multiple words.
```

```md
**Rule of thumb:** Quote variable expansions unless you have a specific reason not to.
```

Do not leave shell examples unexplained. Beginners often can run a script long before they understand how it was parsed.

## Safety-first teaching

Shell docs should teach safe habits as defaults, not as optional footnotes.

Important habits to reinforce:

- Quote variable expansions like `"$file"` and `"$dir"`
- Prefer `$(...)` over backticks for command substitution
- Check exit codes when failure matters
- Use descriptive variable names
- Be careful with `rm`, `mv`, `cp`, `chmod`, and recursive operations
- Show dry-run or preview patterns when a script changes or deletes files
- Prefer explicit paths and explicit commands over clever shorthand

When a script could be destructive, say so plainly.

If you show a risky command, add a safer version or a strong warning nearby.

Examples:

- Prefer `rm -- "$file"` over a loosely explained `rm $file`
- Prefer previewing matches before deletion
- Prefer writing logs to a named file rather than silently discarding errors

## Quoting and expansion

This deserves repeated attention because it is one of the biggest sources of shell bugs.

Teach these clearly:

- The shell splits on spaces unless quoting changes that
- Wildcards such as `*` are expanded by the shell
- Variables expand before the command receives its arguments
- Double quotes usually preserve spaces while still allowing variable expansion
- Single quotes prevent variable expansion

Good docs should not merely warn readers to quote things. They should show the broken behavior and the corrected version.

## Portability and shell choice

Be explicit about which shell the page assumes.

For beginner shell scripting pages in this project, it is usually best to teach with:

- `bash` syntax
- A shebang like `#!/usr/bin/env bash`
- Notes when behavior is Unix-specific

Do not casually mix Bash, POSIX `sh`, `zsh`, and PowerShell syntax on the same page.

If a page uses Bash-specific features such as arrays or `[[ ... ]]`, say so. If portability matters, mention it briefly without turning the page into a standards lecture.

Good phrasing:

```md
This example assumes Bash, not generic POSIX `sh`, because it uses `[[ ... ]]` and arrays.
```

## Cross-platform notes

When Windows differences matter, handle them briefly and clearly.

- Prefer WSL as the reference path for Windows readers when teaching Unix shell scripts
- Do not spend large sections translating every command to PowerShell
- Mention when a script assumes Unix tools or Unix file paths

Shell scripting pages should stay focused. Cross-platform notes should clarify limits, not take over the lesson.

## Safe default code patterns

Prefer these patterns in docs:

```bash
#!/usr/bin/env bash
```

```bash
if [ -f "$file" ]; then
  echo "Found file"
fi
```

```bash
for file in *.log; do
  echo "$file"
done
```

```bash
output=$(command)
```

```bash
some_command >>"$log_file" 2>&1
```

Use more advanced patterns only when the page is ready to explain them. Simpler and readable beats clever.

## Patterns to avoid in beginner docs

Avoid normalizing fragile or confusing habits such as:

- Unquoted variables in ordinary file paths
- Backtick command substitution
- Dense one-liners with multiple fragile expansions
- Examples that depend on hidden shell state
- Destructive commands without explanation
- Mysterious special variables with no introduction
- Overly compressed conditionals that save space but hurt clarity

Avoid writing shell like this unless the page is specifically explaining why it is hard to read:

```bash
for f in $files;do rm -rf $f;done
```

Prefer:

```bash
for file in "$@"; do
  rm -- "$file"
done
```

If even that example is too risky for the lesson, use `echo` instead of `rm`.

## Teaching system-task scripts

Shell scripting becomes most valuable when readers see it solve real tasks.

Good example tasks:

- Renaming a batch of files
- Searching logs and saving results
- Running a backup command with a timestamp
- Checking whether a service or file exists
- Wrapping a repeated development command

For these pages:

- State what the task is up front
- Show the full script early
- Explain why shell is a good fit
- Point out where the script depends on external commands
- Say when a bigger language like Python would be easier to maintain

That last point matters. Good shell docs should teach capability without pretending shell is always the best tool.

## Best-practice guidance

Whenever relevant, reinforce advice like:

- Keep scripts small and focused
- Use functions when a script starts repeating itself
- Prefer readable names over short cryptic ones
- Print useful error messages
- Exit with non-zero status on failure
- Test scripts on safe sample files before using them on real data
- Treat shell scripts as real code, not disposable magic

## Summary sections

Use `## Summary` for substantial pages.

A strong shell scripting summary should restate:

- What the concept does
- What mental model to keep
- What safe habit to remember
- What pattern to use first in real scripts

Example:

```md
## Summary

- Shell variables store values the script can reuse.
- Quote variable expansions like `"$name"` to preserve spaces safely.
- Use descriptive names and small examples before building larger scripts.
```

## Final quality check

Before publishing a shell scripting page, check:

- Does the page teach a real scripting concept or task clearly?
- Is the shell being assumed obvious and consistent?
- Are examples short, runnable, and explained?
- Are risky commands handled responsibly?
- Have quoting, expansion, or exit behavior been explained when relevant?
- Does the page teach a habit, not just syntax?
- Would a beginner understand why the script works, not just what to copy?

If the answer to the last question is no, the page needs more explanation even if the code is technically correct.

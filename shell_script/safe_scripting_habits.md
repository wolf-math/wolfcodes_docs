---
title: Safe Scripting Habits
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Why safe scripting habits matter

Shell scripts are close to the operating system.

That is part of what makes them useful, but it also means mistakes can have real consequences:

- deleting the wrong files
- overwriting output
- running a command in the wrong directory
- using the wrong input file
- continuing after an important command failed

Safe scripting habits are not an advanced bonus. They are part of basic shell scripting.

## Quote variable expansions

If you remember one safety habit early, make it this one.

Use:

```bash
cp "$source_file" "$target_file"
```

not:

```bash
cp $source_file $target_file
```

Why?

Because unquoted variables can split on spaces or expand in surprising ways.

If a variable contains:

```text
My Notes.txt
```

then:

```bash
cat $file
```

can break into multiple pieces, while:

```bash
cat "$file"
```

preserves it as one path.

## Check important input early

If your script needs arguments or files, validate them before doing real work.

Example:

```bash
#!/usr/bin/env bash

if [ -z "$1" ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

if [ ! -f "$1" ]; then
  echo "Error: file not found: $1"
  exit 1
fi
```

This is safer than letting the script fail much later in a less obvious way.

## Be explicit about directories

Many script mistakes are really location mistakes.

Bad pattern:

```bash
rm build/output.txt
```

This assumes the script is being run from the exact directory you expected.

Safer pattern:

```bash
cd ~/projects/my-app || exit 1
rm build/output.txt
```

or at least make the dependency on the directory obvious.

The point is not that every script must use `cd`. The point is that scripts should not quietly depend on context when they can be clearer.

## Stop when important commands fail

If a command matters, do not ignore its failure.

Example:

```bash
cd "$project_dir" || exit 1
```

This means:

> "If changing into this directory fails, stop the script immediately."

That is much safer than continuing in the wrong place.

This pattern is especially important after commands like:

- `cd`
- `cp`
- `mv`
- `mkdir`
- network or build commands your script depends on

## Preview destructive work first

If a script deletes, moves, or overwrites files, preview the behavior when possible.

Example:

```bash
for file in *.tmp; do
  echo "Would remove: $file"
done
```

Once that looks right, you can replace the preview with the real command:

```bash
for file in *.tmp; do
  rm -- "$file"
done
```

This habit saves people from a lot of avoidable mistakes.

## Treat `rm`, `mv`, and `cp` with respect

Commands that change files deserve extra care.

Useful habits:

- quote the paths
- preview in loops first
- avoid large destructive one-liners
- make target locations obvious
- do not assume a wildcard matched what you thought it matched

This is a good example of shell scripting style:

```bash
echo "Would copy $source_file to $target_dir"
```

before:

```bash
cp "$source_file" "$target_dir"
```

when the script is still being tested.

## Use clear names

This is not shell-specific, but it matters a lot in scripts.

Prefer:

```bash
backup_dir="$HOME/backups"
log_file="cleanup.log"
```

over:

```bash
b="$HOME/backups"
l="cleanup.log"
```

Shell scripts are already dense enough. Clear names reduce risk.

## Prefer readable scripts over clever one-liners

This:

```bash
for file in "$@"; do
  cp -- "$file" "$backup_dir"
done
```

is usually better for a guide than a compressed line that does too much at once.

Small readable scripts are easier to:

- debug
- review
- trust
- modify later

## Use logging and messages

A good script often says what it is doing.

Example:

```bash
echo "Creating backup in $backup_dir"
```

or:

```bash
echo "Error: missing input file"
```

These messages make scripts easier to follow and easier to debug.

Silent failure is frustrating. Clear messages are a safety feature.

## Be careful with `>`

Remember:

```bash
command > file.txt
```

overwrites the file.

If the file should grow over time, use:

```bash
command >> file.txt
```

instead.

Any script that writes files should be explicit about whether replacement is intentional.

## Prefer `$(...)` over backticks

This is partly a readability habit and partly a safety habit.

Prefer:

```bash
timestamp=$(date +%F)
```

over:

```bash
timestamp=`date +%F`
```

The `$(...)` form is easier to read and maintain.

## A small safer script example

```bash
#!/usr/bin/env bash

backup_dir="$HOME/backups"
source_file="$1"

if [ -z "$source_file" ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

if [ ! -f "$source_file" ]; then
  echo "Error: file not found: $source_file"
  exit 1
fi

mkdir -p "$backup_dir" || exit 1
cp "$source_file" "$backup_dir" || exit 1
echo "Backed up $source_file to $backup_dir"
```

**Why this version is safer:**

- it checks for missing input
- it checks that the file exists
- it quotes paths
- it stops if important commands fail
- it prints a clear result message

This is not fancy, but it is reliable beginner style.

## Common mistakes

### Assuming the script is in the right directory

Be careful when relative paths matter.

### Acting on files before validating input

Check first. Change things second.

### Letting the script continue after a critical failure

If a required step fails, stop and report it.

### Testing with real data first

Use sample files when possible, especially for rename, move, or delete scripts.

## Best practices

- Quote variable expansions
- Validate required input early
- Stop when important commands fail
- Preview destructive loops with `echo`
- Use clear variable names
- Print useful messages
- Favor readable multi-line scripts over clever compressed ones

## Summary

- Safe shell scripting is about reducing surprises.
- Quote variables, validate input, and stop on important failures.
- Preview destructive work before doing it for real.
- Clear names and clear messages make scripts easier to trust.
- A simple careful script is better than a clever risky one.

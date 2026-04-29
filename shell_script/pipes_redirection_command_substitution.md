---
title: Pipes, Redirection, and Command Substitution
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are pipes, redirection, and command substitution?

These are three of the most useful ways shell scripts connect commands together.

- **pipes** send one command's output into another command
- **redirection** sends output into a file
- **command substitution** captures a command's output into another command or variable

If shell scripts are glue for command-line tools, these features are some of the most important glue points.

## Pipes

A pipe uses `|`:

```bash
command1 | command2
```

It means:

> "Run `command1`, and send its output into `command2`."

Example:

```bash
grep "ERROR" server.log | wc -l
```

This:

1. finds lines containing `ERROR`
2. sends those lines into `wc -l`
3. counts them

**Output might be:**

```text
12
```

## Why pipes matter in scripts

Pipes let a script build small workflows from simple commands.

Example:

```bash
#!/usr/bin/env bash
grep "ERROR" server.log | head -n 5
```

This script is tiny, but still useful. It combines two tools:

- `grep` to filter
- `head` to limit the result

That is a very common shell scripting pattern.

## Redirection with `>` and `>>`

Redirection sends command output to a file.

### Overwrite with `>`

```bash
echo "Start" > log.txt
```

This writes to `log.txt`, replacing its old contents if the file already exists.

### Append with `>>`

```bash
echo "Another line" >> log.txt
```

This adds to the end of the file instead of replacing it.

## Redirection in scripts

Redirection is very common when scripts save logs, reports, or filtered results.

Example:

```bash
#!/usr/bin/env bash
grep -i "error" app.log > errors.txt
echo "Saved results to errors.txt"
```

This script:

- searches for matching lines
- saves them to a file
- prints a confirmation message

## Be careful with `>`

This is one of the most important beginner warnings:

```bash
command > file.txt
```

**overwrites** `file.txt`.

If you meant to keep the previous contents, use:

```bash
command >> file.txt
```

instead.

When a script writes to files, be very clear about whether it should replace or append.

## Redirecting both output and errors

Sometimes you want to save both normal output and error output in the same file.

Example:

```bash
some_command >>"$log_file" 2>&1
```

You do not need to master this syntax immediately, but the practical meaning is:

> "Append both normal output and error output to the log file."

This is very useful in scripts that log what happened during a run.

## Command substitution

Command substitution means:

> "Run a command and use its output as a value."

The modern syntax is:

```bash
$(command)
```

Example:

```bash
today=$(date +%F)
echo "$today"
```

Possible output:

```text
2026-04-28
```

The `date +%F` command runs first, and its output becomes the value of `today`.

## Why command substitution is useful

It lets a script capture useful information dynamically.

Examples:

- timestamps
- current directory names
- results from `grep`
- counts from `wc -l`
- output from helper commands

## A practical example

```bash
#!/usr/bin/env bash

error_count=$(grep -i "error" app.log | wc -l)
echo "Found $error_count error lines"
```

This script:

1. runs the command pipeline
2. captures the output into `error_count`
3. prints the result in a readable sentence

This is often easier to work with than trying to visually inspect pipeline output by hand.

## Prefer `$(...)` over backticks

You may see older shell code like this:

```bash
today=`date +%F`
```

Avoid teaching that style as the default.

Prefer:

```bash
today=$(date +%F)
```

It is easier to read and easier to nest safely.

## Putting all three together

Here is a small script that uses pipes, redirection, and command substitution together:

```bash
#!/usr/bin/env bash

today=$(date +%F)
report_file="errors-$today.txt"

grep -i "error" app.log | head -n 20 >"$report_file"

line_count=$(wc -l <"$report_file")
echo "Saved $line_count lines to $report_file"
```

**What this script does:**

- captures today's date
- builds a report file name
- pipes filtered log lines into `head`
- redirects the result into a file
- counts the saved lines
- prints a summary

This is a great example of what shell scripts are good at: connecting small tools into a repeatable task.

## A quick note on `<`

In:

```bash
line_count=$(wc -l <"$report_file")
```

the `<` sends the file into the command as input.

You do not need to use input redirection constantly as a beginner, but it is worth recognizing when you see it.

## Common mistakes

### Overwriting when you meant to append

Use `>>` for logs you want to grow over time.

### Forgetting to quote file variables

Use:

```bash
>"$report_file"
```

not:

```bash
>$report_file
```

### Using backticks by default

Prefer `$(...)` for command substitution.

### Building huge one-liners too early

Pipes are powerful, but readability matters. In scripts, it is often better to split complex workflows into a few understandable steps.

## Best practices

- Use pipes to connect simple commands into small workflows
- Use `>` when you intentionally want to replace a file
- Use `>>` when you want to keep previous output
- Use `$(...)` to capture command output cleanly
- Quote file variables in redirections
- Keep pipelines readable enough that someone else can explain them

## Summary

- Pipes send one command's output into another command.
- Redirection sends output into files.
- Command substitution captures command output as a value.
- `>` overwrites; `>>` appends.
- Prefer `$(...)` over backticks.
- These features are some of the most powerful ways shell scripts connect small tools together.

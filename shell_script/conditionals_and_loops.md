---
title: Conditionals and Loops
sidebar_position: 4
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are conditionals and loops?

Conditionals and loops let a shell script make decisions and repeat work.

Without them, a script is just:

> "Run this line, then this line, then this line."

That is useful, but limited.

With conditionals and loops, the script can do things like:

- run only if a file exists
- print a message when input is missing
- repeat the same command for many files
- stop early when something is wrong

These are some of the first features that make shell scripts feel like real programs.

## `if`: running code only when a condition is true

The most common conditional is `if`.

Example:

```bash
#!/usr/bin/env bash

if [ -f "notes.txt" ]; then
  echo "File exists"
fi
```

This means:

1. check whether `notes.txt` exists as a file
2. if it does, print `File exists`

## The shape of an `if` block

This is the basic pattern:

```bash
if [ condition ]; then
  command
fi
```

Important pieces:

- `if` starts the conditional
- `[ ... ]` contains the test
- `then` starts the block that runs if the test succeeds
- `fi` ends the conditional

`fi` is `if` backwards. That may look strange at first, but you get used to it quickly.

## Common tests inside conditionals

These come up constantly in shell scripts.

Inside:

```bash
[ ... ]
```

the small operators are **tests**. They are short pieces of conditional syntax that ask questions like:

- does this file exist?
- is this a directory?
- is this string empty?

They are not commands by themselves. They are part of the test expression the `if` statement is evaluating.

You do not need to memorize a huge catalog right away. A small set of common tests covers a lot of beginner shell scripts.

| Test | Meaning | Common use |
| --- | --- | --- |
| `-f "$path"` | Is this a regular file? | Check whether a file exists before reading or copying it |
| `-d "$path"` | Is this a directory? | Check whether a folder exists before entering or creating files in it |
| `-e "$path"` | Does this path exist at all? | Check for either a file or directory when you do not care which |
| `-z "$value"` | Is this string empty? | Check whether an argument or variable is missing |
| `-n "$value"` | Is this string non-empty? | Check whether an argument or variable has content |
| `grep -q "pattern" file` | Did `grep` find a match, without printing it? | Use a command's success or failure inside `if` when you want to test whether text exists |

### Check whether a file exists

```bash
if [ -f "$file" ]; then
  echo "Regular file exists"
fi
```

Here, `-f "$file"` means:

> "Check whether `$file` exists and is a regular file."

### Check whether a directory exists

```bash
if [ -d "$dir" ]; then
  echo "Directory exists"
fi
```

Here, `-d "$dir"` means:

> "Check whether `$dir` exists and is a directory."

### Check whether a string is empty

```bash
if [ -z "$1" ]; then
  echo "Missing argument"
fi
```

Here, `-z "$1"` means:

> "Check whether the first argument is empty."

For beginners, these tests are much more useful than memorizing lots of symbolic operators early.

## `if` / `else`

Sometimes you want one branch for success and another for failure.

```bash
#!/usr/bin/env bash

if [ -f "$1" ]; then
  echo "Found file: $1"
else
  echo "File not found: $1"
fi
```

This says:

- if the file exists, print one message
- otherwise, print the other message

## `elif`: more than two branches

Use `elif` when you need more than just yes/no.

```bash
#!/usr/bin/env bash

if [ -z "$1" ]; then
  echo "No argument provided"
elif [ -d "$1" ]; then
  echo "That is a directory"
elif [ -f "$1" ]; then
  echo "That is a file"
else
  echo "Path exists, but it is something else"
fi
```

This kind of structure is very useful in small utility scripts.

## Using exit codes inside conditionals

A key shell idea is that conditionals often rely on **command success or failure**.

Example:

```bash
if grep -q "ERROR" server.log; then
  echo "Errors found"
else
  echo "No errors found"
fi
```

Here the script is not checking a variable. It is checking whether the `grep` command succeeded.

One detail that is easy to miss:

- `-q` here is **not** one of the `[ ... ]` test operators above
- it is a **`grep` flag** meaning "quiet"

So:

```bash
grep -q "ERROR" server.log
```

means:

> "Search for `ERROR`, but do not print matching lines. Just succeed if a match is found."

That is a very shell-like pattern:

> run a command, and branch based on its exit status

## `for` loops

A `for` loop repeats a block for each item in a list.

Example:

```bash
#!/usr/bin/env bash

for name in Alice Bob Charlie; do
  echo "Hello, $name"
done
```

**Output:**

```text
Hello, Alice
Hello, Bob
Hello, Charlie
```

This means:

- set `name` to `Alice`, run the block
- set `name` to `Bob`, run the block
- set `name` to `Charlie`, run the block

## Looping over script arguments

One of the most useful real patterns is looping over `"$@"`.

```bash
#!/usr/bin/env bash

for file in "$@"; do
  echo "Processing: $file"
done
```

If you run:

```bash
bash script.sh a.txt b.txt c.txt
```

the loop processes each argument in order.

This is much safer than trying to squeeze multiple file names into one variable manually.

## Looping over matching files

Shell loops are often used to work with many files.

```bash
#!/usr/bin/env bash

for file in *.log; do
  echo "Found log file: $file"
done
```

This is a common pattern for batch work.

Examples:

- compress each log file
- rename each image
- search each report
- move matching files into another folder

## Be careful with loops that change files

Loops become dangerous when they do destructive work.

For example, this is safer as a preview:

```bash
for file in *.tmp; do
  echo "Would remove: $file"
done
```

than jumping straight to:

```bash
for file in *.tmp; do
  rm -- "$file"
done
```

When a loop affects real files, preview first if you can.

## `while` loops

A `while` loop repeats as long as a condition stays true.

Example:

```bash
#!/usr/bin/env bash

count=1

while [ "$count" -le 3 ]; do
  echo "Count: $count"
  count=$((count + 1))
done
```

**Output:**

```text
Count: 1
Count: 2
Count: 3
```

This is useful when the script should keep running until a condition changes.

For beginner shell scripting, `for` loops are more common and easier to read, but `while` loops are still worth knowing.

## A practical example

Here is a small script that checks several paths:

```bash
#!/usr/bin/env bash

for path in "$@"; do
  if [ -f "$path" ]; then
    echo "File: $path"
  elif [ -d "$path" ]; then
    echo "Directory: $path"
  else
    echo "Missing: $path"
  fi
done
```

**What this script does:**

- loops over each argument
- checks whether that path is a file
- checks whether it is a directory
- reports when the path does not exist

This is a good example of shell scripting style:

- small
- practical
- file-oriented
- built around simple command-line checks

## Common mistakes

### Forgetting quotes

Use:

```bash
if [ -f "$file" ]; then
```

not:

```bash
if [ -f $file ]; then
```

### Forgetting `then`, `do`, or `fi`

Shell syntax is small, but it is picky. Blocks need their closing keywords:

- `then`
- `fi`
- `do`
- `done`

### Using loops for work that should be previewed first

If a loop deletes, moves, or overwrites files, start with `echo` until you trust it.

### Reaching for complex logic too early

In shell scripts, simple conditions and simple loops go a long way. Keep them readable.

## Best practices

- Use `if` for clear checks like missing arguments or file existence
- Use `for` loops for repeated work over arguments or matching files
- Quote variables inside tests and loops
- Prefer small readable blocks over compressed one-liners
- Preview destructive loop behavior with `echo` first
- Let command success and failure help drive your conditionals

## Summary

- `if` lets a script run code only when a condition is true.
- `else` and `elif` let you handle other cases.
- `for` loops repeat work for each item in a list.
- `while` loops repeat while a condition stays true.
- Shell conditionals often rely on command exit status, not just variables.
- Simple, quoted, readable control flow is usually the best style.

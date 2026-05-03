---
title: Variables, Arguments, and Exit Codes
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are variables, arguments, and exit codes?

These are three of the most important building blocks in shell scripts:

- **variables** store values your script can reuse
- **arguments** let you pass information into the script
- **exit codes** tell you whether a command succeeded or failed

If you only learn a few shell scripting concepts early, make these part of the first set.

They are what turn:

> "a fixed file of commands"

into:

> "a reusable script that can react to input and failures."

## Shell variables

A **variable** stores a value so you can use it later in the script.

```bash
#!/usr/bin/env bash
name="Aaron"
echo "Hello, $name"
```

**Output:**

```text
Hello, Aaron
```

### How assignment works

In shell scripts, variable assignment looks like this:

```bash
name="Aaron"
```

Important detail:

- no spaces around `=`

Good:

```bash
name="Aaron"
```

Wrong:

```bash
name = "Aaron"
```

The version with spaces is not variable assignment in shell syntax.

## Reading a variable

To use the variable later, prefix its name with `$`:

```bash
name="Aaron"
echo "$name"
```

The `$name` part means:

> "Expand this variable to its stored value."

## Quote variable expansions

This is one of the most important shell habits:

```bash
echo "$name"
```

not:

```bash
echo $name
```

Why?

Because unquoted variables can break when their values contain spaces or wildcard characters.

Example:

```bash
file="My Notes.txt"
cat "$file"
```

**Rule of thumb:** Quote variable expansions unless you have a specific reason not to.

## Useful beginner examples

### A file path

```bash
log_file="errors.log"
grep "ERROR" server.log >"$log_file"
```

### A project directory

```bash
project_dir="$HOME/projects/my-app"
cd "$project_dir"
```

### A reusable message

```bash
message="Backup complete"
echo "$message"
```

## Script arguments

Arguments let you pass values into a script from the command line.

Suppose you have a script named `greet.sh`:

```bash
#!/usr/bin/env bash
echo "Hello, $1"
```

If you run:

```bash
bash greet.sh Aaron
```

the output is:

```text
Hello, Aaron
```

The `Aaron` part is an argument passed to the script.

## Positional arguments

Shell scripts receive arguments in numbered positions:

- `$1` = first argument
- `$2` = second argument
- `$3` = third argument

Example:

```bash
#!/usr/bin/env bash
echo "First: $1"
echo "Second: $2"
```

If you run:

```bash
bash script.sh apple banana
```

you get:

```text
First: apple
Second: banana
```

This is why they are called **positional arguments**. The position matters.

## A practical argument example

Here is a small file-copy script:

```bash
#!/usr/bin/env bash
cp "$1" "$2"
echo "Copied $1 to $2"
```

You could run it like this:

```bash
bash copy.sh report.txt report-backup.txt
```

That makes the script reusable because the file names are not hard-coded.

## `$0` and the script name

There is one other special value worth knowing early:

- `$0` is the script name as it was invoked

Example:

```bash
#!/usr/bin/env bash
echo "You ran: $0"
```

This is often useful in usage messages.

## `"$@"`: all arguments

When you want to work with all arguments, `"$@"` is an important pattern.

```bash
#!/usr/bin/env bash
for item in "$@"; do
  echo "Argument: $item"
done
```

If you run:

```bash
bash show_args.sh one two three
```

you get:

```text
Argument: one
Argument: two
Argument: three
```

This is the safe way to loop over the arguments passed to a script.

## Checking whether an argument was provided

Sometimes your script should fail early if the user forgot an argument.

This example uses an `if` conditional before we have fully taught conditionals.

Do not worry about the overall conditional syntax yet. For now, the important idea is:

- check whether the first argument is missing
- print a helpful message if it is
- stop the script with an error

The next guide, [Conditionals and Loops](./conditionals_and_loops), explains that syntax properly.

One piece is worth naming right away:

- `-z` means "is this string empty?"

Example:

```bash
#!/usr/bin/env bash

if [ -z "$1" ]; then
  echo "Usage: $0 <name>"
  exit 1
fi

echo "Hello, $1"
```

If no argument is passed, the script prints a usage message and exits with an error code.

That leads us to the next important idea.

## Exit codes

Every command finishes with an **exit code**.

The basic rule is:

- `0` means success
- non-zero means something went wrong

This is how shell scripts know whether a command worked.

Example:

```bash
mkdir new-folder
```

If the command succeeds, it exits with `0`.

If it fails, it exits with something else.

## Checking the last exit code with `$?`

Right after a command runs, `$?` contains its exit code.

Example:

```bash
mkdir test-folder
echo "$?"
```

Possible output:

```text
0
```

If the command fails, the number will usually be non-zero.

You do not need to memorize every non-zero code. The main lesson is success vs failure.

## Why exit codes matter in scripts

Shell scripts often run commands that can fail:

- copying a missing file
- changing into a missing directory
- searching a file that does not exist
- running a tool that is not installed

If your script ignores failure, it may keep going and do the wrong thing afterward.

Example:

```bash
#!/usr/bin/env bash
cd "$1"
npm run dev
```

If the `cd` fails, the script may still try to run `npm run dev` in the wrong directory.

That is why exit behavior matters.

## Exiting from your own script

You can set your own script's exit code with `exit`.

Example:

```bash
#!/usr/bin/env bash

if [ -z "$1" ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

echo "Working with $1"
```

Here:

- `exit 1` means the script is failing on purpose because the required input was missing

That is a good habit. If something important is wrong, do not pretend the script succeeded.

## A small script using all three ideas

```bash
#!/usr/bin/env bash

target_file="$1"

if [ -z "$target_file" ]; then
  echo "Usage: $0 <file>"
  exit 1
fi

if [ ! -f "$target_file" ]; then
  echo "Error: file not found: $target_file"
  exit 1
fi

echo "Showing first 5 lines of $target_file"
head -n 5 "$target_file"
```

**What this script does:**

- stores the first argument in a variable
- checks whether the argument exists
- checks whether the file exists
- exits with an error if something is wrong
- runs the real command only when the input looks valid

This example uses two small test operators:

- `-z "$target_file"` means "is this string empty?"
- `-f "$target_file"` means "does this path point to a regular file?"

If the surrounding `if [ ... ]; then` syntax still looks unfamiliar, that is expected. The next guide, [Conditionals and Loops](./conditionals_and_loops), breaks it down in detail.

That is already much safer than blindly running `head "$1"` with no checks.

## Common mistakes

### Forgetting quotes

Use:

```bash
cp "$1" "$2"
```

not:

```bash
cp $1 $2
```

### Using spaces in assignment

Use:

```bash
name="Aaron"
```

not:

```bash
name = "Aaron"
```

### Ignoring missing arguments

If a script needs input, check for it and print a clear usage message instead of failing mysteriously.

### Forgetting that non-zero means failure

Shell scripts treat exit status as a real signal. If a command fails, that is not just a visual inconvenience.

## Best practices

- Use variables to avoid repetition
- Quote variable expansions like `"$file"` and `"$1"`
- Use arguments instead of hard-coding values when a script should be reusable
- Print usage messages when required input is missing
- Use non-zero exit codes when the script should report failure
- Treat exit codes as part of the script's logic, not as an obscure shell detail

## Summary

- Variables store values your script can reuse.
- Positional arguments like `$1` and `$2` let the script accept input.
- `"$@"` is the safe way to work with all arguments.
- Exit code `0` means success; non-zero means failure.
- `exit 1` is a simple way to stop the script when something important is wrong.
- Quoting variables and checking arguments early makes scripts much more reliable.

---
title: Debugging Shell Scripts
sidebar_position: 8
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Why shell scripts need debugging

Shell scripts are small, but they can still fail in confusing ways.

Common reasons:

- the script ran in the wrong directory
- an argument was missing
- a variable expanded differently than expected
- a command failed earlier than you realized
- a file path did not exist

Debugging shell scripts is mostly about making the script's behavior more visible.

## Start by reading the error carefully

If the script prints an error, slow down and read the whole message.

Look for:

- which command failed
- which file or path is mentioned
- whether the problem is missing input, wrong location, or permissions

This sounds basic, but it is the first step surprisingly often.

## Print values with `echo`

One of the simplest debugging techniques is to print the values your script is using.

Example:

```bash
#!/usr/bin/env bash

echo "Argument 1: $1"
echo "Current directory: $PWD"
echo "Log file: $log_file"
```

This helps answer questions like:

- did the script receive the argument I expected?
- is the variable empty?
- am I in the directory I thought I was in?

For beginners, this is one of the most useful debugging habits.

## Check steps one at a time

If a script has several commands, do not treat it as one giant mystery.

Break it into questions:

1. Did the script start?
2. Did the variable get the expected value?
3. Did the file exist?
4. Did `cd` succeed?
5. Did the main command produce output?

This turns debugging into a sequence of small checks instead of blind guessing.

## Use temporary `echo` lines in loops and conditionals

If you are unsure whether a loop or conditional is doing what you think, print messages inside it.

Example:

```bash
for file in "$@"; do
  echo "Looping over: $file"
done
```

or:

```bash
if [ -f "$file" ]; then
  echo "File exists: $file"
else
  echo "Missing file: $file"
fi
```

This is often enough to reveal where the script's mental model and reality differ.

## Use `bash -x` to trace execution

Bash has a very helpful debugging mode:

```bash
bash -x script.sh
```

This runs the script while printing each command as Bash executes it.

That is useful when you want to see:

- what expanded variables turned into
- which branch the script took
- which command ran right before failure

You do not need to use `-x` for every script, but it is one of the most practical shell debugging tools to know.

## A simple example

Suppose this script fails:

```bash
#!/usr/bin/env bash

cd "$1"
ls
```

If you run:

```bash
bash -x script.sh missing-folder
```

you might see output that makes the failure obvious:

```text
+ cd missing-folder
script.sh: line 3: cd: missing-folder: No such file or directory
+ ls
```

Now you know:

- the argument was `missing-folder`
- the `cd` failed
- the script still continued afterward

That gives you a clear next fix.

## Check exit behavior

Sometimes the real bug is not the first failure. It is that the script kept going.

Example:

```bash
cd "$project_dir" || exit 1
```

When debugging, ask:

- which command was allowed to fail silently?
- should the script have stopped there?

Many shell bugs become easier once you take exit behavior seriously.

## Debugging file paths

File path mistakes are extremely common in shell scripts.

Helpful checks:

```bash
pwd
ls
echo "$file"
```

These answer:

- where is the script running?
- what files are actually here?
- what exact path is the variable holding?

Do not underestimate how often the bug is just "wrong directory" or "wrong path."

## Debugging argument handling

If the script depends on arguments, print them while debugging:

```bash
echo "Script name: $0"
echo "First argument: $1"
echo "All arguments: $@"
```

If `$1` is empty, the issue may be the way you ran the script, not the body of the script itself.

## Keep the script small while debugging

If a script becomes hard to reason about, simplify it temporarily.

For example:

- comment out later steps
- replace risky commands with `echo`
- reduce a loop to one example file
- test with sample data instead of real data

This helps isolate the problem without making the debugging session more dangerous.

## A practical debugging checklist

When a shell script is not working, check:

1. Did it receive the arguments you expected?
2. Are the key variables non-empty and correctly quoted?
3. Is the script running in the directory you expected?
4. Do the input files actually exist?
5. Did an earlier command fail?
6. Should the script have stopped at that failure?
7. Would `bash -x script.sh` make the behavior clearer?

## Best practices

- Read the full error message first
- Add temporary `echo` lines to inspect values and flow
- Use `bash -x` when you need to trace command execution
- Debug one step at a time
- Replace destructive commands with previews while investigating
- Treat path mistakes and missing arguments as likely causes before assuming something exotic

## Summary

- Debugging shell scripts is mostly about making behavior visible.
- `echo` is a useful beginner debugging tool.
- `bash -x script.sh` is one of the most helpful built-in ways to trace a script.
- Many bugs come from missing arguments, wrong paths, or ignored command failures.
- Small careful debugging steps usually work better than guessing.

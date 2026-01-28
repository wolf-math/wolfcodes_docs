---
title: Redirection and Pipes
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

Redirection and pipes are where the command line starts to feel a little magical.

They let you:

- Save command output to files
- Append without overwriting
- Connect commands together like Lego bricks

You don’t need to go deep into Unix internals to use these effectively. A few core patterns go a long way.

## The core symbols

We’ll focus on three:

- `>` — redirect output to a file (overwrite)
- `>>` — redirect output to a file (append)
- `|` — pipe: send output of one command into another

## `>`: Redirect output to a file (overwrite)

Normally, commands print to your terminal:

```bash
ls
```

With `>` you can send that output to a **file instead**:

```bash
ls > files.txt
```

This:
- Runs `ls`
- Takes what would have been printed to the screen
- Writes it to `files.txt` instead
- **Overwrites** `files.txt` if it already exists

**Mental model**:

> “Take the output of this command, and put it in that file instead of the screen.”

Examples:

```bash
# Save a list of files for later
ls -la > listing.txt

# Save search results
grep "ERROR" server.log > errors.txt
```

Be careful: `>` **replaces** the file. If you want to keep what’s already there, use `>>`.

## `>>`: Append output to a file

`>>` works like `>`, but it **adds to the end** of the file instead of overwriting it.

```bash
echo "First line" > notes.txt   # create / overwrite
echo "Second line" >> notes.txt # append
```

Now `notes.txt` contains:

```text
First line
Second line
```

Use `>>` when:

- You’re building a log or history file
- You want to keep previous content and add more

Examples:

```bash
# Append timestamps to a log file
date >> debug.log

# Append errors from different runs
grep "ERROR" run1.log >> combined_errors.log
grep "ERROR" run2.log >> combined_errors.log
```

## `|`: Pipes – connecting commands together

The pipe character `|` connects **two commands**:

```bash
command1 | command2
```

Meaning:

> “Run `command1`, and send its output directly into `command2` as input.”

Your terminal doesn’t see the intermediate output; it just flows from one program to the next.

### Simple example: `ls` + `grep`

```bash
ls | grep ".txt"
```

This:

1. Runs `ls`
2. Sends its output to `grep`
3. `grep` filters lines that contain `.txt`

You only see matching lines.

### Viewing with `less`

When a command prints a lot of output, it’s helpful to pipe into `less`:

```bash
git log | less
```

Now you can:
- Scroll with `↑` / `↓`
- Page with `Space` / `b`
- Search with `/`
- Quit with `q`

This pattern works with many commands:

```bash
ps aux | less
docker ps -a | less
kubectl get pods --all-namespaces | less
```

### Chaining multiple pipes

You can chain multiple pipes together:

```bash
cat server.log | grep "ERROR" | head -n 20
```

Step-by-step:

1. `cat server.log` prints the whole file
2. `grep "ERROR"` keeps only lines with `"ERROR"`
3. `head -n 20` shows the first 20 matching lines

Even though this looks long, it’s still just:

> “Take this, then this, then this.”

## Common redirection and pipe patterns

### Search and save

```bash
grep "ERROR" server.log > errors.txt
```

Find matching lines and save them to a file.

### Search, then inspect interactively

```bash
grep "timeout" server.log | less
```

Filter first, then page through results.

### Follow logs and filter

```bash
tail -f server.log | grep -i "error"
```

Watch only the lines that contain “error” (case-insensitive).

Press `Ctrl+C` to stop.

### Count matches

```bash
grep -i "error" server.log | wc -l
```

`wc -l` counts lines, so this tells you how many error lines exist.

## A note on input vs output (just enough theory)

Unix commands typically work with three data streams:

- **stdin** (standard input) — where a program reads from
- **stdout** (standard output) — where normal output goes
- **stderr** (standard error) — where error messages go

You don’t need to memorize the names, but:

- `>` and `>>` redirect **stdout** to files
- `|` connects stdout of one command to stdin of another

Errors often still show up in your terminal even if you redirect output—because they go to `stderr`. That’s usually a good thing for beginners.

## Windows notes

In Unix-like shells (bash, zsh, WSL), `>`, `>>`, and `|` behave as described above.

On Windows:

- PowerShell also supports `>`, `>>`, and `|`, but commands often work with **objects** instead of plain text
- Old `cmd.exe` uses `>` and `|` with text, but the command set is quite different

For learning redirection and pipes, using:

- **macOS or Linux**, or
- **WSL on Windows**

will give you the cleanest experience.

## Summary

- `>` redirects output to a file and **overwrites** it.
- `>>` redirects output to a file and **appends** to it.
- `|` connects commands: the output of the left command becomes the input of the right command.
- You can chain pipes to build simple, composable “pipelines” that would be hard to do in a GUI.
- You don’t need to understand all of Unix I/O—just remember these three operators and gradually practice with real commands.


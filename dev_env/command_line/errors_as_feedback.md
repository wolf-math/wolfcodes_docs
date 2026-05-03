---
title: Errors Are Feedback, Not Failure
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

The command line can feel hostile when you’re new because it is **very honest**.

When something goes wrong, it does not try to hide it behind a friendly dialog. It prints an error message—often bluntly—and waits for you to respond.

The key mindset shift:

> Errors are **feedback** telling you what to fix, not a judgment of your ability.

## Common error messages and what they mean

### `command not found`

Example:

```bash
pythn script.py
# zsh: command not found: pythn
```

This means:

- The shell looked through your `PATH`
- It **could not find a program** named `pythn`

Checklist:

1. **Check spelling** (this solves most cases)
2. Check if the program is installed:
   ```bash
   which python
   which node
   ```
3. On Windows + WSL, make sure you’re in the **right environment** (PowerShell vs WSL vs cmd)

### `No such file or directory`

Example:

```bash
cat notes.txt
# cat: notes.txt: No such file or directory
```

This means:

- The file or directory you referenced **doesn’t exist at the path you gave**

Checklist:

1. Where are you?
   ```bash
   pwd
   ```
2. What’s actually here?
   ```bash
   ls
   ```
3. Are you using the correct **path**?
   - Right directory?
   - Correct spelling?
   - Using relative vs absolute paths correctly?

Often this error just means: *“You think you’re in one directory, but you’re in another.”*

### `Permission denied`

Example:

```bash
cat /etc/shadow
# cat: /etc/shadow: Permission denied
```

This means:

- Your **user account** does not have permission to do what you’re trying to do

Checklist:

1. Are you trying to:
   - Access a system file?
   - Write to a protected directory?
2. Do you really need to do this as your normal user?
3. If appropriate, you may need `sudo` (we’ll talk more about this in the permissions section).

As a beginner, treat `permission denied` as:

> “You probably shouldn’t be doing this casually. Slow down and understand why.”

## How to read error messages

When an error appears:

1. **Stop and read the entire line**
2. Look for:
   - The **command name**
   - The **file or path** it mentions
   - The **reason** at the end (`not found`, `permission denied`, etc.)

Example:

```bash
cp file.txt /etc/
# cp: /etc/file.txt: Permission denied
```

Break it down:

- Command: `cp`
- Target: `/etc/file.txt`
- Reason: `Permission denied`

The command is fine; the path is the problem: `/etc` is a system directory.

## A simple debugging checklist

When a command fails, walk through these:

1. **Spelling**
   - Command name
   - File or directory names
2. **Location**
   - `pwd` — am I in the directory I think I’m in?
   - `ls` — does the thing I’m referencing actually exist here?
3. **Permissions**
   - Is this a system file or directory?
   - Do I need `sudo`? (And should I be doing this at all?)
4. **Environment**
   - Which shell am I using? (`echo $SHELL`)
   - Which program is actually being run? (`which python`, `which node`)

This sounds like a lot, but with practice it becomes automatic.

## Copy-paste commands carefully

It’s common to copy commands from tutorials. When something goes wrong:

1. **Don’t just paste again** and hope for a different result
2. Read the error message
3. Adjust based on your:
   - Directory layout
   - File names
   - OS / shell (Unix vs Windows)

If a tutorial says:

```bash
cd my-project
```

But your folder is called `my_project`, you’ll get `No such file or directory`. The fix is not to repeat the command; it’s to adjust to your reality:

```bash
cd my_project
```

## Seeing errors as part of the workflow

Every experienced developer:

- Sees **errors all day**
- Uses them as **navigation tools**
- Rarely runs complex commands perfectly on the first try

The real skill is not avoiding errors—it’s:

- Staying calm
- Reading the message
- Tweaking and trying again

## Summary

- Errors are **feedback**, not failure; they tell you what to fix.
- Common messages:
  - `command not found` → spelling / program not installed / PATH issue
  - `No such file or directory` → wrong path or directory
  - `Permission denied` → user does not have rights; slow down and understand why
- Use a simple checklist: spelling → location (`pwd`, `ls`) → permissions → environment.
- The goal is not zero errors; the goal is to make errors **predictable, readable, and fixable**.


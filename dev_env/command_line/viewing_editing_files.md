---
title: Viewing and Editing Files
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

You can do a surprising amount of work in the command line just by **looking at files**. You do **not** need to become a terminal text editor expert to be productive.

This page focuses on **reading** files safely and understanding your options for **editing** them.

## Viewing files from the command line

### `cat`: Dump the whole file

**`cat`** (concatenate) prints a file’s contents straight to the terminal.

```bash
cat notes.txt
```

**Use it when**:
- The file is **short**
- You just want a quick look

**Downside**: For long files, `cat` will flood your screen and you’ll have to scroll back manually.

### `less`: Scrollable viewer (recommended)

**`less`** is a **pager**—a program that lets you scroll through output one screen at a time.

```bash
less notes.txt
```

Once inside `less`:
- Press `Space` to go down a page
- Press `b` to go back a page
- Press `↑` / `↓` to move line by line
- Press `/` then type text to search
- Press `q` to quit and return to the shell

**Mental model**: `less` is a temporary viewer. It never edits the file; it only shows you what’s inside.

### `head` and `tail`: Just the beginning or end

Sometimes you only care about the **start** or **end** of a file.

```bash
# First 10 lines (default)
head server.log

# First 20 lines
head -n 20 server.log

# Last 10 lines (default)
tail server.log

# Last 50 lines
tail -n 50 server.log
```

**Use cases**:
- `head` to check file structure or headers
- `tail` to see the most recent log entries or output

### `tail -f`: Follow a growing file

**`tail -f`** is very useful for watching logs as they update.

```bash
tail -f server.log
```

This:
- Shows the last lines of `server.log`
- **Keeps running**
- Prints new lines as they are appended

Press `Ctrl+C` to stop following and return to the prompt.

## Choosing how to edit files

You have three main options:

1. **Graphical editor** (VS Code, PyCharm, etc.)
2. **Beginner-friendly terminal editor** (`nano`)
3. **Power-user terminal editors** (`vim`, `emacs`) — optional, not required

### Using a graphical editor (common in real projects)

Most developers use a graphical editor even when working heavily in the command line.

Examples:
- VS Code: `code`
- JetBrains tools: `idea`, `pycharm`, etc. (if installed)

```bash
# Open a single file
code notes.txt

# Open the current directory as a project
code .
```

**Typical workflow**:
- Use the command line for **navigation and running commands**
- Use your editor for **actual writing and editing**

This is a perfectly valid (and recommended) way to work as a beginner.

### `nano`: A gentle terminal editor

If you want to stay in the terminal and make small edits, **`nano`** is a good starting point.

```bash
nano notes.txt
```

At the bottom, you’ll see commands like:

- `^O` = **Ctrl+O** (write out / save)
- `^X` = **Ctrl+X** (exit)
- `^K` = **Ctrl+K** (cut line)
- `^U` = **Ctrl+U** (paste line)

Basic `nano` workflow:

1. Open a file:
   ```bash
   nano notes.txt
   ```
2. Type or edit text
3. Save with **Ctrl+O**, press Enter to confirm
4. Exit with **Ctrl+X**

### `vim` and `emacs`: Powerful but optional

You’ll see references to **`vim`** and **`emacs`** everywhere. They are extremely powerful editors—but they come with a steep learning curve.

For this guide:
- You **do not** need `vim` or `emacs` to be productive
- It’s fine to treat them as **advanced tools for later**

If you accidentally open `vim` and get stuck:

1. Press `Esc`
2. Type `:q!`
3. Press Enter

That quits without saving.

## Combining viewing commands with other tools

Viewing commands become more powerful when you **combine** them with other commands using pipes (covered in detail in the redirection and pipes section).

Examples:

```bash
# View only the first 50 lines of a long command’s output
some-long-command | head -n 50

# View search results one page at a time
grep "ERROR" server.log | less

# Follow only lines that match a pattern (using grep -i for case-insensitive)
tail -f server.log | grep -i "error"
```

You don’t need to memorize these patterns now. The important idea is:

> You can **send output** from one command into viewers like `less`, `head`, and `tail` to keep things manageable.

## Summary

- **Reading files**:
  - `cat` prints the whole file (best for short files)
  - `less` lets you scroll, search, and then quit cleanly
  - `head` / `tail` show the beginning or end of files
  - `tail -f` is great for watching logs update in real time
- **Editing files**:
  - It’s normal to use VS Code or another GUI editor, even as a heavy CLI user
  - `nano` is a beginner-friendly terminal editor if you want to stay in the shell
  - `vim`/`emacs` are powerful but optional for beginners
- You can combine viewing commands with other tools using pipes to keep output readable and focused.


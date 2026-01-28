---
title: Programs, Arguments, and Flags
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

This is the point where the command line starts to **click**.

Every shell command you run follows the same basic pattern:

> **Program** + **arguments** + **flags/options**

Once you see this, the command line stops feeling like a pile of magic strings and starts feeling like a consistent language.

## The basic shape of a command

Take this example:

```bash
ls -l /home/user
```

Break it down:

- **`ls`** → the **program** you’re running
- **`-l`** → a **flag/option** that changes how `ls` behaves
- **`/home/user`** → an **argument** (in this case, a path)

You can read it as:

> “Run the **`ls` program** with the **`-l` option** on the **`/home/user` directory**.”

This mental model applies to almost everything you’ll run in the shell.

## Programs: What you’re actually running

When you type the first word of a command, the shell treats it as the **program name**:

```bash
python script.py
git status
node server.js
docker ps
```

In each case:

- `python`, `git`, `node`, `docker` are **programs**
- The rest are **arguments** telling that program what to do

The shell decides **where to find** that program using your `PATH` (we’ll talk about that in the environment section), but the concept is always the same: first word = program.

## Arguments: What the program should operate on

Arguments are the “things” you pass to a program:

- File names
- Directories
- URLs
- Usernames
- Subcommands

Examples:

```bash
# File as argument
cat notes.txt

# Directory as argument
ls Documents

# Script as argument
python app.py

# URL as argument
curl https://example.com
```

Some programs use **subcommands** as the first argument:

```bash
git status
git commit -m "Initial commit"
docker run python:3.12
```

Here:
- `git` is the program
- `status` / `commit` / `run` are **subcommands**
- The rest are flags and arguments to those subcommands

## Flags and options: How the program should behave

Flags (also called **options**) change what a program does or how it does it.

They usually:
- Start with `-` (short flags) or `--` (long flags)
- Come **before** or **around** the main arguments

Examples:

```bash
ls -l           # long listing format
ls -a           # include hidden files
ls -la          # combine flags

grep -i "error" server.log   # case-insensitive search

python -m venv .venv         # run module "venv"

git commit -m "Message"      # provide a commit message
```

Patterns:
- `-l`, `-a`, `-i`, `-m` → short flags
- `--help`, `--version`, `--all` → long flags

Many programs support **both** short and long versions:

```bash
ls -a
ls --all      # often equivalent
```

## Reading a command like a sentence

When you see a command, train yourself to **parse** it:

```bash
grep -i "error" server.log
```

You can read this as:

> “Run **`grep`** (the program) with the **`-i`** option (case-insensitive), searching for the **string `"error"`** inside the file **`server.log`**.”

Another example:

```bash
docker run -p 8000:8000 my-app-image
```

Read it as:

> “Run **`docker`**, using the **`run` subcommand**, map port **8000:8000** with `-p`, and start the container from the image **`my-app-image`**.”

Once you get used to this mental translation, complex-looking commands become much less scary.

## Getting help from programs

Most command line programs can tell you how they want to be used.

Common patterns:

```bash
program --help
program -h
man program    # manual page (Unix)
```

Examples:

```bash
ls --help
git help commit
python --help
```

You don’t need to memorize every flag. Instead:

1. **Recognize the shape** (program + flags + arguments)
2. Use `--help` when you’re unsure
3. Copy only what you can **explain in your own words**

## Quoting and spaces

The shell splits your command into **words** based on spaces. Quoting lets you treat multiple words as a **single argument**.

```bash
# Two separate arguments: Hello and World
echo Hello World

# One argument: Hello World
echo "Hello World"
```

Common places you’ll need quotes:

- Filenames with spaces:
  ```bash
  cat "My Notes.txt"
  ```
- Messages:
  ```bash
  git commit -m "Add README and setup instructions"
  ```
- Search strings:
  ```bash
  grep "user not found" server.log
  ```

If something behaves strangely, **check your quotes and spaces first**.

## Examples from real tools

### Git

```bash
git status
git add src/
git commit -m "Implement feature X"
```

- Program: `git`
- Subcommands: `status`, `add`, `commit`
- Flags: `-m`
- Arguments: `src/`, `"Implement feature X"`

### Python

```bash
python app.py
python -m venv .venv
python -m http.server 8000
```

- Program: `python`
- Flag: `-m` (“run this module as a script”)
- Arguments: `app.py`, `venv`, `.venv`, `http.server`, `8000`

### Package managers

```bash
pip install requests
pip install -U pytest

npm install
npm install react
```

You don’t need to know every option—just how to **read** and **reason about** the ones you see.

## Summary

- Most commands follow the same pattern:
  - **Program** (what to run)
  - **Flags/options** (how to run it)
  - **Arguments** (what to run it on)
- You can read commands like sentences: “Run this program, with these options, on this input.”
- Use `--help` and `man` to explore flags when needed; don’t try to memorize everything.
- Quoting keeps multiple words together as a single argument—very important for spaces and messages.
- Once this model clicks, the command line becomes far more predictable and less mysterious.


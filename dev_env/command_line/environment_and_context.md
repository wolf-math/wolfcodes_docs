---
title: Environment and Context
sidebar_position: 7
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

So far, we’ve focused on **commands** and **files**. This page is about the **environment** those commands run in: the invisible context that explains why `python` sometimes works and sometimes doesn’t.

You don’t need to be an expert in shell internals. You just need a clear mental model.

## What is the environment?

When you run a program from the shell, it:

- Runs **in a directory** (your current working directory)
- Sees a set of **environment variables**
- Inherits certain settings from the **shell that launched it**

Together, these form the program’s **environment**.

You’ve already seen one part:

```bash
pwd   # which directory am I in?
```

Now we’ll look at the other big piece: **environment variables**.

## Environment variables: Named pieces of context

An environment variable is just:

> A **name** → stored **string value** the shell passes to programs.

Examples you’ll see often:

- `PATH`
- `HOME`
- `SHELL`
- `USER`

### Viewing environment variables with `echo`

To read an environment variable, use `echo` and a `$` prefix:

```bash
echo $HOME
echo $SHELL
echo $USER
```

On most Unix-like systems:

- `$HOME` is your home directory
- `$SHELL` is the path to your login shell (e.g., `/bin/zsh`)

### Listing all environment variables

You can list everything with:

```bash
env
```

This prints a lot of data. You don’t need to understand every entry; it’s just useful to know this exists.

## `PATH`: Why some commands “just work”

`PATH` is the most important environment variable for command line work.

```bash
echo $PATH
```

You’ll see a colon-separated list of directories, something like:

```bash
/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

**Mental model**:

> When you type a command like `python` or `git`, the shell searches each directory in `PATH` **in order** until it finds an executable with that name.

So when you run:

```bash
python
```

The shell effectively does:

1. Look in `/usr/local/bin` for a file named `python`
2. If not found, look in `/usr/bin`
3. Then `/bin`, and so on

If it finds an executable, it runs it. If not, you see:

```bash
command not found: python
```

### Why `python` sometimes “disappears”

Common reasons `python` (or any tool) suddenly stops working:

- You installed a new version that lives in a different directory
- You created a [**virtual environment**](/docs/python/guides/standard_library/virtual_env) and activated/deactivated it
- Your `PATH` changed (e.g., new shell config, new tool)

The fix is almost always about:

- Making sure the right directory is on your `PATH`
- Or calling a more specific command (`python3`, `pip3`, etc.)

You don’t need to manually edit `PATH` often, but understanding the **idea** removes a lot of mystery.

## Temporary environment variables

You can set environment variables **for a single command**:

```bash
ENV_NAME=value some-command
```

Example:

```bash
DJANGO_SETTINGS_MODULE=myproject.settings python manage.py runserver
```

This:
- Sets `DJANGO_SETTINGS_MODULE` **only** for that `python` process
- Leaves the rest of your shell environment unchanged

## Persistent environment variables (high-level)

To make environment variables **permanent** for your shell, you usually add lines to your shell config file (`~/.bashrc`, `~/.zshrc`, etc.):

```bash
export MY_VAR="some-value"
export PATH="$HOME/.local/bin:$PATH"
```

We won’t go deep into shell config files here. The key idea is:

- `export` marks a shell variable to be passed down to child processes as part of the environment
- Shell startup files are where persistent configuration lives

## Context beyond environment variables

Programs also care about:

- **Current directory** (`pwd`)
- **User identity** (affects permissions)
- **OS and shell** (Unix vs Windows, bash vs zsh vs PowerShell)

Two commands that look identical in your history might behave differently if:

- You run them from a different directory
- You switched from your global Python to a virtual environment
- You moved from a Unix shell to PowerShell

When something “mysteriously” stops working, inspect the context:

1. Where am I?
   ```bash
   pwd
   ```
2. Which shell am I using?
   ```bash
   echo $SHELL
   ```
3. What does my `PATH` look like?
   ```bash
   echo $PATH
   ```
4. Which Python (or other tool) is actually being run?
   ```bash
   which python
   which python3
   which node
   ```

On Windows PowerShell, use:

```powershell
echo $env:PATH
Get-Command python
```

## Why this matters for real projects

Real-world tools rely heavily on environment and context:

- **[Virtual environments](/docs/python/guides/standard_library/virtual_env)** (Python) adjust `PATH` so `python` and `pip` point to project-specific versions
- **Language toolchains** (Node, Rust, etc.) install executables into directories added to `PATH`
- **Cloud CLIs** (AWS, Azure, etc.) read credentials from environment variables
- **Build systems** and scripts rely on consistent working directories

You don’t need to master all of this at once. Start by:

- Knowing that the environment **exists**
- Using `echo` and `env` to peek at it
- Checking `PATH` and `which` when commands surprise you

## Summary

- A program runs inside an **environment**: current directory, environment variables, and shell settings.
- **Environment variables** are named strings passed to programs (`HOME`, `SHELL`, `USER`, etc.).
- `PATH` controls **which commands are found** when you type something like `python` or `git`.
- When commands behave inconsistently, check:
  - `pwd` for your directory
  - `echo $SHELL` for your shell
  - `echo $PATH` and `which program` to see what’s being run
- You don’t need to edit environment variables constantly, but understanding the concept makes debugging CLI issues much less frustrating.


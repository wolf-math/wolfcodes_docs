---
title: How to Handle Windows
sidebar_position: 11
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

This guide focuses on **Unix-like shells** (macOS, Linux, and WSL).

If you’re on Windows, you don’t need a completely different mental model—you just need to know how Windows maps onto these Unix concepts.

## The honest positioning

> This is **not** a Windows administration guide.
>
> The recommended way to follow along on Windows is to use **WSL (Windows Subsystem for Linux)** and run a Linux shell.

That way:

- Commands in this guide work the same on macOS, Linux, and Windows (via WSL)
- You avoid learning two different ecosystems at once

## Three main options on Windows

### 1. WSL (Windows Subsystem for Linux) — **recommended**

WSL lets you run a real Linux environment **inside** Windows.

Characteristics:

- You get a Unix-like shell (`bash`, `zsh`, etc.)
- Same commands as this guide
- Access to Linux tools and package managers
- Works well with Git, Python, Node, Docker, and other dev tools

Typical setup:

- Install WSL (e.g., `wsl --install` from an elevated PowerShell)
- Choose a Linux distribution (Ubuntu is common)
- Open **Windows Terminal** or a WSL terminal profile

From there, you can follow this entire command line guide almost exactly as if you were on Linux.

### 2. PowerShell

PowerShell is:

- A modern Windows shell
- Designed around **objects**, not just plain text
- Very powerful for Windows system administration

However:

- Commands don’t always map 1:1 to Unix commands
- Many online tutorials assume a Unix shell

You can still benefit from the **concepts** in this guide—programs, arguments, pipes, etc.—but specific commands and examples will differ.

### 3. Git Bash

Git Bash:

- Comes with Git for Windows
- Provides a lightweight Unix-like shell on top of Windows
- Supports many familiar commands: `ls`, `cd`, `cp`, `rm`, etc.

It’s a good option for:

- Quick Git workflows
- Simple Unix-like commands

Limitations:

- Not a full Linux environment
- Some tools and packages assume a “real” Linux system

For anything beyond simple workflows, WSL is usually a better long-term choice.

## Minimal mapping table

Some basic commands across Unix and Windows PowerShell:

| Concept        | macOS/Linux (bash/zsh) | Windows (PowerShell) |
| ------------- | ---------------------- | -------------------- |
| List files    | `ls`                   | `dir` or `ls`        |
| Change dir    | `cd`                   | `cd`                 |
| Current dir   | `pwd`                  | `pwd`                |
| Remove file   | `rm`                   | `Remove-Item` or `del` |

Notes:

- Newer versions of PowerShell include aliases so `ls`, `pwd`, and `cd` work
- Under the hood, many PowerShell commands are doing **object-based** operations, not plain text

In WSL, you can use the Unix commands directly:

```bash
ls
cd
pwd
rm file.txt
```

## Paths: `/` vs `\`

On Unix:

- Paths use `/`:
  ```bash
  /home/user/projects
  ```

On traditional Windows:

- Paths use `\` and drive letters:
  ```text
  C:\Users\UserName\Projects
  ```

In WSL:

- Your Linux home is something like:
  ```bash
  /home/username
  ```
- Windows drives are mounted under `/mnt`:
  ```bash
  /mnt/c/Users/UserName/Projects
  ```

You can work mostly in your **Linux home directory** in WSL and treat it like any other Unix-like system.

## Which should you choose?

For learning and development:

- **macOS / Linux** → use the default shell (zsh or bash)
- **Windows** → use **WSL with a Linux shell** (recommended)

Why WSL:

- Same commands as servers (most servers run Linux)
- Same commands as online tutorials that assume Unix
- Easier to follow along with this guide
- Less mental overhead than juggling PowerShell + Unix simultaneously

## Summary

- This guide is **Unix-first**; Windows is treated as a compatibility layer, not a separate universe.
- On Windows, the best way to follow along is to use **WSL** and run a Linux shell.
- PowerShell and Git Bash can be useful, but commands won’t always match Unix exactly.
- The core **concepts** still apply everywhere: shells, programs, arguments, pipes, permissions—the syntax just varies slightly by environment.


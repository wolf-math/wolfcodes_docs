---
title: Files and Directories
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
This section covers the core concepts and commands for working with files and directories in the command line. Understanding these concepts is essential, as they're the foundation for everything else you'll do.

## Concepts

Before diving into commands, let's understand some fundamental concepts about how files and directories are organized.

### Your starting point: The home directory

When you open a terminal, you usually start in your **home directory** (also called your home folder). This is your personal space on the computer where your documents, pictures, and other files typically live.

```bash
# Your home directory might look like:
# macOS/Linux: /Users/yourname or /home/yourname
# Windows (WSL): /home/yourname
```

**Why this matters**: The home directory is where you'll do most of your work. It's safe, it's yours, and it's the natural starting point for navigating your file system.

### Everything lives in a tree

Files and directories are organized in a **tree structure**. Each directory can contain files and other directories (called subdirectories), which can contain more files and directories, and so on.

```
/
├── Users/
│   ├── alice/
│   │   ├── Documents/
│   │   ├── Pictures/
│   │   └── Downloads/
│   └── bob/
│       └── Documents/
├── etc/
├── var/
└── usr/
```

Think of it like this:
- The **root** (`/`) is the top of the tree. Everything is contained in this directory
- **Directories** are branches that can hold files and other directories
- **Files** are the leaves at the end of branches
- **Paths** are directions for how to get to any file or directory

### `/` is the root

The `/` (forward slash) represents the **root directory**. It is the topmost directory in the entire file system. All other directories are contained within it.

- On Unix-like systems (macOS, Linux): `/` is the system root
- Everything on your computer is somewhere under `/`
- Your home directory is somewhere in this tree: `/Users/yourname` or `/home/yourname`

### You are always somewhere (`pwd`)

The command line is alway open to some directory. Just like in a file explorer where you "open" a folder and see its contents, in the command line you're working within a specific directory. This is your **current working directory**.

You can always check where you are using the `pwd` command (which we'll learn about next). This will **print** the **working directory** showing your current location.

**Mental model**: Think of the command line like being in a building. `pwd` (print working directory) tells you "which room you're currently in."

### Paths: How to find anything

A **path** is the address of a file or directory—it tells you exactly where something is located in the tree. There are two types of paths:

#### Absolute paths

An **absolute path** starts from the root (`/`) and gives you the complete path from the top of the tree all the way to your destination.

```bash
# Examples of absolute paths:
/Users/alice/Documents/Projects/README.md
/home/username/pictures/vacation.jpg
/etc/passwd
```

**Characteristics**:
- Always start with `/`
- Work from anywhere in the file system
- Give the complete location from the root

**Example**: `/Users/alice/Documents` always points to Alice's Documents folder, regardless of where you currently are.

#### Relative paths

A **relative path** is relative to where you currently are. It doesn't start with `/`, it tells you how to get somewhere from your current location.

To understand relative paths, imagine you're in `/Users/alice` and Alice's directory structure looks like this:

```
/Users/alice/
├── Documents/
│   └── Projects/
│       └── README.md
├── Pictures/
│   └── vacation.jpg
└── Downloads/
    └── file.txt
```

Now, if you're currently in `/Users/alice`, these are relative paths:

```bash
# If you're in /Users/alice, these are relative paths:
Documents/Projects/README.md    # Goes into Documents, then Projects, then README.md
Pictures/vacation.jpg            # Goes into Pictures, then vacation.jpg
Downloads/file.txt               # Goes into Downloads, then file.txt
```

If you were in `/Users/alice/Documents` instead, you could use `..` to go up to the parent directory:

```bash
# If you're in /Users/alice/Documents, these are relative paths:
Projects/README.md               # Goes into Projects (sibling to current directory)
../Pictures/vacation.jpg         # Goes up one level (to /Users/alice), then into Pictures
../Downloads/file.txt            # Goes up one level (to /Users/alice), then into Downloads
```

**Characteristics**:
- Don't start with `/`
- Work relative to your current directory
- Change meaning depending on where you are

**Example**: If you're in `/Users/alice`, then `Documents` points to `/Users/alice/Documents`. But if you're in `/Users/bob`, then `Documents` would point to `/Users/bob/Documents`.

#### `.` and `..`: Special directory references

There are two special shorthand references for directories:

- **`.`** (single dot): Refers to the **current directory** (where you are right now)
- **`..`** (double dot): Refers to the **parent directory** (one level up in the tree)

```bash
# If you're in /Users/alice/Documents:

.          # Means /Users/alice/Documents (current directory)
..         # Means /Users/alice (parent directory)
../..      # Means /Users (parent's parent)
../Downloads # Means /Users/alice/Downloads (sibling directory)
```

**Why these are useful**:
- **`.`**: Often used to refer to "the current directory" in commands
- **`..`**: Used to go up one level (`cd ..`) or reference files in parent directories

**Example**: If you're in `/Users/alice/Documents/Projects` and want to go to `/Users/alice/Downloads`, you can type:
```bash
cd ../Downloads
```

This says: "Go up one level (`..`) to `/Users/alice`, then into `Downloads`."

## Core commands

The foundation of command line navigation consists of three essential commands for working with files and directories: `pwd`, `ls`, and `cd`.

### `pwd`: Where am I?

**`pwd`** stands for "print working directory." It shows you the absolute path of the directory you're currently in.

```bash
pwd
# Output: /Users/alice/Documents
```

**Use it when**: You need to know exactly where you are in the file system.

**Example**:
```bash
$ pwd
/Users/alice
$ cd Documents
$ pwd
/Users/alice/Documents
```

### `ls`: What's here?

**`ls`** stands for "list." It shows you what's in the current directory (files and subdirectories).

```bash
ls
# Output might look like:
# Documents  Downloads  Pictures  file.txt
```

**Use it when**: You want to see what files and directories are in your current location.

**Example**:
```bash
$ pwd
/Users/alice/Documents
$ ls
Projects  notes.txt  README.md
```

Think of `ls` as asking: "What's in this folder?"

### `cd`: Moving around

**`cd`** stands for "change directory." It moves you to a different directory.

```bash
# Go to a specific directory
cd Documents

# Go to your home directory (shortcut)
cd ~

# Same as `cd ~`
cd

# Go up one level
cd ..

# Go to root
cd /
```

**Use it when**: You want to navigate to a different directory.

**Examples**:
```bash
# Go into the Documents directory (relative path)
$ cd Documents

# Navigate to a nested directory using a relative path
$ cd Documents/Projects

# Go to a sibling directory using relative path
$ cd ../Pictures

# Go back to home directory
$ cd ~

# Go up one level
$ cd ..

# Go to a specific absolute path
$ cd /Users/alice/Pictures
```

Think of `cd` as saying: "Take me to this location."

**Tips**:
- Type `cd` by itself (or `cd ~`) to go to your home directory
- Use `cd ..` to go up one level
- You can use tab completion to auto-complete directory names (press Tab)

## Understanding flags

Commands often have **flags** (also called options) that modify their behavior. Flags usually start with a `-` (dash) and give the command additional instructions.

### Common `ls` flags

The `ls` command has many useful flags. Let's look at two common ones:

#### `ls -l`: Long format

The **`-l`** flag shows files in "long format" with detailed information.

```bash
ls -l
# Output might look like:
# drwxr-xr-x  2 alice  staff   64 Dec  1 10:00 Documents
# -rw-r--r--  1 alice  staff  1024 Dec  1 09:30 file.txt
```

**What you see**:
- File permissions (who can read, write, execute)
- Number of links
- Owner name
- Group name
- File size (in bytes)
- Date and time last modified
- File or directory name

**When to use**: When you need to see file sizes, permissions, or modification dates.

**Example**:
```bash
$ ls -l
total 0
drwxr-xr-x  2 alice  staff   64 Dec  1 10:00 Documents
-rw-r--r--  1 alice  staff  1024 Dec  1 09:30 notes.txt
```

The `d` at the start of `drwxr-xr-x` indicates it's a directory. Regular files don't have this `d`.

#### `ls -a`: Show hidden files

The **`-a`** flag shows "all" files, including **hidden files** (files that start with a dot, like `.gitignore`).

```bash
ls -a
# Output might include:
# .  ..  .gitignore  Documents  file.txt
```

**What are hidden files?**:
- Files and directories whose names start with `.` are hidden
- They're hidden by default because they're usually system or configuration files
- Common examples: `.git`, `.gitignore`, `.bashrc`, `.zshrc`

**When to use**: When you need to see configuration files or system files that are normally hidden.

**Example**:
```bash
$ ls
Documents  file.txt

$ ls -a
.  ..  .gitignore  Documents  file.txt
```

Notice that `.` and `..` show up when using `-a`. These are the current and parent directory references we learned about earlier.

### Combining flags

You can combine multiple flags together:

```bash
# Show all files in long format
ls -la

# This is equivalent to:
ls -l -a
```

**Example**:
```bash
$ ls -la
total 0
drwxr-xr-x  4 alice  staff   128 Dec  1 10:00 .
drwxr-xr-x  5 alice  staff   160 Dec  1 09:00 ..
-rw-r--r--  1 alice  staff   1024 Dec  1 09:30 .gitignore
drwxr-xr-x  2 alice  staff   64 Dec  1 10:00 Documents
-rw-r--r--  1 alice  staff  512 Dec  1 09:30 file.txt
```

## Practice: navigating the file system

Let's practice with a simple navigation exercise:

```bash
# 1. Check where you are
pwd
# You'll probably see something like: /Users/yourname

# 2. See what's in your current directory
ls

# 3. Go into a directory (if you have one)
cd Documents
pwd
ls

# 4. Go back up one level
cd ..
pwd

# 5. Go to your home directory
cd ~
pwd

# 6. Try listing with flags
ls -l
ls -a
ls -la
```

## Summary

- **Home directory**: Your starting point (usually `/Users/yourname` or `/home/yourname`)
- **Tree structure**: Files and directories are organized like a tree, starting from `/` (root)
- **You're always somewhere**: The `pwd` command shows your current location
- **Paths**: 
  - **Absolute paths** start with `/` and give the complete location
  - **Relative paths** are relative to your current directory
  - `.` = current directory, `..` = parent directory
- **Core commands**:
  - `pwd`: Show where you are
  - `ls`: List what's in the current directory
  - `cd`: Change to a different directory
- **Flags**: Modify command behavior (`ls -l` for long format, `ls -a` for all files including hidden ones)

These concepts and commands are the foundation of everything else in the command line. Once you understand paths, navigation, and how to see what's around you, you're ready to learn about working with files themselves.

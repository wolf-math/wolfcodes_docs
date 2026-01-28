---
title: Creating, Moving, and Removing Things
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

Now that you know how to navigate and see what's in your file system, it's time to learn how to create, move, and remove files and directories.

## Creating directories: `mkdir`

**`mkdir`** stands for "make directory." It creates a new directory (folder) in your current location or at a specified path.

```bash
# Create a directory in the current location
mkdir Projects

# Create a directory with a specific path
mkdir Documents/Projects

# Create multiple directories at once
mkdir folder1 folder2 folder3
```

**Use it when**: You want to create a new folder to organize your files.

**Examples**:
```bash
# Create a directory called "Projects"
$ mkdir Projects
$ ls
Documents  Downloads  Projects

# Create a nested directory structure
$ mkdir Documents/MyProject
$ ls Documents
MyProject  file.txt

# Create multiple directories
$ mkdir test1 test2 test3
$ ls
test1  test2  test3
```

Think of `mkdir` as saying: "Create a new folder here."

### Creating nested directories

Sometimes you want to create a directory structure that doesn't exist yet. For example, you might want to create `Documents/Projects/2024/January`, but `Projects` or `2024` might not exist yet.

Use the `-p` flag (which stands for "parents") to create all necessary parent directories:

```bash
# This will create Documents, Projects, 2024, and January if they don't exist
mkdir -p Documents/Projects/2024/January
```

**Without `-p`**: If any parent directory doesn't exist, the command will fail.
**With `-p`**: Creates all necessary parent directories automatically.

**Example**:
```bash
# This might fail if Projects doesn't exist
$ mkdir Documents/Projects/2024
mkdir: Documents/Projects: No such file or directory

# This will create everything needed
$ mkdir -p Documents/Projects/2024
$ ls -R Documents
Documents:
Projects

Documents/Projects:
2024

Documents/Projects/2024:
```

## Creating files: `touch`

**`touch`** creates an empty file. If the file already exists, it updates the file's modification time (but doesn't change the contents).

```bash
# Create a new empty file
touch file.txt

# Create multiple files
touch file1.txt file2.txt file3.txt
```

**Use it when**: You want to create a new empty file (often before editing it with a text editor).

**Examples**:
```bash
# Create a new file
$ touch notes.txt
$ ls
notes.txt

# Create multiple files
$ touch todo.txt ideas.txt reminders.txt
$ ls
ideas.txt  reminders.txt  todo.txt

# If the file already exists, touch updates its timestamp
$ touch notes.txt
# The file still exists, but its "last modified" time is now updated
```

Think of `touch` as saying: "Create an empty file here" or "Update this file's timestamp."

**Common use case**: Creating placeholder files before editing them:
```bash
touch README.md
# Then edit it with your text editor
code README.md
# or
nano README.md
```

## Copying files and directories: `cp`

**`cp`** stands for "copy." It creates a duplicate of a file or directory in a new location.

### Copying files

```bash
# Copy a file to a new location
cp source.txt destination.txt

# Copy a file into a directory
cp file.txt Documents/

# Copy multiple files into a directory
cp file1.txt file2.txt Documents/
```

**Use it when**: You want to duplicate a file without removing the original.

**Examples**:
```bash
# Copy a file with a new name
$ cp notes.txt notes_backup.txt
$ ls
notes.txt  notes_backup.txt

# Copy a file into a directory
$ cp notes.txt Documents/
$ ls Documents
notes.txt

# Copy multiple files
$ cp file1.txt file2.txt Documents/
$ ls Documents
file1.txt  file2.txt  notes.txt
```

Think of `cp` as saying: "Make a copy of this file here."

### Copying directories

To copy a directory and all its contents, you need the `-r` flag (which stands for "recursive"):

```bash
# Copy a directory and everything inside it
cp -r Projects Projects_backup
```

**Why `-r` is needed**: Directories can contain other directories and files. The `-r` flag tells `cp` to copy everything recursively (go into subdirectories and copy their contents too).

**Example**:
```bash
# This won't work without -r
$ cp Projects Projects_backup
cp: Projects is a directory (not copied)

# This will copy the directory and all its contents
$ cp -r Projects Projects_backup
$ ls
Projects  Projects_backup

# Both directories now have the same contents
$ ls Projects
file1.txt  file2.txt
$ ls Projects_backup
file1.txt  file2.txt
```

**Mental model**: Copying a directory is like copying a folder and everything inside it. The `-r` flag means "go into subdirectories and copy those too."

## Moving and renaming: `mv`

**`mv`** stands for "move." It moves files or directories from one location to another. It's also used to rename files.

### Moving files

```bash
# Move a file to a different location
mv file.txt Documents/

# Move a file and rename it at the same time
mv oldname.txt Documents/newname.txt

# Move multiple files
mv file1.txt file2.txt Documents/
```

**Use it when**: You want to relocate a file or directory to a different location.

**Examples**:
```bash
# Move a file into a directory
$ mv notes.txt Documents/
$ ls
Documents  file.txt
$ ls Documents
notes.txt

# Move and rename in one step
$ mv oldfile.txt Documents/newfile.txt
$ ls Documents
newfile.txt
```

Think of `mv` as saying: "Move this from here to there."

### Renaming files

The same `mv` command is used to rename files. When you "move" a file to the same location but with a different name, you're renaming it:

```bash
# Rename a file
mv oldname.txt newname.txt
```

**Example**:
```bash
# Rename a file
$ mv notes.txt journal.txt
$ ls
journal.txt

# The file is the same, just with a new name
```

**Mental model**: Renaming is just moving a file to the same location with a different name. The command line doesn't have a separate "rename" command—`mv` does both.

### Moving directories

Unlike `cp`, `mv` works with directories without needing any special flags:

```bash
# Move a directory
mv Projects Documents/
```

**Example**:
```bash
# Move a directory
$ mv Projects Documents/
$ ls
Documents
$ ls Documents
Projects
```

## Removing files and directories: `rm`

**`rm`** stands for "remove." It deletes files and directories permanently. **This is irreversible.**

### ⚠️ Safety first: Understanding permanent deletion

Before we learn how to use `rm`, there's something critical you need to understand: **deleting files in the command line is permanent**.

#### No trash can, no undo

Unlike clicking "Delete" in a file manager (like Finder or File Explorer), when you delete something in the command line:

- **There is no trash can or recycle bin**
- **There is no undo**
- **The file is gone immediately and permanently**

This is the most important thing to remember when working with `rm`. Once you delete a file, it's gone forever (unless you have backups or specialized recovery tools).

**Mental model**: Think of the command line like using a paper shredder instead of a trash can. Once something goes through, it's gone. Be deliberate and careful.

#### Start slow and be careful

When you're learning `rm`:

1. **Practice in a safe location**: Start in your home directory or a test folder
2. **Double-check your paths**: Make sure you're deleting the right file
3. **Start with one file at a time**: Don't use wildcards (`*`) until you're confident
4. **Use `ls` to verify**: Check what files exist before and after operations

### Removing files

```bash
# Delete a single file
rm file.txt

# Delete multiple files
rm file1.txt file2.txt file3.txt

# Delete files using wildcards
rm *.txt
```

**Use it when**: You want to permanently delete files (be very careful!).

**Examples**:
```bash
# Delete a single file
$ rm notes.txt
$ ls
# notes.txt is gone

# Delete multiple files
$ rm file1.txt file2.txt file3.txt
$ ls
# All three files are gone
```

**⚠️ Warning**: Once you run `rm`, the file is gone forever. There's no undo.

### Removing directories

To remove a directory, you need the `-r` flag (recursive), just like with `cp`:

```bash
# Remove a directory and all its contents
rm -r Projects
```

**Why `-r` is needed**: Directories contain files and other directories. The `-r` flag tells `rm` to remove everything inside recursively.

**Example**:
```bash
# This won't work without -r
$ rm Projects
rm: Projects is a directory

# This will remove the directory and everything inside
$ rm -r Projects
$ ls
# Projects is gone, along with all its contents
```

**⚠️ Warning**: `rm -r` will delete the directory and **everything inside it**, including all subdirectories and files. Be absolutely certain before using this.

### The `-i` flag: Interactive mode (safety net)

The `-i` flag makes `rm` ask for confirmation before deleting each file. This is a safety net that can help prevent accidental deletions:

```bash
# Delete with confirmation
rm -i file.txt
# Output: remove file.txt? (y/n)

# Delete directory with confirmation
rm -ri Projects
# Will ask for each file and directory
```

**Example**:
```bash
# Safe deletion with confirmation
$ rm -i notes.txt
remove notes.txt? (y/n) y
# File deleted after confirmation

$ rm -i notes.txt
remove notes.txt? (y/n) n
# File not deleted
```

**When to use `-i`**:
- When you're learning
- When you're not 100% sure
- When working with important files
- When using wildcards (like `rm -i *.txt`)

**Combining flags**: You can combine `-r` and `-i`:
```bash
rm -ri Projects
# This will recursively delete Projects and ask for confirmation on each item
```

### Common dangerous patterns to avoid

Here are some `rm` commands that can cause serious problems if used carelessly:

```bash
# ⚠️ DANGEROUS: Deletes everything in current directory
rm -r *

# ⚠️ DANGEROUS: Deletes everything (including hidden files)
rm -rf ./*

# ⚠️ DANGEROUS: Never run this (deletes everything from root)
rm -rf /
```

**Never run `rm -rf /`** or similar commands that target the root directory. This can delete your entire system.

**Best practice**: Always use `ls` first to see what you're about to delete:
```bash
# Safe approach
$ ls *.txt
file1.txt  file2.txt  file3.txt
# Now you can see what will be deleted
$ rm *.txt
```

## Practice: Creating and organizing files

Let's practice these commands in a safe way. Create a practice directory first:

```bash
# 1. Create a practice directory
mkdir practice_files
cd practice_files

# 2. Create some files
touch file1.txt file2.txt file3.txt
ls

# 3. Create a subdirectory
mkdir subfolder
ls

# 4. Copy a file
cp file1.txt file1_backup.txt
ls

# 5. Move a file into the subdirectory
mv file2.txt subfolder/
ls
ls subfolder

# 6. Rename a file
mv file3.txt renamed_file.txt
ls

# 7. Create a nested directory structure
mkdir -p projects/2024/january
ls -R projects

# 8. Practice safe deletion (with -i flag)
rm -i file1_backup.txt
# Type 'y' to confirm or 'n' to cancel

# 9. Clean up (remove the practice directory)
cd ..
rm -r practice_files
```

## Summary

- **Safety first**: `rm` permanently deletes files—there's no trash can or undo
- **Start slow**: Practice in safe locations, double-check paths, verify with `ls`
- **Creating**:
  - `mkdir`: Create directories (`mkdir -p` for nested structures)
  - `touch`: Create empty files
- **Copying**:
  - `cp`: Copy files
  - `cp -r`: Copy directories and their contents
- **Moving and renaming**:
  - `mv`: Move files/directories or rename them (same command for both)
- **Removing**:
  - `rm`: Delete files permanently
  - `rm -r`: Delete directories and their contents permanently
  - `rm -i`: Interactive mode (asks for confirmation—use this when learning!)
- **Best practices**:
  - Use `ls` to verify before deleting
  - Start with `rm -i` when learning
  - Never use `rm -rf /` or similar dangerous patterns
  - Practice in safe locations first

Remember: The command line gives you powerful tools, but with great power comes great responsibility. Always be deliberate and careful, especially with `rm`. When in doubt, use `rm -i` or double-check with `ls` first.

---
title: Permissions (Just Enough)
sidebar_position: 10
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Permissions control **who can do what** with files and directories.

You do not need to become a sysadmin or security expert. For most development work, you just need a gentle understanding of:

- Read / write / execute
- Basic `ls -l` output
- The idea of `chmod`
- Why `sudo` exists and when to be careful

## Read, write, execute (r, w, x)

In Unix-like systems, each file or directory has three basic kinds of permission:

- **Read (`r`)** — can view the contents
- **Write (`w`)** — can modify or delete
- **Execute (`x`)** — can run (for programs) or access (for directories)

Permissions are defined separately for:

- **Owner** — usually the user who created the file
- **Group** — a set of users
- **Others** — everyone else

## Seeing permissions with `ls -l`

Use `ls -l` to view permission details:

```bash
ls -l
```

Example output:

```bash
-rw-r--r--  1 alice  staff   1024 Dec  1 09:30 notes.txt
drwxr-xr-x  2 alice  staff     64 Dec  1 10:00 scripts
```

Break down the first column:

- `-rw-r--r--`

Position by position:

- 1st char:
  - `-` = regular file
  - `d` = directory
- Next 3 (`rw-`) → permissions for **owner**
- Next 3 (`r--`) → permissions for **group**
- Last 3 (`r--`) → permissions for **others**

So for `notes.txt`:

- Owner: `rw-` → can read and write
- Group: `r--` → can only read
- Others: `r--` → can only read

For `scripts`:

- `drwxr-xr-x`
- It’s a directory (`d`)
- Owner: `rwx` → can read, write, and execute
- Group: `r-x` → can read and execute
- Others: `r-x` → can read and execute

**Note**: “Execute” on a directory means:

- You can enter it (`cd scripts`)
- You can access files by name inside it

## `chmod`: Changing permissions (conceptual)

`chmod` (change mode) changes file permissions.

You’ll most often see it used to **make a file executable**:

```bash
chmod +x script.sh
```

This:
- Adds (`+`) execute permission (`x`)
- For owner, group, and others (by default)

Now you can run:

```bash
./script.sh
```

Common patterns:

```bash
# Make a script executable only for the owner
chmod u+x script.sh

# Remove write permission for others
chmod o-w file.txt
```

As a beginner, you don’t need to memorize all the combinations. Just recognize:

- `chmod` is how you **change** permissions
- `ls -l` is how you **inspect** permissions

## `sudo`: Superuser do (handle with care)

`sudo` lets you run a command with **elevated privileges** (usually as the `root` user).

```bash
sudo apt update
sudo apt install python3
```

This is powerful and potentially dangerous. With `sudo` you can:

- Install system packages
- Change system configuration
- Delete critical files

Guidelines:

- Use `sudo` only when:
  - You understand what the command is doing
  - It genuinely needs system-level access
- Avoid `sudo` for:
  - Day-to-day project work in your home directory
  - Random commands from the internet that you don’t understand

If you see a tutorial that prepends **every** command with `sudo`, be cautious.

### When `sudo` makes sense

Examples where `sudo` is normally appropriate:

- Installing system packages:
  ```bash
  sudo apt install git
  ```
- Editing system config:
  ```bash
  sudo nano /etc/hosts
  ```

Examples where you **usually don’t** want `sudo`:

- Installing Python packages for a project:
  ```bash
  # Better: use a virtual environment, not sudo
  pip install requests
  ```
- Running development servers in your home directory:
  ```bash
  python manage.py runserver
  ```

## Connecting permissions to errors

When you see:

```bash
Permission denied
```

Ask:

1. What file or directory is it complaining about?
2. Does `ls -l` show that:
   - You don’t have write permission?
   - You don’t have execute permission on a directory?
3. Should this really be a system-level operation?
4. Is the fix:
   - Change file ownership/permissions (advanced), or
   - Use `sudo` intentionally, or
   - Simply work in your home directory instead?

Often, the safest and correct solution is:

- “Don’t put your project in a protected system directory.”

## Windows notes

On Windows:

- NTFS permissions are different under the hood
- PowerShell has its own command set for permissions

However, if you use **WSL** (recommended for this guide), you’ll see the same Unix-style permissions model (`ls -l`, `chmod`, etc.) inside your Linux environment.

## Summary

- Permissions answer: **who can do what** with a file or directory.
- `ls -l` shows you:
  - File type (`-` or `d`)
  - Read, write, execute bits for owner, group, and others
- `chmod` changes permissions; most commonly you’ll see it to make scripts executable.
- `sudo` runs commands with elevated privileges—powerful but risky; use it deliberately, not as a habit.
- When in doubt, work in your home directory and keep project files there; reserve system-level changes for intentional, well-understood operations.


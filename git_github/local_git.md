---
title: Git Without GitHub
sidebar_position: 2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

In this guide, you’ll use Git **locally only**. No GitHub yet.

In this tutorial you will:

- Create a folder for a project
- Turn it into a Git repository
- Make your first commits
- Practice the day‑to‑day Git workflow that you’ll use constantly

## 1. Create your first local repository

Pick a place where you keep code projects, for example `~/code`.

If you're not familiar with these commands, see the [files and directories guide](/docs/command_line/files_directories).

```bash
# create your project folder
mkdir -p ~/code/my-first-git-project

# navigate into your project folder
cd ~/code/my-first-git-project
```

Now turn this folder into a Git repository:

```bash
git init
```

Git creates a hidden `.git` directory.  
That folder is where Git stores **all history and metadata**.

You now have:

- A **working directory**: `my-first-git-project/`
- An empty **repository** with no commits yet

Check the status:

```bash
git status
```

You should see something like:

```text
On branch main

No commits yet

nothing to commit (create/copy files and use "git add" to track)
```

## 2. Create a file and see what Git notices

Create a simple file:

```bash
echo "Hello Git!" > notes.txt
```

Learn more about [viewing and editing files](/docs/command_line/viewing_editing_files) in the command line.

Check status again:

```bash
git status
```

Now you’ll see:

```text
Untracked files:
  (use "git add <file>..." to include in what will be committed)
    notes.txt
```

### Tracked vs untracked

- **Untracked**: Git sees the file exists, but is not tracking it yet
- **Tracked**: Git is watching the file for changes and can include it in commits

New files start as **untracked** until you explicitly add them.

## 3. Stage and commit your first change

### Step 1: Stage the file

Add `notes.txt` to the staging area:

```bash
git add notes.txt
```

Check status:

```bash
git status
```

You should see:

```text
Changes to be committed:
  (use "git restore --staged <file>..." to unstage)
    new file:   notes.txt
```

This means:

- The **working directory** and **staging area** now include `notes.txt`
- The **repository** still has no commits

### Step 2: Create your first commit

```bash
git commit -m "Add initial notes file"
```

Git opens a new entry in the project’s history with:

- The content of the staged changes
- Your name and email (from `git config`)
- The commit message

Check the log:

```bash
git log --oneline
```

You should see one commit, something like:

```text
abc1234 Add initial notes file
```

You’ve just:

- Edited the **working directory**
- Staged changes into the **staging area**
- Saved a snapshot into the **repository**

## 4. The everyday Git loop

Most of your time with Git follows this simple cycle:

1. **Edit** files in your editor
2. **See what changed**
3. **Stage** the changes you want to keep
4. **Commit** those staged changes with a clear message

Let’s walk through this with your `notes.txt` file.

### Step 1: Edit a file

Open `notes.txt` in your editor and make a few changes, e.g.:

```text
Hello Git!

- Learn how commits work
- Practice staging changes
- Push to GitHub later
```

### Step 2: Check what changed

```bash
git status
```

You’ll see:

```text
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
    modified:   notes.txt
```

To see the actual line‑by‑line changes:

```bash
git diff
```

### Step 3: Stage the changes

You can stage everything:

```bash
git add .
```

Or just a specific file:

```bash
git add notes.txt
```

Check status:

```bash
git status
```

You should now see `changes to be committed`.

### Step 4: Commit with a meaningful message

```bash
git commit -m "Expand notes with learning checklist"
```

Run:

```bash
git log --oneline
```

Now you have **two** commits forming a simple history.

## 5. Writing good commit messages

Commit messages are tiny pieces of documentation. Good messages make history **readable**.

Some tips:

- Use the **present tense** (“Add feature” not “Added feature”)
- Explain **why** the change exists, not just what files changed
- Keep it short but specific:
  - `Fix login bug when username is blank`
  - `Refactor user service to separate validation`

Avoid:

- `misc changes`
- `fix`
- `wip` (work‑in‑progress) as a final commit message

## 6. Summary: Git without GitHub

You’ve learned the 90% workflow you’ll use every day:

```text
edit files → git status → git diff → git add → git commit
```

At this point:

- Your project is version‑controlled locally
- You can see its history with `git log`
- You can safely experiment, knowing you can always go back to an earlier commit

Next, you’ll learn what **GitHub** adds on top—remotes, backups, and collaboration—and then connect this local repository to GitHub.


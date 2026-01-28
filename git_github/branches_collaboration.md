---
title: Branches & Collaboration
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

Branches let you **experiment safely** without breaking your main code.  
GitHub then gives you tools (like pull requests) to share and review those changes.

This guide focuses on a **simple, beginner‑friendly branching workflow**—no rebasing or advanced history rewriting.

## 1. What is a branch?

So far, you can imagine your Git history like this:

```text
commit A  →  commit B  →  commit C
```

A **branch** is just a **named pointer** to a specific commit.

- `main` is usually the default branch
- When you create a new branch, you’re saying:

> “Start a new line of development from this commit.”

Conceptually:

```text
           feature-login
          /
commit A — B — C  ← main
```

Both branches share history up to a point, then diverge.

## 2. Why use branches?

Branches are powerful because they let you:

- Keep `main` (or `master`) **stable**
- Experiment or build features in isolation
- Review changes before merging them into the main line of development

Common uses:

- **Feature branches**: `feature/signup-form`
- **Bugfix branches**: `fix/login-crash`
- **Experiment branches**: `spike/new-idea`

## 3. Creating and switching branches

Start from your local repository’s `main` branch:

```bash
git status
```

Make sure you’re on `main` and your working directory is clean (no uncommitted changes).

### Create and switch to a new branch

```bash
git checkout -b feature-notes-formatting
```

This does two things:

1. Creates a new branch called `feature-notes-formatting`
2. Checks it out (switches your working directory to that branch)

You can confirm:

```bash
git branch
```

The current branch will have a `*` next to it.

## 4. Make commits on your feature branch

Now make some changes—edit files, run tests, etc. Then:

```bash
git status
git add .
git commit -m "Improve notes formatting and headings"
```

You’ve just added a commit **on your feature branch**, not on `main`.

Your history conceptually:

```text
commit A — B — C      ← main
             \
              D       ← feature-notes-formatting
```

## 5. Merging a branch back into `main`

Once you’re happy with your changes:

1. Switch back to `main`
2. Merge the feature branch into it

```bash
git checkout main
git merge feature-notes-formatting
```

If Git can combine the changes automatically, you’ll see a “fast‑forward” or “merge” message.

Your history becomes:

```text
commit A — B — C — D  ← main, feature-notes-formatting
```

At this point you can optionally delete the feature branch:

```bash
git branch -d feature-notes-formatting
```

## 6. Pulling changes from GitHub

When you work with a remote (like GitHub), others may push commits to the same branch.

To **update your local branch** with the latest remote changes:

```bash
git pull
```

**This is equivalent to:**

- `git fetch` (download new commits from the remote)
- `git merge` (merge them into your current branch)

**If:**

- No one else has changed the parts of the code you’re working on

Git will usually do a **fast‑forward**:

```text
Local:   A — B
Remote:  A — B — C
```

After `git pull`, your local branch just walks forward to match the remote.

If both you and someone else changed the same lines, Git may ask you to resolve a **merge conflict**. That’s normal—take your time, read the conflict markers, and decide what the final version should be.

## 7. GitHub collaboration basics

Once your branch is on GitHub, you can open a **pull request (PR)**.

The typical flow:

1. Create a branch locally
2. Commit your changes
3. Push the branch to GitHub:

   ```bash
   git push -u origin feature-notes-formatting
   ```

4. On GitHub, open a **pull request** from `feature-notes-formatting` into `main`
5. Teammates review your changes, leave comments, and request updates
6. Once approved, the PR is merged and your changes land on `main`

Even when working solo, PRs can still be useful:

- They give you a clean diff of what’s about to change
- They create a documented discussion thread for major changes

## 8. Forks vs collaborators (high level)

There are two common ways to contribute to a repository on GitHub:

- **Collaborator**:
  - You’re added directly to the repo with write access
  - You can create branches in the main repository
- **Fork**:
  - You create your own copy (“fork”) of the repository under your account
  - You make changes in your fork
  - You open a pull request **from your fork** back to the original repo

Forks are common in open source, where maintainers don’t want to give write access to everyone.

## 9. Summary

You’ve learned how to:

- Use branches to isolate work and keep `main` stable
- Merge branches back into `main` once they’re ready
- Pull updates from GitHub to stay in sync
- Think about pull requests, forks, and collaborators at a high level

Next, you’ll look at common Git mistakes beginners make—and how to recover from them without panic.


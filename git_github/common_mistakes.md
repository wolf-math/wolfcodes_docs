---
title: Common Git Mistakes (and How to Fix Them)
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

Everyone makes mistakes with Git.  
The goal of this guide is to teach you **calm recovery**, not perfection.

> When something goes wrong, stop, breathe, and read the error message slowly.

## 1. “I forgot to commit”

Symptom:

- You’ve been editing files for a while
- You realize you haven’t committed anything

Good news: this is easy to fix.

### See what changed

```bash
git status
git diff
```

If the changes are all related, stage and commit them:

```bash
git add .
git commit -m "Describe what you just did"
```

If the changes should be split into multiple commits, you can:

- Stage them in pieces (by file or even by hunk), or
- Use your editor or `git add -p` (interactive) once you’re more comfortable

For beginners, **one reasonable commit is better than none**.

## 2. “I committed the wrong thing”

Maybe you:

- Committed a debug print
- Included the wrong file
- Forgot to stage one important file

If you **haven’t pushed yet**, you have lots of safe options.

### Option 1: Add a new “fixup” commit

Simplest and safest:

1. Fix the code
2. Commit again

```bash
git add .
git commit -m "Fix accidental changes in previous commit"
```

Your history stays honest and easy to follow.

### Option 2: Undo the last commit but keep your changes (soft reset)

If you just made a commit and realize the message or contents are wrong, and you **haven’t pushed**:

```bash
git reset --soft HEAD~1
```

This:

- Moves `HEAD` back one commit
- Keeps all the changes from that commit **staged**

You can then:

- Adjust what’s staged if needed
- Create a new commit with a better message:

```bash
git commit -m "Better commit message"
```

> Avoid using more destructive options like `git reset --hard` until you’re comfortable with Git and have backups.

## 3. “I pushed to main by accident”

This is very common, especially when teams prefer feature branches.

### If you’re working alone

If the change is fine but just landed on `main` too early:

- You can usually leave it and adjust your workflow next time:
  - Create a branch **before** you start working
  - Push that branch and use pull requests

If the change is **truly wrong** and you pushed it:

- The safest approach is often:
  - Create a **new commit** that reverts or fixes the bad change
  - Avoid rewriting history on shared branches unless you know what you’re doing

### If you’re on a team

Some teams have rules like “no direct pushes to main”.  
If you accidentally push:

1. Let the team know
2. Open a pull request to revert or fix the change if needed
3. Adjust your local workflow:
   - Make a habit of creating branches: `git checkout -b feature-name`

## 4. Undoing changes to a file you haven’t committed

Symptom:

- You changed a file
- You haven’t committed yet
- You decide you want to throw those local changes away

### Discard changes in the working directory

If you’re sure you want to discard local modifications to a file:

```bash
git restore path/to/file
```

This resets the file to match the last commit on the current branch.

To discard **all** modified files (use with care):

```bash
git restore .
```

> This only affects **uncommitted** changes. Once something is committed, you use different tools.

## 5. “Git is showing me a scary error message”

Git error messages can look intimidating, but they usually contain:

- What went wrong
- What Git expected
- A hint about what to do next

General approach:

1. **Scroll up** to read the *first* error line
2. Look for phrases like:
   - “would be overwritten by merge”
   - “You have divergent branches”
   - “Your local changes would be overwritten”
3. Don’t keep guessing—look up the exact error message if needed

Two very common cases:

### Case 1: “Your local changes would be overwritten by merge”

This means:

- You ran something like `git pull`
- Git needs to modify files that you’ve also changed locally

Options:

- Commit or stash your local changes first, then try again
- Or decide you don’t need those local changes and restore them

### Case 2: “fatal: refusing to merge unrelated histories”

This usually happens when:

- You created commits in a local repo
- The remote repo (GitHub) also has unrelated commits (e.g. created with a README)

Beginner‑friendly fix:

- Decide **which history matters**
- Often the easiest path is:
  - Start from the repo you care about most
  - Create a **fresh remote or local clone** to get back to a clean state

## 6. What to learn next

Once you’re comfortable with:

- Local Git workflows
- Connecting to GitHub
- Basic branching and merging
- Recovering from simple mistakes

You’re ready to explore:

- `.gitignore` for avoiding committing generated files and secrets
- GitHub Issues for tracking work
- Tags and releases for marking important versions
- More advanced history tools:
  - `git revert` for safe, explicit undo commits
  - `git rebase` for rewriting history on branches you haven’t shared yet

The most important habit is this:

> Make small, frequent commits with clear messages.  
> Small steps are easier to undo.


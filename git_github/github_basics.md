---
title: GitHub & Remotes
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

So far you’ve used Git **locally**: commits live only on your machine.  
GitHub adds **remotes**, collaboration tools, and a web UI on top of Git.

This guide focuses on **concepts**, not commands. The next guide shows you how to connect Git to GitHub step by step.

## 1. What GitHub adds on top of Git

Git handles:

- Local history (commits)
- Branches and merging
- Comparing versions

GitHub adds:

- **Remote repositories**: copies of your repo hosted in the cloud
- **Backups**: if your laptop dies, your code lives on GitHub
- **Collaboration tools**:
  - Pull requests
  - Code review
  - Issues
  - Wikis and documentation

You can think of it this way:

- **Git** = version control engine
- **GitHub** = collaboration platform built around Git

## 2. Local vs remote repositories

Every Git project can have:

- One **local repository** (your machine)
- Zero or more **remote repositories**

Most projects use one main remote called `origin`:

- `origin` usually points to a GitHub URL, e.g.  
  `git@github.com:username/my-project.git`

### Syncing local and remote

Once a remote exists, you:

- **Push** local commits **up** to GitHub
- **Pull** remote commits **down** to your machine

Conceptually:

```text
Local repo  ← git pull  ←  Remote (GitHub)
Local repo  → git push  →  Remote (GitHub)
```

Git keeps track of which local branches correspond to which remote branches (e.g. `main` ↔ `origin/main`).

## 3. Public vs private repositories

When you create a repository on GitHub, you choose:

- **Public**:
  - Visible to everyone
  - Great for open source, portfolios, and learning
- **Private**:
  - Only you (and invited collaborators) can see it
  - Good for work projects, experiments, or anything sensitive

You can change visibility later, but it’s best to think about it up front.

## 4. When do you actually need GitHub?

You **don’t need GitHub** for:

- Simple solo projects
- Quick experiments on your machine
- Temporary scripts or throwaway code

You **do want GitHub** when:

- You care about backup and not losing work
- You want to show your work to others (portfolio)
- You collaborate with other people
- You work on open source or company projects

It’s completely fine to:

1. Start a project locally
2. Get a few commits in
3. Only later decide, “This is worth putting on GitHub”

## 5. Pull requests and collaboration (high level)

GitHub’s most important collaboration feature is the **pull request (PR)**.

At a high level:

- You create a **branch** for a change
- You push that branch to GitHub
- You open a **pull request** asking to merge your changes into a main branch (often `main`)
- Teammates:
  - Review the code
  - Leave comments
  - Suggest or request changes
- Once everyone is happy, the PR is merged

You can think of a PR as:

> “Here is a set of commits I’d like to merge. Let’s talk about it first.”

We’ll revisit PRs after you’re comfortable with:

- Local Git
- Connecting to a remote
- Basic branching

## 6. The `gh` CLI (GitHub from your terminal)

GitHub provides a command‑line tool called **`gh`**:

- Lets you log in once and then interact with GitHub from the terminal
- Can create repositories and pull requests without leaving your shell

In the next guide, you’ll:

- Install `gh`
- Authenticate with GitHub using SSH
- Create a GitHub repository
- Connect your local Git repository to that remote

## 7. Summary

You now know:

- How GitHub relates to Git
- What a **remote** is and why `origin` matters
- When GitHub is useful vs when local Git is enough
- What pull requests are at a conceptual level

Next up: you’ll **connect your local Git repo to GitHub**, using your existing project as a starting point.


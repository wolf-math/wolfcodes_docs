---
title: Git Fundamentals
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## Who this guide is for

This is a **beginner‑friendly crash course** in Git and GitHub.  
It assumes:

- You can do very basic [terminal navigation](/docs/command_line/files_directories) (`cd`, `ls`, `mkdir`)
- You understand [how command line commands work](/docs/command_line/programs_arguments_flags)
- You have a code editor (VS Code is a great default)
- You are comfortable copying and pasting commands

You **do not** need to know any Git yet.

## 1. What problem does Git solve?

Imagine working on a project without version control:

- You copy folders like `my-app-final`, `my-app-final-v2`, `my-app-final-v3-for-real`
- You accidentally overwrite working code with a broken experiment
- You can’t easily see *what* changed or *when*
- Sharing changes with others is done by zipping folders or emailing files

Git fixes this by being a **version control system**:

- It tracks changes to your project over time
- It lets you move backward and forward through history
- It lets multiple people work on the same code without stepping on each other

### Git vs GitHub

It’s very common to mix these up:

- **Git**: a tool that lives on your computer.  
  It tracks versions of your files in a **repository** (or "repo").
- **GitHub**: a website that hosts Git repositories in the cloud.  
  It adds collaboration features like pull requests, issues, and code review.

You can use **Git without GitHub** (locally only), but you can’t really use GitHub without Git.

### Core vocabulary

You’ll see these terms a lot:

- **Repository (repo)**: the project that Git is tracking.  
  A folder on your machine that has a hidden `.git` folder inside.
- **Commit**: a snapshot of your project at a moment in time, with a message.
- **History**: the ordered list of commits that shows how your project evolved.
- **Local vs remote**:
  - **Local**: on your computer
  - **Remote**: hosted somewhere else (e.g. GitHub)

Keep these in mind as we build a mental model.

## 2. How Git thinks: the core mental model

When Git confuses people, it’s usually because they don’t have a mental model.  

Git thinks in **three main areas**:

1. **Working directory**
2. **Staging area**
3. **Repository (history)**

### Working directory

This is just your project folder:

- You open files in your editor
- You add, delete, or modify code
- Nothing here is permanent yet from Git’s perspective

### Staging area (the “waiting room”)

The staging area is where you tell Git:

> “These are the exact changes I want in my next snapshot.”

Commands like:

```bash
git add file.py
git add .
```

take changes from the **working directory** and move them into the **staging area**.

You can think of the staging area as:

- A checklist of changes you’re about to commit
- A way to group related edits into a single meaningful snapshot

### Repository (history of commits)

**When you run:**

```bash
git commit -m "Describe the change"
```

**Git:**

- Takes whatever is in the **staging area**
- Saves it as a **commit** in the **repository**
- Records:
  - Exactly which files changed
  - The content of those changes
  - Who made the commit and when
  - Your commit message

From then on, that commit is part of your project’s **history**.

### Commits are snapshots, not just diffs

It’s useful to imagine each commit as a **snapshot of your entire project** at a moment in time.

- Git stores these snapshots efficiently (under the hood it uses diffs)
- But conceptually you can think:
  - Commit A = what the whole project looked like at time A
  - Commit B = what the whole project looked like at time B

This makes it easy to:

- Go back to how the project looked yesterday
- Compare “before” and “after” for a bug fix
- Understand the story of the codebase over time

### A simple picture

You can imagine your work flowing like this:

```text
Working directory  →  Staging area  →  Repository (commits)
     (edit)             (git add)          (git commit)
```

And over time, commits form a **history**:

```text
commit A  →  commit B  →  commit C  →  ...
```

For now, we’ll assume this history is a straight line.  
Later, when we talk about **branches**, we’ll see how Git lets histories split and merge safely.

## 3. Installing Git

Before we can use Git, we need to make sure it’s installed.

### Check if Git is already installed

Open your terminal and run:

```bash
git --version
```

If you see something like:

```text
git version 2.45.0
```

you’re good to go.

If you get an error like `command not found`, install Git using the instructions below.

### Install Git on macOS

You have two common options:

1. **Xcode Command Line Tools** (simple)
2. **Homebrew** (recommended if you already use Homebrew)

**Option 1: Xcode Command Line Tools**

```bash
xcode-select --install
```

Follow the prompts. This installs Git and other developer tools.

**Option 2: Homebrew**

If you use [Homebrew](https://brew.sh/):

```bash
brew install git
```

### Install Git on Linux

Use your distribution’s package manager:

```bash
# Debian/Ubuntu
sudo apt update
sudo apt install git

# Fedora
sudo dnf install git

# Arch Linux
sudo pacman -S git
```

### Install Git on Windows

Install **Git for Windows**:

- Go to `https://gitforwindows.org/`
- Download the installer
- Accept the defaults unless you have a specific reason not to

This gives you:

- Git
- A terminal called **Git Bash**, which is a good shell for beginners

### Basic Git configuration

Once Git is installed, run these commands to tell Git who you are.

Replace the placeholders with your actual name and email:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

You only need to do this **once per machine**.

Git will now attach this identity to your future commits.

## 4. What’s next?

You now have:

- A mental model of how Git thinks (working directory → staging area → commits)
- Git installed on your machine
- Your name and email configured

Next, we’ll create your **first local repository** and make your first commits **without GitHub**. This keeps things simple and lets you get comfortable with Git itself before adding remotes and collaboration.


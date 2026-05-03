---
title: Using the Command Line in Real Projects
sidebar_position: 12
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

So far we’ve focused on **how** the command line works.

This page focuses on **why developers keep using it every day**, and how it fits into real workflows with tools like Git, Python, Node, and Docker.

You don’t need to master all of these at once. The goal is to see how the pieces connect.

## Typical project workflow with the CLI

In a day-to-day development project, the command line is usually where you:

- Navigate to your project
- Create and activate environments
- Install dependencies
- Run servers, scripts, and tests
- Use Git

The GUI editor (VS Code, etc.) is usually where you:

- Edit code
- Browse files
- Use integrated tools

The command line and editor are **partners**, not competitors.

## Git: version control from the CLI

[Git](/docs/git_github/fundamentals) is primarily a command line tool, even if your editor adds buttons on top.

Common commands:

```bash
# Check what changed
git status

# See the history
git log

# Stage changes
git add file1.py file2.py
git add .

# Commit with a message
git commit -m "Describe what changed and why"

# Push to remote
git push
```

Learn more about these commands in the [Git basics guide](/docs/git_github/local_git).

Why the CLI is a good fit for Git:

- Commands are **precise and repeatable**
- History is textual and easy to share
- Scripts and CI systems use the same commands

You don’t need every Git feature to start. Even:

```bash
git status
git add .
git commit -m "Initial commit"
git push
```

gets you very far.

## Python projects and virtual environments

Python is a good example of how the CLI and environment concepts come together. Learn more about [virtual environments](/docs/python/guides/standard_library/virtual_env) in the Python documentation.

### Creating a virtual environment

From your project directory:

```bash
python -m venv .venv
```

This uses Python's [`-m` flag](/docs/python/guides/standard_library/modules) to run the `venv` module.

This:

- Creates a `.venv` directory with a project-specific Python installation

### Activating the virtual environment

On macOS/Linux/WSL:

```bash
source .venv/bin/activate
```

On Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

After activation:

- Your shell prompt usually changes
- `python` and `pip` now point into `.venv`

You can confirm with:

```bash
which python
which pip
```

### Installing dependencies

With the virtual environment active:

```bash
pip install requests
pip install fastapi uvicorn
```

Often you’ll keep dependencies in a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Running scripts and apps

Still inside your project directory and virtual environment:

```bash
python app.py
python -m module_name
pytest
```

The command line gives you:

- **One place** to run all of these tools
- Control over **which environment** they run in

## Node / JavaScript projects

[Node](/docs/javascript/guides/basics/running_javascript) and npm also lean heavily on the CLI. If you're new to JavaScript, start with the [JavaScript basics guide](/docs/javascript/guides/basics/intro).

Common patterns:

```bash
# Initialize a new project
npm init

# Install dependencies
npm install react
npm install --save-dev typescript

# Run scripts defined in package.json
npm run dev
npm run build
npm test
```

Here, the command line is how you:

- Install tools and libraries
- Run dev servers and build steps
- Plug into project-specific workflows (`npm run ...`)

## Docker and containers (later in your journey)

You don’t need Docker on day one, but it’s a good example of why the CLI matters long-term.

Typical commands:

```bash
docker build -t my-app .
docker run -p 8000:8000 my-app
docker ps
docker logs container-id
```

Why containers lean on the CLI:

- Scripts and CI systems need **text-based commands**
- You often repeat the same operations many times
- Copy-pasteable, shareable commands are essential

Even if you start with GUI tools for Docker, the underlying operations are almost always command line invocations.

## Automation and reproducibility

One of the biggest reasons developers love the CLI:

> You can write down **exactly** what you did, and someone else (or future you) can run the same commands.

Examples:

```bash
# setup.sh
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

```bash
# run_dev.sh
source .venv/bin/activate
export FLASK_ENV=development
flask run
```

Instead of a fuzzy “click this, then that, then maybe this”, you have:

- A **documented sequence** of commands
- A script you can run again tomorrow
- Something that can be checked into Git and shared with your team

## Where to practice these skills

Some ideas for practicing CLI use in real projects:

- Create a small Python or Node project
- Use Git from the command line:
  - `git status`, `git add`, `git commit`, `git log`
- Use a virtual environment or project-local tools
- Run a development server:
  - `python -m http.server`
  - `npm run dev`
  - `uvicorn app:app --reload`

The goal is not to memorize every command—it’s to get comfortable with:

- Navigating into your project
- Running core workflows from the terminal
- Reading and responding to output and errors

## Summary

- The command line is where you **orchestrate** real projects: Git, environments, servers, tests, and tools.
- Editors are for writing code; the CLI is for **running** and **managing** it.
- Python, Node, Docker, and many other ecosystems assume you’re comfortable with basic shell usage.
- Over time, you’ll build small collections of commands and scripts that make your own workflows fast, predictable, and sharable.


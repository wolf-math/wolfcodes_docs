---
title: Virtual Environments
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
## What is a virtual environment?

A **virtual environment** is an isolated Python environment that allows you to install packages separately from your system Python installation. Each virtual environment has its own Python interpreter and its own set of installed packages, completely separate from other projects and your system Python.

Think of it like a separate workspace for each project. You can have different versions of the same package in different virtual environments without conflicts.

If you're not familiar with command line navigation, see the [files and directories guide](/docs/command_line/files_directories). To understand how commands work, see [programs, arguments, and flags](/docs/command_line/programs_arguments_flags).

```bash
# Create a virtual environment
python -m venv <environment_name>

# Activate it (on Windows)
<environment_name>\Scripts\activate

# Activate it (on macOS/Linux)
source <environment_name>/bin/activate
```

## Why this matters

Virtual environments are essential for Python development because they solve several critical problems:

- **Dependency isolation**: Different projects can use different versions of the same package without conflicts
- **Reproducibility**: You can ensure everyone working on a project uses the same package versions
- **Clean system**: Keeps your system Python installation clean and avoids "dependency hell"
- **Version management**: Test your code with different package versions easily
- **Deployment**: Match your development environment to production

Without virtual environments, installing packages globally can lead to:
- Version conflicts between projects
- Breaking system tools that depend on specific package versions
- Difficulty reproducing bugs (works on your machine, but not others')
- Uninstalling a package breaking other projects

Using virtual environments is considered a best practice and is essential for any serious Python development.

## Creating a virtual environment

Python 3.3+ includes the `venv` module for creating virtual environments. The process is straightforward:

### Basic creation

```bash
python -m venv venv
```

This creates a new directory called `venv` (you can name it anything) containing:
- A copy of the Python interpreter
- A `pip` installation for installing packages
- Scripts to activate/deactivate the environment

### Specifying Python version

If you have multiple Python versions installed, you can specify which one to use:

```bash
# Use Python 3.11 specifically
python3.11 -m venv venv

# Or use the full path
/usr/bin/python3.11 -m venv venv
```

### Custom location

You can create the virtual environment in any location:

```bash
# Create in a specific directory
python -m venv /path/to/myproject_env

# Create in the current directory with a custom name
python -m venv .venv
```

## Activating a virtual environment

Once created, you need to **activate** the virtual environment before using it. Activation modifies your shell's PATH so that commands like `python` and `pip` point to the virtual environment's versions. Learn more about [environment variables and PATH](/docs/command_line/environment_and_context) in the command line guide.

### On Windows (Command Prompt)

```cmd
venv\Scripts\activate
```

### On Windows (PowerShell)

```powershell
venv\Scripts\Activate.ps1
```

If you get an execution policy error, run:
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### On macOS and Linux

```bash
source venv/bin/activate
```

### Verifying activation

When activated, you'll see the environment name in your prompt:

```bash
(venv) $ python --version
Python 3.11.5

(venv) $ which python
/path/to/venv/bin/python
```

The `(venv)` prefix indicates the virtual environment is active.

## Deactivating a virtual environment

To exit the virtual environment and return to your system Python:

```bash
deactivate
```

This command works on all platforms and removes the environment name from your prompt.

## Installing packages in a virtual environment

Once activated, use `pip` normally—packages install into the virtual environment:

```bash
# Activate first
source venv/bin/activate

# Install packages
pip install requests
pip install flask==2.3.0
pip install numpy pandas matplotlib

# List installed packages
pip list

# Show package information
pip show requests
```

All packages install into the virtual environment's `site-packages` directory, completely isolated from your system Python.

## Managing dependencies

### Creating a requirements file

Save your project's dependencies to a file:

```bash
pip freeze > requirements.txt
```

This creates a `requirements.txt` file listing all installed packages and their versions:

```
requests==2.31.0
flask==2.3.0
numpy==1.24.3
pandas==2.0.3
```

### Installing from requirements.txt

Others (or you on a different machine) can recreate the environment:

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate

# Install all dependencies
pip install -r requirements.txt
```

This ensures everyone uses the same package versions.

## Virtual environment best practices

**1. One environment per project**

Create a separate virtual environment for each project:

```bash
project1/
  venv/
  app.py

project2/
  venv/
  app.py
```

**2. Don't commit the environment**

Add the virtual environment directory to `.gitignore`:

```gitignore
# Virtual environments
venv/
env/
.venv/
ENV/
```

Commit `requirements.txt` instead, not the entire `venv/` directory.

**3. Use descriptive names**

Name your environment clearly:

```bash
# Good
python -m venv myproject_env
python -m venv django_blog_env

# Less clear
python -m venv env
python -m venv test
```

**4. Keep requirements.txt updated**

Update `requirements.txt` whenever you install new packages:

```bash
pip install new-package
pip freeze > requirements.txt
```

**5. Use consistent Python versions**

Specify the Python version in your project documentation:

```bash
# Use Python 3.11 for this project
python3.11 -m venv venv
```

## Common workflows

### Starting a new project

```bash
# 1. Create project directory
mkdir myproject
cd myproject

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
source venv/bin/activate  # macOS/Linux
# or
venv\Scripts\activate  # Windows

# 4. Install packages
pip install flask requests

# 5. Save dependencies
pip freeze > requirements.txt
```

### Working on an existing project

```bash
# 1. Clone or navigate to project
cd existing-project

# 2. Create virtual environment
python -m venv venv

# 3. Activate it
source venv/bin/activate

# 4. Install dependencies
pip install -r requirements.txt
```

### Switching between projects

```bash
# Work on project 1
cd project1
source venv/bin/activate
# ... do work ...

# Switch to project 2
deactivate
cd ../project2
source venv/bin/activate
# ... do work ...
```

## Troubleshooting

### Virtual environment not found

If you get "No such file or directory", make sure you're in the right directory and the environment was created:

```bash
# Check if venv exists
ls -la venv/  # macOS/Linux
dir venv\     # Windows

# Recreate if needed
python -m venv venv
```

### Wrong Python version

If the virtual environment uses the wrong Python version, delete it and recreate with the correct version:

```bash
# Remove old environment
rm -rf venv  # macOS/Linux
rmdir /s venv  # Windows

# Create with correct version
python3.11 -m venv venv
```

### Packages not found after activation

Make sure the virtual environment is activated (check for `(venv)` in your prompt) and packages were installed in the activated environment:

```bash
# Verify activation
which python  # Should point to venv/bin/python

# Reinstall if needed
pip install -r requirements.txt
```

## Alternatives to venv

While `venv` is built into Python and recommended, there are alternatives:

- **virtualenv**: Older tool, similar to `venv` but works with Python 2
- **conda**: Package and environment manager, popular in data science
- **poetry**: Modern dependency management with virtual environment handling built-in
- **pipenv**: Combines `pip` and `virtualenv` with a `Pipfile` for dependencies

For most projects, `venv` is the simplest and most widely supported option.

## Summary

Virtual environments are essential for Python development. They provide:

- **Isolation**: Each project has its own package environment
- **Reproducibility**: `requirements.txt` ensures consistent setups
- **Safety**: Protects your system Python installation
- **Flexibility**: Easy to test different package versions

Always use a virtual environment for your Python projects. It's a small step that prevents many headaches down the road.

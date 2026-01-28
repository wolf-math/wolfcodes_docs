---
title: The Shell
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
## Terminal vs. shell: a crucial distinction

When you open a command line interface, you're actually using **two different things**:

- **Terminal**: The window or application you see
- **Shell**: The program inside the terminal that interprets your commands

This distinction is huge for beginners. Understanding it helps you know what you're actually working with and why things might look or behave differently.

### The terminal (the window)

The **terminal** is the visual application. It's the window that displays text. It's like a container that shows you what's happening.

Different terminal applications:
- **macOS**: Terminal.app, iTerm2, Hyper
- **Windows**: Command Prompt, PowerShell window, Windows Terminal
- **Linux**: GNOME Terminal, Konsole, xterm

All these are just different ways to display the same thing: a text interface.

### The shell (the program)

The **shell** is the actual program running inside the terminal that:
- Reads the commands you type
- Interprets what they mean
- Executes the programs
- Displays the output

The shell is what actually does the work. Different shells have different features, syntax, and capabilities.

## Why this matters

Understanding terminal vs. shell helps you realize:

1. **You can use different terminals with the same shell**: You might prefer one terminal application's appearance while using the same shell (like bash) in all of them.

2. **You can use different shells in the same terminal**: Your terminal window can run different shell programs (bash, zsh, etc.).

3. **Shell features are what matter**: When learning command line concepts, you're learning shell features, not terminal features.

4. **Commands depend on your shell**: Some commands work differently (or not at all) depending on which shell you're using.

## Common shells

Different operating systems come with different default shells, and you can install and use others.

### macOS and Linux

#### bash

**bash** (Bourne Again Shell) is one of the most widely used shells. It's been around since 1989 and is the default on many Linux distributions.

```bash
# You're probably using bash if your prompt ends with $
# Example: username@computer:~/Documents$
```

**Characteristics**:
- Very common and well-documented
- Good compatibility across systems
- Extensive scripting capabilities
- Widely used in tutorials and documentation

#### zsh

**zsh** (Z Shell) is the default shell on modern macOS (since macOS Catalina). It's built on bash but with additional features.

```bash
# You're probably using zsh if your prompt shows % or a fancy theme
# Example: ➜  ~ Documents
```

**Characteristics**:
- Default on modern macOS
- Enhanced auto-completion
- Better command history search
- More customization options
- Highly compatible with bash

:::note 
Most bash commands work in zsh, so if you learn bash concepts, they translate to zsh.
:::

:::tip Enhancing zsh with oh-my-zsh
I personally use zsh with **[oh-my-zsh](https://ohmyz.sh/)**, which is a configuration framework that makes zsh even more beginner-friendly and useful.

**Colors that help understanding**: oh-my-zsh adds color-coding to your command line. For example, file names appear in different colors, and git branches are highlighted. This visual feedback helps you quickly see what type of file you're looking at or what branch you're working on.

**Aliases**: oh-my-zsh includes shortcuts (called aliases) for common commands. Instead of typing long commands, you can use short versions. For example, you might type `gst` instead of `git status`, or `ll` instead of `ls -la`.

**Git tools**: oh-my-zsh includes helpful git shortcuts and information. Your prompt can show which git branch you're on, and there are quick shortcuts for common git operations.

These features make the command line more visual and easier to navigate, especially when you're just starting out. oh-my-zsh is optional—plain zsh works great too—but it's a popular way to enhance the experience.

Similar customization frameworks are available for all shells. bash has frameworks like bash-it, PowerShell has modules like oh-my-posh, and most shells support themes and plugins. These tools help make any shell more visual and beginner-friendly.
:::

### Windows

#### Command Prompt (cmd.exe)

The traditional Windows command line. Limited compared to modern shells.

```cmd
# You're probably using cmd if your prompt shows C:\>
# Example: C:\Users\YourName>
```

**Characteristics**:
- Built into Windows
- Different command syntax from Unix shells
- Limited scripting capabilities
- Not recommended for serious development work

#### PowerShell

A modern shell for Windows with more features and better scripting.

```powershell
# You're probably using PowerShell if your prompt shows PS
# Example: PS C:\Users\YourName>
```

**Characteristics**:
- More powerful than Command Prompt
- Uses objects instead of just text
- Better scripting language
- Good for Windows system administration

#### WSL (Windows Subsystem for Linux)

**WSL** allows you to run a Linux environment directly on Windows, including Linux shells like bash or zsh. This is the **recommended** option for Windows developers.

**Characteristics**:
- Runs actual Linux shells (bash, zsh, etc.)
- Same commands as macOS/Linux
- Access to Linux tools and utilities
- Best option for cross-platform development
- Lets you use the same tutorials and commands as other platforms

**Setting up WSL**: Install from Microsoft Store or using `wsl --install` in PowerShell.

## Checking which shell you're using

To see which shell you're currently using:

```bash
# Most shells support this
echo $SHELL

# Or check the process
ps -p $$
```

On Windows (PowerShell):
```powershell
echo $PSVersionTable.PSVersion
```

## Shell concepts, not vendor-specific commands

When learning the command line, you're learning **shell concepts** that apply across different shells:

### Universal concepts

These concepts work across bash, zsh, and other Unix-like shells:

- **Navigation**: Moving between directories (`cd`, `pwd`)
- **File operations**: Creating, reading, copying, moving files
- **Input/output redirection**: Sending output to files (`>`, `>>`)
- **Piping**: Connecting commands together (`|`)
- **Variables**: Storing and using values
- **Scripts**: Writing reusable command sequences

### Shell differences

While the concepts are similar, specific syntax can vary:

- **Variable syntax**: `$VAR` (bash/zsh) vs `$env:VAR` (PowerShell)
- **Path separators**: `/` (Unix) vs `\` (Windows cmd)
- **Wildcards**: `*` works similarly, but some patterns differ
- **Scripting**: Bash scripts (`.sh`) vs PowerShell scripts (`.ps1`)

### Focus on concepts

This guide focuses on **shell concepts** that work across systems. When you understand the concept (like "redirecting output"), you can apply it in any shell, even if the exact syntax differs slightly.

## Which shell should you use?

### For beginners

**macOS**: Use **zsh** (it's the default). Most bash tutorials work in zsh.

**Linux**: Use **bash** (usually the default). It's well-documented and widely used.

**Windows**: Use **WSL with bash**. This gives you the same experience as macOS/Linux and access to the same tutorials and commands.

### Why WSL for Windows?

WSL is recommended because:
- Same commands as other platforms
- Same tutorials apply
- Better for web development (most tools assume Unix-like environments)
- Easier to follow along with online guides
- Same scripting language as servers (most servers run Linux)

### Don't worry too much

For most tasks, the differences between bash and zsh are minimal. If you learn one, you can use the other easily. The core concepts are the same.

## Summary

- **Terminal** = The window/application you see
- **Shell** = The program interpreting your commands
- **Common shells**: bash, zsh (macOS/Linux), PowerShell, WSL (Windows)
- **Focus on concepts**: Learn shell concepts, not vendor-specific commands
- **WSL recommended**: Windows users should use WSL for the best experience

Remember: You're learning how shells work, not just memorizing commands. The concepts you learn will apply regardless of which terminal application you prefer or which shell you're using.

:::tip Quick reminder
If you're using zsh (especially on macOS), consider checking out [oh-my-zsh](https://ohmyz.sh/). It adds helpful colors, shortcuts, and git integration that make the command line more visual and easier to navigate as you learn.
:::

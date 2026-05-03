---
title: Writing and Running a Script
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

## What does it mean to write a shell script?

Writing a shell script means putting shell commands into a file so you can run them again later.

If the first guide answered:

> "What are shell scripts for?"

this guide answers:

> "What does one actually look like, and how do I run it?"

At the beginner level, that is the main job:

1. Create a file
2. Put commands in it
3. Run the file through the shell

## The smallest script

Here is the smallest useful example:

```bash
#!/usr/bin/env bash
echo "Hello from a script"
```

If you save that in a file named `hello.sh`, you have a shell script.

## What each line does

Let’s look at it line by line.

### The `#!` shebang

```bash
#!/usr/bin/env bash
```

This first line is called the **shebang**.

It tells the operating system which program should be used to run the script. In this case, it says:

> "Run this file with `bash`."

Using:

```bash
#!/usr/bin/env bash
```

is a common, portable way to say:

> "Find `bash` in the current environment and use it."

For this guide section, we are teaching **Bash-style shell scripts**, so using a Bash shebang keeps the examples consistent.

### The command lines

```bash
echo "Hello from a script"
```

This is just a normal shell command.

That is one of the most important things to understand:

> A shell script is not a different universe from the terminal.

It is mostly the same commands you would type interactively, just saved in a file.

## Saving the file

You can create a script in any text editor and save it with a name like:

```text
hello.sh
backup.sh
start-dev.sh
```

The `.sh` part is a common naming convention for shell scripts.

It is useful because it signals:

- this is a shell script
- this file is probably meant to be run

But the extension is only a convention. The shell does not require `.sh` as long as the file contents are valid and you run it correctly.

## Running the script with `bash`

The simplest way to run a script is to pass the file to `bash` directly:

```bash
bash hello.sh
```

This says:

> "Start the `bash` program, and give it `hello.sh` to run."

This is often the easiest way for beginners to start because it does not require changing file permissions first.

If the file contains:

```bash
#!/usr/bin/env bash
echo "Hello from a script"
```

then:

```bash
bash hello.sh
```

prints:

```text
Hello from a script
```

## Running the script as a program

Later, you will often run scripts like this:

```bash
./hello.sh
```

This feels more like running a normal program, but it requires one extra step: the file must be **executable**.

You can make it executable with:

```bash
chmod +x hello.sh
```

Then you can run:

```bash
./hello.sh
```

and the system will use the shebang to decide how to run it.

### Why `./hello.sh` instead of just `hello.sh`?

This is an important shell habit.

When you type a command, the shell usually searches for programs in the directories listed in your `PATH`.

Your current directory is often **not** searched automatically.

So:

```bash
hello.sh
```

usually will not work unless that file is in your `PATH`.

But:

```bash
./hello.sh
```

means:

> "Run the file named `hello.sh` from the current directory."

The `./` is not decoration. It tells the shell exactly where to look.

## Two common ways to run a script

For beginners, these are the two main patterns:

### Run it with `bash`

```bash
bash hello.sh
```

Use this when:

- you are just getting started
- you do not want to think about executable permissions yet
- you want to be explicit that Bash is running the file

### Run it directly

```bash
./hello.sh
```

Use this when:

- the script has a proper shebang
- the file is executable
- you want it to behave like a reusable tool

Both are valid. The second style is more common in real projects, but the first is often easier to understand at the beginning.

## A slightly more realistic example

Here is a tiny script you might actually keep:

```bash
#!/usr/bin/env bash
echo "Starting development server..."
cd ~/projects/my-app
npm run dev
```

This script:

1. prints a message
2. changes into a project directory
3. starts the dev server

That is already enough to be useful.

## How the shell reads a script

When Bash runs a script, it reads the file from top to bottom and executes each command in order.

For example:

```bash
#!/usr/bin/env bash
echo "One"
echo "Two"
echo "Three"
```

**Output:**

```text
One
Two
Three
```

The script is not mysterious. It is mostly:

> "Read the next line. Run it. Move to the next line."

Later you will learn conditionals, loops, functions, and arguments, but the top-to-bottom model is the foundation.

## Where to keep scripts

For personal practice, you can keep scripts anywhere.

For real projects, a common pattern is a folder like:

```text
scripts/
```

Examples:

```text
scripts/dev.sh
scripts/setup.sh
scripts/backup.sh
```

This makes scripts easier to discover and keeps them out of the way of your application code.

## Common mistakes

Here are the most common beginner problems when running a shell script.

### The file is not executable

If you try:

```bash
./hello.sh
```

and get a permission-related error, the file may not be executable yet.

Use:

```bash
chmod +x hello.sh
```

Then try again.

### You forgot `./`

If you try:

```bash
hello.sh
```

and the shell says the command was not found, the problem may simply be that the shell is not looking in the current directory.

Use:

```bash
./hello.sh
```

instead.

### The script uses the wrong shell

Some scripts behave differently in different shells.

If you write a Bash-style script, use a Bash shebang:

```bash
#!/usr/bin/env bash
```

and run it with Bash.

This matters more once you start using Bash-specific features, but it is a good habit from the start.

### You saved commands that only work from one directory

A script may assume it is being run from a certain place.

For example:

```bash
python manage.py runserver
```

only works if the script is in the right project context.

If a script depends on a directory, be explicit:

```bash
cd ~/projects/my-app
python manage.py runserver
```

That makes the script more predictable.

## Aliases vs scripts

This is a very good place to draw the line between two similar ideas:

- **alias**: a shortcut name for a command
- **script**: a file containing commands

They are related, but they are not the same thing.

### What an alias is

An alias is a custom shortcut you define inside your shell configuration.

Example:

```bash
alias gs="git status"
```

Now typing:

```bash
gs
```

runs:

```bash
git status
```

Aliases are great for:

- shortening commands you type often
- making personal command-line habits faster
- reducing repetitive typing for small interactive commands

## When to use an alias instead of a script

An alias is usually the better choice when:

- the task is just one command
- you want a quick personal shortcut
- the behavior does not need much logic

Examples:

```bash
alias gs="git status"
alias ll="ls -la"
alias serve="python -m http.server 8000"
```

These are basically convenience shortcuts.

## When to use a script instead of an alias

A script is usually the better choice when:

- you need multiple commands
- you want something you can save in a project
- you want something teammates can run too
- you want to add arguments, checks, or logic later

For example, this starts to feel like a script:

```bash
#!/usr/bin/env bash
cd ~/projects/my-app
source .venv/bin/activate
python manage.py runserver
```

You *could* try to squeeze that into an alias, but it becomes harder to read, harder to share, and harder to maintain.

That is a strong signal that a script is the better tool.

## A useful rule of thumb

Use this simple guideline:

- If you want a **shorter name for one command**, use an alias
- If you want a **reusable file of commands**, use a script

Aliases are for shortcuts.

Scripts are for workflows.

## Best practices

As you start writing scripts, keep these habits:

- Start with `bash script.sh` if direct execution still feels confusing
- Use a shebang like `#!/usr/bin/env bash`
- Give scripts descriptive names
- Keep early scripts short and focused
- Be explicit about directories when the task depends on location
- Move longer repeated workflows into scripts instead of giant aliases

You do not need to write large scripts right away. A small script that saves you a few repeated steps is already real progress.

## Summary

- Writing a shell script means saving shell commands in a file.
- The smallest useful script usually has a shebang and one command.
- You can run a script with `bash script.sh` or, after `chmod +x`, with `./script.sh`.
- `./` means "run this file from the current directory."
- Aliases are shortcuts for commands, while scripts are reusable files for workflows.
- When a task grows beyond a tiny shortcut, a script is usually the better choice.

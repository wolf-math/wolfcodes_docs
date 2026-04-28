---
title: Getting Started
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
## What is Python?

**Python** is a beginner-friendly programming language that is used for automation, web development, data work, artificial intelligence, and many other kinds of software. It is known for readable syntax, which makes it a strong first language and a practical everyday tool.

In this guide section, you will gradually use Python to build a small **vinyl record library tracker**. We will start tiny, with simple print statements and a few music-themed values, then grow that into a full project over time.

## Why this matters

Python is a great language for learning how programs work because it lets you focus on ideas instead of a lot of ceremony. You can write a tiny script in a few lines, but the same language can also power a complete application.

That makes Python a good fit for the guide project too. The same basics you use to print one record title today will eventually help you save, search, and organize a whole record collection.

## What you'll need

To get started with Python, you need:

1. **Python installed** on your computer (version 3.8 or newer)
2. **A text editor** or code editor (like VS Code, PyCharm, or even a simple text editor)
3. **A [terminal or command prompt](/docs/command_line/what_it_is)** to run your programs

### Checking if Python is installed

Open your terminal (or command prompt on Windows) and type:

```bash
python --version
```

or

```bash
python3 --version
```

If Python is installed, you'll see something like `Python 3.11.5`. If you get an error, you'll need to [download and install Python](https://www.python.org/downloads/) first.

If you're not familiar with how command line commands work, see the [programs, arguments, and flags guide](/docs/command_line/programs_arguments_flags).

## Your first Python program

Let's start with the smallest kind of Python program: one that prints a message to the screen.

### Option 1: Using Python interactively

You can run Python code directly in an interactive session. Open your terminal and type `python` (or `python3`):

Use this for quick tests and experimentation. It's great for learning and trying out code snippets.

```python
>>> print("Now spinning: Are You Experienced")
Now spinning: Are You Experienced
```

That's it! You just ran your first Python program. The `print()` function displays whatever you put inside the parentheses.

### Option 2: Creating a Python file

For real programs, you'll usually write code in a file. Create a new file called `first_record.py` and add this line:

Use this for programs you want to save and run multiple times. This is how you'll write most of your Python code.

```python
print("Now spinning: Are You Experienced")
```

Save the file, then run it from your terminal:

```bash
python first_record.py
```

or

```bash
python3 first_record.py
```

You should see:

```text
Now spinning: Are You Experienced
```

Congratulations! You've written and run your first Python script.

## What just happened?

Let's break down what you did:

- **`print()`** is a built-in Python function that displays text (or other values) on the screen
- **`"Now spinning: Are You Experienced"`** is a [string](../types_variables/types), which is a piece of text enclosed in quotes
- When you ran the program, Python executed the `print()` function and displayed the message

## In the vinyl tracker

This first script is tiny, but it already lives in the same world as the final project.

```python
print("Vinyl Record Library Tracker")
print("Now spinning: Blue Train")
```

This is not a full app yet. It is just the smallest possible version of a music-focused program:

- it has output
- it has text
- it has a clear purpose

Later guides will teach you how to store record details in variables, group records into collections, and build this into a real terminal app.

## Next steps

Now that you've run your first program, you're ready to learn more. The next lessons will teach you:

- **Variables**: Storing and using data in your programs
- **Types**: Understanding different kinds of data (numbers, text, etc.)
- **Conditionals**: Making decisions in your code

For now, try changing the message so it prints a different artist or album:

```python
print("Vinyl Record Library Tracker")
print("Now spinning: Electric Ladyland")
print("Next up: Rumours")
```

Run it again and see all three lines appear. That small change is the beginning of writing your own programs.

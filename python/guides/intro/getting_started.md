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
## Welcome to Python!

Python is a powerful, beginner-friendly programming language used for everything from web development to data science, automation, and artificial intelligence. It's known for its clean, readable syntax that reads almost like English, making it an excellent choice for your first programming language.

## Why Python?

Python is designed to be easy to learn and use. Unlike some languages that require lots of setup and complex syntax, Python lets you focus on solving problems rather than fighting with the language itself. It's also incredibly versatile, so the same language you use to write a simple script can power major applications used by millions of people.

## What you'll need

To get started with Python, you need:

1. **Python installed** on your computer (version 3.8 or newer)
2. **A text editor** or code editor (like VS Code, PyCharm, or even a simple text editor)
3. **A [terminal or command prompt](/dev_env/command_line/what_it_is)** to run your programs

### Checking if Python is installed

Open your terminal (or command prompt on Windows) and type:

```bash
python --version
```

or

```bash
python3 --version
```

If you don't have Python installed you can set up your entire developer environment by following the steps [in the setup guide](/dev_env/setup/).

If you're not familiar with how command line commands work, see the [programs, arguments, and flags guide](/dev_env/command_line/programs_arguments_flags).

## Your first Python program

Let's start with the classic "Hello, World!" program. Writing your first program that prints "Hello World!" to the terminal, in any language, is one of the oldest developer traditions. 

### Option 1: Using Python interactively

You can run Python code directly in an interactive session. Open your terminal and type `python` (or `python3`). A new environment for writing Python code will open. 

:::note
Some operating systems still use old Python 2 code, so writing `python3` is sometimes necessary. We will not be learning any Python 2 code here.
:::


Use this for quick tests and experimentation. It's great for learning and trying out code snippets.

```python
>>> print("Hello, World!")
Hello, World!
```

That's it! You just ran your first Python program. The `print()` function displays whatever you put inside the parentheses.

### Option 2: Creating a Python file

Use this for programs you want to save and run multiple times. This is how you'll write most of your Python code.

For real programs, you'll write code in a Python file. Create a new file called `hello.py` and add this line:


```python
print("Hello, World!")
```

Save the file, then run it from your terminal:

```bash
python hello.py
```

or

```bash
python3 hello.py
```

You should see:

```
Hello, World!
```

Congratulations! You've written and run your first Python program!

## What just happened?

- **`print()`** is a built-in Python function that displays text (or other values) on the screen
- **`"Hello, World!"`** is a [string](../types_variables/types), which is a piece of text enclosed in quotes
- When you ran the program, Python executed the `print()` function and displayed the message

## Next steps

Now that you've run your first program, you're ready to learn more! The next lessons will teach you:

- **Variables**: Storing and using data in your programs
- **Types**: Understanding different kinds of data (numbers, text, etc.)
- **Conditionals**: Making decisions in your code

But for now, take a moment to celebrate—you're officially a Python programmer! Try modifying your program to print different messages:

```python
print("Hello, World!")
print("Python is fun!")
print("I'm learning to code!")
```

Run it again and see all three messages appear. You're on your way!

---
title: How Python Runs Code
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
## What happens when Python runs your code?

Python executes your code step by step at runtime. Building a clear mental model of that process will make the rest of Python much easier to understand.

Even in the vinyl tracker project, Python is not looking at your whole app all at once. It is still just running one piece of code, then the next, in order.

## Why this matters

This topic explains why:

- variables must exist before you use them
- errors appear on specific lines
- some output appears before a crash
- program order matters in every guide that comes after this one

## Top to bottom execution

Python executes your code **line by line, from top to bottom**, just like reading a book:

```python
print("Loading Vinyl Record Library Tracker")
print("Checking collection")
print("Ready to browse records")
```

**What happens:**
1. Line 1 runs and prints `Loading Vinyl Record Library Tracker`
2. Line 2 runs and prints `Checking collection`
3. Line 3 runs and prints `Ready to browse records`

**Output:**
```text
Loading Vinyl Record Library Tracker
Checking collection
Ready to browse records
```

Python doesn't look ahead or jump around. It processes each line in order, one at a time.

## Runtime execution

Python executes code **when you run the program** (this is called "runtime"), not when you write it or save the file. This means:

- Python doesn't check for errors until it tries to run a line
- You can write code that has errors, and Python won't complain until it reaches that line
- The file can be opened and viewed without any problems. The errors only appear when Python tries to execute the code

```python
print("Opening collection")
print("Looking for favorite records")
print(unknown_record)  # Python does not discover this problem until this line runs
```

When you run this, Python will:
1. Run line 1 and print `Opening collection`
2. Run line 2 and print `Looking for favorite records`
3. Reach line 3 and **then** discover the error because `unknown_record` does not exist

Python runs the code up to the error, then stops.

## Variables are created when lines run

Variables don't exist until Python executes the line that creates them. You'll learn more about variables in the next section, but here's the key idea:

```python
print(record_title)  # Error! record_title does not exist yet
record_title = "Blue Train"
print(record_title)  # Works! record_title exists now
```

**Timeline:**
- Before line 1 runs: `record_title` does not exist
- Line 1 runs: Python tries to print `record_title`, but it does not exist
- Line 2 runs: `record_title` is created and set to `"Blue Train"`
- Line 3 runs: `record_title` now exists, so Python can print it

This is why order matters! You can't use a variable before it's created. Python reads your code from top to bottom, so everything must be created before you try to use it.

## Errors happen when execution reaches the line

Errors don't happen when you write code or open a file. They happen when Python tries to execute a problematic line:

```python
print("Loading records")
print("Calculating collection value")
print(10 / 0)  # Error happens here, when Python runs this line
print("Saving collection")  # Python never reaches this line
```

**What happens:**
1. Line 1 runs successfully
2. Line 2 runs successfully
3. Line 3 runs → Python tries to divide by zero → **Error occurs**
4. Line 4 never runs because Python stops at the error

**Output:**
```text
Loading records
Calculating collection value
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

This is important to understand: Python will run all the code up to the error, but nothing after it.

## Building the mental timeline

Think of Python execution as a timeline:

```text
Time →  line 1 runs → line 2 runs → line 3 runs → line 4 runs → ...
         title set     artist set    print runs     save runs
```

Each line:
- Only runs **after** the previous line finishes
- Can use variables created **before** it
- Can cause errors that **stop** execution
- Doesn't know about lines that come **after** it

This mental model will help you understand:
- Why variables must be created before use
- Why errors appear at specific lines
- How Python processes your code step by step

## In the vinyl tracker

Even the final project follows this exact model.

When the capstone app starts, Python:

1. imports modules
2. creates values and helper functions
3. calls `main()`
4. loads the collection
5. shows the menu
6. waits for the user to choose an action

That may sound more advanced, but it is still the same basic rule: Python keeps moving through code in order.

## Summary

Understanding how Python runs code gives you a solid foundation:

- **Execution model:** Python runs code top to bottom, line by line, at runtime
- **Variables are created when lines run:** Variables don't exist until Python executes the line that creates them
- **Errors happen when execution reaches the line:** Python runs all code up to an error, then stops
- **Mental timeline:** Think of execution as a timeline—each line runs after the previous one finishes

This mental model will make everything else in Python easier to understand—from variables and conditionals to functions and beyond!

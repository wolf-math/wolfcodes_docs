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
Understanding how Python executes your code is crucial for learning Python effectively. Let's build a mental model of what happens when Python runs your program.

### Top to bottom execution

Python executes your code **line by line, from top to bottom**, just like reading a book:

```python
print("First")
print("Second")
print("Third")
```

**What happens:**
1. Line 1 runs → Python prints "First"
2. Line 2 runs → Python prints "Second"
3. Line 3 runs → Python prints "Third"

**Output:**
```
First
Second
Third
```

Python doesn't look ahead or jump around. It processes each line in order, one at a time.

### Runtime execution

Python executes code **when you run the program** (this is called "runtime"), not when you write it or save the file. This means:

- Python doesn't check for errors until it tries to run a line
- You can write code that has errors, and Python won't complain until it reaches that line
- The file can be opened and viewed without any problems. The errors only appear when Python tries to execute the code

```python
print("Hello")
print("World")
print(unknown_thing)  # This line has an error, but Python doesn't know until it tries to run it
```

When you run this, Python will:
1. Successfully run line 1 and print "Hello"
2. Successfully run line 2 and print "World"
3. Try to run line 3 and **then** discover the error (because `unknown_thing` doesn't exist)

Python runs the code up to the error, then stops.

### Variables are created when lines run

Variables don't exist until Python executes the line that creates them. You'll learn more about variables in the next section, but here's the key idea:

```python
print(name)  # Error! name doesn't exist yet
name = "Alice"
print(name)  # Works! name exists now, prints "Alice"
```

**Timeline:**
- Before line 1 runs: `name` doesn't exist
- Line 1 runs: Python tries to print `name`, but it doesn't exist → **Error**
- Line 2 runs: `name` is created and set to "Alice"
- Line 3 runs: `name` exists, so it prints "Alice"

This is why order matters! You can't use a variable before it's created. Python reads your code from top to bottom, so everything must be created before you try to use it.

### Errors happen when execution reaches the line

Errors don't happen when you write code or open a file. They happen when Python tries to execute a problematic line:

```python
print("This runs")
print("This also runs")
print(10 / 0)  # Error happens HERE, when this line runs
print("This never runs")  # Python never reaches this line
```

**What happens:**
1. Line 1 runs successfully and prints "This runs"
2. Line 2 runs successfully and prints "This also runs"
3. Line 3 runs → Python tries to divide by zero → **Error occurs**
4. Line 4 never runs because Python stops at the error

**Output:**
```
This runs
This also runs
Traceback (most recent call last):
  ...
ZeroDivisionError: division by zero
```

This is important to understand: Python will run all the code up to the error, but nothing after it.

### Building the mental timeline

Think of Python execution as a timeline:

```
Time →  Line 1 runs → Line 2 runs → Line 3 runs → Line 4 runs → ...
         x created   y created     print happens   ...
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

As you learn more about Python (variables, conditionals, functions), this foundation will make everything easier to understand!







## Summary

Understanding how Python runs code gives you a solid foundation:

- **Execution model:** Python runs code top to bottom, line by line, at runtime
- **Variables are created when lines run:** Variables don't exist until Python executes the line that creates them
- **Errors happen when execution reaches the line:** Python runs all code up to an error, then stops
- **Mental timeline:** Think of execution as a timeline—each line runs after the previous one finishes

This mental model will make everything else in Python easier to understand—from variables and conditionals to functions and beyond!

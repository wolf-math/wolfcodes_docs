---
title: The REPL vs Script
sidebar_position: 4
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
Python can run code in two different ways: **interactively** (REPL) or as a **script**. Understanding the difference prevents confusion.

### REPL (Interactive Mode)

**REPL** stands for "Read-Eval-Print Loop." It's what happens when you type `python` (or `python3`) in your terminal and see the `>>>` prompt.

**Characteristics:**
- Runs **one line at a time**
- Shows results **immediately** after each line
- Great for **testing** and **experimenting**
- Variables persist between lines (until you exit)

```python
>>> print("Hello")
Hello
>>> print("World")
World
>>> name = "Alice"
>>> print(name)
Alice
```

**When to use:** Testing code, trying things out, learning, debugging

### Script (File Mode)

A **script** is a `.py` file that Python runs from top to bottom.

**Characteristics:**
- Runs **all lines in order, once**
- Only shows output from `print()` statements
- Great for **saving** and **reusing** code
- Variables exist for the entire program run

```python
# saved as example.py
print("First line")
print("Second line")
print("Third line")
```

When you run `python example.py`, Python executes all lines in order, from top to bottom.

**When to use:** Writing programs, saving your work, creating reusable code

### Key differences

| Feature | REPL (Interactive) | Script (File) |
|---------|-------------------|---------------|
| Execution | One line at a time | All lines, top to bottom |
| Output | Shows result of every expression | Only shows `print()` output |
| Persistence | Until you exit | For the program run |
| Best for | Testing, learning | Writing programs |

### Common confusion

**"Why did it work in the REPL but not in my script?"**

This usually happens because:

1. **In REPL:** You might have typed some code earlier that created variables or set things up
2. **In Script:** The script starts completely fresh—nothing from previous runs exists

```python
# In REPL, you might have done:
>>> name = "Alice"
>>> # Then later...
>>> print(name)  # Works! name exists from earlier

# But in a script:
print(name)  # Error! name was never created in this script
name = "Alice"
```

**Solution:** Make sure everything your script needs is created in the script itself, in the right order (top to bottom).

### Using VS Code

If you're using VS Code (or another code editor):

- **Interactive mode:** Use the integrated terminal and type `python` to start a REPL
- **Script mode:** Write code in a `.py` file and run it with the "Run" button or `python filename.py`

Both modes are useful:
- Use **interactive mode** to test ideas quickly
- Use **script mode** to write and save your programs

## Summary

Python can run code in two different ways:

- **REPL (Interactive Mode):** Runs one line at a time, shows results immediately, great for testing and learning. Start it by typing `python` in your terminal.
- **Script (File Mode):** Runs all lines in a `.py` file from top to bottom, only shows `print()` output, great for saving and reusing code. Run it with `python filename.py`.

**Key differences:**
- REPL runs one line at a time; scripts run all lines in order
- REPL shows results immediately; scripts only show `print()` output
- REPL is great for testing; scripts are great for writing programs

**Common pitfall:** Code that works in the REPL might not work in a script if you forgot to include setup code. Always make sure your script has everything it needs, in the right order (top to bottom).

Understanding when to use each mode will make you a more effective Python programmer!
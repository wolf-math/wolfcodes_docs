---
title: File Handling Basics
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What is file handling?

**File handling** is how Python reads from and writes to files on your computer. It lets your programs:
- Load data from text or binary files (logs, CSVs, configuration, images, etc.)
- Save results, reports, or user data
- Append new information to existing files

At its core, file handling is about three steps:
1. **Open** a file
2. **Read from or write to** it
3. **Close** the file when you’re done

Python provides the built-in [`open()`](../../../python/language_reference/built-in#open) function for this.

## Why this matters

Most real-world programs don’t live in isolation, they read and write files. Whether you’re:
- Processing logs
- Loading configuration
- Saving model outputs
- Working with CSVs or JSON

So you’ll need to understand how Python handles files safely and efficiently. Good file handling helps you:
- Avoid data loss (by closing files properly)
- Prevent bugs (like reading the wrong encoding)
- Write code that behaves well across different operating systems

This first guide focuses on the *basics* of opening, reading, and closing files. Later guides can cover CSV, JSON, binary data, and more advanced patterns.

## Opening files

Use `open(path, mode, encoding=...)` to get a **file object**.

```python
f = open("example.txt", "r", encoding="utf-8")
```

- **`path`**: where the file lives (relative or absolute path)
- **`mode`**: how you want to use the file (read, write, etc.)
- **`encoding`**: how text is represented on disk (for text files)

### Common modes

| Mode | Meaning                      | Creates file? | Truncates file? |
| ---- | --------------------------- | ------------- | --------------- |
| `"r"`  | Read (text, default)         | No            | No              |
| `"w"`  | Write (text)                 | Yes           | Yes (clears it) |
| `"a"`  | Append (text)                | Yes           | No              |
| `"rb"` | Read binary                  | No            | No              |
| `"wb"` | Write binary                 | Yes           | Yes             |

```python
# Read existing text file
f = open("notes.txt", "r", encoding="utf-8")

# Create or overwrite text file
f = open("output.txt", "w", encoding="utf-8")

# Append to the end of a file
f = open("log.txt", "a", encoding="utf-8")
```

## Reading files

Once a file is open for reading, you can:

### Read the whole file

```python
f = open("example.txt", "r", encoding="utf-8")
contents = f.read()
print(contents)
f.close()
```

Be careful with `read()` on very large files because it loads everything into memory.

### Read line by line

```python
f = open("example.txt", "r", encoding="utf-8")

for line in f:
    print(line.rstrip())  # remove trailing newline

f.close()
```

This is memory efficient because it reads one line at a time.

### Read specific amounts

```python
f = open("data.txt", "r", encoding="utf-8")

chunk = f.read(10)   # read 10 characters
line = f.readline()  # read one line
lines = f.readlines()  # read remaining lines into a list

f.close()
```

## Writing files

Open a file in `"w"` or `"a"` mode to write text.

```python
f = open("output.txt", "w", encoding="utf-8")
f.write("First line\n")
f.write("Second line\n")
f.close()
```

- `"w"` starts from an empty file (or creates a new one).
- `"a"` appends to the end without deleting existing content.

```python
f = open("log.txt", "a", encoding="utf-8")
f.write("New log entry\n")
f.close()
```

## Always closing files

**Always close files when you're done with them.** Forgetting to close a file can cause serious problems:

- **Memory leaks**: The file stays in memory, consuming resources. If your program opens many files without closing them, it can run out of memory.
- **Resource leaks**: File descriptors remain open, which are limited system resources. Opening too many files without closing them can prevent your program (or other programs) from opening new files.
- **Data loss**: Buffered data may not be written to disk until the file is closed, risking data loss if your program crashes.
- **File locking**: Other programs may be unable to access the file while it's open.
- **Error handling**: If an error occurs before `close()` is called, the file will remain open in memory indefinitely.

You *can* call `close()` manually:

```python
f = open("example.txt", "r", encoding="utf-8")
try:
    data = f.read()
finally:
    f.close()  # Always runs, even if an error occurs
```

This works, but it's easy to forget the `finally` block, and if an error happens before `close()`, the file stays open. There's a better way.

## Using `with` (context managers)

The recommended pattern is to use a `with` statement. It:
- Opens the file
- Ensures it’s closed automatically, even if an error occurs

```python
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.rstrip())
```

Inside the `with` block:
- `f` is your file object
- When the block ends, `f.close()` is called automatically

The same pattern works for writing:

```python
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("Hello, file!\n")
    f.write("This was written safely.\n")
```

## Text vs binary mode

So far we’ve used text modes like `"r"` and `"w"`. For **binary data** (images, audio, etc.), use binary modes:

```python
# Read binary
with open("image.png", "rb") as f:
    data = f.read()   # bytes, not str

# Write binary
with open("copy.png", "wb") as f:
    f.write(data)
```

- Text mode (`"r"`, `"w"`, `"a"`) works with `str` and handles encoding/decoding.
- Binary mode (`"rb"`, `"wb"`, `"ab"`) works with `bytes` and does *no* encoding.

## Handling common errors

### File not found

```python
try:
    with open("missing.txt", "r", encoding="utf-8") as f:
        contents = f.read()
except FileNotFoundError:
    print("File does not exist!")
```

### Permission denied

```python
try:
    with open("/root/secret.txt", "r", encoding="utf-8") as f:
        contents = f.read()
except PermissionError:
    print("You don't have permission to read this file.")
```

## Summary

In this first part you learned:

- How to open files with `open(path, mode, encoding=...)`
- The most common modes: `"r"`, `"w"`, `"a"`, `"rb"`, `"wb"`
- How to read entire files or line by line
- How to write and append to files
- Why `with open(...) as f:` is the safest pattern
- The difference between text and binary modes

Later installments can build on this by exploring:
- Working with CSV and JSON files
- Path handling with `pathlib`
- Temporary files and directories
- More advanced error handling and patterns



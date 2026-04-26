---
title: Separate pure logic from I/O
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

Code is easier to test when the core logic is separate from reading files, making network requests, printing output, or touching a database. A small separation between pure logic and I/O often pays off immediately.

## Why this matters

Functions become hard to test when they do everything at once:

```python
def count_errors(path: str) -> int:
    with open(path) as file:
        lines = file.readlines()
    print("Counting errors...")
    return sum(1 for line in lines if "ERROR" in line)
```

This mixes together:

- reading a file
- printing a message
- counting matching lines

The counting logic is simple, but testing it now requires a file on disk or extra mocking.

## Pull the logic into its own function

```python
def count_error_lines(lines: list[str]) -> int:
    return sum(1 for line in lines if "ERROR" in line)


def count_errors_in_file(path: str) -> int:
    with open(path) as file:
        return count_error_lines(file.readlines())
```

Now the logic can be tested with plain input values:

```python
lines = ["INFO started", "ERROR failed", "ERROR retried"]
print(count_error_lines(lines))
```

**Output:**

```text
2
```

## Pure logic is easier to reuse

A pure function is one that depends on its inputs and returns a result without hidden side effects.

That kind of function is easier to:

- test
- reuse
- debug
- move into another module later

The I/O layer still matters, but it should usually be thin. Let it gather inputs and pass them into logic functions.

## Rules of thumb

- Keep file access, printing, and network calls near the edges of the program.
- Move calculations and transformations into separate functions.
- Test logic with plain values when possible.
- If a function is hard to test, check whether I/O and logic are mixed together.

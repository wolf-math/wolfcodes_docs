---
title: Closures in loops
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

# Late binding in closures

Closures in Python capture variables, not their values at the moment the inner function is created. This surprises many people in loops, where several functions end up using the same final value.

## What is happening?

This pattern looks like it should work:

```python
functions = []

for i in range(3):
    functions.append(lambda: i)

print([func() for func in functions])
```

**Output:**

```text
[2, 2, 2]
```

**What you might expect:** Each function remembers its own loop value.

**What actually happens:** Each function looks up `i` later, after the loop has finished.

## Why this surprises people

The inner function closes over the variable name `i`, not a frozen copy of its value. By the time the functions run, the loop is done and `i` contains its last value.

This is called late binding.

## Prefer this instead

One common fix is to bind the current value as a default argument:

```python
functions = []

for i in range(3):
    functions.append(lambda i=i: i)

print([func() for func in functions])
```

**Output:**

```text
[0, 1, 2]
```

Now each lambda gets its own value.

You can also use a regular helper function when that reads more clearly.

## Rules of thumb

- Be careful with closures created inside loops.
- Remember that closures capture variables, not snapshot values.
- Use a default argument such as `lambda i=i: i` when you need the current loop value.
- Prefer a small named function when the lambda workaround feels cryptic.

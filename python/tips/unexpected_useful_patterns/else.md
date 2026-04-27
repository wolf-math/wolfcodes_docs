---
title: Loop else blocks
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

# `for/else` and `while/else`

Python loops can have an `else` block. This is unusual, but it can be useful when you want one block to run only if the loop did not exit with `break`.

## What is happening?

In a `for` or `while` loop, the `else` block runs if the loop finishes normally.

```python
items = [1, 3, 5]

for item in items:
    if item % 2 == 0:
        print("Found an even number")
        break
else:
    print("No even numbers found")
```

**Output:**

```text
No even numbers found
```

If the loop hits `break`, the `else` block is skipped.

## Why it is useful

This pattern can remove an extra flag variable in search-style code:

```python
for user in users:
    if user.id == target_id:
        target = user
        break
else:
    raise LookupError("User not found")
```

That makes the success path and the "not found" path live together.

## Use it carefully

`for/else` is powerful, but it is also unfamiliar to many readers. It works best when:

- the loop is short
- the `break` condition is clear
- the `else` block naturally means "nothing matched"

If the logic is complex, an explicit helper function or a simpler structure may be easier to read.

## Rules of thumb

- Read loop `else` as "no `break` happened."
- Use it for short search-style loops.
- Avoid it when the control flow is already complex.
- Prefer clarity over cleverness if teammates may misread the pattern.

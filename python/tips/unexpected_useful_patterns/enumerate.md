---
title: enumerate() for indexes
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `enumerate()` instead of manual counters

`enumerate()` is a simple built-in that makes indexed loops easier to read. It is usually better than managing a counter variable by hand.

## What is `enumerate()`?

`enumerate()` yields both the index and the item from an iterable.

Without it, code often looks like this:

```python
index = 0

for name in names:
    print(index, name)
    index += 1
```

That works, but the counter management is noise.

## Prefer this instead

```python
for index, name in enumerate(names):
    print(index, name)
```

This says exactly what the loop is doing and removes a variable that only exists for bookkeeping.

You can also choose a starting value:

```python
for line_number, line in enumerate(lines, start=1):
    print(line_number, line)
```

That is especially useful for human-facing numbering.

## Why it is useful

`enumerate()` improves code because:

- the loop intent is obvious
- there is less mutable state to manage
- off-by-one mistakes become less likely

It is a small change, but it adds up across a codebase.

## Rules of thumb

- Use `enumerate()` when you need both an item and its index.
- Use `start=1` when the numbering is for people rather than zero-based indexing.
- Avoid manual counter variables in simple loops.
- Prefer the loop structure that states the intent directly.

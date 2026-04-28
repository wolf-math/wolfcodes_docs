---
title: Repeated nested lists
sidebar_position: 10
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# List multiplication and shared nested values

List multiplication repeats references, not independent nested objects. This becomes surprising when the repeated value is mutable.

## What is happening?

```python
rows = [[]] * 3
rows[0].append("x")

print(rows)
```

**Output:**

```text
[['x'], ['x'], ['x']]
```

**What you might expect:** Only the first inner list changes.

**What actually happens:** All three entries refer to the same inner list.

## Why this happens

`[[]] * 3` does not create three separate lists. It creates one list and repeats the reference three times.

This affects other nested mutables too, such as dictionaries or sets.

## Prefer this instead

Use a comprehension to build separate inner objects:

```python
rows = [[] for _ in range(3)]
rows[0].append("x")

print(rows)
```

**Output:**

```text
[['x'], [], []]
```

Now each inner list is independent.

## Rules of thumb

- Be careful with list multiplication when the repeated value is mutable.
- Remember that multiplication repeats references.
- Use a comprehension when you need distinct nested objects.
- If one nested change appears everywhere, shared references are the likely cause.

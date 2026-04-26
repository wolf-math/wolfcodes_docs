---
title: Iterating while mutating
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Changing a list or dictionary while iterating over it can produce skipped items, repeated work, or runtime errors. It is one of those bugs that often looks fine in a small example and fails later in real data.

## What is happening?

Here is a common list bug:

```python
items = [1, 2, 3, 4]

for item in items:
    if item % 2 == 0:
        items.remove(item)

print(items)
```

**Output:**

```text
[1, 3]
```

That result happens to look correct here, but the pattern is still unsafe because the list is being modified while the loop is walking through it.

A similar pattern with dictionaries can raise an error immediately.

## Why this matters

Mutation changes the structure the iterator is relying on. That can lead to:

- skipped elements
- confusing ordering behavior
- dictionary size errors
- hard-to-reproduce data bugs

## Prefer one of these patterns

Build a new collection:

```python
items = [1, 2, 3, 4]
filtered = [item for item in items if item % 2 != 0]
```

Or iterate over a copy when mutation is truly intended:

```python
items = [1, 2, 3, 4]

for item in items[:]:
    if item % 2 == 0:
        items.remove(item)
```

Both options make the behavior much easier to reason about.

## Rules of thumb

- Avoid mutating a collection while iterating over it.
- Prefer building a new list or dictionary.
- Iterate over a copy only when in-place mutation is intentional.
- If loop behavior feels inconsistent, check for hidden mutation first.

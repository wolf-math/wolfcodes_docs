---
title: Counter and defaultdict
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

The `collections` module has tools that solve common data tasks with less code and fewer edge cases. Two of the most useful are `Counter` for frequency counting and `defaultdict` for grouping or accumulating values.

## Why this matters

Many counting and grouping problems start with manual dictionary setup:

```python
counts = {}

for word in words:
    if word not in counts:
        counts[word] = 0
    counts[word] += 1
```

This works, but Python already has tools built for exactly this pattern.

## Use `Counter` for counting

```python
from collections import Counter

counts = Counter(words)
print(counts["python"])
```

`Counter` makes it obvious that the real task is frequency counting.

It also gives you helpful operations such as most common items:

```python
from collections import Counter

counts = Counter(["a", "b", "a", "c", "a"])
print(counts.most_common(2))
```

**Output:**

```text
[('a', 3), ('b', 1)]
```

## Use `defaultdict` for grouping

When the real task is "collect several values under the same key," `defaultdict` removes repeated setup:

```python
from collections import defaultdict

groups = defaultdict(list)

for user, team in memberships:
    groups[team].append(user)
```

This is often clearer than checking whether each key already exists.

## Prefer the tool that matches the task

These types help because they make your intent visible:

- `Counter` means counting
- `defaultdict(list)` means grouping
- `defaultdict(int)` means accumulating numeric totals

That clarity is usually as valuable as the shorter code.

## Rules of thumb

- Reach for `Counter` when the task is frequency counting.
- Reach for `defaultdict` when you keep initializing missing keys.
- Let the data structure describe the job.
- Prefer these tools over hand-rolled dictionary setup for common patterns.

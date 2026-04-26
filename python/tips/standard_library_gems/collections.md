---
title: `collections`
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

`collections` contains data structures that often fit real problems better than plain lists or dictionaries. A few tools in this module can make code both shorter and clearer.

## Why it is useful

The most practical tools here are:

- `Counter` for frequency counting
- `defaultdict` for grouping and accumulating
- `deque` for efficient append and pop operations at both ends
- `namedtuple` when a lightweight structured record is enough

Each one makes the intended data shape more obvious.

## A few high-value patterns

Counting:

```python
from collections import Counter

counts = Counter(["a", "b", "a"])
print(counts["a"])
```

Grouping:

```python
from collections import defaultdict

groups = defaultdict(list)
groups["python"].append("tips")
```

Queue-like behavior:

```python
from collections import deque

items = deque([1, 2, 3])
items.appendleft(0)
print(items.popleft())
```

## When not to use it

Do not reach for these types just because they exist. Use them when they match the actual job better than a normal list or dictionary.

## Rules of thumb

- Use `Counter` for counts, not hand-rolled dictionaries.
- Use `defaultdict` when missing-key setup keeps repeating.
- Use `deque` when operations at the left side matter.
- Let the data structure communicate the task.

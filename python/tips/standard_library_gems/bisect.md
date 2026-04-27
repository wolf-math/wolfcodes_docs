---
title: Bisect and heapq
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

# `bisect` and `heapq` for ordered data

`bisect` and `heapq` solve two common performance problems without extra dependencies. `bisect` helps you work with sorted lists efficiently, and `heapq` helps you keep track of smallest or largest items.

## What are `bisect` and `heapq`?

`bisect` finds insertion points in sorted lists:

```python
from bisect import bisect_left

scores = [10, 20, 30, 40]
index = bisect_left(scores, 25)
print(index)
```

**Output:**

```text
2
```

`heapq` maintains a heap, which is useful for priority queues and top-N problems:

```python
import heapq

values = [5, 1, 8, 3]
print(heapq.nsmallest(2, values))
```

**Output:**

```text
[1, 3]
```

## Why they are useful

These modules help when:

- a list stays sorted and needs fast lookups
- you need to insert into an ordered list
- you want the smallest or largest few items
- you need a priority queue

They let you use simple built-in data structures more effectively.

## When not to use them

`bisect` assumes the list is already sorted. `heapq` is great for top-priority access, but not for keeping a fully sorted list at all times.

## Rules of thumb

- Use `bisect` for searching or inserting in sorted lists.
- Use `heapq` for priority queues and top-N tasks.
- Reach for these before writing custom ordered-collection logic.

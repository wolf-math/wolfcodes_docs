---
title: `difflib`
sidebar_position: 7
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`difflib` gives you quick comparison tools for text and sequences. It is useful for debugging, building review tools, and explaining how two values differ.

## What is `difflib`?

One of its simplest tools is `unified_diff`:

```python
from difflib import unified_diff

before = ["name=alice\n", "role=user\n"]
after = ["name=alice\n", "role=admin\n"]

print("".join(unified_diff(before, after, fromfile="before", tofile="after")))
```

This produces a familiar diff-style output.

## Why it is useful

`difflib` is handy for:

- comparing generated text
- debugging config changes
- building lightweight file-difference views
- showing users what changed

It can save time before you reach for a larger diff tool.

## Rules of thumb

- Use `difflib` when explaining differences matters.
- Reach for it in debugging and tooling code.
- Prefer it over hand-written line-by-line comparison logic.

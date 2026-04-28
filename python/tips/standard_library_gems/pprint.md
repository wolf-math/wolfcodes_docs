---
title: Pprint
sidebar_position: 12
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `pprint` for readable debugging output

`pprint` makes nested Python data easier to inspect during debugging. It is a simple tool, but it saves time whenever plain `print()` becomes hard to read.

## What is `pprint`?

```python
from pprint import pprint

data = {"users": [{"name": "Ada", "roles": ["admin", "editor"]}]}
pprint(data)
```

It formats nested structures with indentation so you can scan them more easily.

## Why it is useful

Use `pprint` when debugging:

- nested dictionaries
- lists of records
- parsed JSON-like data
- complex intermediate results

## Rules of thumb

- Use `pprint` when `print()` output becomes noisy.
- Reach for it during debugging and REPL work.
- Prefer it for human inspection, not structured serialization.

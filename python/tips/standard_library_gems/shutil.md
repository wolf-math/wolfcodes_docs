---
title: `shutil`
sidebar_position: 14
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`shutil` provides high-level file and directory operations. It is a practical tool when you need to copy, move, archive, or remove filesystem content without writing low-level loops yourself.

## Why it is useful

Useful operations include:

- `copy()` and `copy2()`
- `copytree()`
- `move()`
- `rmtree()`
- `make_archive()`

Example:

```python
import shutil

shutil.copy("report.txt", "backup/report.txt")
```

## When to be careful

These functions can affect large parts of the filesystem quickly. Double-check paths, especially for recursive operations like `rmtree()` and `copytree()`.

## Rules of thumb

- Use `shutil` for high-level filesystem tasks.
- Prefer built-in helpers over manual copy loops.
- Be especially careful with recursive operations.

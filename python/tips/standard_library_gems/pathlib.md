---
title: `pathlib`
sidebar_position: 11
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`pathlib` is the standard-library tool for filesystem paths. It usually leads to clearer, safer code than building path strings by hand.

## What is `pathlib`?

```python
from pathlib import Path

config_path = Path("config") / "settings.json"
print(config_path)
```

**Output:**

```text
config/settings.json
```

`Path` objects support joining, inspection, and common filesystem operations in a readable way.

## Why it is useful

It helps with:

- cross-platform path handling
- path joins without manual slashes
- readable access to names, suffixes, and parents

## Rules of thumb

- Prefer `Path` objects over manual path strings.
- Use `/` to join path segments.
- Keep values as paths until a library truly needs a string.

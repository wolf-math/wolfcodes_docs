---
title: Pathlib for file paths
sidebar_position: 8
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Use `pathlib` for file paths

`pathlib` is the standard library tool for working with file system paths. It usually produces clearer code than building path strings by hand, and it handles path operations in a way that works across operating systems.

## Why this matters

Raw string paths tend to collect small mistakes:

```python
config_path = "config/" + filename + ".json"
```

This style is easy to get wrong when:

- a slash is missing or duplicated
- the code runs on another operating system
- you need the parent directory, file name, or suffix

`pathlib` gives you path objects with useful methods instead of making you manipulate strings manually.

## Prefer `Path` objects

```python
from pathlib import Path

filename = "settings"
config_path = Path("config") / f"{filename}.json"

print(config_path)
```

**Output:**

```text
config/settings.json
```

The `/` operator joins path segments in a readable way, and the result is still a path object that can be inspected or reused.

## Common tasks become easier

`pathlib` keeps file operations and path operations close together:

```python
from pathlib import Path

path = Path("data") / "report.txt"

print(path.name)
print(path.suffix)
print(path.parent)
```

**Output:**

```text
report.txt
.txt
data
```

That is usually easier to read than splitting strings and joining them again later.

## When to use strings anyway

Some libraries still expect plain strings. In those cases, you can convert a path object with `str(path)`.

:::note
Many modern libraries accept `Path` objects directly, so it is often worth trying that first.
:::

## Rules of thumb

- Reach for `pathlib` before manual path-string building.
- Use `Path(...) / "child"` to join path segments.
- Keep values as path objects until a library truly needs a string.
- Use path methods such as `.name`, `.suffix`, and `.parent` instead of string slicing.

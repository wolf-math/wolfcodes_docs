---
title: dict.get() and missing vs `None`
sidebar_position: 4
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`dict.get(key, default)` is convenient, but it does not tell you whether a key is missing or whether the key exists with a value of `None`. Those are often different situations.

## What is happening?

```python
data = {"timeout": None}

print(data.get("timeout", 30))
print(data.get("retries", 3))
```

**Output:**

```text
None
3
```

This is fine when `None` is a valid, meaningful value. The subtle bug appears when code treats `.get()` as a reliable way to distinguish "missing" from "present."

## Why this surprises people

Consider this:

```python
data = {"timeout": None}

if data.get("timeout") is None:
    print("Use default timeout")
```

That condition is true whether:

- `"timeout"` is missing
- `"timeout"` exists and is explicitly `None`

If your program needs to treat those cases differently, `.get()` alone is not enough.

## Prefer this instead

Check membership when the distinction matters:

```python
if "timeout" in data:
    timeout = data["timeout"]
else:
    timeout = 30
```

Another useful pattern is to use a sentinel object when `None` is a valid stored value.

## Rules of thumb

- Use `.get()` when missing and default behavior can be treated the same way.
- Do not rely on `.get()` to distinguish missing keys from stored `None` values.
- Use `in` or a sentinel object when that distinction matters.
- Be explicit when `None` is part of the data model.

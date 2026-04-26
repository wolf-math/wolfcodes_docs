---
title: `traceback`
sidebar_position: 20
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`traceback` helps you format and report exceptions more usefully. It is especially handy in CLI tools, logging, and debugging helpers where you want better error output than a bare message.

## What is `traceback`?

```python
import traceback

try:
    1 / 0
except ZeroDivisionError:
    print(traceback.format_exc())
```

This captures the full stack trace as a string.

## Why it is useful

Use `traceback` when you want to:

- log detailed exception information
- show full debug output in tools
- preserve stack traces in custom error reporting

## Rules of thumb

- Use `traceback` when error details matter.
- Prefer full stack traces over vague failure messages during debugging.
- Format or log exceptions deliberately instead of discarding context.

---
title: Exception handler order
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Exception order and broad handlers

The order of `except` blocks matters, and broad handlers such as `except Exception:` can hide real bugs. A handler that is too general can catch errors you did not mean to recover from.

## What is happening?

```python
try:
    value = int("abc")
except Exception:
    print("Something went wrong")
except ValueError:
    print("Bad number")
```

This `ValueError` handler is effectively unreachable because `Exception` catches it first.

## Why this matters

Broad exception handling can make code look stable while quietly swallowing problems such as:

- type mistakes
- programming errors
- unexpected library failures
- bugs that deserve to crash loudly during development

It also makes debugging harder because the original error path is blurred.

## Prefer narrow exception handling

Catch the specific error you expect:

```python
try:
    value = int("abc")
except ValueError:
    print("Bad number")
```

If you need several handlers, put more specific exceptions first and broader ones later.

```python
try:
    ...
except ValueError:
    ...
except Exception:
    ...
```

Even then, a broad final handler should usually log clearly or re-raise unless there is a strong reason to suppress the error.

## Rules of thumb

- Catch the most specific exception you can.
- Order `except` blocks from specific to general.
- Be cautious with `except Exception:`.
- Do not hide programming mistakes behind recovery code meant for expected failures.

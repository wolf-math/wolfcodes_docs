---
title: `contextlib`
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`contextlib` gives you tools for writing and combining cleanup logic. It is especially useful when you want context-manager behavior without writing a full class.

## What is `contextlib`?

One of its most useful features is the `@contextmanager` decorator:

```python
from contextlib import contextmanager


@contextmanager
def log_block(name: str):
    print(f"Starting {name}")
    try:
        yield
    finally:
        print(f"Finished {name}")
```

Now you can use it with `with`:

```python
with log_block("job"):
    print("running")
```

## Why it is useful

`contextlib` helps with:

- custom setup and teardown blocks
- optional cleanup
- suppressing specific exceptions carefully
- combining multiple context managers cleanly

It keeps resource-handling code small and readable.

## Other high-value helpers

- `closing()` for objects that need `.close()`
- `suppress()` for narrowly scoped exception suppression
- `nullcontext()` when a context manager is optional

## Rules of thumb

- Use `@contextmanager` for simple custom cleanup logic.
- Prefer `contextlib` helpers over repetitive boilerplate.
- Keep exception suppression narrow and explicit.

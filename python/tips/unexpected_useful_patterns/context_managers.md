---
title: Context managers for cleanup
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

Context managers let Python set something up, run a block of code, and then clean up reliably afterward. They are useful far beyond files, especially anywhere a resource or temporary state must be restored.

## What is a context manager?

The most familiar example is opening a file:

```python
with open("data.txt") as file:
    content = file.read()
```

When the block ends, Python closes the file automatically, even if an error occurs.

That same pattern works for many kinds of setup and cleanup.

## Why it is useful

Context managers help with:

- files
- locks
- database connections
- temporary directories
- redirected output
- custom setup and teardown logic

The key benefit is reliability. Cleanup happens in one clear place instead of depending on scattered manual calls.

## Prefer `with` for temporary resources

Without a context manager, cleanup is easier to forget:

```python
file = open("data.txt")
content = file.read()
file.close()
```

If an error happens between `open()` and `close()`, the cleanup may never run.

With `with`, the cleanup is tied directly to the block:

```python
with open("data.txt") as file:
    content = file.read()
```

## You can create your own

Python also lets you build custom context managers for temporary state and cleanup rules. That is helpful when code must always restore something after a block finishes.

## Rules of thumb

- Use `with` when a resource needs reliable cleanup.
- Reach for context managers beyond files, not just for file handling.
- Prefer block-scoped setup and teardown over manual open-and-close patterns.
- If code must always restore state, a context manager is often a good fit.

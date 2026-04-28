---
title: Run code only in main
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

# Use `if __name__ == "__main__":` to avoid import side effects

Put top-level script behavior behind `if __name__ == "__main__":`. This keeps a file importable without running code immediately, which makes reuse and testing much easier.

## What is happening?

When Python imports a module, it executes the module's top-level code. That means code like this runs during import:

```python
print("Starting job")
run_daily_report()
```

That is risky because importing the module now causes side effects.

## Why this matters

Imports should usually make functions and classes available, not start real work.

Unexpected top-level side effects can:

- print output during tests
- open files or network connections
- trigger jobs by accident
- make modules harder to reuse

## Prefer this instead

```python
def main() -> None:
    print("Starting job")
    run_daily_report()


if __name__ == "__main__":
    main()
```

Now the file behaves well in both cases:

- when run directly, it executes `main()`
- when imported, it only defines functions and classes

## Why the check works

When Python runs a file directly, `__name__` is set to `"__main__"`. When the file is imported as a module, `__name__` is set to the module name instead.

That makes the guard a clean way to separate import-time definitions from script-time behavior.

## Rules of thumb

- Keep executable script behavior inside `main()`.
- Use `if __name__ == "__main__":` to call `main()`.
- Avoid doing real work at import time.
- Treat imports as setup for reuse, not as a trigger for side effects.

---
title: Subprocess
sidebar_position: 17
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `subprocess.run()` for safer command execution

`subprocess.run()` is the safest default for running external commands from Python. It is clearer and less error-prone than older process APIs or shell-string hacks.

## Why it is useful

```python
import subprocess

result = subprocess.run(
    ["python3", "--version"],
    check=True,
    capture_output=True,
    text=True,
)

print(result.stdout.strip())
```

This pattern gives you:

- explicit arguments
- output capture
- clear failure handling with `check=True`

## Prefer argument lists over shell strings

Passing a list avoids many quoting problems and is usually safer than building one shell command string by hand.

## When to be careful

Only use `shell=True` when you truly need shell behavior and understand the tradeoffs.

## Rules of thumb

- Prefer `subprocess.run()` for external commands.
- Pass arguments as a list.
- Use `check=True` when command failure should raise an error.

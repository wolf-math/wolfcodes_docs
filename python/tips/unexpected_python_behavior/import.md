---
title: Avoid import *
sidebar_position: 7
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Avoid `from module import *`

`from module import *` makes code harder to read because it hides where names come from. It also increases the chance of accidental name collisions.

## Why this surprises people

Wildcard imports seem convenient at first:

```python
from math import *

print(sqrt(16))
```

The code works, but a reader no longer knows which names are local and which came from another module.

That gets worse in larger files, where imported names can quietly shadow existing names or each other.

## Why this matters

Wildcard imports make code harder to reason about because:

- names appear without visible origins
- static analysis becomes less clear
- collisions are easier to introduce
- reviews require more context to understand the namespace

This is mostly a readability and maintenance problem, which is exactly why it causes bugs later.

## Prefer explicit imports

```python
import math

print(math.sqrt(16))
```

Or import the specific names you need:

```python
from math import sqrt

print(sqrt(16))
```

Both patterns make the dependency visible.

## Rules of thumb

- Avoid `from module import *` in normal application code.
- Prefer `import module` when the module name adds clarity.
- Prefer explicit named imports when only a few names are needed.
- Make imported names easy for future readers to trace.

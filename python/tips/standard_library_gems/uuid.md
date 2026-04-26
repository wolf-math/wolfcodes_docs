---
title: `uuid`
sidebar_position: 22
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`uuid` is a simple way to generate identifiers that are very unlikely to collide. It is useful for filenames, record IDs, and request correlation values.

## What is `uuid`?

```python
import uuid

value = uuid.uuid4()
print(value)
```

`uuid4()` creates a random UUID.

## Why it is useful

Use UUIDs when:

- uniqueness matters more than readability
- ids are created across many systems or processes
- you need quick local ids without coordination

## Rules of thumb

- Use `uuid4()` for general-purpose unique identifiers.
- Reach for `uuid` before inventing your own id scheme for simple uniqueness needs.
- Do not use UUIDs when short human-readable ids are the real requirement.

---
title: Tempfile
sidebar_position: 18
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `tempfile` for safe temporary files and directories

`tempfile` is the safe way to create temporary files and directories. It avoids naming collisions and handles cleanup more reliably than hand-picked temp paths.

## Why it is useful

```python
from tempfile import TemporaryDirectory
from pathlib import Path

with TemporaryDirectory() as temp_dir:
    path = Path(temp_dir) / "output.txt"
    path.write_text("hello")
    print(path.exists())
```

**Output:**

```text
True
```

When the block ends, the temporary directory is cleaned up automatically.

## Good use cases

- tests
- intermediate files
- short-lived exports
- temporary workspaces

## Rules of thumb

- Use `tempfile` instead of inventing temp paths yourself.
- Prefer block-scoped temp resources with automatic cleanup.
- Reach for `TemporaryDirectory` when several temp files belong together.

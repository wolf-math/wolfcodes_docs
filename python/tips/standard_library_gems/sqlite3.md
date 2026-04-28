---
title: SQLite
sidebar_position: 15
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `sqlite3` for lightweight local persistence

`sqlite3` gives you a lightweight SQL database without installing a separate server. It is a strong choice for local tools, prototypes, tests, and small applications.

## What is `sqlite3`?

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("create table users (name text)")
conn.execute("insert into users values (?)", ("Ada",))
rows = conn.execute("select name from users").fetchall()
print(rows)
```

**Output:**

```text
[('Ada',)]
```

## Why it is useful

It works well for:

- local persistence
- CLI tools
- test fixtures
- small embedded databases

It lets you use real SQL without extra infrastructure.

## Rules of thumb

- Use `sqlite3` for lightweight local persistence.
- Prefer parameterized queries with `?` placeholders.
- Reach for it before adding a full database server to a small tool.

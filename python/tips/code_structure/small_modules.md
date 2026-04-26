---
title: Prefer small modules with clear jobs
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

Small modules are easier to understand, test, and change. A module should usually have one clear responsibility instead of becoming a general dumping ground for unrelated helpers.

## Why this matters

Large catch-all files often start with good intentions:

```python
# utils.py
def format_date(value): ...
def send_email(message): ...
def parse_csv(path): ...
def retry_request(url): ...
```

Over time, a file like this becomes hard to navigate because it answers no clear question. Readers have to scan the whole module to learn what belongs there.

## Group code by responsibility

A clearer structure is to place related code together:

- `dates.py` for date formatting helpers
- `notifications.py` for mail-related behavior
- `csv_tools.py` for CSV parsing
- `http.py` for request helpers

This makes imports tell a story:

```python
from csv_tools import parse_csv
from notifications import send_email
```

The names communicate intent before a reader opens the files.

## Smaller modules improve maintenance

When modules have a narrow purpose:

- it is easier to find the right code
- imports stay more meaningful
- tests can focus on one area
- refactors affect fewer unrelated functions

This does not mean every file must be tiny. It means a file should feel coherent.

## Watch for dumping-ground names

Files with names like these often deserve a second look:

- `utils.py`
- `helpers.py`
- `misc.py`
- `common.py`

Sometimes they are fine temporarily, but they often hide missing structure. If a module keeps collecting unrelated functions, split it by responsibility.

## Rules of thumb

- Prefer modules that answer one clear question.
- Group related functions together.
- Be cautious with catch-all names like `utils.py`.
- Split a module when its contents stop feeling coherent.

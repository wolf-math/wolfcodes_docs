---
title: CSV
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

# `csv` for reliable tabular text

The `csv` module is the reliable way to read and write CSV data in Python. It handles quoting, delimiters, and edge cases that are easy to get wrong with manual string splitting.

## Why it is useful

This is fragile:

```python
line = 'alice,"New York, NY"'
print(line.split(","))
```

Quoted commas break simple parsing. `csv` handles that correctly.

## Prefer the `csv` module

```python
import csv
from io import StringIO

text = 'name,city\nalice,"New York, NY"\n'
reader = csv.DictReader(StringIO(text))

for row in reader:
    print(row["city"])
```

**Output:**

```text
New York, NY
```

## Useful patterns

- `csv.reader` for simple row-based reading
- `csv.DictReader` when named columns are clearer
- `csv.writer` and `csv.DictWriter` for output

## Rules of thumb

- Use `csv`, not `split(",")`, for tabular text.
- Prefer `DictReader` when column names matter.
- Let the module handle quoting and delimiters for you.

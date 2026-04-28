---
title: Statistics
sidebar_position: 16
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `statistics` for quick numeric summaries

`statistics` is a handy module for basic numeric summaries. It saves you from rewriting common calculations like means and medians.

## Why it is useful

```python
import statistics

scores = [90, 70, 85, 95]
print(statistics.mean(scores))
print(statistics.median(scores))
```

For quick analysis, this is often all you need.

## Good use cases

- summaries in scripts
- simple reports
- quick data checks
- lightweight numerical tooling

## Rules of thumb

- Use `statistics` for basic descriptive summaries.
- Reach for it before writing custom mean or median code.
- Move to heavier tools only when the problem truly grows beyond it.

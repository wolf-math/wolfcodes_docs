---
title: Timeit
sidebar_position: 19
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# `timeit` for honest micro-benchmarks

`timeit` helps you measure small pieces of Python code more honestly than casual timing with `time.time()`. It is useful for quick performance checks and micro-benchmarks.

## Why it is useful

```python
import timeit

duration = timeit.timeit("sum(range(100))", number=10000)
print(duration)
```

`timeit` runs the code many times and is designed to reduce noise from one-off measurements.

## When to use it

- comparing two small implementations
- checking whether a change really helps
- exploring performance interactively

## When not to overuse it

Micro-benchmarks can mislead if they are too far from real program behavior. Use `timeit` for focused questions, not as the whole performance story.

## Rules of thumb

- Use `timeit` for small timing comparisons.
- Benchmark the actual code shapes you care about.
- Treat micro-benchmarks as clues, not final truth.

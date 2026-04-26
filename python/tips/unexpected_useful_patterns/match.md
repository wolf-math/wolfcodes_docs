---
title: Structural pattern matching
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

Structural pattern matching with `match` can make some branching code much clearer. It is most useful when you are dispatching based on shapes of data, not just comparing one simple value.

## What is `match`?

`match` lets you branch on patterns:

```python
command = ["move", 10, 20]

match command:
    case ["move", x, y]:
        print(f"Move to {x}, {y}")
    case ["quit"]:
        print("Quit")
```

This can be easier to read than several nested `if` checks when the real question is "what kind of structure is this?"

## Why it is useful

Pattern matching works well when code needs to handle:

- different tuple or list shapes
- structured command formats
- nested data with recognizable forms
- several related cases that would otherwise need repetitive unpacking

It can make data-oriented branching feel more declarative.

## Do not use it everywhere

`match` is not automatically better than `if` and `elif`.

Use `if` and `elif` when:

- the conditions are simple boolean checks
- only a couple of cases exist
- the team is more familiar with straightforward conditionals

`match` helps most when it removes repetitive shape checking and unpacking.

## Rules of thumb

- Use `match` when the structure of the data is the key decision.
- Prefer it for multi-shape branching, not routine boolean conditions.
- Keep cases readable and focused.
- If `match` makes the code feel more magical than clear, use `if` instead.

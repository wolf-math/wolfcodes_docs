---
title: dataclasses for simple data objects
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

`dataclasses` are a good default when a class mostly stores data. They remove repetitive boilerplate and make it easier to see what fields an object has.

## What `dataclasses` are

A dataclass is a class that automatically gets common methods based on its fields, such as `__init__()` and a readable `__repr__()`.

Without `dataclasses`, a simple container class often looks like this:

```python
class User:
    def __init__(self, name: str, email: str, active: bool = True) -> None:
        self.name = name
        self.email = email
        self.active = active
```

That is not wrong, but it becomes repetitive across a codebase.

## Prefer this instead

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    email: str
    active: bool = True
```

The important information is now front and center:

- which fields exist
- which types they expect
- which fields have defaults

This is especially useful for configuration objects, parsed records, and data passed between parts of a program.

## Why this matters

Dataclasses help code structure in a few ways:

- they make plain data objects obvious
- they reduce copy-pasted class boilerplate
- they work well with type hints and editors
- they make constructor signatures easy to scan

That clarity matters when a project grows and more objects move between modules.

## Dataclasses are for data-first classes

Dataclasses are a great fit when the class mainly represents state:

```python
from dataclasses import dataclass


@dataclass
class AppConfig:
    host: str
    port: int
    debug: bool = False
```

They are less useful when:

- the class has complex custom initialization
- behavior matters more than stored fields
- the object manages external resources or lifecycle rules

In those cases, a regular class may be clearer.

## Rules of thumb

- Use `@dataclass` for plain data containers.
- Keep dataclasses focused on representing state clearly.
- Reach for a regular class when the object is behavior-heavy or lifecycle-heavy.
- Let the field definitions tell the story of the object.

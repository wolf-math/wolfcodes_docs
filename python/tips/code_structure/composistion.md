---
title: Composition vs inheritance
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

# Prefer composition over deep inheritance

Composition usually leads to simpler Python code than deep inheritance chains. When one object uses another object to do part of its work, the behavior stays easier to test, swap, and reason about.

## Why this matters

Inheritance is useful when a subclass is truly a more specific version of a base class. It becomes harder to manage when classes inherit mostly to reuse code.

Deep class hierarchies often create problems like:

- methods that are overridden in several places
- constructors that must coordinate with `super()`
- base classes that take on too many responsibilities
- changes in one class affecting unrelated subclasses

Composition avoids much of that by letting objects collaborate directly.

## Prefer objects with clear roles

This kind of inheritance often starts small and becomes awkward over time:

```python
class FileLogger:
    def log(self, message: str) -> None:
        print(f"[file] {message}")


class TimestampedFileLogger(FileLogger):
    def log(self, message: str) -> None:
        super().log(f"2026-04-26 {message}")
```

This works, but adding more behavior usually means more subclasses:

- `JsonFileLogger`
- `TimestampedJsonFileLogger`
- `BufferedTimestampedFileLogger`

That is often a sign that behavior should be combined rather than inherited.

## Use composition to combine behavior

With composition, one object can delegate part of the work to another:

```python
class FileLogger:
    def log(self, message: str) -> None:
        print(f"[file] {message}")


class TimestampLogger:
    def __init__(self, logger: FileLogger) -> None:
        self.logger = logger

    def log(self, message: str) -> None:
        self.logger.log(f"2026-04-26 {message}")


logger = TimestampLogger(FileLogger())
logger.log("started")
```

Now each class has one clear job:

- `FileLogger` writes messages
- `TimestampLogger` adds a timestamp

If you want different behavior later, you can provide a different logger object instead of creating another subclass.

## When inheritance is still a good fit

Inheritance is still useful when there is a stable, meaningful "is-a" relationship.

Examples:

- a custom exception inheriting from `Exception`
- a framework base class designed for subclassing
- a small hierarchy with shared behavior and clear contracts

The problem is not inheritance itself. The problem is using inheritance as the default tool for code reuse.

## Rules of thumb

- Prefer composition when you want to combine behaviors.
- Use inheritance when the subtype relationship is genuinely clear.
- If subclasses multiply to cover combinations of features, switch to composition.
- Keep objects small and give each one a narrow responsibility.

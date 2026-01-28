---
title: Dunder Methods
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
## What are dunder methods?

**Dunder methods** (short for *double underscore*) are special methods whose names start and end with `__`, like `__init__`, `__str__`, or `__len__`.  
They let your classes hook into Python’s built‑in behavior:

- `__init__` — called when you create an instance
- `__str__` — what `print(obj)` shows
- `__len__` — what `len(obj)` returns
- `__getitem__` — how `obj[key]` works
- Arithmetic like `+`, `-`, `*`, comparison operators, iteration, and more

You rarely call dunder methods directly. Instead, Python calls them **for you** when you use normal syntax.

```python
len(obj)        # calls obj.__len__()
str(obj)        # calls obj.__str__()
obj[0]          # calls obj.__getitem__(0)
obj == other    # calls obj.__eq__(other)
```

Adding the right dunder methods makes your classes feel like **natural, built-in types**.

## Why this matters

Dunder methods let you:

- Make your objects **print nicely** (easier to debug and log)
- Work with built-in functions (`len`, `iter`, `reversed`, `sorted`, …)
- Support familiar syntax (`[]`, `in`, arithmetic operators)
- Integrate with Python protocols (iteration, context managers, numeric types)

You don’t need to memorize all of them. Start with a handful that make your classes easier to use and debug, then learn more as you need them.

## Object construction: `__init__`

You’ve already seen `__init__` in earlier sections. It runs after a new instance is created and is used to initialize attributes:

```python
class User:
    def __init__(self, username, active=True):
        self.username = username
        self.active = active

u = User("alice")
```

- `User("alice")` → Python creates a new `User` instance, then calls `User.__init__(that_instance, "alice")`.
- You don’t return anything from `__init__`. It must return `None`.

## String representation: `__repr__` and `__str__`

Two of the most useful dunder methods are `__repr__` and `__str__`.

- `__repr__(self)` — unambiguous representation for developers (used by `repr(obj)` and the interactive shell).
- `__str__(self)` — human‑friendly string (used by `str(obj)` and `print(obj)`).

If you only define `__repr__`, Python will fall back to it for `str()` in many contexts.

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

    def __str__(self):
        return f"({self.x}, {self.y})"

p = Point(2, 3)
print(p)          # (2, 3)
print(repr(p))    # Point(x=2, y=3)
```

Good `__repr__` output makes debugging and logging much easier.

## Container behavior: `__len__`, `__getitem__`, `__contains__`

If your class behaves like a sequence or collection, implement the basic container protocol.

### `__len__`

`len(obj)` calls `obj.__len__()`:

```python
class TodoList:
    def __init__(self):
        self._items = []

    def add(self, title):
        self._items.append(title)

    def __len__(self):
        return len(self._items)

todos = TodoList()
todos.add("Write docs")
todos.add("Review PRs")
print(len(todos))  # 2
```

### `__getitem__` and iteration

`obj[index]` calls `obj.__getitem__(index)`.  
If you implement `__getitem__` with integer indices starting at 0, your object can often be iterated over automatically:

```python
class TodoList:
    def __init__(self):
        self._items = []

    def add(self, title):
        self._items.append(title)

    def __len__(self):
        return len(self._items)

    def __getitem__(self, index):
        return self._items[index]

todos = TodoList()
todos.add("Write docs")
todos.add("Fix bugs")

print(todos[0])  # "Write docs"

for item in todos:      # uses __getitem__ and __len__
    print(item)
```

For more control over iteration (especially for non-indexable data), you can implement `__iter__`, but `__getitem__` is often enough for simple cases.

### `__contains__`

`x in obj` calls `obj.__contains__(x)` if defined:

```python
class TodoList:
    # ... as above ...

    def __contains__(self, title):
        return title in self._items

"Write docs" in todos   # True
"Go to gym" in todos    # False
```

## Operator overloading: `__add__`, `__eq__`, etc.

Dunder methods also power operators like `+`, `-`, `==`, `<`, and more.

Use this carefully—operator overloading should follow clear, intuitive rules.

### Equality: `__eq__`

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if not isinstance(other, Point):
            return NotImplemented
        return (self.x, self.y) == (other.x, other.y)

p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1 == p2)  # True
```

Returning `NotImplemented` lets Python try the reverse comparison or fall back gracefully.

### Addition: `__add__`

```python
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector2D):
            return NotImplemented
        return Vector2D(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"

v1 = Vector2D(1, 2)
v2 = Vector2D(3, 4)
print(v1 + v2)   # Vector2D(4, 6)
```

You can also implement other arithmetic methods like `__sub__`, `__mul__`, and their “right-hand” versions (`__radd__`, etc.) when needed.

## Making your class iterable: `__iter__`

To control iteration explicitly, implement `__iter__` and optionally `__next__` (on a separate iterator object).

```python
class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        current = self.start
        while current > 0:
            yield current
            current -= 1

for n in Countdown(3):
    print(n)
# 3
# 2
# 1
```

Using [`yield`](../../language_reference/keywords/#yield) inside `__iter__` is a simple way to create an iterator without writing a separate class.

## Context managers: `__enter__` and `__exit__`

Context managers let you use the `with` statement to manage resources (files, locks, database connections, etc.).

```python
class ManagedResource:
    def __enter__(self):
        print("Acquiring resource")
        return self

    def __exit__(self, exc_type, exc, tb):
        print("Releasing resource")
        # return True to suppress the exception, or False/None to propagate it
        return False

with ManagedResource() as r:
    print("Inside with block")
```

Output:

```text
Acquiring resource
Inside with block
Releasing resource
```

Files use this protocol internally, which is why you can write:

```python
with open("data.txt", "r", encoding="utf-8") as f:
    contents = f.read()
```

## When (and when not) to use dunder methods

**Use dunder methods when:**

- Your class naturally behaves like a **built-in type** (sequence, mapping, number, context manager).
- You want to improve **debugging** and **logging** with a good `__repr__`/`__str__`.
- You need your objects to work with Python’s built-in functions and syntax.

**Be cautious when:**

- Overloading operators in ways that **surprise** other developers.
- Implementing many dunder methods without a clear, consistent mental model.

**As a rule of thumb:**

- Start with `__repr__` (and optionally `__str__`).
- Add `__len__`, `__iter__`, `__getitem__`, or `__contains__` if your object is a collection.
- Add arithmetic or comparison dunders **only** if they are natural and unambiguous.

## Summary

- Dunder methods are special hooks that connect your classes to Python’s built‑in behavior.
- You usually interact with them via normal syntax (`len`, `[]`, `+`, `with`, etc.).
- Implementing a few well-chosen dunder methods can make your classes feel like first‑class citizens in the language.

As you build more complex classes, revisit this guide and add dunder methods when they clearly improve your code’s readability and ergonomics. You don’t need all of them—just the ones that make your objects easier to use and reason about.

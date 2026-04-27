---
title: Type Hints and Annotations
sidebar_position: 2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

## What are type hints?

**Type hints** (also called **type annotations**) are notes you add to Python code to describe what kinds of values a function expects and what it returns.

```python
def min_max(values: list[int]) -> tuple[int, int]:
    return min(values), max(values)
```

**What this says:**
1. `values` should be a list of integers.
2. The function returns a tuple with two integers.

Type hints help readers understand your code faster. They are especially useful on function parameters and return values, which is why you'll often see them in function definitions first.

## Why this matters

Type hints make function signatures more informative. When you read an annotated function, you can usually tell what kind of input it expects and what kind of result it produces without reading the whole implementation.

They also help in real projects because:

- Editors can give better autocomplete.
- Static type checkers can catch mistakes before you run the code.
- Function interfaces become clearer when you work with other people.

Even if you are writing small programs, type hints are a good habit for code that other people will read or reuse.

## Important: type hints are usually not enforced at runtime

If you're coming from TypeScript, this is the biggest mental shift.

Python will usually **not** reject the wrong type just because you added an annotation:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

print(greet(123))  # Python still runs this
```

**What happens:**
1. Python stores the annotations on the function.
2. Python still calls the function normally.
3. Unless you add your own checks, the annotation does not block bad input.

Type hints are mainly for:

- Human readers
- Editors and IDEs
- Static type checkers like `mypy` and `pyright`

If you want runtime validation, you must write it yourself:

```python
def greet(name: str) -> str:
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    return f"Hello, {name}!"
```

**Rule of thumb:** Use type hints to describe your code, not to enforce it at runtime.

## Annotating function parameters and return values

This is the most common place to start.

```python
def add(a: int, b: int) -> int:
    return a + b
```

**How it works:**
- `a: int` says `a` should be an integer.
- `b: int` says `b` should be an integer.
- `-> int` says the function returns an integer.

Here are a few more examples:

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

def is_even(n: int) -> bool:
    return n % 2 == 0

def get_initials(first: str, last: str) -> str:
    return first[0] + last[0]
```

If a function does not return a useful value, annotate it with `None`:

```python
def print_report(title: str) -> None:
    print(f"Report: {title}")
```

**Important:** `-> None` does not mean the function does nothing. It means the function does not return a useful result to the caller.

## Annotating variables

You can annotate variables too:

```python
name: str = "Alice"
age: int = 30
is_admin: bool = False
```

This is especially helpful when the type is not obvious:

```python
user_ids: list[int] = []
scores: dict[str, float] = {}
```

Variable annotations are optional. In beginner code, you will usually get the most value from annotating function signatures first.

## Annotating collections

Collections often hold many values of the same kind. Type hints let you describe both the collection type and the item type.

### Lists

```python
numbers: list[int] = [1, 2, 3]
names: list[str] = ["Alice", "Bob"]
```

This means:

- `numbers` is a list of integers
- `names` is a list of strings

### Dictionaries

```python
prices: dict[str, float] = {
    "apple": 1.25,
    "banana": 0.75,
}
```

This means:

- keys should be strings
- values should be floats

### Tuples

Use `tuple[...]` when position matters and each position has meaning.

```python
point: tuple[int, int] = (10, 20)
name_and_age: tuple[str, int] = ("Alice", 30)
```

### Sets

```python
tags: set[str] = {"python", "web", "api"}
```

## Choosing modern vs older annotation syntax

Python's modern style uses built-in collection names:

```python
names: list[str] = ["Alice", "Bob"]
scores: dict[str, int] = {"Alice": 10}
```

Older code often imports these from `typing`:

```python
from typing import Dict, List

names: List[str] = ["Alice", "Bob"]
scores: Dict[str, int] = {"Alice": 10}
```

**Use this by default:** Prefer `list[str]`, `dict[str, int]`, and similar built-in forms in modern Python code.

:::note
You will still see `List[...]`, `Dict[...]`, and similar forms in older codebases, tutorials, and libraries.
:::

## Optional values and `None`

Sometimes a value may be missing. In type hints, that usually means the value can be a real type or `None`.

```python
def find_user(user_id: int) -> str | None:
    if user_id == 1:
        return "Alice"
    return None
```

**How to read this:** The function returns either a `str` or `None`.

Older code may use `Optional[str]`, which means the same thing:

```python
from typing import Optional

def find_user(user_id: int) -> Optional[str]:
    if user_id == 1:
        return "Alice"
    return None
```

**Use this by default:** In modern Python, `str | None` is usually the clearest form.

## Using more than one possible type

If a value could be one of several types, use `|`:

```python
def double(value: int | float) -> int | float:
    return value * 2
```

Older code may use `Union`:

```python
from typing import Union

def double(value: Union[int, float]) -> Union[int, float]:
    return value * 2
```

**Rule of thumb:** Prefer `|` in modern Python unless you are working in an older codebase that already uses `Union[...]`.

## Using `Any`

Sometimes you do not want to be specific about the type.

```python
from typing import Any

def log_value(value: Any) -> None:
    print(value)
```

`Any` means "accept anything" from the type checker's point of view.

**Important:** `Any` is flexible, but too much of it removes many of the benefits of type hints.

## Annotating functions that take other functions

When a function accepts another function as an argument, use `Callable`.

```python
from collections.abc import Callable

def apply_twice(func: Callable[[int], int], value: int) -> int:
    return func(func(value))
```

**How to read this:** `Callable[[int], int]` means "a function that takes one `int` and returns an `int`."

Example:

```python
def add_one(x: int) -> int:
    return x + 1

result = apply_twice(add_one, 3)
print(result)  # 5
```

## Annotating `*args` and `**kwargs`

You can annotate flexible parameter lists too.

```python
def total(*numbers: int) -> int:
    return sum(numbers)
```

This means each value passed into `*numbers` should be an `int`.

For `**kwargs`:

```python
def print_scores(**scores: int) -> None:
    for name, score in scores.items():
        print(name, score)
```

This means each keyword value should be an `int`.

## Creating type aliases

If a type is repeated often, give it a shorter and more meaningful name:

```python
UserName = str
Scores = dict[UserName, int]

def score_for(user: UserName, scores: Scores) -> int:
    return scores[user]
```

Type aliases make annotations easier to read by expressing meaning, not just structure.

## Common patterns

### Annotating a simple helper function

```python
def parse_line(line: str) -> list[str]:
    return line.split(",")
```

This is a good default pattern for small reusable helpers: annotate the input and annotate the return value.

### Returning a value that may be missing

```python
def get_status(code: int) -> str | None:
    if code == 200:
        return "ok"
    return None
```

Use this pattern when a function may or may not find a result.

### Describing structured return data

```python
def make_user(name: str, age: int) -> dict[str, str | int]:
    return {"name": name, "age": age}
```

This kind of annotation helps readers understand the shape of returned data without opening the function body.

## Common mistakes

### Mistaking type hints for runtime checks

This is the most common misunderstanding.

```python
def square(x: int) -> int:
    return x * x
```

That annotation does **not** automatically reject bad input at runtime.

### Using `Any` too early

```python
from typing import Any

def process_user(data: Any) -> Any:
    return data
```

This is legal, but it does not tell the reader much.

A clearer version is usually better:

```python
def process_user(name: str) -> str:
    return name.strip()
```

### Making annotations harder to read than the code

Bad:

```python
from typing import Any

def transform(data: list[dict[str, Any] | tuple[str, int] | None]) -> list[dict[str, Any] | tuple[str, int] | None]:
    return data
```

Good:

```python
def average(values: list[float]) -> float:
    return sum(values) / len(values)
```

The bad example is technically valid, but it is much harder to read than most beginner code needs to be. The good example keeps the annotation useful without making the signature feel heavy.

**Rule of thumb:** Start with clear, ordinary annotations. Do not reach for advanced typing features unless they solve a real problem.

## When to use type hints

Type hints are especially useful when:

- You are writing functions other people will call
- You are building larger programs
- You are returning structured data
- You are passing functions into functions
- You want better editor help

For very small throwaway scripts, you do not need to annotate everything. For reusable code, function annotations are a strong default.

## Static type checking

Type hints become much more useful when you run a static type checker such as:

- `mypy`
- `pyright`

These tools analyze your code and warn you about likely type mistakes before runtime.

```python
def greet(name: str) -> str:
    return f"Hello, {name}!"

greet(123)
```

Python itself may still run this code, but a type checker can flag it as likely wrong.

## Summary

- Type hints describe what kinds of values your code expects.
- They are most useful on function parameters and return values.
- Python usually does not enforce them at runtime.
- The safest default is to start with simple annotations on reusable functions.
- Prefer clear, modern forms like `list[str]` and `str | None` when they fit your codebase.

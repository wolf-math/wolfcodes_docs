---
title: Keywords
sidebar_position: 20
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## Properties

```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

## Definition

a keyword is a special word that is part of Python's syntax. They are not functions, methods, or objects. They define how the language is structured and executed.

| Category                      | Examples                                                                     | Description                                 |
| ----------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------- |
| **Control flow**              | `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `return`, `yield` | Manage loops and decision-making            |
| **Structure and definitions** | `def`, `class`, `lambda`, `with`, `as`                                       | Define functions, classes, and contexts     |
| **Logical and comparison**    | `and`, `or`, `not`, `is`, `in`                                               | Combine or compare values                   |
| **Exception handling**        | `try`, `except`, `finally`, `raise`, `assert`                                | Handle errors and enforce conditions        |
| **Import and namespace**      | `import`, `from`, `global`, `nonlocal`, `del`                                | Manage scope and module access              |
| **Special purpose**           | `True`, `False`, `None`, `pass`, `await`, `async`, `match`, `case`           | Language-level constants or syntax keywords |

## Keyword definitions

### `if`

Starts a conditional block that executes code only when a condition is `True`. The bread and butter of decision-making.

```python
>>> if x > 0:
...     print("positive")
```

---

### `elif`

Short for "else if". Chains additional conditions after an `if` statement. Python's way of saying "but what if...?"

```python
>>> if x > 0:
...     print("positive")
... elif x < 0:
...     print("negative")
```

---

### `else`

The catch-all clause. Executes when all preceding conditions are `False`. The default path when nothing else matches.

```python
>>> if x > 0:
...     print("positive")
... else:
...     print("zero or negative")
```

---

### `for`

Iterates over items in an iterable (lists, strings, ranges, etc.). Python's preferred way to loop when you know what you're iterating over.

```python
>>> for item in [1, 2, 3]:
...     print(item)
```

---

### `while`

Creates a loop that continues as long as a condition is `True`. Use with caution—make sure your condition eventually becomes `False`, or you'll loop forever.

```python
>>> count = 0
>>> while count < 3:
...     print(count)
...     count += 1
```

---

### `break`

Immediately exits the nearest enclosing loop. The emergency exit button for loops.

```python
>>> for i in range(10):
...     if i == 5:
...         break
...     print(i)
```

---

### `continue`

Skips the rest of the current loop iteration and jumps to the next one. Like saying "skip this one, keep going."

```python
>>> for i in range(5):
...     if i == 2:
...         continue
...     print(i)
```

---

### `return`

Exits a function and optionally sends a value back to the caller. Functions without `return` implicitly return `None`.

```python
>>> def add(a, b):
...     return a + b
```

---

### `yield`

Produces a value from a generator function, pausing execution until the next value is requested. Makes functions lazy and memory-efficient.

```python
>>> def count():
...     yield 1
...     yield 2
...     yield 3
```

---

### `def`

Defines a function. The keyword that turns code into reusable blocks.

```python
>>> def greet(name):
...     return f"Hello, {name}!"
```

---

### `class`

Defines a class, Python's way of creating custom types with attributes and methods. The blueprint for objects.

```python
>>> class Dog:
...     def bark(self):
...         return "Woof!"
```

---

### `lambda`

Creates an anonymous function in a single expression. Perfect for quick, one-off functions that don't need a name.

```python
>>> square = lambda x: x ** 2
>>> square(5)
25
```

---

### `with`

Manages context managers, ensuring proper setup and cleanup (like closing files). Python's way of saying "do this, then clean up automatically."

```python
>>> with open('file.txt') as f:
...     content = f.read()
```

---

### `as`

Used with `import` or `with` to assign an alias or bind a context manager variable. Gives things a new name.

```python
>>> import datetime as dt
>>> with open('file.txt') as f:
...     pass
```

---

### `and`

Logical AND operator. Returns `True` only if both operands are truthy. Short-circuits: stops evaluating if the first operand is falsy.

```python
>>> True and False
False
>>> 5 > 3 and 2 < 4
True
```

---

### `or`

Logical OR operator. Returns `True` if either operand is truthy. Short-circuits: stops evaluating if the first operand is truthy.

```python
>>> True or False
True
>>> 5 < 3 or 2 < 4
True
```

---

### `not`

Logical NOT operator. Inverts the truth value of its operand. Turns `True` into `False` and vice versa.

```python
>>> not True
False
>>> not 0
True
```

---

### `is`

Identity operator. Checks if two variables reference the same object in memory. Different from `==`, which checks equality.

```python
>>> a = [1, 2, 3]
>>> b = a
>>> a is b
True
>>> a == [1, 2, 3]
True
>>> a is [1, 2, 3]
False
```

---

### `in`

Membership operator. Checks if a value exists in a container (list, string, dict keys, etc.). Also used in `for` loops.

```python
>>> 2 in [1, 2, 3]
True
>>> 'a' in 'hello'
False
```

---

### `try`

Starts a block where exceptions might occur. The "attempt this" keyword.

```python
>>> try:
...     result = 10 / 0
... except ZeroDivisionError:
...     print("Can't divide by zero!")
```

---

### `except`

Catches and handles specific exceptions that occur in a `try` block. The safety net.

```python
>>> try:
...     x = int("not a number")
... except ValueError:
...     print("That's not a number!")
```

---

### `finally`

A block that always executes, whether an exception occurred or not. Perfect for cleanup code that must run no matter what.

```python
>>> try:
...     f = open('file.txt')
... finally:
...     f.close()  # Always closes, even if an error occurs
```

---

### `raise`

Explicitly raises an exception. Python's way of saying "something went wrong, handle this!"

```python
>>> if x < 0:
...     raise ValueError("x must be non-negative")
```

---

### `assert`

Raises an `AssertionError` if a condition is `False`. Used for debugging and sanity checks. Can be disabled with the `-O` flag.

```python
>>> assert x > 0, "x must be positive"
```

---

### `import`

Loads a module so you can use its contents. The gateway to Python's vast ecosystem.

```python
>>> import math
>>> math.sqrt(16)
4.0
```

---

### `from`

Used with `import` to selectively import specific items from a module. Lets you cherry-pick what you need.

```python
>>> from math import sqrt
>>> sqrt(16)
4.0
```

---

### `global`

Declares that a variable inside a function refers to the global scope. Use sparingly—it can make code harder to understand.

```python
>>> x = 10
>>> def increment():
...     global x
...     x += 1
```

---

### `nonlocal`

Declares that a variable refers to the nearest enclosing (non-global) scope. For when you need to modify a variable from an outer function.

```python
>>> def outer():
...     x = 10
...     def inner():
...         nonlocal x
...         x += 1
...     return x
```

---

### `del`

Deletes a variable, list item, or dictionary key. Removes the reference, not necessarily the object itself (Python's garbage collector handles that).

```python
>>> x = 5
>>> del x
>>> my_list = [1, 2, 3]
>>> del my_list[0]
```

---

### `True`

The boolean value representing truth. One of Python's two boolean constants (the other being `False`).

```python
>>> if True:
...     print("This always runs")
```

---

### `False`

The boolean value representing falsity. The opposite of `True`, and the default truthiness of empty containers.

```python
>>> if False:
...     print("This never runs")
```

---

### `None`

Python's null value. Represents the absence of a value. Functions without a `return` statement implicitly return `None`.

```python
>>> x = None
>>> if x is None:
...     print("x has no value")
```

---

### `pass`

A no-op statement. Does nothing, but is syntactically required where code is expected. Python's way of saying "I'll fill this in later."

```python
>>> def todo():
...     pass  # Placeholder for future code
```

---

### `async`

Declares an asynchronous function (coroutine). Functions that can pause and resume, perfect for I/O operations.

```python
>>> async def fetch_data():
...     # Can use await here
...     pass
```

---

### `await`

Pauses execution of an async function until an awaitable completes. Only usable inside `async` functions.

```python
>>> async def main():
...     result = await some_async_operation()
```

---

### `match`

Introduces a match statement (Python 3.10+), similar to switch statements in other languages. Provides pattern matching capabilities.

```python
>>> match status:
...     case 200:
...         print("Success")
...     case 404:
...         print("Not found")
```

---

### `case`

Defines individual patterns within a `match` statement. Each `case` represents a possible match condition.

```python
>>> match value:
...     case "hello":
...         print("Greeting")
...     case _:  # Default case
...         print("Unknown")
```

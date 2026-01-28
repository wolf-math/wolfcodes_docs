---
title: Decorators
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
## What are decorators?

A **decorator** is a function that wraps another function to add or modify behavior *without* changing the wrapped function’s code. In Python syntax, decorators are written with the `@decorator_name` line above a function definition.

Under the hood, this:

```python
@decorator
def func():
    ...
```

is equivalent to:

```python
def func():
    ...

func = decorator(func)
```

Decorators are a practical application of **higher-order functions**: they take a function as input and return a new function.

## Why this matters

Decorators let you:

- **Reuse cross-cutting behavior** like logging, timing, caching, and access control.
- **Keep business logic clean** by moving boilerplate out of your core functions.
- **Compose behavior** by stacking multiple decorators.

They show up everywhere in real-world Python:

- `@classmethod`, `@staticmethod`, `@property` in classes
- `@app.route("/path")` in web frameworks
- `@pytest.mark.parametrize` in tests

Understanding decorators is essential for reading and writing modern Python.

## A simple decorator

Let’s start with a minimal decorator that prints before and after a function call.

```python
def debug(func):
    """Print the function name and arguments each time it's called."""

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper
```

Use it with `@debug`:

```python
@debug
def add(a, b):
    return a + b

add(2, 3)
# Calling add with args=(2, 3), kwargs={}
# add returned 5
```

Here:

- `debug` takes `func` as an argument.
- It defines `wrapper`, which calls `func` and adds extra behavior.
- It returns `wrapper`, which becomes the new version of `add`.

## Decorators and `*args`, `**kwargs`

Real-world decorators should work with **any** function signature. That’s why decorators almost always use `*args` and `**kwargs`.

```python
def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"→ {func.__name__} called")
        result = func(*args, **kwargs)
        print(f"← {func.__name__} finished")
        return result
    return wrapper
```

This decorator can wrap functions with any parameters:

```python
@log_calls
def greet(name, punctuation="!"):
    print(f"Hello, {name}{punctuation}")

greet("Alice")
greet("Bob", punctuation="!!!")
```

## Preserving metadata with `functools.wraps`

By default, the wrapper function hides the original function’s name and docstring:

```python
@debug
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

print(multiply.__name__)  # 'wrapper', not 'multiply'
print(multiply.__doc__)   # None
```

Use [`functools.wraps`](https://docs.python.org/3/library/functools.html#functools.wraps) to copy metadata from the original function to the wrapper:

```python
import functools

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper
```

Now:

```python
@debug
def multiply(a, b):
    """Multiply two numbers."""
    return a * b

print(multiply.__name__)  # 'multiply'
print(multiply.__doc__)   # 'Multiply two numbers.'
```

Always use `@functools.wraps` in real decorators unless you have a very specific reason not to.

## Decorators with arguments

Sometimes you want to configure a decorator, e.g., set a logging level or a label. This means **the decorator itself needs parameters**.

Pattern:

1. Outer function: takes decorator arguments, returns the real decorator.
2. Decorator: takes the function and returns a wrapper.
3. Wrapper: wraps the function call.

```python
import functools

def repeat(times):
    """Decorator factory to repeat a function call."""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper

    return decorator
```

Usage:

```python
@repeat(3)
def say(message):
    print(message)

say("Hello")
# Hello
# Hello
# Hello
```

Here, `repeat(3)` returns a decorator, which then wraps `say`.

## Common real-world patterns

### Timing a function

```python
import functools
import time

def timing(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper
```

### Simple access control (role check)

```python
import functools

def require_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(user, *args, **kwargs):
            if role not in user.get("roles", []):
                raise PermissionError(f"User lacks role: {role}")
            return func(user, *args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_user(user, target_id):
    print(f"User {target_id} deleted")
```

### Caching results

You can write your own caching decorator, but Python also provides [`functools.lru_cache`](https://docs.python.org/3/library/functools.html#functools.lru_cache):

```python
import functools

@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

## Decorating methods

Decorators work the same way on functions and methods. When you decorate a method inside a class, the wrapper still receives `self` as the first argument:

```python
import functools

def log_method(func):
    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        print(f"{self.__class__.__name__}.{func.__name__} called")
        return func(self, *args, **kwargs)
    return wrapper

class Greeter:
    @log_method
    def greet(self, name):
        return f"Hello, {name}!"
```

## Built-in decorators

Python includes several decorators you’ll see frequently:

- `@property` — turn a method into a managed attribute
- `@staticmethod` — define a function stored on a class that doesn’t get `self` or `cls`
- `@classmethod` — method that receives the class (`cls`) instead of the instance

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("radius must be non-negative")
        self._radius = value
```

## When (and when not) to use decorators

Decorators are a good choice when:

- You see the **same pattern** repeated across many functions.
- You want to **separate concerns** (e.g., logging vs. business logic).
- You need **reusable wrappers** that can be applied with one line.

They can be overkill when:

- The behavior is used only once.
- The decorator logic is more complicated than the function it wraps.
- It makes the control flow harder to follow for your future self.

When in doubt, start with a normal helper function. If you notice a pattern repeating, refactor it into a decorator.


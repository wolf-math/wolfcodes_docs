---
title: Decorators
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

This guide covers advanced decorator concepts and patterns. For fundamental decorator concepts, see the [guide on decorators](../../guides/functions/decorators).

## Execution timing: Definition time vs call time

This is crucial: decorators run at **definition time**, not call time. The decorator executes when Python defines the function, not when you call it.

### Definition time execution

```python
def decorator(func):
    print(f"Decorator running for {func.__name__}")
    def wrapper():
        print(f"Wrapper running for {func.__name__}")
        return func()
    return wrapper

@decorator
def greet():
    print("Hello!")

print("Function defined")
greet()
# Output:
# Decorator running for greet
# Function defined
# Wrapper running for greet
# Hello!
```

<!-- Execution flow:

```
Definition Time (runs once):
┌─────────────────────────┐
│ Python encounters        │
│ @decorator               │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Decorator runs           │
│ Creates wrapper          │
│ Print: "Decorator        │
│ running for greet"       │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Function definition      │
│ complete                 │
│ Print: "Function defined"│
└─────────────────────────┘

Call Time (runs each time greet() is called):
┌─────────────────────────┐
│ greet() called          │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Wrapper runs            │
│ Print: "Wrapper running  │
│ for greet"               │
└───────────┬─────────────┘
            │
            ▼
┌─────────────────────────┐
│ Original greet()         │
│ executes                 │
│ Print: "Hello!"          │
└─────────────────────────┘
``` -->

Notice that "Decorator running for greet" prints immediately when the function is defined, before you even call `greet()`. The decorator runs once when Python processes the `@decorator` line.

### Call time execution

The wrapper function runs each time you call the decorated function:

```python
def count_calls(func):
    call_count = 0
    def wrapper():
        nonlocal call_count
        call_count += 1
        print(f"Function called {call_count} times")
        return func()
    return wrapper

@count_calls
def greet():
    print("Hello!")

greet()
# Output:
# Function called 1 times
# Hello!

greet()
# Output:
# Function called 2 times
# Hello!
```

The decorator itself (`count_calls`) runs once at definition time, creating the wrapper. The wrapper runs each time you call `greet()`, tracking the call count.

### Why this matters

Understanding execution timing helps you avoid common mistakes:

```python
# This won't work as expected
def bad_decorator(func):
    # This runs at definition time, not call time
    print("Setting up...")
    return func

@bad_decorator
def greet():
    print("Hello!")

# "Setting up..." already printed
greet()  # Just prints "Hello!"
```

If you need setup code to run at call time, put it in the wrapper, not in the decorator itself.

### State in decorators

Because decorators run at definition time, you can use closures to maintain state across function calls:

```python
def call_counter(func):
    count = 0  # This is captured in the closure
    
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal count
        count += 1
        print(f"{func.__name__} has been called {count} times")
        return func(*args, **kwargs)
    
    return wrapper

@call_counter
def process_data(data):
    return data.upper()

process_data("hello")  # process_data has been called 1 times
process_data("world")  # process_data has been called 2 times
```

The `count` variable is created once at definition time and persists across all calls to the decorated function. This is a closure: the wrapper function captures the `count` variable from the decorator's scope.

## Stacking decorators

You can apply multiple decorators to the same function. They stack from bottom to top:

```python
from functools import wraps

def bold(func):
    @wraps(func)
    def wrapper():
        return f"<b>{func()}</b>"
    return wrapper

def italic(func):
    @wraps(func)
    def wrapper():
        return f"<i>{func()}</i>"
    return wrapper

@bold
@italic
def greet():
    return "Hello"

print(greet())
# Output:
# <b><i>Hello</i></b>
```

The decorators apply from bottom to top: first `italic` wraps `greet`, then `bold` wraps the result. This is equivalent to:

```python
greet = bold(italic(greet))
```

### Order matters

The order of decorators affects the result:

```python
@bold
@italic
def text1():
    return "Hello"

@italic
@bold
def text2():
    return "Hello"

print(text1())  # <b><i>Hello</i></b>
print(text2())  # <i><b>Hello</b></i>
```

Different order, different result. Think of decorators as layers: the bottom decorator is the innermost layer.

### Real-world example: Authentication and logging

```python
from functools import wraps

def require_auth(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise PermissionError("Not authenticated")
        return func(*args, **kwargs)
    return wrapper

def log_calls(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result
    return wrapper

@require_auth
@log_calls
def delete_user(user_id):
    return f"Deleted user {user_id}"
```

When you call `delete_user()`, it first checks authentication, then logs the call, then executes the function. The decorators compose together. The order matters: authentication happens before logging, so if authentication fails, the function call is never logged.

## Decorators with arguments: The pattern explained

Decorators that accept arguments require an extra layer: a function that returns a decorator. Understanding this pattern is key to writing flexible decorators.

### The three-layer structure

```python
from functools import wraps

def repeat(times):
    # Layer 1: Outer function (takes decorator arguments)
    def decorator(func):
        # Layer 2: Decorator (takes the function)
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Layer 3: Wrapper (wraps the function call)
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def greet():
    print("Hello!")

greet()
# Output:
# Hello!
# Hello!
# Hello!
```

Here's what happens step by step:
1. `repeat(3)` is called, returning the `decorator` function
2. That decorator is applied to `greet`, returning the `wrapper` function
3. When you call `greet()`, the wrapper executes

This is equivalent to:

```python
decorator = repeat(3)
greet = decorator(greet)
```

### Why the extra layer?

Without arguments, a decorator is a function that takes a function. With arguments, you need a function that returns a function that takes a function:

```python
# No arguments: decorator(func)
def simple_decorator(func):
    return wrapper

# With arguments: decorator(args)(func)
def decorator_with_args(arg):
    def actual_decorator(func):
        return wrapper
    return actual_decorator
```

The outer function handles the arguments and creates a closure that captures them. The inner function is the actual decorator that uses those captured arguments.

### Real-world example: Rate limiting

```python
from functools import wraps
import time

def rate_limit(calls_per_second):
    min_interval = 1.0 / calls_per_second
    last_called = [0.0]  # Using list to allow modification in closure
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed = time.time() - last_called[0]
            if elapsed < min_interval:
                time.sleep(min_interval - elapsed)
            last_called[0] = time.time()
            return func(*args, **kwargs)
        return wrapper
    return decorator

@rate_limit(2)  # Max 2 calls per second
def api_call():
    print("API called")
    return "success"

api_call()
time.sleep(0.3)
api_call()  # Will wait to maintain rate limit
```

The decorator takes `calls_per_second` as an argument, then returns a decorator that enforces that rate limit. The `last_called` list is captured in the closure and shared across all calls to the decorated function.

## Why `functools.wraps` matters

When you create a wrapper function, it replaces the original function. This can cause problems with introspection tools that rely on function metadata.

### The problem

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """A greeting function."""
    return "Hello!"

print(greet.__name__)      # wrapper (not greet!)
print(greet.__doc__)       # None (lost the docstring!)
print(help(greet))         # Shows wrapper, not greet
```

The wrapper function has its own name and metadata, not the original function's. This breaks debugging, documentation, and introspection.

### The solution: `functools.wraps`

`functools.wraps` copies the original function's metadata to the wrapper:

```python
from functools import wraps

def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

@my_decorator
def greet():
    """A greeting function."""
    return "Hello!"

print(greet.__name__)      # greet (preserved!)
print(greet.__doc__)       # A greeting function. (preserved!)
print(help(greet))         # Shows greet with its docstring
```

`@wraps(func)` is itself a decorator that copies metadata from `func` to `wrapper`. It preserves:
- `__name__`
- `__doc__`
- `__module__`
- `__annotations__`
- `__qualname__`
- And other attributes

### What `wraps` actually does

`functools.wraps` is a decorator that updates the wrapper function's `__dict__` with attributes from the original function. It's essentially doing:

```python
wrapper.__name__ = func.__name__
wrapper.__doc__ = func.__doc__
wrapper.__module__ = func.__module__
wrapper.__dict__.update(func.__dict__)
# ... and more
```

But it does it correctly and handles edge cases, so always use `wraps` instead of doing it manually.

### When metadata matters

Without `wraps`, debugging becomes harder:

```python
# Without wraps
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    """This function does something slow."""
    time.sleep(1)
    return "done"

# In a traceback, you'd see "wrapper" instead of "slow_function"
# Making debugging much harder
```

With `wraps`, tracebacks and debugging tools show the correct function name, making problems easier to diagnose.

## Class-based decorators

Decorators don't have to be functions. You can create decorators using classes:

```python
from functools import wraps

class CountCalls:
    def __init__(self, func):
        self.func = func
        self.count = 0
        wraps(func)(self)  # Preserve metadata
    
    def __call__(self, *args, **kwargs):
        self.count += 1
        print(f"{self.func.__name__} called {self.count} times")
        return self.func(*args, **kwargs)

@CountCalls
def greet():
    print("Hello!")

greet()  # greet called 1 times
greet()  # greet called 2 times
```

When you use `@CountCalls`, Python calls `CountCalls(greet)`, which creates an instance. When you call `greet()`, Python calls the instance's `__call__` method.

### Class-based decorators with arguments

You can also create class-based decorators that accept arguments:

```python
from functools import wraps

class Repeat:
    def __init__(self, times):
        self.times = times
    
    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(self.times):
                result = func(*args, **kwargs)
            return result
        return wrapper

@Repeat(3)
def greet():
    print("Hello!")

greet()
# Output:
# Hello!
# Hello!
# Hello!
```

Here, `Repeat(3)` creates an instance, then that instance is called with `greet` as an argument, which returns the wrapper.

## Summary

- **Execution timing matters**: Decorators run at definition time, wrappers run at call time. This affects when state is created and when code executes.
- **Decorators stack bottom to top**: Multiple decorators apply from the bottom up, and order matters.
- **Decorators with arguments need three layers**: Outer function (takes arguments), decorator (takes function), wrapper (wraps call).
- **Always use `functools.wraps`**: Preserves function metadata for debugging, documentation, and introspection.
- **Decorators can be classes**: Classes can act as decorators by implementing `__call__` or `__init__` appropriately.

Understanding these advanced concepts helps you write more sophisticated decorators and debug decorator-related issues. For fundamental decorator concepts and common patterns, see the [guide on decorators](../../guides/functions/decorators).

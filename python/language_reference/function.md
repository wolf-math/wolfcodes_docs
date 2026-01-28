---
title: Function
sidebar_position: 22
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
>>> def f(x, y=1): return x + y
>>> [name for name in dir(f) if not name.startswith("__")]
['__annotations__', '__call__', '__closure__', '__code__', '__defaults__', '__dict__', '__doc__', '__globals__', '__kwdefaults__', '__module__', '__name__', '__qualname__']
```

## Definition

In Python, a **function** is a first-class object created with `def` or `lambda`. Functions can be stored in variables, passed to other functions, returned from functions, and inspected at runtime. They support positional arguments, keyword arguments, defaults, `*args`, `**kwargs`, and type annotations.

```python
def add(a, b):
    return a + b

result = add(2, 3)
```

## Creating and using functions

```python
def greet(name: str, punctuation: str = "!") -> str:
    """Return a greeting."""
    return f"Hello, {name}{punctuation}"
```

### Lambda (anonymous) functions

```python
square = lambda x: x * x
square(4)  # 16
```

### Parameters and arguments

- **Positional**: `f(1, 2)`
- **Keyword**: `f(a=1, b=2)`
- **Defaults**: defined in the function signature
- **Var-positional** (`*args`): collects extra positional args
- **Var-keyword** (`**kwargs`): collects extra keyword args
- **Keyword-only**: parameters after `*` must be passed by name

```python
def demo(a, b=1, *args, scale=1, **kwargs):
    return (a + b + sum(args)) * scale

demo(1, 2, 3, 4, scale=2)  # (1+2+3+4)*2 = 20
```

### Returning values

Use `return` to send a value back to the caller. `return` without a value (or reaching the end) yields `None`.

```python
def maybe(flag):
    if flag:
        return 42
    # returns None otherwise
```

### Docstrings and annotations

```python
def area(radius: float) -> float:
    """Compute the area of a circle."""
    import math
    return math.pi * radius * radius

area.__doc__        # "Compute the area of a circle."
area.__annotations__  # {'radius': <class 'float'>, 'return': <class 'float'>}
```

### First-class functions

Functions can be stored, passed, and returned just like other objects.

```python
def apply(fn, value):
    return fn(value)

apply(lambda x: x + 1, 5)  # 6
```

### Closures

Inner functions can capture variables from the enclosing scope.

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

add5 = make_adder(5)
add5(10)  # 15
```

### Decorators

Functions can be wrapped to add behavior.

```python
def log(fn):
    def wrapper(*args, **kwargs):
        print("calling", fn.__name__)
        return fn(*args, **kwargs)
    return wrapper

@log
def hello(name):
    return f"hi {name}"
```

### Introspection attributes

- `__name__` — function name
- `__qualname__` — qualified name (includes enclosing scopes)
- `__defaults__` / `__kwdefaults__` — default arg values
- `__code__` — code object (e.g., `co_varnames`, `co_consts`)
- `__closure__` — cells for closed-over variables
- `__globals__` — global namespace dict
- `__dict__` — writable attribute dict
- `__annotations__` — type hints
- `__doc__` — docstring

## Dunder methods

| Dunder Method     | Operation              | Example (normal syntax) | Example (dunder call) |
| --- | --- | --- | --- |
| `__call__`        | Invoke the function    | `f(3)`                  | `f.__call__(3)`       |
| `__name__`        | Function name          | `f.__name__`            | *(attribute)*         |
| `__qualname__`    | Qualified name         | `f.__qualname__`        | *(attribute)*         |
| `__defaults__`    | Default positional     | `f.__defaults__`        | *(attribute)*         |
| `__kwdefaults__`  | Default keyword-only   | `f.__kwdefaults__`      | *(attribute)*         |
| `__code__`        | Code object metadata   | `f.__code__.co_varnames`| *(attribute)*         |
| `__annotations__` | Type hints             | `f.__annotations__`     | *(attribute)*         |
| `__doc__`         | Docstring              | `f.__doc__`             | *(attribute)*         |
| `__dict__`        | Custom attributes      | `f.__dict__`            | *(attribute)*         |
| `__module__`      | Module name            | `f.__module__`          | *(attribute)*         |

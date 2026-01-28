---
title: Higher-order Functions
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
## What are higher-order functions?

A **higher-order function** is a function that does **at least one** of the following:
- **Takes one or more functions as arguments**, or
- **Returns a function as its result**.

In Python, functions are *first-class citizens*, which means you can:
- Store them in variables
- Pass them to other functions
- Return them from functions
- Put them in lists, dicts, and other data structures

```python
def shout(name):
    return f"HELLO, {name.upper()}!"

# function as a value
print(shout("Alice"))   # Use it directly
func = shout            # Store in variable
print(func("Bob"))      # Call through variable
```

Many built-in tools in Python, like `map`, `filter`, `sorted`, and `functools.reduce`, are higher-order functions because they accept other functions as arguments.

## Why this matters

Higher-order functions let you:

- **Reduce duplication** by abstracting common patterns (for example, "loop over a list and transform each item")
- **Write more expressive code** by naming the *behavior* instead of writing manual loops everywhere
- **Compose behavior** by building functions out of smaller, reusable functions

They're especially useful when working with:

- Collections (lists, sets, dicts)
- Callbacks and event handlers
- Decorators and function wrappers
- Functional-style programming

Understanding higher-order functions will make it easier to read modern Python code and work with many popular libraries.

## Functions as arguments

Any function that accepts another function as a parameter is a higher-order function.

### Example: Applying a function to a value

```python
def apply_twice(func, value):
    """Call func(value) twice, feeding the result back in."""
    return func(func(value))

def add_one(x):
    return x + 1

print(apply_twice(add_one, 3))  # 5  (3 -> 4 -> 5)
```

Here, `apply_twice` is a higher-order function because it **takes a function** (`func`) as an argument.

## Built-in higher-order functions

Python includes several higher-order functions in the standard library.

### `map`

`map(function, iterable)` applies a function to each element of an iterable.

```python
numbers = [1, 2, 3, 4]

def square(x):
    return x ** 2

squares = list(map(square, numbers))
print(squares)  # [1, 4, 9, 16]
```

You can also use a lambda:

```python
squares = list(map(lambda x: x ** 2, numbers))
```

### `filter`

`filter(function, iterable)` keeps only the items for which the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6]

def is_even(x):
    return x % 2 == 0

evens = list(filter(is_even, numbers))
print(evens)  # [2, 4, 6]
```

### `sorted` with a key function

`sorted(iterable, key=function)` uses the key function to determine the sort order.

```python
words = ["apple", "banana", "kiwi", "cherry"]

# Sort by length
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # ['kiwi', 'apple', 'banana', 'cherry']

# Sort by last character
sorted_by_last = sorted(words, key=lambda w: w[-1])
print(sorted_by_last)    # ['banana', 'apple', 'kiwi', 'cherry']
```

### `functools.reduce`

`reduce(function, iterable)` applies a function cumulatively to the items of an iterable.

```python
from functools import reduce

numbers = [1, 2, 3, 4]

def multiply(x, y):
    return x * y

product = reduce(multiply, numbers)
print(product)  # 24 (1 * 2 * 3 * 4)
```

## Functions that return functions

A function that **returns another function** is also a higher-order function.

### Function factories

```python
def make_multiplier(factor):
    """Return a function that multiplies its input by factor."""
    def multiply(x):
        return x * factor
    return multiply

by_2 = make_multiplier(2)
by_3 = make_multiplier(3)

print(by_2(10))  # 20
print(by_3(10))  # 30
```

Here, `make_multiplier` is a higher-order function because it **returns** the `multiply` function.

### Closures and state

The returned function remembers values from the outer scope. This is called a **closure**.

```python
def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
```

## Decorators: A common higher-order pattern

A **decorator** is a higher-order function that takes a function, wraps it with extra behavior, and returns a new function.

### Simple decorator example

```python
def debug(func):
    """Print the function name and arguments each time it's called."""

    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper

@debug
def add(a, b):
    return a + b

add(2, 3)
# Calling add with args=(2, 3), kwargs={}
# add returned 5
```

Here:

- `debug` is a higher-order function (takes a function and returns a new function).
- `wrapper` is the function that actually runs around `add`.
- `@debug` is shorthand for `add = debug(add)`.

Decorators are used heavily in real-world Python code (web frameworks, testing libraries, CLI tools, and more).

## Combining higher-order functions with lambdas

Because lambda functions are small and anonymous, they pair nicely with higher-order functions.

```python
numbers = [1, 2, 3, 4, 5]

from functools import reduce

evens = filter(lambda x: x % 2 == 0, numbers)
doubled = map(lambda x: x * 2, evens)
total = reduce(lambda x, y: x + y, doubled)

print(total)  # Sum of doubled even numbers: (2*2 + 4*2) = 12
```

In practice, you might prefer list comprehensions for readability, but it's important to understand how these pieces fit together.

## When to use higher-order functions

Higher-order functions are a good fit when:

- You find yourself writing the **same loop pattern** with only the inner operation changing.
- You want to **parameterize behavior** (for example, "do X, but let the caller decide exactly how").
- You need to **wrap or extend behavior** (decorators, logging, timing, access control).

They might be overkill when the logic is simple and a plain `for` loop is clearer to a beginner. As you write more Python, you'll develop a feel for when a higher-order function makes the code more readable versus when it hides too much.



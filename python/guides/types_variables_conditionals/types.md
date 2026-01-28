---
title: Types
sidebar_position: 1
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What is a type?

A **type** describes what a value is and which operations make sense for it. For example, you can add two numbers together, but you can't add a number to a word.

Python is **dynamically typed**, which means you don't need to tell Python what type a value is when you create it. Python figures this out automatically. This makes Python easier to learn than languages where you must declare types ahead of time.

```python
x = 3          # int
y = "hello"    # str
z = [1, 2, 3]  # list
```

Use `type(value)` to see a value's type:

```python
>>> type(3)
<class 'int'>
>>> type("hi")
<class 'str'>
```

## Why this matters

Understanding types is fundamental to Python programming. Every value has a type, and the type determines what you can do with that value. You can add numbers, concatenate strings, and append items to lists, but trying to add a string to a number or call list methods on a number will cause errors. Types help you write correct code by defining what operations are valid for each kind of data. As you learn Python, you'll constantly work with different types, so getting comfortable with the core types early will make everything else easier.

## Core built-in types you'll meet first

- Numbers: `int`, `float`, `complex`
- Text: `str`
- Booleans: `bool`
- Empty/“no value”: `None` (the single instance of type `NoneType`)
- Collections:
  - `list` (mutable sequence)
  - `tuple` (immutable sequence)
  - `dict` (key/value mapping)
  - `set` / `frozenset` (unique unordered elements)

### Numbers

Python has three types of numbers:

```python
>>> 42           # int (whole numbers like 1, 2, 100, -5)
>>> 3.14         # float (decimal numbers like 3.14, 2.5, -0.1)
>>> 1 + 2j       # complex (for advanced math)
```

For now, focus on `int` and `float`. You'll use `int` for counting things (1, 2, 3) and `float` for measurements and calculations with decimals (3.14, 2.5).

### Strings (`str`)

Text is stored in strings, enclosed in quotes. Strings are **immutable**, which means once you create a string, you can't change individual characters in it. If you need to change a string, you create a new one instead.

```python
>>> "hello"
'hello'
>>> "hi " + "there"
'hi there'
>>> "ha" * 3
'hahaha'
```

### Booleans (`bool`)

`True` and `False` are booleans—they represent yes/no or on/off states. You'll use these when you learn about conditionals (making decisions in your code).

```python
>>> True
True
>>> False
False
>>> bool(0)      # 0 converts to False
False
>>> bool("text") # Non-empty strings convert to True
True
```

:::note
You'll learn more about how Python treats different values as "truthy" or "falsy" in the [truthiness](../types_variables_conditionals/truthiness) guide. For now, just know that `True` and `False` are the boolean values.
:::

### None

`None` represents "no value" or "nothing here." It's Python's way of saying "this doesn't have a value yet" or "this is empty."

```python
result = None
print(result)  # None
```

You'll use `None` when you want to indicate that a variable doesn't have a value yet, or when a function doesn't return anything. We'll see more examples of this as you learn more about Python.

### Collections (containers)

Collections are types that can hold multiple values:

```python
>>> [1, 2, 3]                 # list - ordered, can be changed
>>> (1, 2, 3)                 # tuple - ordered, cannot be changed
>>> {"a": 1, "b": 2}          # dict - stores key/value pairs
>>> {1, 2, 3}                 # set - stores unique items
```

**Mutable vs Immutable**: 
- **Mutable** types (like `list`) can be changed after you create them. You can add, remove, or modify items.
- **Immutable** types (like `tuple` and `str`) cannot be changed after creation. If you need to change them, you create a new one.

Don't worry if this seems abstract right now. You'll get lots of practice with these types in the coming sections: [lists](../iterables/lists), [dictionaries](../iterables/dictionaries), and [sets](../iterables/sets).

### Bytes (binary data)

Bytes are used for working with binary data (like reading files or network data). You probably won't need these until you're working on more advanced projects.

```python
>>> b"hi"             # bytes (immutable)
>>> bytearray(b"hi")  # bytearray (mutable)
```

For now, you can skip this, you'll learn about it when you need it.

## Checking and converting types

You can check what type a value is using `type()`:

```python
>>> type(3)
<class 'int'>
>>> type("hello")
<class 'str'>
```

You can also use `isinstance()` to check if a value is a specific type:

```python
>>> isinstance(3, int)
True
>>> isinstance(3.5, int)
False
```

## Converting between types

Sometimes you need to convert a value from one type to another. Python provides functions for this:

```python
>>> int("5")        # Convert string to integer
5
>>> float("3.14")   # Convert string to decimal number
3.14
>>> str(42)         # Convert number to string
'42'
>>> list("abc")     # Convert string to list of characters
['a', 'b', 'c']
```

:::warning
Be careful: converting invalid input will cause an error. For example, you can't convert the text "not a number" into a number:

```python
>>> int("not a number")
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'not a number'
```
:::

## Identity vs equality

This is an important concept that confuses many beginners. There are two ways to compare values in Python:

- **Equality (`==`)**: Checks if two values have the same **contents** or are equivalent.
- **Identity (`is`)**: Checks if two names refer to the **exact same object** in memory.

Think of it like this, equality asks "do these have the same value?" while identity asks "are these the exact same thing?"

```python
>>> a = [1, 2, 3]
>>> b = [1, 2, 3]
>>> a == b    # Do they have the same contents? Yes!
True
>>> a is b    # Are they the same object? No! They're two different lists
False
```

Here's what's happening: `a` and `b` are two separate lists that happen to contain the same values. They're like two identical shopping lists written on different pieces of paper. They have the same contents, but they're different objects.

But if you assign one name to another:

```python
>>> a = [1, 2, 3]
>>> b = a      # b now refers to the same list as a
>>> a is b     # Are they the same object? Yes!
True
>>> a == b     # Do they have the same contents? Yes!
True
```

Now both `a` and `b` point to the same list object.

**When to use which?**
- Use `==` when you want to check if values are the same (this is what you'll use most of the time).
- Use `is` when you want to check if two names refer to the exact same object. The most common use is checking for `None`: `if value is None:` (not `if value == None:`).

For numbers and strings, `==` and `is` often give the same result, but for lists, dictionaries, and other collections, they're different. Don't worry if this seems confusing—you'll get more comfortable with it as you practice!

## When to choose which type

- Use `int`/`float` for numbers, `str` for text, `bool` for flags.
- Use `list` when you need an ordered, changeable sequence.
- Use `tuple` for fixed groups of items that shouldn’t change.
- Use `dict` for key/value lookups.
- Use `set` when you need uniqueness or fast membership checks.
- Use `bytes`/`bytearray` for binary data.




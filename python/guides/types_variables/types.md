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

A **type** describes what a value is and what you can do with it.

```python
year = 1959
record_title = "Kind of Blue"
genres = ["Jazz", "Modal Jazz"]
```

Here:

- `1959` is an `int`
- `"Kind of Blue"` is a `str`
- `["Jazz", "Modal Jazz"]` is a `list`

Python is **dynamically typed**, which means you do not have to declare types ahead of time. Python figures them out from the values you assign.

## Why this matters

Every value in Python has a type, and the type determines what operations make sense.

For example:

- you can add numbers
- you can join strings
- you can append to lists
- you cannot add a number directly to a string

Understanding types helps you predict what code will do and avoid common mistakes.

The vinyl tracker project depends on several types at once: strings for artist names, numbers for years and prices, booleans for yes/no states, and collections for groups of records.

## Checking a value's type

Use `type()` to inspect a value:

```python
>>> type(1959)
<class 'int'>

>>> type("Rumours")
<class 'str'>
```

You can also use `isinstance()`:

```python
>>> isinstance(22.5, float)
True

>>> isinstance("Blue Train", str)
True
```

## Core built-in types

These are the main built-in types you will meet first:

- numbers: `int`, `float`, `complex`
- text: `str`
- booleans: `bool`
- no value: `None`
- collections: `list`, `tuple`, `dict`, `set`

## Numbers

Python has several number types, but the most common early on are `int` and `float`.

```python
record_count = 12
purchase_price = 18.0
estimated_value = 31.5
```

- `int` is for whole numbers like `12`
- `float` is for decimal numbers like `18.0`

In the record tracker:

- `year` might be an integer
- `purchase_price` might be a float

## Strings

Strings store text.

```python
record_title = "Electric Ladyland"
artist = "Jimi Hendrix"
```

Strings are immutable, which means you cannot change individual characters in place. If you need a different string, Python creates a new one.

```python
artist = "Miles"
artist = artist + " Davis"
```

## Booleans

Booleans are `True` and `False`.

```python
is_first_pressing = True
is_duplicate_copy = False
```

These values are useful for yes/no situations, such as whether a record is a duplicate, whether a wishlist item has been found, or whether a copy is sealed.

## `None`

`None` represents the absence of a value.

```python
notes = None
```

You might use `None` when a record does not have optional information yet, such as missing notes or an unknown estimated value.

## Collections

Collections hold multiple values.

```python
favorite_albums = ["Blue Train", "Rumours", "Are You Experienced"]
record_info = {"title": "Rumours", "year": 1977}
genres = {"Jazz", "Rock", "Psychedelic Rock"}
pressing_details = ("US", 1977)
```

- `list` is ordered and mutable
- `tuple` is ordered and immutable
- `dict` stores key/value pairs
- `set` stores unique values

You will study these more deeply in the data structures section.

## Mutable vs immutable types

Some types can change after creation, and some cannot.

Mutable examples:

- `list`
- `dict`
- `set`

Immutable examples:

- `int`
- `float`
- `str`
- `tuple`

This matters because mutating a list changes the same object, while changing a string usually means creating a new one.

## Converting between types

Sometimes you need to convert one type into another.

```python
year_text = "1977"
year = int(year_text)

price_text = "22.5"
price = float(price_text)

label_number = 42
label_text = str(label_number)
```

**What happens:**

- `int("1977")` produces the integer `1977`
- `float("22.5")` produces the float `22.5`
- `str(42)` produces the string `"42"`

Be careful: invalid conversions raise errors.

```python
>>> int("Blue Train")
Traceback (most recent call last):
  ...
ValueError: invalid literal for int() with base 10: 'Blue Train'
```

## Identity vs equality

Types also matter when you compare values.

```python
record_a = ["Blue Train", 1957]
record_b = ["Blue Train", 1957]
record_c = record_a
```

```python
record_a == record_b  # True
record_a is record_b  # False
record_a is record_c  # True
```

- `==` checks whether values are equal
- `is` checks whether two names point to the same object

## In the vinyl tracker

One record already uses several types at once:

```python
record_title = "Are You Experienced"
artist = "The Jimi Hendrix Experience"
year = 1967
purchase_price = 22.5
is_favorite = True
genres = ["Psychedelic Rock", "Blues Rock"]
notes = None
```

This small example is a preview of the final project:

- strings for names and labels
- numbers for years and prices
- booleans for yes/no states
- lists for groups of values
- `None` when information is missing

As the project grows, understanding these types will make the bigger data structures and classes feel much more natural.

## When to choose which type

- use `int` for counts and years
- use `float` for prices and measured values
- use `str` for names, titles, and genres
- use `bool` for yes/no facts
- use `list` for ordered, changeable groups
- use `tuple` for fixed groups
- use `dict` for labeled record data
- use `set` when uniqueness matters

## Summary

A type describes what a value is and what operations are valid for it. Python figures types out automatically, but understanding them is still essential.

In the vinyl tracker project, types help you model real record data correctly: text for titles, numbers for prices, booleans for flags, and collections for grouped information.

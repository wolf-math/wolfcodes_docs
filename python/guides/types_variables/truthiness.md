---
title: Truthiness
sidebar_position: 3
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What is truthiness?

**Truthiness** is Python's way of treating any value as either truthy or falsy.

Some values behave like `False`, and everything else behaves like `True`.

```python
artist = "Miles Davis"
bool(artist)
```

```python
empty_notes = ""
bool(empty_notes)
```

In the first case, the non-empty string is truthy. In the second case, the empty string is falsy.

## Why this matters

Truthiness makes Python code shorter and more natural.

It helps with:

- checking whether values are empty
- deciding whether optional data exists
- choosing fallback values
- writing cleaner conditions

The vinyl tracker project uses this idea constantly. Empty notes, missing values, empty collections, and optional user input all depend on truthiness.

## Falsy values

These common values are falsy in Python:

- `False`
- `None`
- `0`
- `0.0`
- `""`
- `[]`
- `{}`
- `set()`
- `()`

```python
bool(False)
bool(None)
bool(0)
bool("")
bool([])
```

All of those evaluate to `False`.

## Truthy values

Everything that is not falsy is truthy.

Examples:

- non-zero numbers
- non-empty strings
- non-empty lists
- non-empty dictionaries

```python
bool("Blue Train")
bool(1959)
bool(["Jazz", "Modal Jazz"])
```

All of those evaluate to `True`.

## The `bool()` function

Use `bool()` when you want to convert a value into an explicit boolean.

```python
bool("Rumours")   # True
bool("")          # False
bool(22.5)        # True
bool(0)           # False
```

This is useful when you want to inspect how Python treats a value.

## Truthiness with logical operators

Truthiness works closely with `and`, `or`, and `not`.

### `or`

`or` returns the first truthy value, or the last value if none are truthy.

```python
notes = ""
display_notes = notes or "No notes yet"
```

Because `notes` is an empty string, Python uses `"No notes yet"` instead.

### `and`

`and` returns the first falsy value, or the last value if all are truthy.

```python
"Jazz" and "Blue Train"
```

That expression returns `"Blue Train"` because both values are truthy, so Python ends on the last one.

### `not`

`not` flips truthiness.

```python
not ""
not "Rumours"
```

The first becomes `True`, and the second becomes `False`.

## Truthiness vs explicit comparisons

Sometimes you want to know whether something is empty in general. Other times you need to check for one specific value.

### Truthiness checks

```python
notes = ""
if not notes:
    print("No notes yet")
```

This checks whether `notes` is falsy.

### Explicit comparisons

```python
estimated_value = None
if estimated_value is None:
    print("No estimated value yet")
```

This checks for one specific value: `None`.

Use truthiness when you want a broad empty-or-not check. Use explicit comparisons when the exact value matters.

## Common patterns

### Default values with `or`

```python
artist_name = ""
display_name = artist_name or "Unknown Artist"
```

### Filtering empty values

```python
genres = ["Jazz", "", "Rock", None, "Blues Rock"]
clean_genres = [genre for genre in genres if genre]
```

This keeps only truthy values.

### Checking whether a collection has anything in it

```python
wishlist = []

if not wishlist:
    print("Your wishlist is empty.")
```

## Common pitfalls

### Empty string vs `None`

These are both falsy, but they are not the same thing.

```python
notes = ""
notes is None  # False

notes = None
notes is None  # True
```

### Zero is falsy

```python
purchase_price = 0
bool(purchase_price)  # False
```

That does not mean the value is missing. It only means zero counts as falsy.

### Whitespace is still truthy

```python
notes = " "
bool(notes)  # True
```

A string with spaces is not empty, so Python treats it as truthy.

## In the vinyl tracker

Truthiness makes small project features much cleaner:

```python
notes = ""
display_notes = notes or "No notes yet"

wishlist = []
has_wishlist_items = bool(wishlist)
```

You could also check whether record notes exist before printing them:

```python
if notes:
    print(notes)
```

These are simple examples, but they are the same kinds of checks that show up in the final capstone project when the app handles optional data and empty collections.

## Best practices

- use truthiness for broad empty-or-not checks
- use explicit comparisons when the exact value matters
- remember that `0`, `""`, and empty collections are falsy
- use `or` when you want a fallback value

## Summary

Truthiness is Python's rule for treating any value as truthy or falsy.

It helps you write cleaner checks for empty strings, missing values, and empty collections. In the vinyl tracker project, truthiness is useful for optional notes, fallback labels, and checking whether collections contain any records.

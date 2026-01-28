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

**Truthiness** is Python's way of treating any value as either "truthy" (like `True`) or "falsy" (like `False`). 

In many programming languages, you can only use `True` and `False` when checking conditions. Python is more flexible because you can use any value, and Python will automatically treat it as truthy or falsy based on what it is.

Think of it this way: some values are "empty" or "nothing" (falsy), and everything else is "something" (truthy).

```python
>>> name = "Alice"
>>> bool(name)  # Non-empty string is truthy
True

>>> items = []
>>> bool(items)  # Empty list is falsy
False
```

## Why this matters

Truthiness is fundamental to Python programming because:

- **Works with any type**: You don't need to convert values to `True` or `False` first
- **Cleaner code**: Instead of writing `if value == True:`, you can just write `if value:` 
- **Logical operators**: `and`, `or`, and `not` work with truthiness to create useful expressions
- **Default values**: You can use `or` to provide fallback values when something is empty or missing
- **Common patterns**: Many Python code patterns rely on truthiness

:::note
You'll see truthiness in action when you learn about [conditionals](./conditionals) (making decisions in your code). For now, we'll focus on understanding which values are truthy and which are falsy.
:::

## Falsy values

These values are considered **falsy** in Python. They evaluate to `False` in boolean contexts:

### The falsy values

1. **`False`** - The boolean `False` itself
2. **`None`** - Python's way of saying "no value"
3. **`0`** - The number zero (integer)
4. **`0.0`** - The number zero (decimal/float)
5. **`""`** - An empty string (no text)
6. **`[]`** - An empty list (no items)
7. **`{}`** - An empty dictionary (no key-value pairs)
8. **`set()`** - An empty set (no unique items)
9. **`()`** - An empty tuple (no items)

:::note
There's also `0j` (complex zero), but you probably won't need that until you're doing advanced math. For now, just remember that zero in any form is falsy.
:::

```python
# All of these are falsy
>>> bool(False)
False

>>> bool(None)
False

>>> bool(0)
False

>>> bool("")
False

>>> bool([])
False

>>> bool({})
False
```

### Testing falsy values

You can use the `bool()` function to see if a value is falsy (returns `False`) or truthy (returns `True`):

```python
>>> bool(False)
False

>>> bool(None)
False

>>> bool(0)
False

>>> bool("")
False

>>> bool([])
False

>>> bool({})
False
```

All of these return `False` because they're falsy values.

## Truthy values

Everything that's not falsy is **truthy**. These will evaluate to `True` in boolean contexts:

```python
# All of these are truthy
>>> bool(True)
True

>>> bool(1)
True

>>> bool(-1)  # Negative numbers are truthy!
True

>>> bool("hello")
True

>>> bool([1, 2, 3])
True

>>> bool({"key": "value"})
True
```

### Common truthy values

- **Non-zero numbers**: `1`, `-1`, `3.14`, `-0.5` (any number that isn't zero)
- **Non-empty strings**: `"hello"`, `" "` (even a string with just a space is truthy!)
- **Non-empty collections**: `[1]`, `{"key": "value"}`, `(1,)`, `{1}` (any collection with at least one item)
- **Most objects**: Functions, modules, and other objects are usually truthy

The key idea: if it's not empty and not zero, it's truthy!

```python
>>> bool(1)
True

>>> bool(-1)
True

>>> bool("hello")
True

>>> bool(" ")  # Even a single space is truthy!
True

>>> bool([1, 2, 3])
True

>>> bool({"key": "value"})
True
```

## Using truthiness with logical operators

The logical operators `and`, `or`, and `not` work with truthiness in interesting ways. Let's see how they behave:

### `or` - Returns the first truthy value, or the last value if all are falsy

The `or` operator is useful for providing default values:

```python
>>> name = ""
>>> result = name or "Anonymous"  # name is falsy, so use "Anonymous"
>>> result
"Anonymous"

>>> name = "Alice"
>>> result = name or "Anonymous"  # name is truthy, so use "Alice"
>>> result
"Alice"
```

Think of `or` as saying: "Use the first value if it's truthy, otherwise use the second value."

### `and` - Returns the first falsy value, or the last value if all are truthy

```python
>>> "hello" and "world"  # First is truthy, so return the second
"world"

>>> "" and "world"       # First is falsy, so return the first (falsy value)
""
```

Think of `and` as saying: "If the first value is truthy, return the second value. Otherwise, return the first value."

### `not` - Inverts truthiness

```python
>>> not ""        # Empty string is falsy, so not "" is True
True

>>> not "hello"   # Non-empty string is truthy, so not "hello" is False
False

>>> not []        # Empty list is falsy, so not [] is True
True
```

The `not` operator flips truthy to `False` and falsy to `True`.

## Common patterns

### Default values with `or`

```python
>>> user_name = None
>>> display_name = user_name or "Anonymous"
>>> display_name
"Anonymous"

>>> user_name = ""
>>> display_name = user_name or "Anonymous"
>>> display_name
"Anonymous"

>>> user_name = "Alice"
>>> display_name = user_name or "Anonymous"
>>> display_name
"Alice"
```

### Filtering falsy values

You can use truthiness to filter out empty or falsy values from a list. (You'll learn more about this when you study lists and loops.)

```python
>>> names = ["Alice", "", "Bob", None, "Charlie", ""]
>>> valid_names = [name for name in names if name]  # Only keep truthy names
>>> valid_names
["Alice", "Bob", "Charlie"]
```

This keeps only the names that are truthy (non-empty strings), filtering out empty strings and `None`.

### Chaining defaults

```python
>>> value1 = None
>>> value2 = None
>>> value3 = "found"
>>> result = value1 or value2 or value3 or "default"
>>> result
"found"
```

## The `bool()` function

The `bool()` function explicitly converts any value to a boolean:

```python
>>> bool(0)
False

>>> bool(1)
True

>>> bool("")
False

>>> bool("hello")
True

>>> bool([])
False

>>> bool([1, 2, 3])
True
```

This is useful when you need an explicit boolean value rather than relying on truthiness in a conditional.

## Custom truthiness (advanced)

:::note
This section covers advanced topics about creating your own classes. You can skip this for now and come back to it after you've learned about [classes and object-oriented programming](../oop/intro).
:::

When you create your own classes, you can control how they behave with truthiness by defining special methods. This is an advanced topic, so don't worry if it seems confusing right now.

If you create a class and don't define these special methods, instances of your class will always be truthy.

## Truthiness vs. explicit comparisons

Sometimes you need to be specific about what you're checking for. There's a difference between checking if something is falsy and checking if it's a specific value:

### Explicit comparisons

These check for specific values:

```python
>>> value = None
>>> value is not None  # Is value specifically None? No, it IS None
False

>>> name = ""
>>> name != ""  # Is name not equal to empty string? No, it IS ""
False

>>> count = 0
>>> count == 0  # Is count equal to zero? Yes
True
```

### Truthiness evaluation

These check if something is truthy or falsy (could be multiple things):

```python
>>> name = "Alice"
>>> bool(name)  # Is name truthy? Yes (non-empty string)
True

>>> items = [1, 2, 3]
>>> bool(items)  # Is items truthy? Yes (non-empty list)
True

>>> user_input = ""
>>> bool(user_input)  # Is user_input truthy? No (empty string is falsy)
False
```

**When to use which?**
- Use **truthiness** (`bool(value)`) when you want to know if something has a value (not empty, not zero, not None)
- Use **explicit comparisons** (`value == 0`, `value is None`) when you need to check for a specific value

:::note
When you learn about [conditionals](./conditionals), you'll see that `if value:` uses truthiness, while `if value is not None:` uses explicit comparison. Both have their place, and you'll learn when to use each one.
:::

## Common pitfalls

### Empty string vs. None

```python
>>> name = ""
>>> bool(name)  # False - empty string is falsy
False

>>> name is None  # False - name is "", not None
False

>>> name = None
>>> bool(name)  # False - None is falsy
False

>>> name is None  # True - name is actually None
True
```

### Zero is falsy

```python
>>> count = 0
>>> bool(count)  # False - 0 is falsy!
False

>>> count is not None  # True - 0 is a valid value, just falsy
True
```

Remember: `0` is a valid number, but it's falsy. If you need to distinguish between "no value" and "zero", use explicit checks.

### Space in strings

```python
>>> name = " "  # String with just a space
>>> bool(name)  # True - non-empty string is truthy!
True

>>> bool(name.strip())  # False - stripped string is ""
False
```

A string containing only whitespace is truthy because it's not empty. To check for "meaningful" content, strip whitespace first.


## Best practices

Here are some guidelines for working with truthiness:

1. **Use `bool()` when you need an explicit boolean**: If you need a `True` or `False` value specifically, use `bool(value)`
2. **Be explicit when the distinction matters**: Use `is None` or `== ""` when you need to check for a specific value, not just whether something is falsy
3. **Remember edge cases**: `0`, `""`, and `[]` are falsy—make sure that's what you want in your code
4. **Use `or` for defaults**: `value or "default"` is a common and useful pattern for providing fallback values

```python
# Good: Using bool() for explicit conversion
>>> items = [1, 2, 3]
>>> bool(items)
True

# Good: Explicit when distinction matters
>>> count = 0
>>> count is not None  # Distinguishes between 0 and None
True

# Good: Using truthiness for defaults
>>> user_input = ""
>>> result = user_input or "default"
>>> result
"default"
```

## Summary

Truthiness is a powerful Python feature that makes code more readable:

- **Falsy values**: `False`, `None`, `0`, `0.0`, `""`, `[]`, `{}`, `set()`, `()` — these are all "empty" or "nothing"
- **Truthy values**: Everything else — any non-zero number, non-empty string, non-empty collection, etc.
- **The `bool()` function**: Converts any value to an explicit `True` or `False`
- **Logical operators**: `and`, `or`, and `not` work with truthiness to create useful expressions
- **Default values**: Use `or` to provide fallback values when something is falsy (e.g., `name or "Anonymous"`)
- **Best practices**: Use `bool()` for explicit conversion, be explicit when you need to check for specific values

Understanding truthiness helps you write cleaner, more readable code. You'll use this knowledge extensively when you learn about [conditionals](./conditionals) (making decisions in your code)!

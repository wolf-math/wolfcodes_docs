---
title: Mutability, Identity, and Object Semantics
sidebar_position: 1.5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
This guide explains how Python compares objects, what makes objects the "same," and how copying works. 

## `==` Vs `is`: equality vs identity

Python has two ways to compare objects: `==` checks if **values** are equal, while `is` checks if they're the **same object**.

### `==` checks equality

The `==` operator checks if two objects have the same **value**:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True - same values
```

Even though `a` and `b` are different objects in memory, they contain the same values, so `==` returns `True`.

### `is` checks identity

The `is` operator checks if two names reference the **same object**:

```python
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False - different objects

c = a
print(a is c)  # True - same object
```

`a` and `b` are different list objects (even though they have the same contents), so `a is b` is `False`. But `c = a` makes `c` reference the same object as `a`, so `a is c` is `True`.

### When to use each

**Use `==` when:**
- Comparing values (numbers, strings, list contents, etc.)
- Checking if two objects represent the same data
- Most comparisons in everyday code

**Use `is` when:**
- Checking for `None`: `if x is None:`
- Checking for sentinel values: `if result is MISSING:`
- Verifying two names reference the same object
- Performance-critical code (slightly faster than `==`)

```python
# Good: use 'is' for None
if user is None:
    print("No user")

# Good: use 'is' for sentinel values
MISSING = object()
if value is MISSING:
    print("Value not provided")

# Good: use '==' for value comparison
if user.age == 18:
    print("User is 18")
```

:::note
Never use `==` to compare with `None`. Always use `is None` or `is not None`. This is both more Pythonic and slightly faster.
:::

## Object identity

Every object in Python has a unique **identity**—think of it as the object's memory address. The `id()` function returns this identity, and `is` compares identities.

### Understanding `id()`

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(id(a))  # 140234567890123 (example)
print(id(b))  # 140234567890456 (different)
print(id(c))  # 140234567890123 (same as a)

print(a is b)  # False - different identities
print(a is c)  # True - same identity
```

Two objects with the same value can have different identities. Two names referencing the same object will have the same identity.

### Identity persists through mutation

When you mutate an object, its identity stays the same:

```python
my_list = [1, 2, 3]
original_id = id(my_list)

my_list.append(4)
print(id(my_list))  # Same as original_id
print(my_list is my_list)  # True (obviously)
```

The object's identity doesn't change when you modify it. Only rebinding changes which object a name references.

### Identity vs equality summary

| Comparison | What it checks | Example |
|------------|---------------|---------|
| `a == b` | Do they have the same value? | `[1, 2] == [1, 2]` → `True` |
| `a is b` | Are they the same object? | `[1, 2] is [1, 2]` → `False` |
| `id(a) == id(b)` | Same as `a is b` | Equivalent to identity check |

## Shallow vs deep copies

Sometimes you want a copy of an object. Python offers two types: **shallow copies** and **deep copies**. The difference matters when objects contain other objects.

### Shallow copies

A **shallow copy** creates a new object, but it doesn't recursively copy nested objects. Instead, it copies references to the nested objects.

```python
import copy

original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

print(original == shallow)  # True - same values
print(original is shallow)  # False - different objects

# But the nested lists are the same objects!
print(original[0] is shallow[0])  # True - same nested list
```

When you modify a nested object in a shallow copy, the original is also affected:

```python
original = [[1, 2], [3, 4]]
shallow = copy.copy(original)

shallow[0].append(5)
print(shallow)   # [[1, 2, 5], [3, 4]]
print(original)  # [[1, 2, 5], [3, 4]] - also changed!
```

This happens because `shallow[0]` and `original[0]` reference the same list object.

### Deep copies

A **deep copy** creates a new object and recursively copies all nested objects:

```python
import copy

original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

print(original == deep)  # True - same values
print(original is deep)  # False - different objects
print(original[0] is deep[0])  # False - different nested lists too!
```

Now modifications to the deep copy don't affect the original:

```python
original = [[1, 2], [3, 4]]
deep = copy.deepcopy(original)

deep[0].append(5)
print(deep)      # [[1, 2, 5], [3, 4]]
print(original)  # [[1, 2], [3, 4]] - unchanged!
```

### When to use each

**Use shallow copies when:**
- You have a flat structure (no nested mutable objects)
- You want to share nested objects (sometimes intentional)
- Performance matters (shallow copies are faster)

**Use deep copies when:**
- You have nested mutable objects
- You need complete independence between copies
- You're not sure which you need (safer default)

### Copy methods for common types

Some types have built-in copy methods that create shallow copies:

```python
import copy

# Lists
original = [1, 2, 3]
shallow = original.copy()  # or original[:] or list(original)
deep = copy.deepcopy(original)

print(original is shallow)  # False - different objects
print(original is deep)     # False - different objects
print(shallow == deep)      # True - same values

# Dictionaries
original = {"a": 1, "b": 2}
shallow = original.copy()
deep = copy.deepcopy(original)

print(original is shallow)  # False
print(original is deep)     # False
print(shallow == deep)      # True

# Sets
original = {1, 2, 3}
shallow = original.copy()
deep = copy.deepcopy(original)

print(original is shallow)  # False
print(original is deep)     # False
print(shallow == deep)      # True
```

For nested structures, the difference between shallow and deep copies becomes clear:

```python
import copy

# Nested list example
original = [[1, 2], [3, 4]]
shallow = original.copy()
deep = copy.deepcopy(original)

# Modify nested list
shallow[0].append(5)
deep[1].append(6)

print(original)  # [[1, 2, 5], [3, 4]] - affected by shallow copy
print(shallow)   # [[1, 2, 5], [3, 4]]
print(deep)      # [[1, 2], [3, 4, 6]] - independent
```

For deep copies, always use `copy.deepcopy()`. The built-in `.copy()` methods only create shallow copies.

## Why small integers appear "cached"

You might notice something surprising with small integers:

```python
a = 256
b = 256
print(a is b)  # True - same object!

c = 257
d = 257
print(c is d)  # False - different objects (usually)
```

This is called **interning**. CPython (the standard Python implementation) caches small integers (typically -5 to 256) as an optimization. These integers are reused, so multiple assignments create references to the same object.

### Don't rely on interning

**Important:** This is an implementation detail. Don't write code that depends on it:

```python
# BAD: Don't do this
a = 100
b = 100
if a is b:  # Might work, but unreliable
    print("Same object")

# GOOD: Use == for value comparison
a = 100
b = 100
if a == b:  # Always correct
    print("Same value")
```

The range of interned integers can vary between Python versions and implementations. Always use `==` for value comparisons, never `is` for integers (except when checking for `None`).

### Why this optimization exists

Small integers are used frequently (loop counters, indices, small calculations). By reusing the same objects, Python:
- Saves memory (no need to create new objects for common values)
- Speeds up comparisons (identity checks are faster than value checks)
- Simplifies some internal operations

But this is purely an optimization. Your code should never depend on it.

## Why strings are immutable by design

Strings in Python are **immutable**—once created, they cannot be changed. This is a deliberate design choice with important benefits.

### What immutability means

```python
text = "Hello"
text[0] = "h"  # TypeError: 'str' object does not support item assignment
```

You cannot modify a string in place. Any operation that appears to change a string actually creates a new string:

```python
text = "Hello"
new_text = text.upper()  # Creates a new string
print(text)      # "Hello" - original unchanged
print(new_text)  # "HELLO" - new object
```

### Benefits of immutable strings

**1. Safety and predictability**

Since strings can't be changed, you can safely pass them around without worrying about accidental modifications:

```python
def process_name(name):
    # Can't accidentally modify 'name' here
    return name.upper()

my_name = "Alice"
result = process_name(my_name)
print(my_name)  # "Alice" - guaranteed unchanged
```

**2. Hashability**

Immutable objects can be used as dictionary keys and set elements:

```python
# Strings can be keys
user_data = {"alice": 25, "bob": 30}

# Lists cannot (they're mutable)
# invalid = {[1, 2]: "value"}  # TypeError: unhashable type: 'list'
```

**3. Memory efficiency (interning)**

Like small integers, Python interns some strings (string literals, some computed strings). This allows string identity checks to work for common cases:

```python
a = "hello"
b = "hello"
print(a is b)  # True - same object (usually, but don't rely on it!)
```

But again, this is an implementation detail. Always use `==` for string comparisons.

**4. Thread safety**

Immutable objects are inherently thread-safe. Multiple threads can reference the same string without synchronization issues.

### Why not make strings mutable?

If strings were mutable, you'd have to constantly worry about:
- Accidental modifications when passing strings to functions
- Thread safety issues
- Unpredictable behavior when strings are used as keys
- More complex memory management

Immutability makes strings safer and more predictable, which is worth the small performance cost of creating new strings for modifications.

### Working with strings efficiently

If you need to build a string from many parts, use `.join()` instead of concatenation:

```python
# Inefficient: creates many intermediate strings
result = ""
for word in words:
    result += word  # Creates new string each time

# Efficient: builds list, joins once
result = "".join(words)  # Single string creation
```

The `.join()` method is faster because it builds the final string in one operation, rather than creating many intermediate strings.

## Summary

- **`==` checks equality** (same values), **`is` checks identity** (same object)
- Use `is` for `None` and sentinel values, `==` for everything else
- **Shallow copies** share nested objects; **deep copies** are completely independent
- Small integers are interned as an optimization—don't rely on it
- **Strings are immutable** by design for safety, hashability, and predictability
- Always use `==` for value comparisons; `is` is for identity checks only

Understanding these concepts helps you write more predictable code and avoid subtle bugs related to object identity and mutability.

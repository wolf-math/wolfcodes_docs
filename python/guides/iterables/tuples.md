---
title: Tuples
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
Tuples are immutable sequences of items, similar to lists but with one key difference: once created, tuples cannot be modified. This immutability makes them perfect for fixed data, returning multiple values from functions, and using as dictionary keys.

## What are tuples?

A **tuple** is an ordered, immutable collection of items enclosed in parentheses `()`. Tuples are:
- **Ordered**: Items have a specific position (index)
- **Immutable**: Cannot be changed after creation
- **Indexed**: Each item has a position starting from 0
- **Flexible**: Can contain items of different types

```python
point = (3, 4)
colors = ('red', 'green', 'blue')
mixed = ('apple', 2, True, 3.14)  # Can mix types!
```

## Why this matters

Tuples are essential when you need fixed, unchangeable data. Their immutability makes them safe to use as dictionary keys and prevents accidental modifications. Tuples are perfect for representing fixed pairs or groups of related values, like coordinates, database records, or function return values. They're also slightly more memory-efficient than lists and can make your code's intent clearer. **If you use a tuple, you're signaling that the data shouldn't change**. Understanding when to use tuples versus lists helps you write more appropriate and efficient code.

## Creating tuples

### Tuples with items

Put items inside parentheses, separated by commas:

```python
fruits = ('apple', 'banana', 'orange')
numbers = (1, 2, 3, 4, 5)
```

### Parentheses are optional

For simple tuples, you can omit the parentheses:

```python
# These are equivalent
point1 = (3, 4)
point2 = 3, 4

print(point1 == point2)  # True
```

### Single-element tuples

A single-element tuple requires a trailing comma:

```python
# This is NOT a tuple (it's just an integer with parentheses)
not_a_tuple = (42)
print(type(not_a_tuple))  # <class 'int'>

# This IS a tuple
is_a_tuple = (42,)
print(type(is_a_tuple))  # <class 'tuple'>

# Without parentheses, comma makes it a tuple
also_tuple = 42,
print(type(also_tuple))  # <class 'tuple'>
```

### Empty tuples

Create an empty tuple with `()`:

```python
empty = ()
# or
empty = tuple()
```

### Using the `tuple()` constructor

Convert other sequences into tuples using the [`tuple()`](../../language_reference/tuple) constructor:

```python
numbers = tuple([1, 2, 3])  # (1, 2, 3)
chars = tuple("hello")      # ('h', 'e', 'l', 'l', 'o')
```

## Accessing elements

### Indexing

Access individual items using their index (position), just like [lists](./lists):

```python
fruits = ('apple', 'banana', 'orange')

fruits[0]   # 'apple' (first item)
fruits[1]   # 'banana' (second item)
fruits[2]   # 'orange' (third item)
```

### Negative indexing

Use negative numbers to count from the end:

```python
fruits = ('apple', 'banana', 'orange')

fruits[-1]  # 'orange' (last item)
fruits[-2]  # 'banana' (second to last)
fruits[-3]  # 'apple' (third from last)
```

### Index errors

Trying to access an index that doesn't exist raises an `IndexError`:

```python
fruits = ('apple', 'banana')
fruits[5]  # IndexError: tuple index out of range
```

## Immutability

Tuples are **immutable**, meaning you cannot change them after creation:

```python
fruits = ('apple', 'banana', 'orange')

fruits[0] = 'grape'  # TypeError: 'tuple' object does not support item assignment
fruits.append('grape')  # AttributeError: 'tuple' object has no attribute 'append'
fruits.remove('apple')  # AttributeError: 'tuple' object has no attribute 'remove'
```

### Creating new tuples

Since tuples can't be modified, you create new tuples instead:

```python
fruits = ('apple', 'banana', 'orange')

# Create a new tuple with modified content
new_fruits = ('grape',) + fruits[1:]  # ('grape', 'banana', 'orange')

# Or replace the entire tuple
fruits = ('grape', 'banana', 'orange')
```

## Slicing

You can slice tuples, just like lists:

```python
fruits = ('apple', 'banana', 'orange', 'grape')

fruits[0:2]   # ('apple', 'banana')
fruits[:2]    # ('apple', 'banana') (from start)
fruits[2:]    # ('orange', 'grape') (to end)
fruits[::2]   # ('apple', 'orange') (every 2nd item)
```

Slicing the tuple creates a new tuple. It doesn't modify the original.

## Common operations

### Length

Get the number of items with [`len()`](../../language_reference/built-in#len):

```python
fruits = ('apple', 'banana', 'orange')
print(len(fruits))  # 3
```

### Membership testing

Check if an item exists with `in`:

```python
fruits = ('apple', 'banana', 'orange')

'apple' in fruits   # True
'grape' in fruits   # False
'apple' not in fruits  # False
```

### Concatenation

Combine tuples with `+`:

```python
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(combined)  # (1, 2, 3, 4, 5, 6)
```

### Repetition

Repeat a tuple with `*`:

```python
numbers = (1, 2)
repeated = numbers * 3
print(repeated)  # (1, 2, 1, 2, 1, 2)
```

### Iteration

Loop through items with [`for`](./for_loops) loops:

```python
fruits = ('apple', 'banana', 'orange')

for fruit in fruits:
    print(fruit)
```

## Packing and unpacking

### Tuple packing

Creating a tuple by putting values together is called **packing**:

```python
# Packing: creating a tuple
point = 3, 4  # Packs 3 and 4 into a tuple
print(point)  # (3, 4)
```

### Tuple unpacking

Extracting values from a tuple into variables is called **unpacking**:

```python
point = (3, 4)

# Unpacking: extracting values
x, y = point
print(x)  # 3
print(y)  # 4
```

### Extended unpacking

Use `*` to capture multiple items:

```python
numbers = (1, 2, 3, 4, 5)

first, *rest = numbers
print(first)  # 1
print(rest)   # [2, 3, 4, 5] (note: rest is a list)

first, *middle, last = numbers
print(first)   # 1
print(middle)  # [2, 3, 4]
print(last)    # 5
```

### Multiple assignment

Tuple unpacking is often used for multiple assignment:

```python
# Swapping variables (no temporary variable needed!)
a = 5
b = 10

a, b = b, a
print(a)  # 10
print(b)  # 5
```

## Tuple methods

### `count()`

Count how many times an item appears:

```python
numbers = (1, 2, 2, 3, 2, 4)
print(numbers.count(2))  # 3
print(numbers.count(5))  # 0
```

### `index()`

Find the index of the first occurrence of a value:

```python
fruits = ('apple', 'banana', 'orange', 'banana')

print(fruits.index('banana'))  # 1
print(fruits.index('orange'))  # 2

fruits.index('grape')  # ValueError: tuple.index(x): x not in tuple
```

## Common use cases

### Returning multiple values from functions

:::note
You'll learn about functions in detail later, but here's a preview of how tuples can work with them.
:::

Tuples are perfect for returning multiple values:

```python
def get_name_and_age():
    return ("Alice", 30)

name, age = get_name_and_age()
print(f"{name} is {age} years old")
```

### Coordinates and pairs

Represent fixed pairs of values:

```python
point = (3, 4)
coordinates = (10, 20)

x, y = point
print(f"Point at ({x}, {y})")
```

### Dictionary keys

Tuples can be used as [dictionary](./dictionaries) keys (unlike lists, which are mutable):

```python
# Tuples as keys (works because they're immutable)
locations = {
    (0, 0): "Origin",
    (1, 1): "Corner",
    (2, 3): "Point"
}

print(locations[(1, 1)])  # "Corner"

# Lists can't be keys (they're mutable)
# locations[[0, 0]] = "Origin"  # TypeError: unhashable type: 'list'
```

### Fixed sequences

Use tuples when the sequence shouldn't change:

```python
# Days of the week (never change)
days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# RGB color values (fixed)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
```

### Protecting data

Use tuples to ensure data integrity when you want to prevent accidental modifications:

```python
# Database record (shouldn't be modified)
student_record = ('Alice', '12345', 'A')
# Can't accidentally modify it - this would raise an error:
# student_record[0] = 'Bob'  # TypeError: 'tuple' object does not support item assignment

# Configuration settings that shouldn't change
app_config = ('localhost', 8080, True)  # host, port, debug_mode

# Constants or fixed values
PI_DIGITS = (3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5)
```

If you used a list instead, you could accidentally modify these values, which might cause bugs. Tuples prevent such accidental changes.

## Tuples vs lists

See the [lists guide](./lists) for more details on lists.

| Feature | Tuples | Lists |
|---------|--------|-------|
| Mutability | Immutable | Mutable |
| Syntax | `()` or commas | `[]` |
| Use case | Fixed data, keys | Changing collections |
| Performance | Slightly faster | Slightly slower |
| Memory | Slightly less | Slightly more |

### When to use tuples

- When data shouldn't change
- When you need a dictionary key
- When returning multiple values from a function
- When you want to ensure data integrity
- For fixed, constant sequences

### When to use lists

- When you need to add, remove, or modify items
- When working with sequences that change
- When you need list-specific methods

```python
# Good: Use tuple for fixed coordinates
point = (3, 4)

# Good: Use list for changing collection
shopping_list = ['apple', 'banana']
shopping_list.append('orange')

# Good: Use tuple as dictionary key
locations = {(0, 0): "start", (1, 1): "end"}

# Bad: Can't use list as dictionary key
# locations = {[0, 0]: "start"}  # TypeError
```

## Converting between tuples and lists

### Tuple to list

```python
t = (1, 2, 3)
l = list(t)
print(l)  # [1, 2, 3]
```

### List to tuple

```python
l = [1, 2, 3]
t = tuple(l)
print(t)  # (1, 2, 3)
```

## Nested tuples

Tuples can contain other tuples (or lists):

```python
matrix = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print(matrix[0][1])  # 2 (first row, second column)

# Can also contain lists (but the tuple itself is still immutable)
mixed = (1, [2, 3], 4)
mixed[1].append(5)  # This works! The list inside is still mutable
print(mixed)  # (1, [2, 3, 5], 4)
```

## Best practices

- **Use tuples for fixed data**: When values shouldn't change
- **Use tuples as dictionary keys**: They're hashable (unlike lists)
- **Use tuples for multiple returns**: Clean way to return multiple values
- **Prefer lists when you need mutability**: Lists are better for changing collections
- **Use descriptive names**: `point`, `coordinates`, `name_age` are clearer than `t`, `x`, `y`
- **Remember single-element syntax**: Use `(value,)` for single-element tuples

```python
# Good: Clear use of tuple
def get_user_info():
    return ("Alice", 30, "Engineer")

name, age, job = get_user_info()

# Good: Tuple as dictionary key
settings = {
    (1920, 1080): "Full HD",
    (2560, 1440): "2K",
    (3840, 2160): "4K"
}

# Avoid: Using tuple when you need mutability
# coordinates = (3, 4)
# coordinates[0] = 5  # Can't do this! Use a list instead
```

## Summary

Tuples are immutable sequences that:
- Cannot be changed after creation
- Are perfect for fixed data and dictionary keys
- Support indexing, slicing the tuple, and iteration like lists
- Enable packing and unpacking for multiple assignment
- Are slightly faster and use less memory than lists

Use tuples when you need fixed, immutable sequences. They're particularly useful for returning multiple values, representing fixed pairs or coordinates, and as dictionary keys. When you need to modify a sequence, use a list instead.


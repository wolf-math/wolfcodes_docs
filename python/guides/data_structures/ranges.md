---
title: Ranges
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
Ranges represent an immutable sequence of evenly spaced integers. They're memory-efficient sequences that generate values on demand. Unlike lists, ranges don't store all values in memory, making them perfect for working with large sequences of numbers.

## What are ranges?

A **range** is an immutable sequence of integers that follows a pattern defined by start, stop, and step values. Ranges are:
- **Immutable**: Cannot be changed after creation
- **Memory efficient**: Don't store all values in memory
- **Lazy**: Generate values as needed
- **Indexed**: Can access values by position
- **Sequence-like**: Support indexing, slicing the range, and membership testing

```python
# Range from 0 to 4 (not including 5)
numbers = range(5)
print(list(numbers))  # [0, 1, 2, 3, 4]
```

## Why this matters

Ranges are essential for creating numeric sequences efficiently, especially when working with loops. They're incredibly memory-efficient because they don't store all values, instead they calculate them on demand. This makes ranges perfect for representing large sequences (even millions of numbers) without consuming excessive memory. Ranges are commonly used with for loops to repeat code a specific number of times or to generate indices for accessing other sequences. Understanding ranges helps you write cleaner loop code and work with numeric sequences without materializing large lists in memory.

## Creating ranges

### Basic syntax

Ranges use the [`range()`](../../language_reference/range) function with three possible forms:

```python
range(stop)           # Start at 0, go up to (but not including) stop
range(start, stop)    # Start at start, go up to (but not including) stop
range(start, stop, step)  # Start at start, step by step, up to (but not including) stop
```

### `range(stop)`

Start at 0 and count up to (but not including) the stop value:

```python
# Range from 0 to 4
r = range(5)
print(list(r))  # [0, 1, 2, 3, 4]
print(r[0])     # 0
print(r[4])     # 4
```

### `range(start, stop)`

Specify both start and stop values:

```python
# Range from 2 to 4
r = range(2, 5)
print(list(r))  # [2, 3, 4]
print(r[0])     # 2
print(r[-1])    # 4
```

### `range(start, stop, step)`

Add a step value to control the increment:

```python
# Range from 0 to 8, step by 2
r = range(0, 10, 2)
print(list(r))  # [0, 2, 4, 6, 8]
print(r[2])     # 4

# Negative step (count backwards)
r = range(10, 0, -2)
print(list(r))  # [10, 8, 6, 4, 2]
print(r[0])     # 10
```

## Accessing range values

### Indexing

Access individual values by index:

```python
r = range(0, 10, 2)
print(r[0])   # 0
print(r[1])   # 2
print(r[2])   # 4
print(r[-1])  # 8 (last value)
print(r[-2])  # 6 (second to last)
```

### Slicing

Slice the range to create new ranges:

```python
r = range(0, 10, 2)
print(list(r))       # [0, 2, 4, 6, 8]

sliced = r[1:3]      # range(2, 6, 2)
print(list(sliced))  # [2, 4]

# Slice from the end
end_slice = r[-2:]
print(list(end_slice))  # [6, 8]
```

### Membership testing

Check if a value is in the range:

```python
r = range(0, 10, 2)
print(4 in r)   # True
print(5 in r)   # False
print(8 in r)   # True
print(-2 in r)  # False
```

:::tip
Membership testing with ranges is very efficient because it's computed mathematically, not by iterating through all values.
:::

### Length

Get the number of values in a range:

```python
print(len(range(10)))        # 10
print(len(range(2, 10)))     # 8
print(len(range(0, 10, 2)))  # 5
print(len(range(10, 0, -1))) # 10
```

## Range attributes

Access the start, stop, and step values directly:

```python
r = range(3, 9, 2)
print(r.start)  # 3
print(r.stop)   # 9
print(r.step)   # 2

# Works with all range forms
r1 = range(5)
print(r1.start)  # 0 (default)
print(r1.stop)   # 5
print(r1.step)   # 1 (default)
```

## Converting ranges

### To lists

Convert ranges to [lists](./lists) when you need all values at once:

```python
numbers = list(range(5))           # [0, 1, 2, 3, 4]
evens = list(range(0, 10, 2))      # [0, 2, 4, 6, 8]
backwards = list(range(10, 0, -1)) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

### To tuples

Convert ranges to [tuples](./tuples):

```python
numbers = tuple(range(5))  # (0, 1, 2, 3, 4)
evens = tuple(range(0, 10, 2))  # (0, 2, 4, 6, 8)
```

### Creating sequences from ranges

Ranges are commonly used to generate sequences:

```python
# Even numbers from 0 to 18
evens = list(range(0, 20, 2))  
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Multiples of 5
multiples = list(range(0, 50, 5))  
# [0, 5, 10, 15, 20, 25, 30, 35, 40, 45]

# Reverse sequence
reverse = list(range(10, 0, -1))  
# [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```

## Range methods

### `count()`

Count how many times a value appears (always 0 or 1 for ranges):

```python
r = range(0, 10, 2)
print(r.count(4))  # 1
print(r.count(5))  # 0
print(r.count(0))  # 1
```

### `index()`

Find the index of a value:

```python
r = range(0, 10, 2)
print(r.index(4))  # 2
print(r.index(0))  # 0
print(r.index(8))  # 4

r.index(5)  # ValueError: 5 is not in range
```

## Common patterns

### Checking if a number is in a range

```python
age = 25
if age in range(18, 66):  # 18 to 65 (inclusive)
    print("Working age")

score = 87
if score in range(90, 101):  # 90 to 100
    print("Grade A")
```

### Generating indices for sequences

Ranges are useful for generating valid indices for other sequences:

```python
items = ['a', 'b', 'c', 'd']
indices = range(len(items))  # range(0, 4)
print(list(indices))  # [0, 1, 2, 3]

# Check if an index is valid
index = 2
if index in range(len(items)):
    print(f"Valid index: {items[index]}")
```

### Creating number sequences

Generate specific number patterns:

```python
# First 10 numbers
first_10 = list(range(10))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Numbers from 1 to 10
one_to_ten = list(range(1, 11))  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Even numbers
evens = list(range(0, 20, 2))  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

# Odd numbers
odds = list(range(1, 20, 2))  # [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
```

### Reversing sequences

Create reverse-ordered ranges:

```python
# Countdown from 10 to 1
countdown = list(range(10, 0, -1))  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# Countdown from 9 to 0
countdown_to_zero = list(range(9, -1, -1))  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
```

## Memory efficiency

Ranges are memory-efficient because they don't store all values:

```python
# This uses very little memory, regardless of size
small_range = range(10)
large_range = range(1_000_000_000)
huge_range = range(1_000_000_000_000)

# All use roughly the same small amount of memory
print(len(small_range))   # 10
print(len(large_range))   # 1000000000 (computed instantly!)
print(len(huge_range))    # 1000000000000 (computed instantly!)

# Converting to a list would use massive amounts of memory
# large_list = list(large_range)  # Would take time and gigabytes of memory!
```

This efficiency makes ranges ideal for representing large sequences without materializing them.

## Limitations

Ranges only work with integers:

```python
# Valid: integers only
range(10)
range(0, 10, 2)
range(10, 0, -1)

# Invalid: floats not allowed
range(0.0, 10.0)  # TypeError: 'float' object cannot be interpreted as an integer
range(0, 10, 0.5)  # TypeError
```

If you need non-integer sequences, you'll need to create them differently (we'll cover this when discussing loops).

## Using ranges with loops

Ranges are commonly used with [for loops](./for_loops) to repeat actions a specific number of times or to iterate through sequences. We'll explore loops in detail in the next section, but here's a brief preview:

```python
# Ranges work perfectly with for loops
# (Loops will be covered in detail later)
for i in range(5):
    print(i)  # Prints 0, 1, 2, 3, 4
```

For now, focus on understanding ranges as sequences that you can inspect, convert, and use with sequence operations.

## Best practices

- **Use ranges for large sequences**: They're much more memory-efficient than creating lists
- **Convert to lists only when needed**: Only call `list(range(...))` if you actually need all values
- **Remember ranges are exclusive**: The stop value is **not** included in the range
- **Use negative steps for reverse sequences**: More readable than complex calculations
- **Take advantage of lazy evaluation**: Ranges compute values on demand, saving memory

```python
# Good: Create range without converting
r = range(1000)

# Only convert if you need the list
numbers = list(r)  # Only when you need all values

# Efficient: Check membership without converting
if 500 in range(1000):
    print("In range")
```

## Summary

Ranges are efficient sequences of integers:
- Memory-efficient (don't store all values)
- Perfect for loops and counting (we'll see in the next section)
- Support indexing, slicing the range, and membership testing
- Immutable and fast
- Perfect for representing large numeric sequences

Ranges are sequences that generate integer values on demand. They're particularly useful for creating numeric patterns and working with indices. In the next section, we'll see how ranges work with loops to iterate through sequences and repeat actions.

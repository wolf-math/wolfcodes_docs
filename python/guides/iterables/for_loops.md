---
title: For Loops
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
For loops let you repeat code for each item in a sequence or iterable. They're one of the most powerful features in Python, allowing you to process collections of data efficiently. You've already seen sequences like [lists](./lists), [tuples](./tuples), strings, [sets](./sets), and [ranges](./ranges). Use `for loops` to work with all of them.

## What are for loops?

A **for loop** iterates over each item in an iterable (like a list, string, or range), executing a block of code once for each item. This eliminates repetitive code and makes it easy to process collections.

## Why this matters

For loops are fundamental to Python programming and essential for processing collections of data. Without loops, you'd have to write repetitive code for each item in a collection, which is impractical and error-prone. For loops let you process entire collections efficiently, whether you're transforming data, filtering items, searching for values, or performing calculations on each element. They're one of the most commonly used control flow structures, appearing in virtually every Python program that works with data. Mastering for loops, along with understanding how to iterate over different types of collections, is crucial for effective Python programming.

## Basic syntax

The basic form of a for loop looks like this:

```python
for <variable> in <iterable>:
    <code to run>
```

The loop variable takes on each value from the iterable in turn, and the indented code block runs once per item.

## Iterating over lists

Loop through each item in a [list](./lists):

```python
fruits = ['apple', 'banana', 'orange']

for fruit in fruits:
    print(fruit)

# Output:
# apple
# banana
# orange
```

The variable name (here `fruit`) can be anything. Use a descriptive name that matches what each item represents.

### Modifying lists while iterating

Be careful when modifying a list while iterating over it:

```python
numbers = [1, 2, 3, 4, 5]

# This can cause issues - items are skipped!
for num in numbers:
    if num == 2:
        numbers.remove(num)  # Dangerous!
```

**Why is this dangerous?** When you remove an item from a list during iteration, the list's internal structure changes. The iterator keeps track of positions by index, so when you remove an item, all subsequent items shift to fill the gap. This causes the iterator to skip the next item because it's already moved past that position. For example, if you remove `2` at index 1, the item that was at index 2 (`3`) moves to index 1, but the iterator has already moved past index 1, so it skips `3` entirely.


```python
# Better: create a new list or iterate over a copy
numbers = [1, 2, 3, 4, 5]
filtered = []
for num in numbers:
    if num != 2:
        filtered.append(num)
```

## Iterating over strings

Loop through each character in a string:

```python
word = "Python"

for char in word:
    print(char)

# Output:
# P
# y
# t
# h
# o
# n
```

Strings are sequences of characters, so loops process them character by character.

## Iterating over ranges

As we saw in the [ranges](./ranges) section, ranges are perfect for loops:

```python
# Count from 0 to 4
for i in range(5):
    print(i)

# Output:
# 0
# 1
# 2
# 3
# 4

# Count from 1 to 10
for i in range(1, 11):
    print(i)

# Count by 2s
for i in range(0, 10, 2):
    print(i)  # 0, 2, 4, 6, 8

# Count backwards
for i in range(10, 0, -1):
    print(i)  # 10, 9, 8, 7, 6, 5, 4, 3, 2, 1
```

Ranges are memory-efficient and commonly used when you need to repeat code a specific number of times.

## Iterating over sets

Loop through items in a [set](./sets) (order may vary):

```python
colors = {'red', 'green', 'blue'}

for color in colors:
    print(color)
```

:::note
Sets are unordered, so the iteration order may vary between runs. Don't rely on a specific order.
:::

## Iterating over tuples

[Tuples](./tuples) work just like lists in loops:

```python
coordinates = (3, 4)

for coord in coordinates:
    print(coord)

# Output:
# 3
# 4

# With multiple tuples
points = [(0, 0), (1, 2), (3, 4)]
for point in points:
    print(point)

# Output:
# (0, 0)
# (1, 2)
# (3, 4)
```

## Getting indices with enumerate()

Often you need both the index and the value. Use [`enumerate()`](../../language_reference/built-in#enumerate) instead of `range(len())`:

```python
fruits = ['apple', 'banana', 'orange']

# Using enumerate (Pythonic way)
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Output:
# 0: apple
# 1: banana
# 2: orange

# Start counting from 1
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}: {fruit}")

# Output:
# 1: apple
# 2: banana
# 3: orange
```

This is more Pythonic and readable than using `range(len())`:

```python
# Less Pythonic (but works)
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

## Iterating over dictionaries

[Dictionaries](./dictionaries) have special iteration behavior. By default, you iterate over keys:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

# Iterate over keys (default)
for key in person:
    print(key)

# Output:
# name
# age
# city

# Explicitly iterate over keys
for key in person.keys():
    print(key)

# Output:
# name
# age
# city

# Iterate over values
for value in person.values():
    print(value)

# Output:
# Alice
# 30
# Boston

# Iterate over key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 30
# city: Boston
```

## Loop control: break and continue

### `break`

Exit the loop immediately:

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        break  # Exit the loop
    print(num)

# Output:
# 1
# 2
```

### `continue`

Skip to the next iteration:

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        continue  # Skip this iteration
    print(num)

# Output:
# 1
# 2
# 4
# 5
```

## The `else` clause

A `for` loop can have an `else` clause that runs if the loop completes normally (without a `break`):

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 10:
        print("Found 10!")
        break
else:
    print("10 not found in list")

# Output:
# 10 not found in list
```

The `else` clause is useful for search patterns:

```python
items = ['apple', 'banana', 'orange']
target = 'grape'

for item in items:
    if item == target:
        print(f"Found {target}!")
        break
else:
    print(f"{target} not found")

# Output:
# grape not found
```

## Nested loops

Loops can be nested (a loop inside another loop):

```python
# Nested loop example
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# Output:
# i=0, j=0
# i=0, j=1
# i=1, j=0
# i=1, j=1
# i=2, j=0
# i=2, j=1
```

### Practical nested loop example

Process nested data structures:

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    for value in row:
        print(value, end=' ')  # end=' ' prints a space instead of a newline
    print()  # New line after each row

# Output:
# 1 2 3
# 4 5 6
# 7 8 9
```

## Common patterns

### Accumulating values

Sum or collect values:

```python
numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total += num

print(total)  

# Output: 
# 15
```

### Filtering items

Collect items that meet a condition:

```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = []

for num in numbers:
    if num % 2 == 0:
        evens.append(num)

print(evens)  

# Output: 
# [2, 4, 6, 8, 10]
```

### Finding items

Search for a specific item:

```python
fruits = ['apple', 'banana', 'orange']
target = 'banana'

for fruit in fruits:
    if fruit == target:
        print(f"Found {target} at index {fruits.index(fruit)}")
        break

# Output:
# Found banana at index 1
```

### Transforming items

Create new lists by transforming items:

```python
numbers = [1, 2, 3, 4, 5]
squares = []

for num in numbers:
    squares.append(num ** 2)

print(squares)  

# Output: 
# [1, 4, 9, 16, 25]
```

### Counting items

Count occurrences:

```python
fruits = ['apple', 'banana', 'apple', 'orange', 'apple']
count = 0

for fruit in fruits:
    if fruit == 'apple':
        count += 1

print(count)  

# Output: 
# 3
```

### Repeating actions

Repeat a task a specific number of times:

```python
for _ in range(5):
    print("Hello!")

# Output:
# Hello!
# Hello!
# Hello!
# Hello!
# Hello!
```

The `_` variable name is a convention meaning "I don't need this value, I just want to repeat this action".

### Processing multiple sequences together

Use `zip()` to iterate over multiple sequences simultaneously:

```python
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]

for name, age in zip(names, ages):
    print(f"{name} is {age} years old")

# Output:
# Alice is 25 years old
# Bob is 30 years old
# Charlie is 35 years old
```

## List comprehensions (preview)

Python offers a concise way to create lists called list comprehensions. They're essentially for loops in a single line:

```python
# Traditional loop
squares = []
for num in range(5):
    squares.append(num ** 2)

# List comprehension (equivalent)
squares = [num ** 2 for num in range(5)]
# [0, 1, 4, 9, 16]
```

List comprehensions will be covered in more detail in the [comprehensions guide](./comprehensions), but they're a powerful way to transform and filter data.

## Best practices

- **Use descriptive variable names**: `for fruit in fruits:` is better than `for x in fruits:`
- **Use [`enumerate()`](../../language_reference/built-in#enumerate) instead of `range(len())`**: More Pythonic when you need indices
- **Don't modify collections while iterating**: Create new collections instead
- **Use `break` and `continue` judiciously**: They can make code harder to follow if overused
- **Consider list comprehensions**: For simple transformations and filtering
- **Use [`zip()`](../../language_reference/built-in#zip) for parallel iteration**: When you need to process multiple sequences together. See the [built-in functions reference](../../language_reference/built-in) for more.
- **Keep loops simple**: If a loop gets complex, consider breaking it into functions

```python
# Good: Clear and readable
fruits = ['apple', 'banana', 'orange']
for fruit in fruits:
    print(fruit)

# Good: Using enumerate when needed
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Avoid: Modifying while iterating
for fruit in fruits:
    if fruit == 'banana':
        fruits.remove(fruit)  # Can cause issues!

# Better: Create a new list
fruits = [f for f in fruits if f != 'banana']
```

## Summary

For loops are essential for processing collections:
- Iterate over any iterable ([lists](./lists), strings, [ranges](./ranges), [sets](./sets), [dictionaries](./dictionaries))
- Use `enumerate()` to get indices
- Control flow with `break` and `continue`
- Use `else` clauses for search patterns
- Nest loops for multidimensional data
- Process and transform data efficiently

For loops are one of Python's most powerful features. They work seamlessly with all the sequence types you've learned about and are the foundation for processing data in Python. Practice iterating over different types of collections to become comfortable with this essential control structure.


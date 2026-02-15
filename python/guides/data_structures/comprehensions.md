---
title: Comprehensions
sidebar_position: 9
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
Comprehensions provide a concise, readable way to create lists, dictionaries, and sets by transforming or filtering data. They're a Pythonic alternative to loops when you're building collections, making your code more compact and often faster.

## What are comprehensions?

A **comprehension** is a compact way to create collections (lists, dictionaries, or sets) from iterables. Instead of writing a loop with `append()` or similar methods, comprehensions let you express the transformation in a single line.

## List comprehensions

List comprehensions create lists by transforming or filtering items from an iterable.

### Basic syntax

```python
[<expression> for <item> in <iterable>]
```

### Simple example

```python
# Create a list of squares
squares = [x**2 for x in range(5)]  # See [ranges](./ranges) for more on range()
print(squares)  # [0, 1, 4, 9, 16]
```

This is equivalent to:

```python
squares = []
for x in range(5):
    squares.append(x**2)
```

### With conditions (filtering)

Add an `if` clause to filter items:

```python
# Only even numbers
evens = [x for x in range(10) if x % 2 == 0]  # See [ranges](./ranges) for more on range()
print(evens)  # [0, 2, 4, 6, 8]
```

This is equivalent to:

```python
evens = []
for x in range(10):
    if x % 2 == 0:
        evens.append(x)
```

### Transforming items

Apply operations to each item:

```python
# Convert strings to uppercase
words = ['hello', 'world', 'python']
uppercase = [word.upper() for word in words]
print(uppercase)  # ['HELLO', 'WORLD', 'PYTHON']

# Extract first character
first_chars = [word[0] for word in words]
print(first_chars)  # ['h', 'w', 'p']

# Multiply numbers
numbers = [1, 2, 3, 4, 5]
doubled = [x * 2 for x in numbers]
print(doubled)  # [2, 4, 6, 8, 10]
```

### Filtering and transforming

Combine filtering and transformation:

```python
# Square only even numbers
squares_of_evens = [x**2 for x in range(10) if x % 2 == 0]
print(squares_of_evens)  # [0, 4, 16, 36, 64]
```

### Multiple conditions

Use `and` to combine multiple conditions:

```python
# Numbers divisible by 2 and 3
divisible_by_6 = [x for x in range(30) if x % 2 == 0 and x % 3 == 0]
print(divisible_by_6)  # [0, 6, 12, 18, 24]
```

### Nested comprehensions

List comprehensions can be nested:

```python
# Flatten a matrix (2D list)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

This is equivalent to:

```python
flattened = []
for row in matrix:
    for num in row:
        flattened.append(num)
```

### Complex examples

```python
# Extract lengths of words longer than 3 characters
words = ['apple', 'an', 'banana', 'it', 'orange']
lengths = [len(word) for word in words if len(word) > 3]
print(lengths)  # [5, 6, 6]

# Create tuples from two lists
names = ['Alice', 'Bob', 'Charlie']
ages = [25, 30, 35]
pairs = [(name, age) for name, age in zip(names, ages)]
print(pairs)  # [('Alice', 25), ('Bob', 30), ('Charlie', 35)]
```

## Dictionary comprehensions

Dictionary comprehensions create dictionaries from iterables.

### Basic syntax

```python
{<key_expression>: <value_expression> for <item> in <iterable>}
```

### Simple example

```python
# Square each number as both key and value
squares = {x: x**2 for x in range(5)}
print(squares)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

### From existing dictionary

Transform an existing dictionary:

```python
# Uppercase all keys
original = {'name': 'Alice', 'age': 30, 'city': 'Boston'}
upper_keys = {k.upper(): v for k, v in original.items()}
print(upper_keys)  # {'NAME': 'Alice', 'AGE': 30, 'CITY': 'Boston'}
```

### With conditions

Filter items:

```python
# Only keep even numbers as keys
evens = {x: x*2 for x in range(10) if x % 2 == 0}
print(evens)  # {0: 0, 2: 4, 4: 8, 6: 12, 8: 16}
```

### From other sequences

Create dictionaries from lists:

```python
# Map words to their lengths
words = ['apple', 'banana', 'orange']
word_lengths = {word: len(word) for word in words}
print(word_lengths)  # {'apple': 5, 'banana': 6, 'orange': 6}

# From list of tuples
pairs = [('a', 1), ('b', 2), ('c', 3)]
dict_from_pairs = {k: v for k, v in pairs}
print(dict_from_pairs)  # {'a': 1, 'b': 2, 'c': 3}
```

### Inverting a dictionary

Swap keys and values:

```python
original = {'a': 1, 'b': 2, 'c': 3}
inverted = {v: k for k, v in original.items()}
print(inverted)  # {1: 'a', 2: 'b', 3: 'c'}
```

## Set comprehensions

Set comprehensions create sets from iterables (and automatically remove duplicates).

### Basic syntax

```python
{<expression> for <item> in <iterable>}
```

### Simple example

```python
# Set of squares
squares = {x**2 for x in range(5)}
print(squares)  # {0, 1, 4, 9, 16}

# Extract unique first letters
words = ['apple', 'banana', 'apricot', 'orange']
first_letters = {word[0] for word in words}
print(first_letters)  # {'a', 'b', 'o'} (unique letters)
```

### With conditions

```python
# Unique even squares
unique_evens = {x**2 for x in range(10) if x % 2 == 0}
print(unique_evens)  # {0, 4, 16, 36, 64}
```

### Removing duplicates

Sets automatically remove duplicates:

```python
# Remove duplicates from a list
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = {x for x in numbers}
print(unique)  # {1, 2, 3, 4}

# Convert back to list if needed
unique_list = list(unique)  # [1, 2, 3, 4] (order may vary)
```

## Comparing comprehensions and loops

### When to use comprehensions

Comprehensions are great when:
- You're creating a new collection (list, dict, or set)
- The transformation is simple and readable
- You want concise, Pythonic code

```python
# Good: Simple transformation
squares = [x**2 for x in range(10)]

# Good: Simple filtering
evens = [x for x in range(10) if x % 2 == 0]
```

### When to use loops

Use loops when:
- The logic is complex or has multiple steps
- You need side effects (like printing) beyond creating a collection
- You need to break or continue based on conditions
- Readability would suffer with a comprehension

```python
# Better with a loop: Complex logic
results = []
for x in range(10):
    squared = x**2
    if squared > 20:
        print(f"Found large square: {squared}")
        results.append(squared)
    elif squared == 0:
        continue
    else:
        results.append(squared)
```

## Common patterns

### Filtering lists

```python
# Keep only positive numbers
numbers = [-2, -1, 0, 1, 2, 3]
positives = [x for x in numbers if x > 0]
print(positives)  # [1, 2, 3]

# Keep only strings longer than 3
words = ['a', 'an', 'the', 'apple', 'banana']
long_words = [word for word in words if len(word) > 3]
print(long_words)  # ['apple', 'banana']
```

### Transforming lists

```python
# Convert to strings
numbers = [1, 2, 3, 4, 5]
strings = [str(x) for x in numbers]
print(strings)  # ['1', '2', '3', '4', '5']

# Apply a function to each item
def double(x):
    return x * 2

numbers = [1, 2, 3, 4, 5]
doubled = [double(x) for x in numbers]
print(doubled)  # [2, 4, 6, 8, 10]
```

### Counting with dictionary comprehensions

```python
# Count word lengths
words = ['apple', 'banana', 'orange', 'kiwi']
length_counts = {word: len(word) for word in words}
print(length_counts)  # {'apple': 5, 'banana': 6, 'orange': 6, 'kiwi': 4}
```

### Conditional expressions (ternary in comprehensions)

Use conditional expressions for more complex transformations:

```python
# Mark numbers as 'even' or 'odd'
numbers = [1, 2, 3, 4, 5]
labels = ['even' if x % 2 == 0 else 'odd' for x in numbers]
print(labels)  # ['odd', 'even', 'odd', 'even', 'odd']

# Square even numbers, cube odd numbers
transformed = [x**2 if x % 2 == 0 else x**3 for x in range(5)]
print(transformed)  # [0, 1, 4, 27, 16]
```

## Nested comprehensions

Comprehensions can be nested for multi-dimensional data:

### List of lists

```python
# Create a matrix
matrix = [[i*j for j in range(3)] for i in range(3)]
print(matrix)  # [[0, 0, 0], [0, 1, 2], [0, 2, 4]]
```

### Flattening nested structures

```python
# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat = [num for row in matrix for num in row]
print(flat)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

### Dictionary from nested data

```python
# Create a dictionary from nested tuples
data = [('Alice', ('age', 30)), ('Bob', ('age', 25))]
people = {name: {key: value} for name, (key, value) in data}
print(people)  # {'Alice': {'age': 30}, 'Bob': {'age': 25}}
```

## Best practices

### Readability over brevity

```python
# Good: Clear and readable
squares = [x**2 for x in range(10) if x % 2 == 0]

# Avoid: Too complex
result = [x**2 if x % 2 == 0 else x**3 if x > 5 else x for x in range(10) if x != 3]
# Better: Use a loop for complex logic
```

### Use appropriate comprehensions

```python
# List comprehension for lists
squares = [x**2 for x in range(10)]

# Set comprehension for unique items
unique_squares = {x**2 for x in range(10)}

# Dictionary comprehension for key-value pairs
square_dict = {x: x**2 for x in range(10)}
```

### Don't use comprehensions for side effects

```python
# Avoid: Comprehension with side effects
[print(x) for x in range(5)]  # Works but not Pythonic

# Better: Use a loop
for x in range(5):
    print(x)
```

### Keep it simple

```python
# Good: Simple transformation
words = ['hello', 'world']
upper = [w.upper() for w in words]

# Good: Simple filtering
evens = [x for x in range(10) if x % 2 == 0]

# Better as a loop: Complex logic
results = []
for item in data:
    if item.is_valid():
        processed = item.process()
        if processed.success:
            results.append(processed.value)
```

## Performance considerations

Comprehensions are generally faster than equivalent loops because they're optimized internally:

```python
# List comprehension (faster)
squares = [x**2 for x in range(1000)]

# Equivalent loop (slower)
squares = []
for x in range(1000):
    squares.append(x**2)
```

However, readability should come first—use comprehensions when they make code clearer, not just because they're faster.

## Summary

Comprehensions provide concise ways to create collections:
- **List comprehensions**: `[x for x in iterable]`
- **Dictionary comprehensions**: `{k: v for k, v in items}`
- **Set comprehensions**: `{x for x in iterable}`
- Support filtering with `if` clauses
- Support conditional expressions for complex transformations
- Can be nested for multi-dimensional data

Use comprehensions when they improve readability and create collections concisely. They're a Pythonic way to transform and filter data, but don't sacrifice clarity for brevity. When logic becomes complex, a regular loop is often clearer.


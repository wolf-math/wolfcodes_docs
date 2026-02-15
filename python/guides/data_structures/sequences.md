---
title: Sequences
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
Sequences are a fundamental concept in Python. They represent ordered collections of items that you can access by position. This guide introduces the concept of sequences and sets the foundation for understanding lists, tuples, ranges, and other ordered data structures covered in this section.

## What are sequences?

A **sequence** is an ordered collection of items where each item has a specific position (index). Sequences are one of the most important concepts in Python because they allow you to work with collections of data in predictable, organized ways.

### Key characteristics

All sequences share these fundamental properties:

- **Ordered**: Items maintain their position. So the first item stays first, the second stays second, and so on
- **Indexed**: Each item has a numeric position (index) starting from 0
- **Iterable**: You can loop through items in order (you'll learn about loops in detail later)
- **Length**: You can count how many items are in the sequence

Think of a sequence like a numbered list where each item has a specific spot. This order and indexing make sequences powerful for organizing and accessing data.

## Types of sequences

Python includes several built-in sequence types that you'll learn about in detail:

- **Lists** ([`list`](../../language_reference/list)): Mutable, changeable collections—perfect when you need to add, remove, or modify items
- **Tuples** ([`tuple`](../../language_reference/tuple)): Immutable, unchangeable collections—ideal for fixed data that shouldn't change
- **Strings** ([`str`](../../language_reference/string)): Immutable sequences of characters—used for text data
- **Ranges** ([`range`](../../language_reference/range)): Immutable sequences of numbers—memory-efficient for numeric sequences
- **Bytes** ([`bytes`](../../language_reference/byte)): Immutable sequences of bytes—used for binary data
- **Bytearrays** ([`bytearray`](../../language_reference/bytearray)): Mutable sequences of bytes—for binary data that needs to change

Each sequence type is optimized for specific purposes, but they all share the same fundamental operations. The following guides will explore each type in depth.

## Basic sequence concepts

While each sequence type has unique features, they all support these core operations:

### Indexing

You can access individual items by their position using square brackets `[]`. Indexes start at 0:

```python
text = "Python"
numbers = [1, 2, 3, 4]

text[0]      # 'P' (first item)
numbers[1]   # 2 (second item)
```

You can also use negative indexes to count from the end:

```python
text[-1]     # 'n' (last item)
numbers[-2]  # 3 (second to last)
```

### Slicing

You can slice the sequence to extract portions using `[start:end]`:

```python
text = "Python"
text[0:3]    # 'Pyt' (items from index 0 to 3, not including 3)
text[:3]     # 'Pyt' (from start to index 3)
text[3:]     # 'hon' (from index 3 to end)
```

### Length and membership

You can check how many items are in a sequence using [`len()`](../../language_reference/built-in#len) and whether an item exists using `in`:

```python
len("hello")        # 5 (there are 5 characters)
3 in [1, 2, 3, 4]   # True (3 is one of the items in the list)
'a' in "Python"     # False ('a' does not appear anywhere in the string)
```

The `in` operator checks for the presence of a single element (like a number or a character), not a slice or pattern. It returns `True` only if that exact element is found in the sequence.

### Iteration

You can loop through sequences to process each item. You'll learn about [for loops](./for_loops) in detail later, but here's a quick preview:

```python
for char in "abc":
    print(char)
```

Output:

```text
a
b
c
```

## Mutability: A key distinction

One of the most important differences between sequence types is **mutability**, meaning whether you can change the sequence after creating it.

### Immutable sequences

Cannot be changed after creation:
- **Tuples**: `(1, 2, 3)`
- **Strings**: `"hello"`
- **Ranges**: `range(5)`
- **Bytes**: `b"hello"`

Once created, you cannot modify individual items. If you need to change them, you must create a new sequence. When you assign a "changed" string (or other immutable type) to a variable, you're actually creating a new object and overwriting what the variable points to. The original string itself remains unchanged.

### Mutable sequences

Can be changed after creation:
- **Lists**: `[1, 2, 3]`
- **Bytearrays**: `bytearray(b"hello")`

You can add, remove, or modify items in place without creating a new sequence.

The choice between mutable and immutable sequences depends on your needs. Immutable sequences are safer (they can't be accidentally changed) and can be used as dictionary keys. Mutable sequences are more flexible when you need to modify data.

## Why this matters

Sequences are everywhere in Python programming and form the foundation for working with collections of data. Understanding sequences helps you:

- **Organize data**: Store and organize related items together in a predictable order
- **Process collections**: Iterate through and transform data efficiently
- **Access data systematically**: Use indexing and slicing to work with specific elements
- **Build complex logic**: Implement algorithms that work with ordered collections

Whether you're processing a list of users, analyzing text character by character, or generating numeric ranges, sequences provide the essential structure you need. Nearly all real-world Python programs use sequences extensively, so mastering them is crucial for effective programming.

## What's next?

The following guides will explore each sequence type in detail:

- **[Lists](./lists)**: Learn about Python's most versatile collection type
- **[Tuples](./tuples)**: Discover when and why to use immutable sequences
- **[Sets](./sets)**: Explore unordered collections (not sequences, but related)
- **[Ranges](./ranges)**: Understand efficient numeric sequences
- **[For loops](./for_loops)**: Learn to iterate over sequences and other iterables
- **[While loops](./while_loops)**: Master conditional iteration
- **[Dictionaries](./dictionaries)**: Work with key-value pairs (not sequences, but essential collections)
- **[Comprehensions](./comprehensions)**: Create sequences concisely

Each guide builds on the concepts introduced here, showing you how to work effectively with different types of collections in Python.

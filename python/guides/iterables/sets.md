---
title: Sets
sidebar_position: 8
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
Sets are unordered collections of unique elements. Unlike lists and tuples, sets don't allow duplicates and don't maintain item order. They're perfect for tasks like removing duplicates, testing membership efficiently, and performing mathematical set operations.

## What are sets?

A **set** is an unordered collection of unique, hashable elements. Sets are:
- **Unordered**: Items don't have a specific position
- **Unique**: No duplicate values allowed
- **Mutable**: You can add and remove items
- **Efficient**: Fast membership testing and set operations

```python
unique_numbers = {1, 2, 3, 4, 5}
colors = {'red', 'green', 'blue'}
```

## Why this matters

Sets are powerful tools for working with unique collections and performing set operations. They excel at tasks like removing duplicates from lists, testing membership efficiently, and finding common or unique elements between collections. Sets provide mathematical set operations (union, intersection, difference) that are natural and readable. Because membership testing in sets is extremely fast (`O(1)` average case), they're ideal when you need to check if items exist in a collection frequently. Understanding sets helps you write more efficient code and solve problems that involve uniqueness or set relationships elegantly.

## Creating sets

### Empty sets

Create an empty set with `set()` (not `{}`, which creates an empty dictionary):

```python
my_set = set()
```

:::warning
`my_set = {}` creates an empty dictionary, not a set! Use `my_set = set()` for empty sets.
:::

### Sets with items

Put items inside curly braces `{}`, separated by commas:

```python
fruits = {'apple', 'banana', 'orange'}
numbers = {1, 2, 3, 4, 5}
```

### From other sequences

Convert [lists](./lists), [tuples](./tuples), or strings into sets:

```python
# From a list
numbers = set([1, 2, 3, 2, 1])  # {1, 2, 3} (duplicates removed)

# From a tuple
colors = set(('red', 'green', 'blue'))

# From a string (creates set of characters)
chars = set("hello")  # {'h', 'e', 'l', 'o'}
```

### Set comprehensions

Create sets using set comprehensions (see [comprehensions](./comprehensions)):

```python
squares = {x**2 for x in range(5)}  # {0, 1, 4, 9, 16}
evens = {x for x in range(10) if x % 2 == 0}  # {0, 2, 4, 6, 8}
```

## Unique elements

Sets automatically remove duplicates:

```python
numbers = {1, 2, 2, 3, 3, 3}
print(numbers)  # {1, 2, 3}

# Converting a list to a set removes duplicates
my_list = [1, 2, 2, 3, 3, 3]
unique = set(my_list)  # {1, 2, 3}
```

This is a common use case for sets:

```python
names = ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob']
unique_names = set(names)  # {'Alice', 'Bob', 'Charlie'}
```

## Modifying sets

### Adding items

#### `add()`

Add a single item:

```python
fruits = {'apple', 'banana'}
fruits.add('orange')
print(fruits)  # {'apple', 'banana', 'orange'}

# Adding a duplicate has no effect
fruits.add('apple')
print(fruits)  # {'apple', 'banana', 'orange'} (unchanged)
```

#### `update()`

Add multiple items from another iterable:

```python
fruits = {'apple', 'banana'}
fruits.update(['orange', 'grape'])
print(fruits)  # {'apple', 'banana', 'orange', 'grape'}

# Can add from multiple sources
fruits.update(['kiwi'], {'mango', 'papaya'})
```

### Removing items

#### `remove()`

Remove a specific item (raises `KeyError` if not found):

```python
fruits = {'apple', 'banana', 'orange'}
fruits.remove('banana')
print(fruits)  # {'apple', 'orange'}

fruits.remove('grape')  # KeyError: 'grape'
```

#### `discard()`

Remove a specific item (no error if not found):

```python
fruits = {'apple', 'banana', 'orange'}
fruits.discard('banana')
print(fruits)  # {'apple', 'orange'}

fruits.discard('grape')  # No error, just does nothing
```

#### `pop()`

Remove and return an arbitrary item (raises `KeyError` if empty):

```python
fruits = {'apple', 'banana', 'orange'}
item = fruits.pop()
print(item)    # One of the items (order is arbitrary)
print(fruits)  # Remaining items
```

:::note
Since sets are unordered, `pop()` removes an arbitrary element. The order may vary between Python versions.
:::

#### `clear()`

Remove all items:

```python
fruits = {'apple', 'banana', 'orange'}
fruits.clear()
print(fruits)  # set()
```

## Set operations

Sets support mathematical set operations that make them powerful for working with collections.

### Union (`|` or `union()`)

Combine sets, keeping all unique elements:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Using | operator
result = set1 | set2  # {1, 2, 3, 4, 5}

# Using union() method
result = set1.union(set2)  # {1, 2, 3, 4, 5}
```

### Intersection (`&` or `intersection()`)

Get elements that are in both sets:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using & operator
result = set1 & set2  # {3, 4}

# Using intersection() method
result = set1.intersection(set2)  # {3, 4}
```

### Difference (`-` or `difference()`)

Get elements in the first set but not in the second:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5}

# Using - operator
result = set1 - set2  # {1, 2}

# Using difference() method
result = set1.difference(set2)  # {1, 2}
```

### Symmetric difference (`^` or `symmetric_difference()`)

Get elements in either set, but not in both:

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Using ^ operator
result = set1 ^ set2  # {1, 2, 5, 6}

# Using symmetric_difference() method
result = set1.symmetric_difference(set2)  # {1, 2, 5, 6}
```

### In-place operations

Modify sets in place using update methods:

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set1.update(set2)        # Union: set1 becomes {1, 2, 3, 4, 5}
set1.intersection_update(set2)  # Intersection: set1 becomes {3}
set1.difference_update(set2)    # Difference: removes set2 items
set1.symmetric_difference_update(set2)  # Symmetric difference
```

## Common operations

### Length

Get the number of items with [`len()`](../../language_reference/built-in#len):

```python
fruits = {'apple', 'banana', 'orange'}
print(len(fruits))  # 3
```

### Membership testing

Check if an item exists using `in` (very fast for sets):

```python
fruits = {'apple', 'banana', 'orange'}

'apple' in fruits     # True
'grape' in fruits     # False
'grape' not in fruits # True
```

:::tip
Membership testing with `in` is very efficient for sets (O(1) average case), much faster than for lists.
:::

### Iteration

Loop through items with [`for`](./for_loops) loops:

```python
fruits = {'apple', 'banana', 'orange'}

for fruit in fruits:
    print(fruit)
```

:::note
Since sets are unordered, the iteration order may vary. Don't rely on a specific order.
:::

## Set comparisons

### Subset and superset

Check if one set is contained in another:

```python
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}

set1.issubset(set2)    # True
set1 <= set2           # True (also checks for strict subset)
set1 < set2            # True (strict subset)

set2.issuperset(set1)  # True
set2 >= set1           # True
set2 > set1            # True (strict superset)
```

### Disjoint sets

Check if two sets have no elements in common:

```python
set1 = {1, 2, 3}
set2 = {4, 5, 6}
set3 = {3, 4, 5}

set1.isdisjoint(set2)  # True (no common elements)
set1.isdisjoint(set3)  # False (both have elements)
```

## Useful set methods

### `copy()`

Create a copy of a set:

```python
original = {1, 2, 3}
copied = original.copy()
copied.add(4)

print(original)  # {1, 2, 3} (unchanged)
print(copied)    # {1, 2, 3, 4}
```

### Converting back to lists

Convert a set to a list (order will be arbitrary):

```python
fruits = {'apple', 'banana', 'orange'}
fruit_list = list(fruits)  # ['orange', 'apple', 'banana'] (order may vary)
```

## Common patterns

### Removing duplicates from a list

```python
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(numbers))  # [1, 2, 3, 4] (order may vary)
```

### Finding common elements

```python
students_math = {'Alice', 'Bob', 'Charlie', 'David'}
students_science = {'Bob', 'Charlie', 'Eve', 'Frank'}

both_classes = students_math & students_science  # {'Bob', 'Charlie'}
```

### Finding unique elements in either set

```python
set1 = {1, 2, 3}
set2 = {3, 4, 5}

unique = set1 ^ set2  # {1, 2, 4, 5} (not in both)
```

### Checking if all items from one set are in another

```python
required_skills = {'Python', 'JavaScript', 'SQL'}
candidate_skills = {'Python', 'JavaScript', 'SQL', 'Docker', 'Kubernetes'}

has_all = required_skills.issubset(candidate_skills)  # True
```

## Sets vs lists vs tuples

See the [lists guide](./lists) and [tuples guide](./tuples) for more details.

| Feature | Sets | Lists | Tuples |
|---------|------|-------|--------|
| Order | No | Yes | Yes |
| Duplicates | No | Yes | Yes |
| Mutable | Yes | Yes | No |
| Indexing | No | Yes | Yes |
| Membership test | Very fast | Slower | Slower |
| Use case | Unique items, set operations | Ordered collections | Fixed data |

## Best practices

- **Use sets for uniqueness**: When you need to ensure no duplicates
- **Use sets for fast membership**: `in` checks are much faster than with lists
- **Use sets for set operations**: Union, intersection, and difference are natural
- **Don't rely on order**: Sets are unordered; if you need order, use a list
- **Use frozensets for immutable sets**: If you need a set as a dictionary key, use [`frozenset()`](../../language_reference/frozenset)
- **Be aware of hashability**: Only hashable types (immutable types) can be set elements

```python
# Good: Hashable types
valid_set = {1, 2, 3, 'a', 'b', (1, 2)}  # Works

# Bad: Unhashable types
invalid_set = {1, 2, [3, 4]}  # TypeError: unhashable type: 'list'
```

## Summary

Sets are powerful tools for working with unique collections:
- Automatically remove duplicates
- Fast membership testing
- Support mathematical set operations
- Unordered but efficient

Use sets when you need to ensure uniqueness, test membership quickly, or perform set operations. They're an essential tool in Python for working with collections of unique items.


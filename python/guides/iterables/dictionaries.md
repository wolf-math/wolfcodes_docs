---
title: Dictionaries
sidebar_position: 7
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
Dictionaries (dicts) are key-value stores that let you organize data by meaningful labels rather than numeric positions. Unlike [lists](./lists) and [tuples](./tuples) that use indexes, dictionaries use keys to access values, making them perfect for representing structured data like user information, configuration settings, or any data where names matter more than position.

## What are dictionaries?

A **dictionary** is an unordered collection of key-value pairs enclosed in curly braces `{}`. Dictionaries are:
- **Key-value pairs**: Data stored as `key: value`
- **Unordered**: Keys don't have a fixed position (in Python 3.7+, insertion order is preserved)
- **Mutable**: You can add, remove, or modify pairs after creation
- **Unique keys**: Each key can appear only once
- **Fast lookups**: Finding values by key is very efficient

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
```

## Why this matters

Dictionaries are one of Python's most powerful and commonly used data structures. They're perfect for representing structured data where you need to access values by meaningful labels rather than numeric positions. Dictionaries excel at fast lookups, making them ideal for storing and retrieving data efficiently. You'll use dictionaries for configuration settings, user information, counting occurrences, grouping data, and mapping relationships. Their ability to associate keys with values makes code more readable and maintainable than using parallel lists or numeric indices. Understanding dictionaries is essential because they appear in nearly every Python application—from simple scripts to complex web frameworks and data processing pipelines.

## Creating dictionaries

### Empty dictionaries

Create an empty dictionary to add items later:

```python
my_dict = {}
# or
my_dict = dict()
```

### Dictionaries with items

Put key-value pairs inside curly braces, separated by commas:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}
fruits = {'apple': 5, 'banana': 3, 'orange': 8}
```

Each pair has a key (before the colon) and a value (after the colon).

### Using the `dict()` constructor

Create dictionaries using the [`dict()`](../../language_reference/dict) constructor:

```python
# From key-value pairs
person = dict(name='Alice', age=30, city='Boston')

# From a list of tuples
items = [('name', 'Alice'), ('age', 30), ('city', 'Boston')]
person = dict(items)
```

:::tip
The literal syntax `{}` is more common and Pythonic than using the `dict()` constructor.
:::

## Accessing values

### Bracket notation

Access values using square brackets and the key:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

person['name']  # 'Alice'
person['age']   # 30
person['city']  # 'Boston'
```

### Using variables as keys

Variables can be used as keys:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}
key = 'name'

person[key]  # 'Alice'
```

### Key errors

Trying to access a key that doesn't exist raises a `KeyError`:

```python
person = {'name': 'Alice', 'age': 30}
person['city']  # KeyError: 'city'
```

### `get()` method

Use `get()` to safely access values without raising errors:

```python
person = {'name': 'Alice', 'age': 30}

person.get('name')      # 'Alice'
person.get('city')      # None (key doesn't exist, returns None)
person.get('city', 'Unknown')  # 'Unknown' (default value if key missing)
```

## Modifying dictionaries

### Adding or updating items

Use bracket notation to add new items or update existing ones:

```python
person = {'name': 'Alice', 'age': 30}

# Update existing key
person['age'] = 31

# Add new key-value pair
person['city'] = 'Boston'

print(person)  # {'name': 'Alice', 'age': 31, 'city': 'Boston'}
```

### `update()`

Update multiple items at once:

```python
person = {'name': 'Alice', 'age': 30}
person.update({'age': 31, 'city': 'Boston', 'job': 'Engineer'})
print(person)  # {'name': 'Alice', 'age': 31, 'city': 'Boston', 'job': 'Engineer'}
```

You can also pass keyword arguments:

```python
person = {'name': 'Alice', 'age': 30}
person.update(age=31, city='Boston')
```

### Removing items

#### `del` statement

Remove a key-value pair using `del`:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}
del person['city']
print(person)  # {'name': 'Alice', 'age': 30}
```

#### `pop()`

Remove and returns a value:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}
city = person.pop('city')
print(city)    # 'Boston'
print(person)  # {'name': 'Alice', 'age': 30}

# With default value if key doesn't exist
city = person.pop('city', 'Unknown')  # Returns 'Unknown' if 'city' not found
```

#### `popitem()`

Remove and returns the last key-value pair (as a tuple):

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}
item = person.popitem()
print(item)    # ('city', 'Boston')
print(person)  # {'name': 'Alice', 'age': 30}
```

#### `clear()`

Remove all items:

```python
person = {'name': 'Alice', 'age': 30}
person.clear()
print(person)  # {}
```

## Nested dictionaries

Dictionaries can contain other dictionaries:

```python
students = {
    'Alice': {'age': 20, 'grade': 'A'},
    'Bob': {'age': 21, 'grade': 'B'},
    'Charlie': {'age': 19, 'grade': 'A'}
}

# Access nested values
print(students['Alice']['age'])     # 20
print(students['Bob']['grade'])     # 'B'

# Modify nested values
students['Alice']['age'] = 21

# Add nested dictionary
students['Diana'] = {'age': 20, 'grade': 'A'}
```

## Dictionary keys and values

### Valid keys

Keys must be **hashable** (immutable) types:
- Strings, numbers, tuples (with hashable elements), booleans, `None`
- Lists, dictionaries, and sets cannot be keys

```python
# Valid keys
valid = {
    'string': 1,
    42: 'number',
    (1, 2): 'tuple',
    True: 'boolean',
    None: 'none'
}

# Invalid keys
# invalid = {[1, 2]: 'list'}  # TypeError: unhashable type: 'list'
# invalid = {{'a': 1}: 'dict'}  # TypeError: unhashable type: 'dict'
```

### Any values

Values can be any type, including mutable types:

```python
mixed = {
    'string': 'text',
    'number': 42,
    'list': [1, 2, 3],
    'dict': {'nested': 'value'},
    'tuple': (1, 2, 3)
}
```

## Getting keys and values

### `keys()`

Get all keys as a view object:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

keys = person.keys()
print(keys)  # dict_keys(['name', 'age', 'city'])

# Convert to a list if needed
key_list = list(person.keys())
print(key_list)  # ['name', 'age', 'city']
```

### `values()`

Get all values as a view object:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

values = person.values()
print(values)  # dict_values(['Alice', 30, 'Boston'])

# Convert to a list if needed
value_list = list(person.values())
print(value_list)  # ['Alice', 30, 'Boston']
```

### `items()`

Get all key-value pairs as tuples:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

items = person.items()
print(items)  # dict_items([('name', 'Alice'), ('age', 30), ('city', 'Boston')])

# Convert to a list if needed
item_list = list(person.items())
print(item_list)  # [('name', 'Alice'), ('age', 30), ('city', 'Boston')]
```

:::note
The `keys()`, `values()`, and `items()` methods return view objects that reflect changes to the dictionary. They're memory-efficient and update automatically.
:::

## Iterating over dictionaries

### Iterating over keys (default)

By default, iterating over a dictionary gives you the keys:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

for key in person:
    print(key)

# Output:
# name
# age
# city
```

This is equivalent to `for key in person.keys():`.

### Iterating over keys explicitly

Use `.keys()` to make your intention clear:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

for key in person.keys():
    print(key)
```

### Iterating over values

Use `.values()` to iterate over values only:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

for value in person.values():
    print(value)

# Output:
# Alice
# 30
# Boston
```

### Iterating over key-value pairs

Use `.items()` to get both keys and values:

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}

for key, value in person.items():
    print(f"{key}: {value}")

# Output:
# name: Alice
# age: 30
# city: Boston
```

This uses tuple unpacking. Each item from `.items()` is a `(key, value)` tuple.

### Practical iteration examples

```python
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}

# Find the highest score
max_score = 0
best_student = None
for name, score in scores.items():
    if score > max_score:
        max_score = score
        best_student = name

print(f"{best_student} has the highest score: {max_score}")

# Calculate average score
total = 0
for score in scores.values():
    total += score
average = total / len(scores)
print(f"Average score: {average}")

# Output:
# Alice has the highest score: 95
# Average score: 91.33333333333333
```

## Common operations

### Length

Get the number of key-value pairs with [`len()`](../../language_reference/built-in#len):

```python
person = {'name': 'Alice', 'age': 30, 'city': 'Boston'}
print(len(person))  # 3
```

### Membership testing

Check if a key exists using `in`:

```python
person = {'name': 'Alice', 'age': 30}

'name' in person      # True
'city' in person      # False
'Alice' in person     # False (checks keys, not values!)
```

To check if a value exists:

```python
person = {'name': 'Alice', 'age': 30}

'Alice' in person.values()  # True
```

### Checking for key before access

```python
person = {'name': 'Alice', 'age': 30}

# Safe access pattern
if 'city' in person:
    city = person['city']
else:
    city = 'Unknown'

# Or use get() for cleaner code
city = person.get('city', 'Unknown')
```

## Useful dictionary methods

### `copy()`

Create a copy of a dictionary:

```python
original = {'name': 'Alice', 'age': 30}
copied = original.copy()
copied['age'] = 31

print(original)  # {'name': 'Alice', 'age': 30} (unchanged)
print(copied)    # {'name': 'Alice', 'age': 31}
```

:::warning
Assigning a dictionary to another variable doesn't create a copy. Below both `original` and `reference` variables refer to the same dictionary:

```python
original = {'name': 'Alice', 'age': 30}
reference = original  # Not a copy!
reference['age'] = 31
print(original)  # {'name': 'Alice', 'age': 31} (also changed!)
```

Use `.copy()` or `dict()` constructor to create a copy.
:::

### `setdefault()`

Get a value, or set a default if the key doesn't exist:

```python
person = {'name': 'Alice', 'age': 30}

# Key exists: returns existing value
age = person.setdefault('age', 25)
print(age)      # 30
print(person)   # {'name': 'Alice', 'age': 30} (unchanged)

# Key doesn't exist: sets and returns default
city = person.setdefault('city', 'Unknown')
print(city)     # 'Unknown'
print(person)   # {'name': 'Alice', 'age': 30, 'city': 'Unknown'}
```

### `fromkeys()`

Create a dictionary from keys with a default value:

```python
# All values are None
keys = ['name', 'age', 'city']
person = dict.fromkeys(keys)
# {'name': None, 'age': None, 'city': None}

# All values are the same
person = dict.fromkeys(keys, 0)
# {'name': 0, 'age': 0, 'city': 0}
```

## Common patterns

### Building a dictionary incrementally

Start with an empty dictionary and add key-value pairs one at a time:

```python
data = {}
data['name'] = 'Alice'
data['age'] = 30
data['city'] = 'Boston'
```

### Counting occurrences

Use a dictionary to count how many times each item appears in a sequence:

```python
words = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']
counts = {}

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)  # {'apple': 3, 'banana': 2, 'orange': 1}
```

### Grouping items

Organize items into groups based on a shared characteristic:

```python
students = [
    ('Alice', 'Math'),
    ('Bob', 'Science'),
    ('Charlie', 'Math'),
    ('Diana', 'Science')
]

by_subject = {}
for name, subject in students:
    if subject not in by_subject:
        by_subject[subject] = []
    by_subject[subject].append(name)

print(by_subject)
# {'Math': ['Alice', 'Charlie'], 'Science': ['Bob', 'Diana']}
```

### Merging dictionaries

Combine multiple dictionaries into one using several different methods:

```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Using update()
merged = dict1.copy()
merged.update(dict2)

# Using unpacking (Python 3.5+)
merged = {**dict1, **dict2}

# Using | operator (Python 3.9+)
merged = dict1 | dict2
```

### Dictionary as a lookup table

Use dictionaries to map one value to another, like translating codes to descriptions:

```python
grades = {
    'A': 'Excellent',
    'B': 'Good',
    'C': 'Average',
    'D': 'Below Average',
    'F': 'Fail'
}

grade = 'B'
print(grades.get(grade, 'Unknown'))  # 'Good'
```

### Dictionary comprehensions

Create dictionaries using comprehensions (see [comprehensions](./comprehensions)):

```python
# Square each number
squares = {x: x**2 for x in range(5)}  # See [ranges](./ranges) for more on range()
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Filter and transform
evens = {x: x*2 for x in range(5) if x % 2 == 0}
# {0: 0, 2: 4, 4: 8}
```

## Best practices

- **Use descriptive keys**: `person['name']` is clearer than `person['n']`
- **Use `get()` for safe access**: Avoids `KeyError` when keys might not exist
- **Use `.items()` when you need both keys and values**: More efficient than separate lookups
- **Prefer dictionary comprehensions**: For creating dictionaries from sequences
- **Be careful with copying**: Use `.copy()` when you need an independent copy
- **Use `in` for key membership**: Fast and readable

```python
# Good: Descriptive keys and safe access
person = {'name': 'Alice', 'age': 30}
name = person.get('name', 'Unknown')

# Good: Using items() for iteration
for key, value in person.items():
    print(f"{key}: {value}")

# Avoid: Accessing without checking
# name = person['name']  # KeyError if 'name' doesn't exist

# Better: Use get() with default
name = person.get('name', 'Unknown')
```

## Summary

Dictionaries are powerful key-value stores:
- Access values by meaningful keys instead of numeric positions
- Fast lookups and efficient membership testing
- Support iteration over keys, values, or items
- Mutable and flexible data structures
- Perfect for representing structured, labeled data

Dictionaries are essential for organizing data by meaningful labels. They're particularly useful when you need to look up values by name rather than position, and they work seamlessly with loops to process key-value data efficiently.


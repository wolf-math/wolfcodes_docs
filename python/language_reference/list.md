---
title: List
sidebar_position: 11
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## Properties

```python
>>> dir(list)
['__add__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

## Definition

A `list` is a collection of items defined with square brackets `[]`. These items are stored location within the list starting at index `0`. Items within a list can be modified, added, or removed, and can contain multiple types, including other lists. Unlike many other programming languages, a list can contain many different types: `['apple', 2, True, 'string cheese']`.

## Using lists

### Instantiation

A list can be instantiated using the _literal_ syntax or with the `list` constructor:

```python
# literal syntax
>>> my_list = ['apple', 2, True, 'string cheese']

# constuctor
>>> my_list = list(['apple', 2, True, 'string cheese'])
```

The most common way is to create it using the literal syntax.

### Accessing elements

List elements are accessed by their index. Indeces start at `0`. A negative index accesses the list from the end of the list.

```python
>>> my_list = ['apple', 2, True, 'string cheese']

>>> my_list[0]
'apple'

>>> my_list[1]
2

>>> my_list[3]
'string cheese'

>>> my_list[-1]
'string cheese'

>>> my_list[-2]
True
```

### Slicing

Lists can be sliced using `[start:end]`, returning items from `start` up to but not including `end`.
Omitting `start` begins the slice at the first element, and omitting `end` extends it to the last element.

```python
>>> my_list[0:3]
['apple', 2, True]

>>> my_list[0:4]
['apple', 2, True, 'string cheese']

>>> my_list[1:-1] # same as [1:3]
[2, True]

>>> my_list[1:3]
[2, True]

>>> my_list[1:]
[2, True, 'string cheese']

>>> my_list[:2]
['apple', 2]
```

### Membership testing

The existence of a value within a list can be checked with the `in` keyword. Returns `True` if the element is in the list and `False` if the element is _not_ in the list.

```python
>>> my_list = ['apple', 2, True, 'string cheese']

>>> 'apple' in my_list
True

>>> 2 in my_list
True

>>> 'chicken' in my_list
False
```

### Unpacking

Lists can be unpacked into multiple variables. The number of variables must match the number of items in the list.

```python
>>> my_list = [10, 20, 30]

>>> a, b, c = my_list

>>> a
10

>>> b
20

>>> c
30
```

If the number of variables doesn't match, a `ValueError` is raised:

```python
>>> my_list = [10, 20, 30]

>>> a, b = my_list
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: too many values to unpack (expected 2)
```

## Dunder methods

| Dunder Method  | Operation         | Example (normal syntax)       | Example (dunder call)               |
| -------------- | ----------------- | ----------------------------- | ----------------------------------- |
| `__getitem__`  | Indexing          | `[1,2,3][0]` → `1`            | `[1,2,3].__getitem__(0)`            |
| `__setitem__`  | Item assignment   | `nums[1] = 9`                 | `nums.__setitem__(1, 9)`            |
| `__delitem__`  | Delete item       | `del nums[1]`                 | `nums.__delitem__(1)`               |
| `__len__`      | Length            | `len(nums)`                   | `nums.__len__()`                    |
| `__contains__` | Membership        | `2 in [1,2,3]` → `True`       | `[1,2,3].__contains__(2)`           |
| `__add__`      | Concatenate       | `[1,2] + [3,4]` → `[1,2,3,4]` | `[1,2].__add__([3,4])`              |
| `__mul__`      | Repeat            | `[1,2]*2` → `[1,2,1,2]`       | `[1,2].__mul__(2)`                  |
| `__iter__`     | Iteration         | `for x in [1,2,3]`            | `it = [1,2,3].__iter__(); next(it)` |
| `__reversed__` | Reverse iteration | `reversed([1,2,3])`           | `[1,2,3].__reversed__()`            |
| `__eq__`       | Equality          | `[1,2]==[1,2]` → `True`       | `[1,2].__eq__([1,2])`               |


---

## `list` Methods

### `append`

Modifies the original list by adding the specified element to the end. 

```python
>>> my_list = [1, 2, 3]

>>> my_list.append(4)

>>> print(my_list)
[1, 2, 3, 4]
```

---

### `clear`

Modifies the original list by empyting it of all elements.

```python
>>> my_list = [1,2,3,4]

>>> print(my_list)
[1,2,3,4]

>>> my_list.clear()

>>> print(my_list)
[]
```

---

### `copy`

Returns a copy (or clone) of a list.


```python
>>> my_list
['string cheese', 'cheddar', 2, 'apple']

>>> my_other = my_list.copy()

>>> my_other
['string cheese', 'cheddar', 2, 'apple']

>>> my_other[1]= 'brie'

>>> my_other
['string cheese', 'brie', 2, 'apple']

>>> my_list
['string cheese', 'cheddar', 2, 'apple']
```

:::note
altering making a copy of a list like this:

```python
my_other = my_list
```

will only create another variable that referrs to the same list. In such a scenario altering `my_list` would also alter `my_other`.
:::

---

### `count`

Returns the number of occurances of an element within a list.

```python
>>> things = [1, 2, 3, 2, 5, 3, 4]

>>> things.count(4)
1

>>> things.count(2)
2

>>> things.count(3)
2

>>> things.count(10)
0
```

---

### `extend`

Adds elements from an iterable to a list.

Iterables that can be used with `extend` include:
* list
* tuple
* range
* str (each character)
* bytes (each byte as an int)
* bytearray
* set
* frozenset
* dict (keys will be appended)
* compressions/generator

```python
>>> my_list = []

>>> my_list.extend([1, 2])                  # list
>>> my_list.extend((3, 4))                  # tuple
>>> my_list.extend(range(2))                # range
>>> my_list.extend("hi")                    # string -> 'h', 'i'
>>> my_list.extend({7, 8})                  # set (unordered)
>>> my_list.extend({'x': 1, 'y': 2})        # dict -> 'x', 'y'
>>> my_list.extend((x*x for x in range(3))) # generator
>>> my_list.extend(open("file.txt"))        # file lines

```


---

### `index`

Returns the index of the first occurance of an element in an array. 

```python
>>> my_list = ['a', 'b', 'c', 'b']

>>> my_list.index('a')
0

>>> my_list.index('b')
1
```

---

### `insert`

Adds an element to an array to a specific location. The first argument is the index at which the new element will be, and the second argument is the element itself. The existing elements are shifted one position to the right.

```python
>>> my_list = ['a', 'b', 'c', 'b']

>>> my_list.insert(2, 'd')

>>> print(my_list)
['a', 'b', 'd', 'c', 'b']
```

---

### `pop`

Removes and returns the last element of a list. 

```python
>>> my_list = ['a', 'b', 'c']

>>> item = my_list.pop()

>>> print(item)
'c'

>>> print(my_list)
['a', 'b']

>>> my_list.pop(0)

>>> print(my_list)
['b']
```


---

### `remove`

Removes an element from an array by its _value_.

```python
>>> my_list = [1,2,3,4]

>>> my_list.remove(2)

>>> print(my_list)
[1, 3, 4]
```

---

### `reverse`

Returns the list in reverse order.

```python
>>> my_list = [1, 2, 3, 4]

>>> my_list.reverse()

>>> print(my_list)
[4, 3, 2, 1]
```

---

### `sort`

Sorts the list either in ascending numerical order or alphabetical order. A list with multiple types cannot be sorted.


numbers:
```python
>>> my_nums = [-99, 10, math.pi]

>>> my_nums.sort()

>>> print(my_nums)
[-99, 3.141592653589793, 10]
```


strings:
```python
>>> my_strings = ['one', 'two', 'three', 'four']

>>> my_strings.sort()

>>> print(my_strings)
['four', 'one', 'three', 'two']
```

strings and numbers:
```python
>>> my_list = [-99, 10, 'wolf', 'python', math.pi]
>>> my_list.sort()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: '<' not supported between instances of 'str' and 'int'
```
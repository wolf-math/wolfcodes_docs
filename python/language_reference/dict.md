---
title: Dict
sidebar_position: 6
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
>>> dir(dict)
['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']
```

## Definition

A dictionary is a collection of _key : value_ pairs grouped by curly braces `{}`. Unlike a [list](./list), dictionaries are **unordered** and values are accessed by their **key**. Pairs within a dictionary can be modified, added, or removed, and can contain multiple types, including other dictionaries and lists. 

## Using dictionaries

### Instantiation

Dictionaries can be instantiated using the  _literal_ syntax, with the `dictionary` constructor, or with keyword arguments:

```python
# literal syntax
my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

# constructor
my_dict = dict([('fruit', 'apple'), ('count', 2), ('is_good', True), ('snack', 'string cheese')])

# keyword arguments
my_dict = dict(fruit='apple', count=2, is_good=True, snack='string cheese')
```

The most common and straighforward way to do this is with the _literal syntax_.

### Accessing elements

Elemets are accessed by a value's key using _bracket notation_.  


```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict['count']
2
```

Variables can also be passed into the bracket notation to obtain a value.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_var = 'snack'

>>> my_dict[my_var]
'string cheese'
```

:::note
Dot notation is not supported in Python
:::

### Modifying elements

Modify elements using bracket notation.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict['fruit': 'banana']

>>> print(my_dict)
{ 'fruit': 'banana', 'count': 2, 'is_good': True, 'snack': 'string cheese' }
```

### Adding elements

Add a new element by using bracket notation

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict['person'] = 'Wolf'

>>> print(my_dict)
{ 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese', 'person': 'Wolf' }
```

### Removing elements

Remove an element with the `del` command.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> del my_dict['count']

>>> print(my_dict)
{ 'fruit': 'apple', 'is_good': True, 'snack': 'string cheese' }
```

### Membership testing

The membership of a _key_ within a dictionary can be tested with the `in` keyword. Returns `True` if the element is in the dictionary and `False` if the element is _not_ in the dictionary.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> 'is_good' in my_dict
True

>>> 'string cheese' in my_dict
False
```

## Dunder methods

| Dunder Method  | Operation     | Example (normal syntax) | Example (dunder call)         |
| -------------- | ------------- | ----------------------- | ----------------------------- |
| `__getitem__`  | Access value  | `d["a"]` → `1`          | `d.__getitem__("a")`          |
| `__setitem__`  | Set key/value | `d["b"] = 2`            | `d.__setitem__("b", 2)`       |
| `__delitem__`  | Delete key    | `del d["a"]`            | `d.__delitem__("a")`          |
| `__contains__` | Membership    | `"a" in d`              | `d.__contains__("a")`         |
| `__len__`      | Length        | `len(d)`                | `d.__len__()`                 |
| `__iter__`     | Iterate keys  | `for k in d`            | `it = d.__iter__(); next(it)` |
| `__eq__`       | Equality      | `{"a":1} == {"a":1}`    | `{"a":1}.__eq__({"a":1})`     |


---

## Dictionary methods

### `clear`

Removes all elements from a dictionary.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict.clear()

>>> print(my_dict)
{}
```

---

### `copy`

Returns a copy (or clone) of a dictionary

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_other_dict  = my_dict.copy()

>>> my_other_dict['editor'] = 'vs code'

>>> del my_dict['snack']

>>> print(my_dict)
{'fruit': 'apple', 'count': 2, 'is_good': True}

>>> print(my_other_dict)
{'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese', 'editor': 'vs code'}
```

:::note
altering making a copy of a dictionary like this:

```python
my_other = my_dict
```

will only create another variable that referrs to the same dictionary. In such a scenario altering `my_dict` would also alter `my_other`.
:::
---

### `fromkeys`

Returns a new dictionary from keys from the given list or tuple, and values from the second parameter. The default value for the second parameter is `None`.

```python
>>> student_list = ['Aaron', 'Max', 'Ryan', 'Betty']

>>> grades = 75

>>> student_grades = dict.fromkeys(student_scores, grades)

>>> print(student_grades)
{'Aaron': 75, 'Max': 75, 'Ryan': 75, 'Betty': 75}
```
---

### `get`

Returns the value of the specified key.

Is there a difference in python between 

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> fav_fruit = my_dict.get('fruit')

>>> print(fav_fruit)
'apple'
```

Unlike accessing with bracket notation, `get` does not raise a key error if the key is not found.

```python
>>> my_dict['color']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'color'

>>> my_dict.get('color')

```

Can also be used with default value if the value is not found.

```python
>>> my_dict.get('color', 'purple')
'purple'
```
---

### `items`

Returns a view object of a list of tuples as the key-value pairs.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict.items()
dict_items([('fruit', 'apple'), ('count', 2), ('is_good', True), ('snack', 'string cheese')])
```
---

### `keys`

Returns a view object of a list of the keys of a dictionary.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict.keys
<built-in method keys of dict object at 0x1043b8100>

>>> my_dict.keys()
dict_keys(['fruit', 'count', 'is_good', 'snack'])
```
---

### `pop`

Returns and removes the given key-value pair.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> snizzack= my_dict.pop('snack')

>>> print(my_dict)
{'fruit': 'apple', 'count': 2, 'is_good': True}

>>> print(snizzack)
string cheese
```
---

### `popitem`

Removes the last key-value pair in a dictionary and returns it as a tuple.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> snizzack = my_dict.popitem()

>>> print(my_dict)
{'fruit': 'apple', 'count': 2, 'is_good': True}

>>> print(snizzack)
('snack', 'string cheese')
```
---

### `setdefault`

If the key exists in the dictionary, returns the value of the given key (just like get) and does not change the dictionary.

If the key does not exist in the dictionary, returns the default value and inserts the key with the provided default value.

#### Key exists:

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> result = my_dict.setdefault('fruit', 'orange')
>>> print(result)
'apple'

>>> print(my_dict)
{'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese'}
```

#### Key does not exist:

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> result = my_dict.setdefault('color', 'red')
>>> print(result)
'red'

>>> print(my_dict)
{'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese', 'color': 'red'}
```

---

### `update`

If a key exists in the dictionary, overwrites the value at that key.

If a key does not exist in the dictionary, creates a new key value pair.

#### Key exists

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict.update({'fruit': 'banana'})
>>> print(my_dict)
{'fruit': 'banana', 'count': 2, 'is_good': True, 'snack': 'string cheese'}
```

#### Key does not exist

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict.update({'color': 'red'})
>>> print(my_dict)
{'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese', 'color': 'red'}
```

#### Updating multiple values

```python
>>> my_dict.update({'fruit': 'grape', 'count': 5})
>>> print(my_dict)
{'fruit': 'grape', 'count': 5, 'is_good': True, 'snack': 'string cheese'}
```

---

### `values`


Returns a view object of a list of the values of a dictionary.

```python
>>> my_dict = { 'fruit': 'apple', 'count': 2, 'is_good': True, 'snack': 'string cheese' }

>>> my_dict.values
<built-in method values of dict object at 0x1043b8100>

>>> my_dict.values()
dict_values(['apple', 2, True, 'string cheese'])
```

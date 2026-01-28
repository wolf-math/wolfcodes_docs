---
title: Memoryview
sidebar_position: 12
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
>>> dir(memoryview)
['__class__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__enter__', '__eq__', '__exit__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'c_contiguous', 'cast', 'contiguous', 'f_contiguous', 'format', 'hex', 'itemsize', 'nbytes', 'ndim', 'obj', 'readonly', 'release', 'shape', 'strides', 'suboffsets', 'tobytes', 'tolist', 'toreadonly']
```

## Definition

A `memoryview` provides a zero-copy, sliceable view over binary data that supports the buffer protocol (e.g., `bytes`, `bytearray`, `array`, `mmap`). It allows reading and writing (if underlying object is writable) without copying the data.

```python
>>> data = bytearray(b"hello")
>>> view = memoryview(data)
>>> view[0]
104
>>> view[0] = 72   # modify in place
>>> data
bytearray(b'Hello')
```

## Creating memoryviews

```python
>>> mv = memoryview(b"abc")              # from bytes (read-only)
>>> mv2 = memoryview(bytearray(b"abc"))  # from bytearray (read/write)
```

## Slicing and casting

Memoryviews can be sliced without copying and cast to change the element format.

```python
>>> mv = memoryview(bytearray(b"abcdef"))
>>> mv[2:4].tobytes()
b'cd'

# cast to view 16-bit unsigned integers (requires aligned size)
>>> mem = memoryview(bytearray(b"\x01\x00\x02\x00"))
>>> mem.cast("H").tolist()
[1, 2]
```

## Attributes

- `format` — element format (PEP 3118 code)
- `itemsize` — size of each element in bytes
- `nbytes` — total bytes
- `ndim`, `shape`, `strides` — multi-dimensional info (for exporters that support it)
- `readonly` — `True` if underlying buffer is read-only
- `obj` — underlying object

## Common methods

- `tobytes()` — return a bytes copy
- `tolist()` — return a list of elements
- `cast(format, shape=None)` — reinterpret view
- `toreadonly()` — get a read-only view
- `release()` — manually release the view (rarely needed; context manager supported)

## Dunder methods

| Dunder Method           | Operation               | Example (normal syntax)         | Example (dunder call)            |
| ----------------------- | ----------------------- | ------------------------------- | -------------------------------- |
| `__getitem__`           | Index                   | `view[0]` → `104`               | `view.__getitem__(0)`            |
| `__setitem__`           | Modify data             | `view[0] = 72`                  | `view.__setitem__(0, 72)`        |
| `__len__`               | Length                  | `len(view)` → `5`               | `view.__len__()`                 |
| `__iter__`              | Iterate                 | `for b in view`                 | `view.__iter__()`                |
| `__eq__`                | Compare                 | `view == memoryview(b'hello')`  | `view.__eq__(other)`             |
| `__enter__`, `__exit__` | Context manager support | `with memoryview(b'abc') as m:` | `m.__enter__()` / `m.__exit__()` |

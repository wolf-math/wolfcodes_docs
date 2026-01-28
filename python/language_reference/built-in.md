---
title: Built-in Functions
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
## Definition

Built-in functions are Python functions that exist in the global namespace. They are available everywhere in your code without needing to import. Some of these functions are not tied to a specific type, such as the `len()` function that can get the length of a list or a string.

```python
>>> import builtins
>>> dir(builtins)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EncodingWarning', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'aiter', 'all', 'anext', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```

You will notice 3 main groups with the output of `dir(builtins)`. The first section is all different error and warning classes. The second is the dunder methods. The last section that this page will discuss is the actual built-in functions of Python.

### `abs`

Returns the absolute value of an [`int`](./int), [`float`](./float), or [`complex`](./complex) number

```python
>>> abs(42)
42

>>> abs(-42)
42

>>> abs(912.234)
912.234

>>> abs(-912.234)
912.234

>>> abs((3+7j))
7.615773105863909

>>> abs((-3+7j))
7.615773105863909
```

The number that's returned for complex numbers is the result of calculating $\sqrt{a^2 + b^2}$. In the above example it is the result of $\sqrt{3^2 + 7^2}$.

---

### `aiter`

Returns an **asynchronous iterator** for an async iterable.
Used inside `async` functions, often with `async for`.

```python
async def main():
    async for x in aiter([1, 2, 3]):
        print(x)
```

Most built-in collections are not async-iterable, so this is primarily used with objects that implement `__aiter__`.

---

### `all`

Returns `True` if **every element** in an iterable is truthy.
Returns `True` for an empty iterable.

```python
>>> all([True, 1, 'x'])
True
>>> all([True, 0, 'x'])
False
>>> all([])
True
```

---

### `anext`

Retrieves the **next item** from an async iterator.
Async version of `next()`.

```python
async def main():
    it = aiter([1, 2, 3])
    first = await anext(it)
    print(first)
```

You can also provide a default:

```python
await anext(it, default_value)
```

---

### `any`

Returns `True` if **at least one** element in an iterable is truthy.

```python
>>> any([0, 0, 5])
True
>>> any([0, False, None])
False
```

Useful for condition checks over lists or generator expressions.

---

### `ascii`

Returns a string containing only ASCII characters.
Non-ASCII characters are escaped using `\x`, `\u`, or `\U`.

```python
>>> ascii("café")
"'caf\\xe9'"
>>> ascii(["α", "β", "γ"])
"['\\u03b1', '\\u03b2', '\\u03b3']"
```

Helpful for debugging or logging where only ASCII output is expected.

---

### `bin`

Converts an integer into its **binary string representation**.

```python
>>> bin(10)
'0b1010'
>>> bin(-3)
'-0b11'
```

The returned value is always a string beginning with `'0b'`.

---

### `bool`

Converts a value to its boolean form (`True` or `False`).
Follows Python’s truthiness rules:

Falsy values include:

* `0`
* `0.0`
* `''` (empty string)
* `[]`, `{}`, `set()`, `tuple()`
* `None`
* objects that define `__bool__` or `__len__` returning `False`/`0`

Examples:

```python
>>> bool(1)
True
>>> bool(0)
False
>>> bool("hello")
True
>>> bool("")
False
```

---

### `breakpoint`

Enters the Python debugger at the current line.

```python
def add(a, b):
    breakpoint()   # pauses here
    return a + b
```

By default this launches `pdb`, but it can be customized via the `PYTHONBREAKPOINT` environment variable (e.g. to use `ipdb`).

---

### `bytearray`

Mutable sequence of bytes (0–255).
Often used for binary data manipulation, network buffers, or file processing.

```python
>>> data = bytearray([65, 66, 67])
>>> data[0] = 97
>>> data
bytearray(b'abc')
```

You can create one from:

* a sequence of integers
* a string + encoding
* an existing bytes object

```python
>>> bytearray("hello", "utf-8")
bytearray(b'hello')
```

---

### `bytes`

Immutable version of `bytearray`.
Represents raw binary data.

```python
>>> b = bytes([65, 66, 67])
>>> b
b'ABC'
```

Common uses:

* reading files in binary mode
* working with network packets
* hashing and cryptographic functions

You must reassign to modify:

```python
>>> b = b'hello'
>>> b = b.replace(b'h', b'H')
>>> b
b'Hello'
```


---

### `callable`

Returns `True` if the object can be called like a function.
This includes functions, classes, methods, and any object implementing `__call__`.

```python
>>> callable(len)
True

>>> class A: pass
>>> callable(A)
True     # classes are callable because you can instantiate them

>>> x = 10
>>> callable(x)
False
```

Useful for checking user-provided objects before attempting to call them.

---

### `chr`

Returns the character associated with a Unicode code point.

```python
>>> chr(97)
'a'
>>> chr(8364)
'€'
```

Inverse of `ord()`.

---

### `classmethod`

Defines a method that receives the **class** as its first argument instead of the instance.
The typical use case is alternative constructors or utilities that operate on the class.

```python
class Person:
    population = 0

    def __init__(self, name):
        self.name = name

    @classmethod
    def create_anonymous(cls):
        return cls("Anonymous")
```

Calling:

```python
>>> Person.create_anonymous()
<Person object at ...>
```

---

### `compile`

Compiles Python source code into a **code object**, which can then be executed with `exec()` or evaluated with `eval()`.

```python
source = "x = 3 + 4"
code = compile(source, filename="<string>", mode="exec")
exec(code)
>>> x
7
```

Modes:

* `"exec"` — multiple statements
* `"eval"` — a single expression
* `"single"` — a single interactive statement

This is rarely needed in everyday programming but useful for dynamic execution engines or tooling.

---

### `complex`

Creates a complex number from real and imaginary parts.

```python
>>> complex(2, 3)
(2+3j)

>>> complex("4-5j")
(4-5j)
```

Equivalent literal syntax:

```python
>>> 2 + 3j
(2+3j)
```

---

### `copyright`

Prints Python copyright information to the console.
Primarily included for interactive sessions.

```python
>>> copyright
Copyright (c) 2001-2024 Python Software Foundation.
All Rights Reserved.
```

Not generally used in application code.

---

### `credits`

Prints contributor acknowledgments for Python.

```python
>>> credits
Thanks to CWI, CNRI, BeOpen.com, Zope Corporation and a cast of thousands
for supporting Python development.
```

Similar to `copyright` — included for completeness.

---

### `delattr`

Deletes an attribute from an object by name.
Raises `AttributeError` if it doesn't exist.

```python
class Foo:
    x = 10

>>> delattr(Foo, "x")
>>> Foo.x
AttributeError
```

Equivalent to:

```python
del Foo.x
```

Useful for dynamic class manipulation or meta-programming.

---

### `dict`

Creates a new dictionary.

```python
>>> dict(a=1, b=2)
{'a': 1, 'b': 2}

>>> dict([("x", 10), ("y", 20)])
{'x': 10, 'y': 20}
```

Three common forms:

1. Literal syntax:

   ```python
   {"a": 1, "b": 2}
   ```
2. Constructor with key/value pairs
3. Constructor with keyword arguments

The literal syntax is the most common.

---

### `dir`

Attempts to return a **list of attributes** available on an object.
If no object is given, it returns the names in the current scope.

```python
>>> dir("hello")
['__add__', '__class__', '__contains__', ...]
```

Useful for:

* introspection
* debugging
* exploring unknown objects in the REPL

Calling without arguments:

```python
>>> x = 10
>>> dir()
['__annotations__', '__builtins__', ..., 'x']
```

---


### `divmod`

Returns a tuple containing the **quotient** and **remainder** of integer division.

```python
>>> divmod(17, 5)
(3, 2)
```

Equivalent to:

```python
(17 // 5, 17 % 5)
```

Works with integers and floats (though float remainders may be imprecise).

---

### `enumerate`

Wraps an iterable and returns pairs of `(index, value)` as you loop over it.

```python
>>> for i, item in enumerate(["a", "b", "c"]):
...     print(i, item)
0 a
1 b
2 c
```

You can provide a custom starting index:

```python
>>> list(enumerate(["x", "y"], start=1))
[(1, 'x'), (2, 'y')]
```

Useful when you need both the index and the value from an iterable.

---

### `eval`

Evaluates a **Python expression** contained in a string and returns its result.

```python
>>> eval("3 + 4")
7
```

Because it executes arbitrary code, it is **unsafe** for any untrusted input.
Primarily used in controlled tools, REPL-like utilities, or code generation.

---

### `exec`

Executes a string of Python code.

```python
source = """
x = 10
y = x * 2
"""
exec(source)
>>> y
20
```

Unlike `eval`, `exec` can run entire blocks of statements.
Also unsafe for untrusted input — use only in safe or controlled environments.

---

### `exit`

Exits the Python interpreter.
Intended for interactive use, not programmatic use.

```python
>>> exit()
```

In scripts, prefer raising `SystemExit` or using `sys.exit()`.

---

### `filter`

Filters items from an iterable using a function that returns `True` or `False`.

```python
>>> nums = [1, 2, 3, 4, 5]
>>> list(filter(lambda x: x % 2 == 0, nums))
[2, 4]
```

If the function is `None`, it removes falsy values:

```python
>>> list(filter(None, [0, 1, "", "hi", [], [1]]))
[1, 'hi', [1]]
```

---

### `float`

Converts a value to a floating-point number.

```python
>>> float(3)
3.0
>>> float("3.14")
3.14
```

If the conversion fails, raises `ValueError`:

```python
>>> float("wolf")
ValueError
```

Also returns special values:

```python
>>> float("inf"), float("-inf"), float("nan")
(inf, -inf, nan)
```

---

### `format`

Converts a value to a formatted string using a **format specification**.

```python
>>> format(3.14159, ".2f")
'3.14'
```

Equivalent to calling the object’s `__format__` method or using f-strings:

```python
>>> f"{3.14159:.2f}"
'3.14'
```

Useful for custom number formatting, padding, alignment, etc.

---

### `frozenset`

An immutable version of `set`.
Supports membership tests and set operations, but cannot be modified.

```python
>>> fs = frozenset([1, 2, 3])
>>> fs
frozenset({1, 2, 3})
```

Because it’s immutable, it can be used as a dictionary key or stored in other sets.

```python
>>> s = {frozenset([1, 2]), frozenset([3, 4])}
```

---

### `getattr`

Retrieves the value of an attribute by name.
If the attribute doesn’t exist, you can provide a default.

```python
class Foo:
    x = 10

>>> getattr(Foo, "x")
10

>>> getattr(Foo, "missing", None)
None
```

Useful for dynamic attribute access or reflective code.

Equivalent to:

```python
Foo.x
```

but with safer fallback handling.

---

### `globals`

Returns a dictionary representing the current **global symbol table**.
Keys are variable/function/class names; values are the corresponding objects.

```python
>>> x = 10
>>> globals()["x"]
10
```

This is mainly used in metaprogramming, dynamic imports, or REPL tools—not everyday scripts.

---

### `hasattr`

Checks whether an object has an attribute with a given name.
Returns `True` or `False`.

```python
class Foo:
    x = 1

>>> hasattr(Foo, "x")
True
>>> hasattr(Foo, "y")
False
```

Equivalent to trying `getattr(obj, name)` and catching `AttributeError`.

---

### `hash`

Returns the hash value of an object, if it’s hashable.

```python
>>> hash("wolf")
4019441485313280249
```

Hashable objects include:

* strings
* numbers
* tuples of hashable items
* custom objects that implement `__hash__`

Unhashable objects (e.g., lists, dicts) raise `TypeError`.

```python
>>> hash([1, 2, 3])
TypeError
```

Useful for dictionary keys, sets, and hashing algorithms.

---

### `help`

Starts the built-in help system.
In an interactive session, it opens a pager with documentation.

```python
>>> help(len)
Help on built-in function len:
```

Can also print module or object help:

```python
>>> import math
>>> help(math)
```

Primarily intended for the REPL, not production code.

---

### `hex`

Converts an integer to a **hexadecimal string**.

```python
>>> hex(255)
'0xff'
>>> hex(-42)
'-0x2a'
```

Always returns a string starting with `'0x'`.

---

### `id`

Returns an integer representing the object’s **identity**.
This is usually the memory address (CPython-specific), but not guaranteed across implementations.

```python
>>> x = "hello"
>>> id(x)
140347612910128
```

Most useful for debugging or comparing object identity.

---

### `input`

Reads a line of text from standard input.
Always returns a string.

```python
>>> name = input("Enter your name: ")
Enter your name: Aaron
```

Important: conversion must be explicit:

```python
>>> age = int(input("Age: "))
```

---

### `int`

Converts a value to an integer.

```python
>>> int(3.9)
3
>>> int("42")
42
```

You can specify a base when converting from a string:

```python
>>> int("ff", 16)
255
```

Raises `ValueError` for invalid strings.

---

### `isinstance`

Checks whether an object is an instance of a class or a tuple of classes.

```python
>>> isinstance(10, int)
True
>>> isinstance("hello", (str, list))
True
```

Commonly used for type checking and validation.

---

### `issubclass`

Checks whether one class is a subclass of another (or a tuple of classes).

```python
class A: pass
class B(A): pass

>>> issubclass(B, A)
True
>>> issubclass(A, B)
False
```

Useful for class hierarchies, inheritance checks, and type constraints.

---


### `iter`

Returns an iterator for an iterable object.

```python
>>> it = iter([1, 2, 3])
>>> next(it)
1
>>> next(it)
2
```

Custom objects can define `__iter__` to control iteration.
Used internally by `for` loops, comprehensions, and generators.

---

### `len`

Returns the length (number of items) of an object.

```python
>>> len("wolf")
4
>>> len([10, 20, 30])
3
>>> len({"a": 1, "b": 2})
2
```

Works for sequences, collections, and any object implementing `__len__`.
Raises `TypeError` if the object has no length.

---

### `license`

Prints the Python license text.
Used only in interactive sessions.

```python
>>> license
A. HISTORY OF THE SOFTWARE
===========================
Python was created in the early 1990s by Guido van Rossum...
```

Not meant for use inside programs.

---

### `list`

Creates a list object.

```python
>>> list("wolf")
['w', 'o', 'l', 'f']
>>> list((1, 2, 3))
[1, 2, 3]
```

Called without arguments, returns an empty list:

```python
>>> list()
[]
```

Used to convert iterables to lists (e.g., ranges, iterators, generators).

Literal syntax (`[1, 2, 3]`) is more common.

---

### `locals`

Returns a dictionary representing the **current local scope**.

```python
def demo():
    x = 10
    y = 20
    return locals()

>>> demo()
{'x': 10, 'y': 20}
```

In functions, modifying the returned dictionary does *not* reliably alter local variables.
Primarily used for debugging, reflection, and certain metaprogramming patterns.

---

### `map`

Applies a function to each item in one or more iterables.

```python
>>> list(map(str.upper, ["a", "b", "c"]))
['A', 'B', 'C']
```

With multiple iterables:

```python
>>> list(map(lambda x, y: x + y, [1, 2], [10, 20]))
[11, 22]
```

Returns a lazy iterator — wrap with `list()` to see results.

---

### `max`

Returns the largest item in an iterable, or the largest of multiple arguments.

```python
>>> max([3, 7, 2])
7
>>> max(10, 4, 9)
10
```

Supports a `key` function:

```python
>>> max(["wolf", "bear", "cat"], key=len)
'wolf'
```

---

### `memoryview`

Creates a memoryview object, allowing direct access to the memory of bytes-like objects without copying.

```python
>>> data = bytearray(b"hello")
>>> mv = memoryview(data)
>>> mv[0]
104
```

You can modify the underlying buffer through the view:

```python
>>> mv[0] = 72
>>> data
bytearray(b'Hello')
```

Useful for efficient binary manipulation and working with large data buffers.

---

### `min`

Returns the smallest item in an iterable, or the smallest of multiple arguments.

```python
>>> min([3, 7, 2])
2
>>> min(10, 4, 9)
4
```

Supports a `key` function:

```python
>>> min(["wolf", "bear", "cat"], key=len)
'cat'
```

---

### `next`

Retrieves the next item from an iterator.

```python
>>> it = iter([1, 2, 3])
>>> next(it)
1
>>> next(it)
2
```

A default can be provided:

```python
>>> next(it, None)
None
```

Used internally by iteration mechanisms (`for`, comprehensions, generators).

---

### `object`

The base class for all Python classes.
Every class implicitly inherits from `object` unless specified otherwise.

```python
>>> o = object()
>>> type(o)
<class 'object'>
```

Provides default implementations of common behaviors (equality, representation, etc.).
Most useful when creating minimal classes:

```python
class Empty(object):
    pass
```

---

### `oct`

Converts an integer to its **octal string** representation.

```python
>>> oct(64)
'0o100'
>>> oct(-9)
'-0o11'
```

Always returns a string beginning with `'0o'`.

---

### `open`

Opens a file and returns a corresponding file object.

```python
>>> f = open("data.txt", "r")

>>> f.read()
"... contents ..."
```

Common modes:

| Mode  | Meaning                     |
| ----- | --------------------------- |
| `"r"` | read (default)              |
| `"w"` | write (overwrites file)     |
| `"a"` | append                      |
| `"b"` | binary mode                 |
| `"t"` | text mode (default)         |
| `"x"` | write, error if file exists |

Use a context manager to ensure proper closing:

```python
with open("log.txt", "w") as f:
    f.write("Hello\n")
```

---

### `ord`

Returns the Unicode code point of a single character.

```python
>>> ord('a')
97

>>> ord('€')
8364
```

Inverse of `chr()`.

---

### `pow`

Raises a number to a power.
Supports an optional third argument for modular exponentiation.

```python
>>> pow(2, 5)
32

>>> pow(2, 5, 13)   # (2**5) % 13
6
```

`pow(a, b, c)` is efficient for large numbers and used frequently in cryptography.

---

### `print`

Writes text to standard output.

```python
>>> print("Hello", "world")
Hello world
```

Common keyword options:

```python
print("A", "B", sep="-")    # A-B
print("Line1", end="")      # no newline
```

Values are automatically converted to strings.

---

### `property`

Creates a managed attribute on a class — often used to add getters, setters, and validation logic.

```python
class Person:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError("Age cannot be negative")
        self._age = value
```

Using:

```python
>>> p = Person(20)
>>> p.age
20
>>> p.age = 30
```

Properties allow you to expose an attribute-like interface while keeping full control internally.

---

### `quit`

Exits the Python interpreter.
Equivalent to `exit()` and intended for interactive use.

```python
>>> quit()
```

Do **not** use in application code — instead call `sys.exit()`.

---

### `range`

Represents an immutable sequence of integers, often used in loops.

```python
>>> range(5)
range(0, 5)     # 0,1,2,3,4
```

Common patterns:

```python
>>> list(range(2, 10, 2))
[2, 4, 6, 8]
```

Ranges are memory-efficient; they do not store each number individually.

---

### `repr`

Returns a string representation of an object that is meant to be unambiguous or useful for debugging.

```python
>>> repr("wolf")
"'wolf'"
>>> repr([1, 2, 3])
'[1, 2, 3]'
```

Classes can define custom representations:

```python
def __repr__(self):
    return f"Point({self.x}, {self.y})"
```

`repr(x)` is often used in logging and debugging tools.

---

### `reversed`

Returns an iterator that yields items from a sequence in reverse order.

```python
>>> list(reversed([1, 2, 3]))
[3, 2, 1]
```

Works with sequences or any object implementing `__reversed__`.

For iterables without known length, use slicing:

```python
>>> [1, 2, 3][::-1]
[3, 2, 1]
```

---

### `round`

Rounds a number to a given number of decimal places.

```python
>>> round(3.14159, 2)
3.14
```

If no precision is given:

```python
>>> round(5.7)
6
```

Python rounds “ties” using **banker’s rounding** (to the nearest even number):

```python
>>> round(2.5)
2
>>> round(3.5)
4
```

---


### `set`

Creates a new **set**, an unordered collection of unique elements.

```python
>>> set([1, 2, 2, 3])
{1, 2, 3}

>>> set("wolf")
{'w', 'o', 'l', 'f'}
```

Called without arguments:

```python
>>> set()
set()
```

Commonly used for membership testing, removing duplicates, and set operations:

```python
>>> {1, 2, 3} & {2, 3, 4}   # intersection
{2, 3}

>>> {1, 2, 3} | {3, 4, 5}   # union
{1, 2, 3, 4, 5}
```

Literal syntax: `{1, 2, 3}`.

---

### `setattr`

Sets an attribute on an object by name.

```python
class Foo:
    pass

>>> f = Foo()
>>> setattr(f, "x", 10)
>>> f.x
10
```

Equivalent to:

```python
f.x = 10
```

Useful when attribute names are dynamic (e.g., loaded from configuration).

---

### `slice`

Creates a slice object, usually used internally by slicing syntax:

```python
>>> s = slice(1, 4)
>>> "python"[s]
'yth'
```

Equivalent to writing:

```python
"python"[1:4]
```

Slice arguments are:

```python
slice(start, stop, step)
```

Can be used with lists, strings, tuples, ranges, and other sequence types.

---

### `sorted`

Returns a **new sorted list** from an iterable.

```python
>>> sorted([3, 1, 2])
[1, 2, 3]
```

Supports reverse sorting and custom keys:

```python
>>> sorted(["wolf", "bear", "cat"], key=len)
['cat', 'wolf', 'bear']

>>> sorted([3, 1, 2], reverse=True)
[3, 2, 1]
```

Unlike `.sort()`, this does *not* modify the original list.

---

### `staticmethod`

Defines a method that receives **no automatic first argument** (`self` or `cls`).
Used for utility functions that logically belong to a class but don't depend on instance or class state.

```python
class Math:
    @staticmethod
    def add(a, b):
        return a + b
```

Calling:

```python
>>> Math.add(2, 3)
5
```

Semantically, it's just a function stored inside a class.

---

### `str`

Creates or converts a value into a string.

```python
>>> str(42)
'42'
>>> str(3.14)
'3.14'
```

Called with no arguments:

```python
>>> str()
''
```

For custom classes, you can define string conversion via `__str__`:

```python
def __str__(self):
    return f"Point({self.x}, {self.y})"
```

`str()` is for **readable** output.
For debug-oriented output, use `repr()`.

---

### `sum`

Adds up items in an iterable and returns the total.

```python
>>> sum([1, 2, 3])
6
```

Supports an optional starting value:

```python
>>> sum([1, 2, 3], start=10)
16
```

Although it works on any numeric type, avoid using `sum()` for string or list concatenation — it's slow and not intended for that purpose.

---

### `super`

Returns a proxy object used to call methods from a parent (super) class.

```python
class A:
    def greet(self):
        return "Hello from A"

class B(A):
    def greet(self):
        return super().greet() + " and B"
```

Using:

```python
>>> B().greet()
'Hello from A and B'
```

Common use cases:

* extending parent class methods
* cooperative multiple inheritance (common in modern Python)
* calling `__init__` of a parent class cleanly

---

### `tuple`

Creates an immutable sequence.

```python
>>> tuple([1, 2, 3])
(1, 2, 3)

>>> tuple("wolf")
('w', 'o', 'l', 'f')
```

Called without arguments:

```python
>>> tuple()
()
```

Literal syntax is more common:

```python
(1, 2, 3)
```

Useful for fixed collections, dictionary keys, and functions returning multiple values.

---

### `type`

With one argument, returns the type of an object.

```python
>>> type(10)
<class 'int'>
>>> type("hello")
<class 'str'>
```

With three arguments, dynamically creates a new class:

```python
MyClass = type("MyClass", (object,), {"x": 10})

>>> obj = MyClass()
>>> obj.x
10
```

This pattern is used internally by metaclasses and certain dynamic frameworks.

---

### `vars`

Returns a dictionary of an object’s `__dict__` attribute.

```python
class Foo:
    def __init__(self):
        self.x = 10
        self.y = 20

>>> vars(Foo())
{'x': 10, 'y': 20}
```

Called with no arguments inside a function, it returns local variables:

```python
def demo():
    a = 1
    b = 2
    return vars()

>>> demo()
{'a': 1, 'b': 2}
```

Useful for introspection and debugging.

---

### `zip`

Combines multiple iterables into tuples, pairing items by position.

```python
>>> list(zip([1, 2, 3], ["a", "b", "c"]))
[(1, 'a'), (2, 'b'), (3, 'c')]
```

Stops at the shortest iterable:

```python
>>> list(zip([1, 2], [10, 20, 30]))
[(1, 10), (2, 20)]
```

Commonly used for:

* iterating over two sequences together
* transposing data
* pairing keys and values

Example: converting two lists into a dictionary:

```python
>>> dict(zip(["a", "b", "c"], [1, 2, 3]))
{'a': 1, 'b': 2, 'c': 3}
```


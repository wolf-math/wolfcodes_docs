---
title: Byte
sidebar_position: 3
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
>>> dir(bytes)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'center', 'count', 'decode', 'endswith', 'expandtabs', 'find', 'fromhex', 'hex', 'index', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

## Definition

A `bytes` object is an immutable sequence of bytes (integers in the range 0-255). Bytes are used to represent binary data, such as file contents read in binary mode, network packets, or encoded text. Unlike [strings](./string), bytes work with raw binary data rather than Unicode characters. Bytes are immutable and cannot be modified in place.

## Using bytes

### Instantiation

Bytes can be created using several methods:

```python
# Using a bytes literal (b prefix)
>>> b'hello'
b'hello'

# Using the bytes() constructor with an iterable of integers
>>> bytes([65, 66, 67])
b'ABC'

# Using bytes() constructor with a string and encoding
>>> bytes('hello', 'utf-8')
b'hello'

# Using bytes() constructor with a size (creates null bytes)
>>> bytes(5)
b'\x00\x00\x00\x00\x00'
```

### Accessing elements

Bytes can be accessed by index, which returns an integer (0-255):

```python
>>> b = b'hello'
>>> b[0]
104

>>> b[1]
101

>>> b[-1]
111
```

### Slicing bytes

Bytes can be sliced similar to strings:

```python
>>> b = b'chicken-nuggets'
>>> b[0:7]
b'chicken'

>>> b[:7]
b'chicken'

>>> b[8:]
b'nuggets'

>>> b[::2]
b'ciknnges'
```

### Basic operations on bytes

Two or more bytes objects can be concatenated with a `+` operator, or a bytes object can be multiplied by an integer with a `*` operator.

```python
>>> b'hello' + b'world'
b'helloworld'

>>> b'hi' * 3
b'hihihi'
```

### Immutability

Bytes are immutable and cannot be modified in place. Operations that would modify bytes return new bytes objects.

```python
>>> b = b'hello'
>>> b[0] = 72
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment

>>> b = b.replace(b'h', b'H')
>>> b
b'Hello'
```

### `in` and `not in`

Existence of a byte value or subsequence within bytes can be checked with `in` or `not in`.

```python
>>> 104 in b'hello'  # 104 is the byte value for 'h'
True

>>> b'el' in b'hello'
True

>>> b'xyz' in b'hello'
False

>>> b'xyz' not in b'hello'
True
```

### Encoding and decoding

Bytes can be decoded to strings using an encoding (default is UTF-8):

```python
>>> b'hello'.decode()
'hello'

>>> b'hello'.decode('utf-8')
'hello'
```

Strings can be encoded to bytes:

```python
>>> 'hello'.encode()
b'hello'

>>> 'hello'.encode('utf-8')
b'hello'
```

## Dunder methods

| Dunder Method | Operation | Example (normal syntax) | Example (dunder call) |
| --- | --- | --- | --- |
| `__add__`| Concatenation | `b"cat" + b"fish"` → `b'catfish'` | `b"cat".__add__(b"fish")` |
| `__mul__`| Repetition | `b"ha" * 3` → `b'hahaha'` | `b"ha".__mul__(3)` |
| `__contains__` | Membership test | `104 in b"cat"` → `False` | `b"cat".__contains__(104)` |
| `__getitem__` | Index access | `b"cat"[1]` → `97` | `b"cat".__getitem__(1)` |
| `__len__`| Length | `len(b"hello")` → `5`| `b"hello".__len__()` |
| `__eq__` | Equality comparison | `b"dog" == b"dog"` → `True` | `b"dog".__eq__(b"dog")` |
| `__ne__` | Inequality comparison | `b"dog" != b"cat"` → `True` | `b"dog".__ne__(b"cat")` |
| `__lt__` | Less than (lexicographic) | `b"ant" < b"bat"` → `True` | `b"ant".__lt__(b"bat")` |
| `__le__` | Less than or equal | `b"ant" <= b"ant"` → `True` | `b"ant".__le__(b"ant")` |
| `__gt__` | Greater than | `b"bat" > b"ant"` → `True` | `b"bat".__gt__(b"ant")` |
| `__ge__` | Greater than or equal | `b"bat" >= b"bat"` → `True` | `b"bat".__ge__(b"bat")` |
| `__str__`| String conversion | `str(b"hi")` → `"b'hi'"`| `b"hi".__str__()` |
| `__repr__` | Object representation | `repr(b"hi")` → `"b'hi'"` | `b"hi".__repr__()` |
| `__mod__`| Bytes formatting (old-style) | `b"%s world" % b"hello"` → `b'hello world'` | `b"%s world".__mod__(b"hello")` |
| `__hash__` | Hash value (for dicts/sets) | `hash(b"key")` | `b"key".__hash__()`|
| `__iter__` | Iteration | `for byte in b"abc": print(byte)`| `it = b"abc".__iter__(); next(it)` |
| `__bool__` | Truthiness | `bool(b"hi")` → `True`, `bool(b"")` → `False` | `b"hi".__bool__()` |
| `__getnewargs__` | Internal use (pickling support) | *(rarely used directly)* | `b"hi".__getnewargs__()` |

---

## Bytes methods

### `capitalize`

Returns a copy of the bytes with the first byte capitalized (if it's an ASCII letter).

```python
>>> b"hello".capitalize()
b'Hello'

>>> b"HELLO".capitalize()
b'Hello'
```

---

### `center`

Returns a bytes object centered in a specified length, padded with the specified byte (default is space `b' '`).

#### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| length    | **True** | The length of the returned bytes object. |
| byte | **False** | The byte to pad the returned bytes object (default is `b' '`). |

```python
>>> b"stuck".center(10, b"U")
b'UUstuckUUU'
```

:::note
If the length is shorter than the original bytes object, no transformation will take place.
:::

---

### `count`

Returns the number of times a subsequence is found within a bytes object.

```python
>>> b"It's not a bug bug, it's a feature feature.".count(b"bug")
2
```

---

### `decode`

Returns a string decoded from the bytes object using the specified encoding (default is UTF-8).

```python
>>> b'hello'.decode()
'hello'

>>> b'hello'.decode('utf-8')
'hello'

>>> b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')
'中文'
```

---

### `endswith`

Returns `True` if a bytes object terminates with a specified subsequence. Otherwise returns `False`.

```python
>>> b"friend".endswith(b"end")
True

>>> b"friend".endswith(b"start")
False
```

---

### `expandtabs`

Sets the size of a tab `\t` byte.

```python
>>> b"guitar\ttab".expandtabs(20)
b'guitar              tab'
```

This does not set the distance between the words. It sets the size of the tab so in this example the word `tab` will begin at index `20`.

---

### `find`

Returns the index of the first matching subsequence within a bytes object. Returns `-1` if not found.

```python
>>> b"Hello world".find(b'wo')
6

>>> b"hello world".find(b'o')
4

>>> b"hello world".find(b'xyz')
-1
```

---

### `fromhex`

Class method that creates a bytes object from a hexadecimal string.

```python
>>> bytes.fromhex('48656c6c6f')
b'Hello'

>>> bytes.fromhex('deadbeef')
b'\xde\xad\xbe\xef'
```

---

### `hex`

Returns a hexadecimal representation of the bytes object.

```python
>>> b'Hello'.hex()
'48656c6c6f'

>>> b'\xde\xad\xbe\xef'.hex()
'deadbeef'
```

---

### `index`

Returns the index of a subsequence within a bytes object. Raises a `ValueError` if not found.

```python
>>> b"Three is a magic number".index(b"ee")
3

>>> b"hello world".index(b"xyz")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: subsection not found
```

:::note
The `index` method only returns the first occurrence of the subsequence.
:::

---

### `isalnum`

Returns `True` if all bytes in the bytes object are alphanumeric ASCII characters, otherwise returns `False`.

```python
>>> b"SytaxTerror12".isalnum()
True

>>> b"My username is SytaxTerror12".isalnum()
False

>>> b"Hello World!!!".isalnum()
False
```

---

### `isalpha`

Returns `True` if all bytes in the bytes object are alphabetic ASCII characters, otherwise returns `False`.

```python
>>> b"Hello".isalpha()
True

>>> b"Hello123".isalpha()
False

>>> b"Hello!!!".isalpha()
False
```

---

### `isascii`

Returns `True` if all bytes in the bytes object are ASCII (values 0-127), otherwise returns `False`.

```python
>>> b'(^_^) [o_o] (^.^)'.isascii()
True

>>> b'\x80\x90'.isascii()
False
```

---

### `isdigit`

Returns `True` if all bytes in the bytes object are ASCII digits (0-9), otherwise returns `False`.

```python
>>> b"123".isdigit()
True

>>> b"12.3".isdigit()
False

>>> b"one".isdigit()
False
```

---

### `islower`

Returns `True` if all ASCII letters in the bytes object are lowercase, otherwise returns `False`.

```python
>>> b"hi".islower()
True

>>> b"Hi".islower()
False

>>> b"hi!".islower()
True
```

---

### `isspace`

Returns `True` if all bytes in the bytes object are ASCII whitespace characters, otherwise returns `False`.

```python
>>> b"    ".isspace()
True

>>> b" ".isspace()
True

>>> b"chicken nuggets".isspace()
False
```

---

### `istitle`

Returns `True` if the bytes object is in title case (first byte of each word is uppercase, rest are lowercase), otherwise returns `False`.

```python
>>> b"Chicken Nuggets".istitle()
True

>>> b"Chicken nuggets".istitle()
False

>>> b"chicken nuggets".istitle()
False
```

---

### `isupper`

Returns `True` if all ASCII letters in the bytes object are uppercase, otherwise returns `False`.

```python
>>> b"CHICKEN".isupper()
True

>>> b"24 CHICKEN NUGGETS".isupper()
True

>>> b"CHICKEN nuggets".isupper()
False
```

---

### `join`

Takes all of the items in an iterable sequence of bytes objects and joins them into a single bytes object.

```python
>>> b"Duck".join((b"Chicken", b"Monkey"))
b'ChickenDuckMonkey'

>>> b"Duck".join([b"Chicken", b"Monkey"])
b'ChickenDuckMonkey'

>>> b",".join([b"a", b"b", b"c"])
b'a,b,c'
```

---

### `ljust`

Returns a left-justified bytes object padded with the specified byte (default is space) to the specified length.

```python
>>> b"chicken".ljust(20)
b'chicken             '

>>> b"chicken".ljust(20, b'X')
b'chickenXXXXXXXXXXXXX'

>>> b"chicken".ljust(5)
b'chicken'
```

---

### `lower`

Returns a copy of the bytes object with all ASCII letters converted to lowercase.

```python
>>> b"HeLlO wOrLd!".lower()
b'hello world!'
```

---

### `lstrip`

Removes leading whitespace (or specified bytes) from the bytes object.

```python
>>> b"     Hello there!".lstrip()
b'Hello there!'

>>> b"XXXHello there!".lstrip(b'X')
b'Hello there!'
```

---

### `maketrans`

Creates a translation table for use with [`translate`](#translate). This is a static method.

```python
>>> table = bytes.maketrans(b'abc', b'xyz')
>>> b'abc'.translate(table)
b'xyz'
```

---

### `partition`

Returns a tuple with 3 elements: all bytes before the first occurrence of the separator, the separator itself, and everything after the separator.

```python
>>> b"Make it so".partition(b"it")
(b'Make ', b'it', b' so')
```

---

### `removeprefix`

Removes the indicated prefix from the bytes object. If the indicated bytes are not at the beginning, no transformation will occur.

```python
>>> b"algorhythm".removeprefix(b"algo")
b'rhythm'

>>> b"algorhythm".removeprefix(b"go")
b'algorhythm'
```

---

### `removesuffix`

Removes the indicated suffix from the bytes object. If the indicated bytes are not at the end, no transformation will occur.

```python
>>> b"algorhythm".removesuffix(b"rhythm")
b'algo'

>>> b"algorhythm".removesuffix(b"rhy")
b'algorhythm'
```

---

### `replace`

Replaces all occurrences of a subsequence within a bytes object with another subsequence.

```python
>>> b"alfalfa farm".replace(b"a", b"g")
b'glfglfg fgrm'

>>> b"alfalfa farm".replace(b"alfalfa", b"soul")
b'soul farm'
```

---

### `rfind`

Returns the index of the last occurrence of a subsequence within a bytes object. Returns `-1` if the matching subsequence is not found.

```python
>>> b"to be or not to be".rfind(b"be")
16

>>> b"to be or not to be".rfind(b"to")
13

>>> b"to be or not to be".rfind(b"42")
-1
```

---

### `rindex`

Returns the index of the last occurrence of a subsequence within a bytes object. Raises a `ValueError` if the matching subsequence is not found.

```python
>>> b"to be or not to be".rindex(b"be")
16

>>> b"to be or not to be".rindex(b"to")
13

>>> b"to be or not to be".rindex(b"42")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: subsection not found
```

---

### `rjust`

Returns a right-justified bytes object padded with the specified byte (default is space) to the specified length.

```python
>>> b"nuggets".rjust(20)
b'             nuggets'

>>> b"nuggets".rjust(20, b'X')
b'XXXXXXXXXXXXXnuggets'
```

---

### `rpartition`

Returns a tuple with 3 elements: all bytes before the last occurrence of the separator, the separator itself, and everything after the separator.

```python
>>> b"Make it so, so it will be".rpartition(b"it")
(b'Make it so, so ', b'it', b' will be')
```

---

### `rsplit`

Returns a list of bytes objects split by the delimiter. The default delimiter is whitespace `b' '`. This is only different from [`split`](#split) when the `maxsplit` parameter is used, in which case `rsplit` will split starting from the right side.

```python
>>> b"guitar bass drums".rsplit()
[b'guitar', b'bass', b'drums']

>>> b"guitar, bass, drums".rsplit(b",")
[b'guitar', b' bass', b' drums']

>>> b"guitar, bass, drums".rsplit(b",", 1)
[b'guitar, bass', b' drums']
```

---

### `rstrip`

Returns the given bytes object with trailing whitespace (or specified bytes) removed.

```python
>>> b"heehaw           ".rstrip()
b'heehaw'

>>> b"heehawXXX".rstrip(b'X')
b'heehaw'
```

---

### `split`

Returns a list of bytes objects split by the delimiter. The default delimiter is whitespace `b' '`. This is only different from [`rsplit`](#rsplit) when the `maxsplit` parameter is used, in which case `split` will split starting from the left side.

```python
>>> b"guitar bass drums".split()
[b'guitar', b'bass', b'drums']

>>> b"guitar, bass, drums".split(b",")
[b'guitar', b' bass', b' drums']

>>> b"guitar, bass, drums".split(b",", 1)
[b'guitar', b' bass, drums']
```

---

### `splitlines`

Returns a list of bytes objects split along new lines `\n`.

```python
>>> b"There are\nbunch of lines".splitlines()
[b'There are', b'bunch of lines']
```

---

### `startswith`

Returns `True` if the bytes object begins with the indicated subsequence, otherwise returns `False`.

```python
>>> b"to be or not to be".startswith(b"t")
True

>>> b"to be or not to be".startswith(b"to")
True

>>> b"to be or not to be".startswith(b"be")
False
```

---

### `strip`

Returns the given bytes object with leading and trailing whitespace (or specified bytes) removed.

```python
>>> b"         hello        there              ".strip()
b'hello        there'

>>> b"XXXhello thereXXX".strip(b'X')
b'hello there'
```

---

### `swapcase`

Returns a new bytes object where all of the uppercase ASCII letters from the original are lowercased, and all of the lowercase ASCII letters from the original are uppercased.

```python
>>> b"Bob had a hamster named Jack".swapcase()
b'bOB HAD A HAMSTER NAMED jACK'
```

---

### `title`

Returns the original bytes object formatted in title case (first byte of each word is uppercase, rest are lowercase).

```python
>>> b"this is the greatest title in the universe... tribute".title()
b'This Is The Greatest Title In The Universe... Tribute'

>>> b"THIS IS THE GREATEST TITLE IN THE UNIVERSE... TRIBUTE".title()
b'This Is The Greatest Title In The Universe... Tribute'
```

---

### `translate`

Returns a bytes object where the indicated bytes are swapped based on a translation table created with [`maketrans`](#maketrans).

```python
>>> table = bytes.maketrans(b"aeiou", b"12345")
>>> b"bass guitar".translate(table)
b'b1ss g5t1r'
```

---

### `upper`

Returns a copy of the bytes object where all ASCII letters are transformed to uppercase.

```python
>>> b"lowercase".upper()
b'LOWERCASE'
```

---

### `zfill`

Returns a new bytes object that fills the beginning of the original with zeros `b'0'` until the specified length has been reached.

```python
>>> b"long enough?".zfill(25)
b'0000000000000long enough?'
```

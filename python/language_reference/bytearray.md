---
title: Bytearray
sidebar_position: 4
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
>>> dir(bytearray)
['__add__', '__alloc__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'capitalize', 'center', 'clear', 'copy', 'count', 'decode', 'endswith', 'expandtabs', 'extend', 'find', 'fromhex', 'hex', 'index', 'insert', 'isalnum', 'isalpha', 'isascii', 'isdigit', 'islower', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'pop', 'remove', 'removeprefix', 'removesuffix', 'replace', 'reverse', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

## Definition

A `bytearray` object is a mutable sequence of bytes (integers in the range 0-255). Bytearrays are used to represent binary data that needs to be modified, such as network buffers, file processing, or binary protocol manipulation. Unlike [`bytes`](./byte), bytearrays can be modified in place. Bytearrays share many methods with bytes but also include mutable operations like `append`, `extend`, `insert`, `pop`, `remove`, and `clear`.

## Using bytearray

### Instantiation

Bytearrays can be created using several methods:

```python
# Using the bytearray() constructor with an iterable of integers
>>> bytearray([65, 66, 67])
bytearray(b'ABC')

# Using bytearray() constructor with a string and encoding
>>> bytearray('hello', 'utf-8')
bytearray(b'hello')

# Using bytearray() constructor with a size (creates null bytes)
>>> bytearray(5)
bytearray(b'\x00\x00\x00\x00\x00')

# Using bytearray() constructor with a bytes object
>>> bytearray(b'hello')
bytearray(b'hello')
```

### Accessing elements

Bytearrays can be accessed by index, which returns an integer (0-255):

```python
>>> ba = bytearray(b'hello')
>>> ba[0]
104

>>> ba[1]
101

>>> ba[-1]
111
```

### Modifying elements

Unlike bytes, bytearrays can be modified in place:

```python
>>> ba = bytearray(b'hello')
>>> ba[0] = 72  # Change 'h' (104) to 'H' (72)
>>> ba
bytearray(b'Hello')

>>> ba[1] = 69  # Change 'e' (101) to 'E' (69)
>>> ba
bytearray(b'HEllo')
```

### Slicing bytearray

Bytearrays can be sliced similar to bytes and lists:

```python
>>> ba = bytearray(b'chicken-nuggets')
>>> ba[0:7]
bytearray(b'chicken')

>>> ba[:7]
bytearray(b'chicken')

>>> ba[8:]
bytearray(b'nuggets')

>>> ba[::2]
bytearray(b'ciknnges')
```

Slices can also be assigned to modify the bytearray:

```python
>>> ba = bytearray(b'hello')
>>> ba[0:2] = b'HE'
>>> ba
bytearray(b'HEllo')
```

### Basic operations on bytearray

Two or more bytearray objects can be concatenated with a `+` operator, or a bytearray can be multiplied by an integer with a `*` operator. These operations return new bytearray objects.

```python
>>> bytearray(b'hello') + bytearray(b'world')
bytearray(b'helloworld')

>>> bytearray(b'hi') * 3
bytearray(b'hihihi')
```

### In-place operations

Bytearrays support in-place operations that modify the original object:

```python
>>> ba = bytearray(b'hello')
>>> ba += b' world'
>>> ba
bytearray(b'hello world')

>>> ba *= 2
>>> ba
bytearray(b'hello worldhello world')
```

### `in` and `not in`

Existence of a byte value or subsequence within a bytearray can be checked with `in` or `not in`.

```python
>>> ba = bytearray(b'hello')
>>> 104 in ba  # 104 is the byte value for 'h'
True

>>> b'el' in ba
True

>>> b'xyz' in ba
False

>>> b'xyz' not in ba
True
```

### Encoding and decoding

Bytearrays can be decoded to strings using an encoding (default is UTF-8):

```python
>>> bytearray(b'hello').decode()
'hello'

>>> bytearray(b'hello').decode('utf-8')
'hello'
```

Strings can be encoded to bytearrays:

```python
>>> bytearray('hello', 'utf-8')
bytearray(b'hello')
```

## Dunder methods

| Dunder Method | Operation | Example (normal syntax) | Example (dunder call) |
| --- | --- | --- | --- |
| `__add__`| Concatenation | `bytearray(b"cat") + bytearray(b"fish")` → `bytearray(b'catfish')` | `bytearray(b"cat").__add__(bytearray(b"fish"))` |
| `__mul__`| Repetition | `bytearray(b"ha") * 3` → `bytearray(b'hahaha')` | `bytearray(b"ha").__mul__(3)` |
| `__contains__` | Membership test | `104 in bytearray(b"cat")` → `False` | `bytearray(b"cat").__contains__(104)` |
| `__getitem__` | Index access | `bytearray(b"cat")[1]` → `97` | `bytearray(b"cat").__getitem__(1)` |
| `__setitem__` | Item assignment | `ba[0] = 72` | `ba.__setitem__(0, 72)` |
| `__delitem__` | Delete item | `del ba[0]` | `ba.__delitem__(0)` |
| `__len__`| Length | `len(bytearray(b"hello"))` → `5`| `bytearray(b"hello").__len__()` |
| `__eq__` | Equality comparison | `bytearray(b"dog") == bytearray(b"dog")` → `True` | `bytearray(b"dog").__eq__(bytearray(b"dog"))` |
| `__ne__` | Inequality comparison | `bytearray(b"dog") != bytearray(b"cat")` → `True` | `bytearray(b"dog").__ne__(bytearray(b"cat"))` |
| `__lt__` | Less than (lexicographic) | `bytearray(b"ant") < bytearray(b"bat")` → `True` | `bytearray(b"ant").__lt__(bytearray(b"bat"))` |
| `__le__` | Less than or equal | `bytearray(b"ant") <= bytearray(b"ant")` → `True` | `bytearray(b"ant").__le__(bytearray(b"ant"))` |
| `__gt__` | Greater than | `bytearray(b"bat") > bytearray(b"ant")` → `True` | `bytearray(b"bat").__gt__(bytearray(b"ant"))` |
| `__ge__` | Greater than or equal | `bytearray(b"bat") >= bytearray(b"bat")` → `True` | `bytearray(b"bat").__ge__(bytearray(b"bat"))` |
| `__iadd__` | In-place addition | `ba += b'!'` | `ba.__iadd__(b'!')` |
| `__imul__` | In-place multiplication | `ba *= 2` | `ba.__imul__(2)` |
| `__str__`| String conversion | `str(bytearray(b"hi"))` → `"bytearray(b'hi')"`| `bytearray(b"hi").__str__()` |
| `__repr__` | Object representation | `repr(bytearray(b"hi"))` → `"bytearray(b'hi')"` | `bytearray(b"hi").__repr__()` |
| `__mod__`| Bytes formatting (old-style) | `bytearray(b"%s world") % b"hello"` → `bytearray(b'hello world')` | `bytearray(b"%s world").__mod__(b"hello")` |
| `__iter__` | Iteration | `for byte in bytearray(b"abc"): print(byte)`| `it = bytearray(b"abc").__iter__(); next(it)` |
| `__bool__` | Truthiness | `bool(bytearray(b"hi"))` → `True`, `bool(bytearray())` → `False` | `bytearray(b"hi").__bool__()` |

---

## Bytearray methods

### `append`

Adds a single byte (integer 0-255) to the end of the bytearray. Modifies the bytearray in place.

```python
>>> ba = bytearray(b'hello')
>>> ba.append(33)  # 33 is '!'
>>> ba
bytearray(b'hello!')
```

---

### `capitalize`

Returns a copy of the bytearray with the first byte capitalized (if it's an ASCII letter). Does not modify the original.

```python
>>> ba = bytearray(b"hello")
>>> ba.capitalize()
bytearray(b'Hello')

>>> ba  # Original unchanged
bytearray(b'hello')
```

---

### `center`

Returns a copy of the bytearray centered in a specified length, padded with the specified byte (default is space `b' '`). Does not modify the original.

#### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| length    | **True** | The length of the returned bytearray. |
| byte | **False** | The byte to pad the returned bytearray (default is `b' '`). |

```python
>>> bytearray(b"stuck").center(10, b"U")
bytearray(b'UUstuckUUU')
```

:::note
If the length is shorter than the original bytearray, no transformation will take place.
:::

---

### `clear`

Removes all elements from the bytearray. Modifies the bytearray in place.

```python
>>> ba = bytearray(b'hello')
>>> ba.clear()
>>> ba
bytearray()
```

---

### `copy`

Returns a copy (or clone) of the bytearray.

```python
>>> ba = bytearray(b'hello')
>>> ba_copy = ba.copy()
>>> ba_copy[0] = 72
>>> ba_copy
bytearray(b'Hello')

>>> ba  # Original unchanged
bytearray(b'hello')
```

---

### `count`

Returns the number of times a subsequence is found within the bytearray.

```python
>>> bytearray(b"It's not a bug bug, it's a feature feature.").count(b"bug")
2
```

---

### `decode`

Returns a string decoded from the bytearray using the specified encoding (default is UTF-8).

```python
>>> bytearray(b'hello').decode()
'hello'

>>> bytearray(b'hello').decode('utf-8')
'hello'
```

---

### `endswith`

Returns `True` if the bytearray terminates with a specified subsequence. Otherwise returns `False`.

```python
>>> bytearray(b"friend").endswith(b"end")
True

>>> bytearray(b"friend").endswith(b"start")
False
```

---

### `expandtabs`

Returns a copy of the bytearray with tab `\t` bytes expanded. Does not modify the original.

```python
>>> bytearray(b"guitar\ttab").expandtabs(20)
bytearray(b'guitar              tab')
```

This does not set the distance between the words. It sets the size of the tab so in this example the word `tab` will begin at index `20`.

---

### `extend`

Adds all elements from an iterable of integers (0-255) to the end of the bytearray. Modifies the bytearray in place.

```python
>>> ba = bytearray(b'hello')
>>> ba.extend([33, 32, 119])  # '! w'
>>> ba
bytearray(b'hello! w')

>>> ba.extend(b'orld')
>>> ba
bytearray(b'hello! world')
```

---

### `find`

Returns the index of the first matching subsequence within the bytearray. Returns `-1` if not found.

```python
>>> bytearray(b"Hello world").find(b'wo')
6

>>> bytearray(b"hello world").find(b'o')
4

>>> bytearray(b"hello world").find(b'xyz')
-1
```

---

### `fromhex`

Class method that creates a bytearray from a hexadecimal string.

```python
>>> bytearray.fromhex('48656c6c6f')
bytearray(b'Hello')

>>> bytearray.fromhex('deadbeef')
bytearray(b'\xde\xad\xbe\xef')
```

---

### `hex`

Returns a hexadecimal representation of the bytearray.

```python
>>> bytearray(b'Hello').hex()
'48656c6c6f'

>>> bytearray(b'\xde\xad\xbe\xef').hex()
'deadbeef'
```

---

### `index`

Returns the index of a subsequence within the bytearray. Raises a `ValueError` if not found.

```python
>>> bytearray(b"Three is a magic number").index(b"ee")
3

>>> bytearray(b"hello world").index(b"xyz")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: subsection not found
```

:::note
The `index` method only returns the first occurrence of the subsequence.
:::

---

### `insert`

Inserts a byte (integer 0-255) at the specified index. Modifies the bytearray in place.

```python
>>> ba = bytearray(b'hello')
>>> ba.insert(0, 72)  # Insert 'H' at the beginning
>>> ba
bytearray(b'Hello')

>>> ba.insert(5, 33)  # Insert '!' at index 5
>>> ba
bytearray(b'Hello!')
```

---

### `isalnum`

Returns `True` if all bytes in the bytearray are alphanumeric ASCII characters, otherwise returns `False`.

```python
>>> bytearray(b"SytaxTerror12").isalnum()
True

>>> bytearray(b"My username is SytaxTerror12").isalnum()
False
```

---

### `isalpha`

Returns `True` if all bytes in the bytearray are alphabetic ASCII characters, otherwise returns `False`.

```python
>>> bytearray(b"Hello").isalpha()
True

>>> bytearray(b"Hello123").isalpha()
False
```

---

### `isascii`

Returns `True` if all bytes in the bytearray are ASCII (values 0-127), otherwise returns `False`.

```python
>>> bytearray(b'(^_^) [o_o]').isascii()
True

>>> bytearray(b'\x80\x90').isascii()
False
```

---

### `isdigit`

Returns `True` if all bytes in the bytearray are ASCII digits (0-9), otherwise returns `False`.

```python
>>> bytearray(b"123").isdigit()
True

>>> bytearray(b"12.3").isdigit()
False
```

---

### `islower`

Returns `True` if all ASCII letters in the bytearray are lowercase, otherwise returns `False`.

```python
>>> bytearray(b"hi").islower()
True

>>> bytearray(b"Hi").islower()
False
```

---

### `isspace`

Returns `True` if all bytes in the bytearray are ASCII whitespace characters, otherwise returns `False`.

```python
>>> bytearray(b"    ").isspace()
True

>>> bytearray(b"chicken nuggets").isspace()
False
```

---

### `istitle`

Returns `True` if the bytearray is in title case (first byte of each word is uppercase, rest are lowercase), otherwise returns `False`.

```python
>>> bytearray(b"Chicken Nuggets").istitle()
True

>>> bytearray(b"Chicken nuggets").istitle()
False
```

---

### `isupper`

Returns `True` if all ASCII letters in the bytearray are uppercase, otherwise returns `False`.

```python
>>> bytearray(b"CHICKEN").isupper()
True

>>> bytearray(b"CHICKEN nuggets").isupper()
False
```

---

### `join`

Takes all of the items in an iterable sequence of bytes objects and joins them into a single bytearray.

```python
>>> bytearray(b"Duck").join((b"Chicken", b"Monkey"))
bytearray(b'ChickenDuckMonkey')

>>> bytearray(b",").join([b"a", b"b", b"c"])
bytearray(b'a,b,c')
```

---

### `ljust`

Returns a copy of the bytearray left-justified and padded with the specified byte (default is space) to the specified length. Does not modify the original.

```python
>>> bytearray(b"chicken").ljust(20)
bytearray(b'chicken             ')

>>> bytearray(b"chicken").ljust(20, b'X')
bytearray(b'chickenXXXXXXXXXXXXX')
```

---

### `lower`

Returns a copy of the bytearray with all ASCII letters converted to lowercase. Does not modify the original.

```python
>>> bytearray(b"HeLlO wOrLd!").lower()
bytearray(b'hello world!')
```

---

### `lstrip`

Returns a copy of the bytearray with leading whitespace (or specified bytes) removed. Does not modify the original.

```python
>>> bytearray(b"     Hello there!").lstrip()
bytearray(b'Hello there!')

>>> bytearray(b"XXXHello there!").lstrip(b'X')
bytearray(b'Hello there!')
```

---

### `maketrans`

Creates a translation table for use with [`translate`](#translate). This is a static method.

```python
>>> table = bytearray.maketrans(b'abc', b'xyz')
>>> bytearray(b'abc').translate(table)
bytearray(b'xyz')
```

---

### `partition`

Returns a tuple with 3 elements: all bytes before the first occurrence of the separator, the separator itself, and everything after the separator.

```python
>>> bytearray(b"Make it so").partition(b"it")
(bytearray(b'Make '), bytearray(b'it'), bytearray(b' so'))
```

---

### `pop`

Removes and returns the byte at the specified index (default is the last byte). Modifies the bytearray in place.

```python
>>> ba = bytearray(b'hello')
>>> ba.pop()
111

>>> ba
bytearray(b'hell')

>>> ba.pop(0)
104

>>> ba
bytearray(b'ell')
```

---

### `remove`

Removes the first occurrence of a byte value from the bytearray. Raises a `ValueError` if the byte is not found. Modifies the bytearray in place.

```python
>>> ba = bytearray(b'hello')
>>> ba.remove(108)  # Remove 'l' (108)
>>> ba
bytearray(b'helo')

>>> ba.remove(120)  # 'x' not found
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: value not in bytearray
```

---

### `removeprefix`

Returns a copy of the bytearray with the indicated prefix removed. If the indicated bytes are not at the beginning, no transformation will occur. Does not modify the original.

```python
>>> bytearray(b"algorhythm").removeprefix(b"algo")
bytearray(b'rhythm')

>>> bytearray(b"algorhythm").removeprefix(b"go")
bytearray(b'algorhythm')
```

---

### `removesuffix`

Returns a copy of the bytearray with the indicated suffix removed. If the indicated bytes are not at the end, no transformation will occur. Does not modify the original.

```python
>>> bytearray(b"algorhythm").removesuffix(b"rhythm")
bytearray(b'algo')

>>> bytearray(b"algorhythm").removesuffix(b"rhy")
bytearray(b'algorhythm')
```

---

### `replace`

Returns a copy of the bytearray with all occurrences of a subsequence replaced with another subsequence. Does not modify the original.

```python
>>> bytearray(b"alfalfa farm").replace(b"a", b"g")
bytearray(b'glfglfg fgrm')

>>> bytearray(b"alfalfa farm").replace(b"alfalfa", b"soul")
bytearray(b'soul farm')
```

---

### `reverse`

Reverses the bytearray in place. Modifies the bytearray.

```python
>>> ba = bytearray(b'hello')
>>> ba.reverse()
>>> ba
bytearray(b'olleh')
```

---

### `rfind`

Returns the index of the last occurrence of a subsequence within the bytearray. Returns `-1` if the matching subsequence is not found.

```python
>>> bytearray(b"to be or not to be").rfind(b"be")
16

>>> bytearray(b"to be or not to be").rfind(b"to")
13

>>> bytearray(b"to be or not to be").rfind(b"42")
-1
```

---

### `rindex`

Returns the index of the last occurrence of a subsequence within the bytearray. Raises a `ValueError` if the matching subsequence is not found.

```python
>>> bytearray(b"to be or not to be").rindex(b"be")
16

>>> bytearray(b"to be or not to be").rindex(b"42")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: subsection not found
```

---

### `rjust`

Returns a copy of the bytearray right-justified and padded with the specified byte (default is space) to the specified length. Does not modify the original.

```python
>>> bytearray(b"nuggets").rjust(20)
bytearray(b'             nuggets')

>>> bytearray(b"nuggets").rjust(20, b'X')
bytearray(b'XXXXXXXXXXXXXnuggets')
```

---

### `rpartition`

Returns a tuple with 3 elements: all bytes before the last occurrence of the separator, the separator itself, and everything after the separator.

```python
>>> bytearray(b"Make it so, so it will be").rpartition(b"it")
(bytearray(b'Make it so, so '), bytearray(b'it'), bytearray(b' will be'))
```

---

### `rsplit`

Returns a list of bytearray objects split by the delimiter. The default delimiter is whitespace `b' '`. This is only different from [`split`](#split) when the `maxsplit` parameter is used, in which case `rsplit` will split starting from the right side.

```python
>>> bytearray(b"guitar bass drums").rsplit()
[bytearray(b'guitar'), bytearray(b'bass'), bytearray(b'drums')]

>>> bytearray(b"guitar, bass, drums").rsplit(b",", 1)
[bytearray(b'guitar, bass'), bytearray(b' drums')]
```

---

### `rstrip`

Returns a copy of the bytearray with trailing whitespace (or specified bytes) removed. Does not modify the original.

```python
>>> bytearray(b"heehaw           ").rstrip()
bytearray(b'heehaw')

>>> bytearray(b"heehawXXX").rstrip(b'X')
bytearray(b'heehaw')
```

---

### `split`

Returns a list of bytearray objects split by the delimiter. The default delimiter is whitespace `b' '`. This is only different from [`rsplit`](#rsplit) when the `maxsplit` parameter is used, in which case `split` will split starting from the left side.

```python
>>> bytearray(b"guitar bass drums").split()
[bytearray(b'guitar'), bytearray(b'bass'), bytearray(b'drums')]

>>> bytearray(b"guitar, bass, drums").split(b",", 1)
[bytearray(b'guitar'), bytearray(b' bass, drums')]
```

---

### `splitlines`

Returns a list of bytearray objects split along new lines `\n`.

```python
>>> bytearray(b"There are\nbunch of lines").splitlines()
[bytearray(b'There are'), bytearray(b'bunch of lines')]
```

---

### `startswith`

Returns `True` if the bytearray begins with the indicated subsequence, otherwise returns `False`.

```python
>>> bytearray(b"to be or not to be").startswith(b"t")
True

>>> bytearray(b"to be or not to be").startswith(b"to")
True

>>> bytearray(b"to be or not to be").startswith(b"be")
False
```

---

### `strip`

Returns a copy of the bytearray with leading and trailing whitespace (or specified bytes) removed. Does not modify the original.

```python
>>> bytearray(b"         hello        there              ").strip()
bytearray(b'hello        there')

>>> bytearray(b"XXXhello thereXXX").strip(b'X')
bytearray(b'hello there')
```

---

### `swapcase`

Returns a copy of the bytearray where all of the uppercase ASCII letters from the original are lowercased, and all of the lowercase ASCII letters from the original are uppercased. Does not modify the original.

```python
>>> bytearray(b"Bob had a hamster named Jack").swapcase()
bytearray(b'bOB HAD A HAMSTER NAMED jACK')
```

---

### `title`

Returns a copy of the bytearray formatted in title case (first byte of each word is uppercase, rest are lowercase). Does not modify the original.

```python
>>> bytearray(b"this is the greatest title").title()
bytearray(b'This Is The Greatest Title')

>>> bytearray(b"THIS IS THE GREATEST TITLE").title()
bytearray(b'This Is The Greatest Title')
```

---

### `translate`

Returns a copy of the bytearray where the indicated bytes are swapped based on a translation table created with [`maketrans`](#maketrans). Does not modify the original.

```python
>>> table = bytearray.maketrans(b"aeiou", b"12345")
>>> bytearray(b"bass guitar").translate(table)
bytearray(b'b1ss g5t1r')
```

---

### `upper`

Returns a copy of the bytearray where all ASCII letters are transformed to uppercase. Does not modify the original.

```python
>>> bytearray(b"lowercase").upper()
bytearray(b'LOWERCASE')
```

---

### `zfill`

Returns a copy of the bytearray that fills the beginning with zeros `b'0'` until the specified length has been reached. Does not modify the original.

```python
>>> bytearray(b"long enough?").zfill(25)
bytearray(b'0000000000000long enough?')
```

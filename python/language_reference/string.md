---
title: String
sidebar_position: 18
date: 28 October 2025
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
>>> dir(str)
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
```

## Definition

A string is any series of characters between a set of quotation marks- double `"` or single `'`. Strings must be terminated with the same type of quotation mark that they were started with. Strings are immutable and cannot be changed in place. Only new strings can be created.  


## Using strings

If a string does not have quotation marks it will be interpreted as a variable.

```python
"this is a string"
'this is also a string'
this is not a string
```

A multiline string can be created with 3 quotation marks (single or double).

```python
"""multi
line
string
"""
```

### Escape characters

the backslash `\` can "escape" a quotation mark. When escaped, Python will interpret the quotation mark as a character instead of the termination of the string.

```python
>>> "The cow says \"moo\""

'The cow says "moo"'
```



A new line can be created within a string with `\n`. 

```python
>>> print("This string will print\non 2 lines")
This string will print
on 2 lines
```

If a string is preceeded by a `r` the escape characters are not treated as escape characters. This is called a `raw string`.

```python
>>> print(r"This string will print\non 1 line")
This string will print\non 1 line
```
### Basic operations on strings

Two or more strings can be added with a `+` operator or a string can be multipled by an `integer` with a `*` operator. 

```python
>>> "hello" * 3
'hellohellohello'

>>> "hello" + "world"
"helloworld'
```

### Operations with non-strings

### f-strings

f-strings allow values to be interpolated into a string. They can be used with any quotation mark type. A set of curly braces contains the values to be interpolated.

```python
>>> year = 2008
>>> print(f"Python 3 was first released in {year}")

'Python 3 was first released in 2008'
```

Expressions can be executed inside of an f-string:

```python
>>> print(f"For computers, time began in the year {2000 - 30}")
"For computers, time began in the year 1970'
```

### Slicing strings

A substring can be extracted from string by _slicing_ using the syntax:

```python
string[start:stop]
```

The `start` is the index of the first character of the slice. The slice continues up to but not including the index `stop`. If no index is specified the respective beginning or end of the string is considered.

```python
>>> "chicken-nuggets"[0:7]
'chicken'

>>> "chicken-nuggets"[:7]
'chicken'

>>> "chicken-nuggets"[3:9]
'cken-n'

>>> "chicken-nuggets"[8:]
'nuggets'
```

#### Step slicing

```python
string[start:stop:step]
```

This will return every 2nd letter of the original string:

```python
>>> "chicken-nuggets"[::2]
'ciknnges'
```

Or every 3rd letter of just "chicken":

```python
>>> "chicken-nuggets"[0:7:3]
'ccn'
```

### `in` and `not in`

Existince of a substring within a string can be checked with `in` or `not in`.

```python
>>> "gg" in "chicken nuggets"
True

>>> "potatoes" in "chicken nuggets"
False

>>> "potatoes" not in "chicken nuggets"
True

>>> "gg" not in "chicken nuggets"
False
```


## Operations on strings

Dunder (double underscore) methods are a list of operations that can be made on strings. 

| Dunder Method | Operation | Example (normal syntax) | Example (dunder call) |
| --- | --- | --- | --- |
| `__add__`| Concatenation | `"cat" + "fish"` → `'catfish'` | `"cat".__add__("fish")` |
| `__mul__`| Repetition | `"ha" * 3` → `'hahaha'` | `"ha".__mul__(3)` |
| `__contains__` | Membership test | `'a' in "cat"` → `True` | `"cat".__contains__('a')` |
| `__getitem__` | Index access | `"cat"[1]` → `'a'` | `"cat".__getitem__(1)` |
| `__len__`| Length | `len("hello")` → `5`| `"hello".__len__()` |
| `__eq__` | Equality comparison | `"dog" == "dog"` → `True` | `"dog".__eq__("dog")` |
| `__ne__` | Inequality comparison | `"dog" != "cat"` → `True` | `"dog".__ne__("cat")` |
| `__lt__` | Less than (lexicographic) | `"ant" < "bat"` → `True` | `"ant".__lt__("bat")` |
| `__le__` | Less than or equal | `"ant" <= "ant"` → `True` | `"ant".__le__("ant")` |
| `__gt__` | Greater than | `"bat" > "ant"` → `True` | `"bat".__gt__("ant")` |
| `__ge__` | Greater than or equal | `"bat" >= "bat"` → `True` | `"bat".__ge__("bat")` |
| `__str__`| String conversion | `str("hi")` → `'hi'`| `"hi".__str__()` |
| `__repr__` | Object representation | `repr("hi")` → `"'hi'"` | `"hi".__repr__()` |
| `__format__` | f-string / format syntax| `f"Word: {'hi'}"` → `'Word: hi'` | `"hi".__format__('')` |
| `__mod__`| String formatting (old-style) | `"%s world" % "hello"` → `'hello world'` | `"%s world".__mod__("hello")` |
| `__hash__` | Hash value (for dicts/sets) | `hash("key")` | `"key".__hash__()`|
| `__iter__` | Iteration | `for ch in "abc": print(ch)`| `it = "abc".__iter__(); next(it)` |
| `__bool__` | Truthiness | `bool("hi")` → `True`, `bool("")` → `False` | `"hi".__bool__()` |
| `__getnewargs__` | Internal use (pickling support) | *(rarely used directly)* | `"hi".__getnewargs__()` |

---

## String methods

### capitalize

Capitalizes the first letter in a string.

```python
>>> "hello".capitalize()
'Hello'
```
---

### `casefold`

Used for text normalization. Most commonly used to compare string values without uppercase or lowercase distictions.

```python
>>> "hElLo WoRlD".casefold()
'hello world'
```

```python
>>> "hElLo WoRlD".casefold() == 'hello world'
True
```

---

### `center`

Returns a string in the center of a specified character. If no character is specified the default is space.

---

#### Parameters

| Parameter | Required | Description |
| --- | --- | --- |
| length    | **True** | The length of the returned string.
| character | **False** | The charachter to pad the returned string (default space " ").

```python
>>> "stuck".center(10, "U")
'UUstuckUUU'
```

:::note
  If the length is shorted than the original string no transformation will take place.
:::

---

### `count`

Returns the number of times a substring is found within a string.

```python
>>> "It’s not a bug bug, it’s a feature feature.".count("bug")
2
```

---

### `encode`

Returns the encoded string in UTF-8. 

```python
>>> "🤖".encode()
b'\xf0\x9f\xa4\x96'
```

---

### `endswith`

Returns `True` if a string terminates with a specified substring. Otherwise returns `False`.

```python
>>> "friend".endswith("end")
True
```

---

### `expandtabs`

Sets the size of a tab `\t`.

```python
>>> "guitar\ttab".expandtabs(20)
'guitar              tab'
```

This does not set the distance between the word. It sets the size of the tab so in this example the word `tab` will begin at index `20`.

---

### `find`

Returns the index of the first matching substring within a string.

```python
>>> "Hello world".find('wo')
6
```

Notice in this instance `find` returns `4` instead of `7`.

```python
>>> "hello world".find('o')
4
```

---

### `format`

Formats a string by interpolating a variable into curly braces.

:::note
f-strings are generally preferred over using the `format` method.
:::

The interpolation can be made either by variable name, numerically, or by order.

```python
>>> "Hello, my name is {name}. You killed my {family_member}. Prepare to {action}".format(name = "Bob", family_member = "hamster", action= "take a nap")
'Hello, my name is Bob. You killed my hamster. Prepare to take a nap'

>>> "Hello, my name is {0}. You killed my {1}. Prepare to {2}".format("Bob", "hamster", "take a nap")
'Hello, my name is Bob. You killed my hamster. Prepare to take a nap'

>>> "Hello, my name is {}. You killed my {}. Prepare to {}".format("Bob", "hamster", "take a nap")
'Hello, my name is Bob. You killed my hamster. Prepare to take a nap'
```

---

### `format_map`

This does the same thing as `format`, except with a dictionary of values.

```python
>>> inigo = {"name": "Bob", "family_member": "hamster", "action": "take a nap"}
>>> "Hello, my name is {name}. You killed my {family_member}. Prepare to {action}".format_map(inigo)
'Hello, my name is Bob. You killed my hamster. Prepare to take a nap'
```

---

### `index`

Returns the index of a substring within a string.

```python
>>> "Three is a magic number".index("ee")
3
```

:::note
The `index` method only returns the first occurance of the substring.
:::

---

### `isalnum`

Returns `True` if a string is all alpha-numeric or `False` if it's not. Spaces are not considered alpha-numeric.

```python
>>> "My username is SytaxTerror12".isalnum()
False

>>> "SytaxTerror12".isalnum()
True

>>> "Hello World!!!".isalnum()
False
```

---

### `isalpha`

Returns `True` if a string is completely alphabetic, other wise returns `False`. This is not limited to Latin based languages. 

```python
>>> "Hello".isalpha()
True

>>> "你好".isalpha()
True

>>> "שלום".isalpha()
True

>>> "مرحبا".isalpha()
True

>>> "Üdvözlöm".isalpha()
True

>>> "Hello!!!".isalpha()
False
```

---

### `isascii`

```python
>>> '(^_^) [o_o] (^.^)  (".") ($.$)'.isascii()
True

>>> "😊😳😙😮🤑".isascii()
False
```

---

### `isdecimal`

```python
>>> "1".isdecimal()
True

>>> "12".isdecimal()
True

>>> "one".isdecimal()
False

>>> "one 2".isdecimal()
False

# exponent
>>> "²".isdecimal()
False

# unicode 0
>>> "\u0030".isdecimal()
True
```

---

### `isdigit`

```python
>>> "1".isdigit()
True

>>> "12".isdigit()
True

>>> "one".isdigit()
False

>>> "one 2".isdigit()
False

# exponent
>>> "²".isdigit()
True

# unicode 0
>>> "\u0030".isdigit()
True
```



---

### `isidentifier`

Returns `True` if the value is suitable for being an identifier (aka a variable name).

```python
>>> "wolf".isIdentifier()
True

>>> "MeaningOfLife42".isIdentifier()
True

>>> "chicken nugget".isIdentifier()
False

>>> "2pac".isIdentifier()
False

>>> "python-code".isIdentifier()
False
```


---

### `islower`

Returns `True` if all letters in the string a lower case, otherwise returns `False`.

```python
>>> "hi".islower()
True

>>> "Hi".islower()
False

>>> "hi!".islower()
True
```


---

### `isnumeric`

Returns `True` if the string is a numeric value, otherwise returns `False`. Operators such as `+`, `-`, `*`, `/`, are not numeric and therefore will return `False`. However, fractions and exponents will return `True`.


```Python
>>> "1".isnumeric()
True

>>> "1.7".isnumeric()
False

>>> "½".isnumeric()
True

>>> "²".isnumeric()
True

# 0 in unicode
>>> "\u0030".isnumeric()
True
```


---

### `isprintable`

Returns `True` if all of the characters in a string are printable, otherwise returns `False`. Strings with backslash, such as new line `\n` or tab `\t`, or strings with unassigned unicode will return `False`

```python
>>> "Chicken Nuggets!".isprintable()
True

>>> "1234".isprintable()
True

>>> "😀".isprintable()
True

>>> " ".isprintable()
True

>>> "\b".isprintable()
False

>>> "\x1b".isprintable()
False

>>> "\u200b".isprintable()
False
```

---

### `isspace`

Returns `True` if the string is a space, otherwise returns `False`

```python
>>> "    ".isspace()
True

>>> " ".isspace()
True

>>> "chicken nuggets".isspace()
False

>>> "chickennuggets".isspace()
False
```

---

### `istitle`

Returns `True` if the string is in title case, otherwise returns `False`

```python
>>> "Chicken Nuggets".istitle()
True

>>> "Chicken nuggets".istitle()
False

>>> "chicken nuggets".istitle()
False

>>> "nugs".istitle()
False

>>> "Nugs".istitle()
True
```

---

### `isupper`

Returns `True` if the string is upper case, otherwise returns `False`.

```python
>>> "CHICKEN".isupper()
True

>>> "24 CHICKEN NUGGETS".isupper()
True

>>> "CHICKEN nuggets".isupper()
False

>>> "chicken nuggets".isupper()
False
```

---

### `join`

Takes all of the items in an iterable sequence and joins them into a single string.

```python
>>> "Duck".join(("Chicken", "Monkey"))
'ChickenDuckMonkey'

>>> "Duck".join(["Chicken", "Monkey"])
'ChickenDuckMonkey'

>>> "Duck".join({"bird": "Chicken", "primate": "Monkey"})
'birdDuckprimate'
```

---

### `ljust`

Returns a left adjugested string padded with the indicated number of spaces.

```python
>>> "chicken".ljust(20)
'chicken             '

>>> "chicken".ljust(5)
'chicken'
```

---

### `lower`

Returns a string to lower case.

```python
>>> "HeLlO wOrLd!".lower()
'hello world!'
```

---

### `lstrip`

Removes leading white space.

```python
>>> "     Hello there!".lstrip()
'Hello there!'
```

---

### `maketrans`

Translates a particular character's ascii code into another. See [`translate`](#translate) for more information.

```python
>>> "Bake sale".translate(str.maketrans("B", "F"))
'Fake sale'

>>> "Bake sale".translate(str.maketrans("a", "i"))
'Bike sile'
```

---

### `partition`

Returns a tuple with 3 elements. All of the strings before the first occurance of the match, the match itself, and everything after the match. 

```python
>>> "Make it so".partition("it")
('Make ', 'it', ' so')
```

---

### `removeprefix`

Removes the indicated beginning of a string. If the indicated string is not at the begining no transformation will occur.

```python
>>> "algorhythm".removeprefix("algo")
'rhythm'

>>> "algorhythm".removeprefix("go")
'algorhythm'
```

---

### `removesuffix`

Removes the indicated end of string. If the indicated string is not at the end no transformation will occur.


```python
>>> "algorhythm".removesuffix("rhythm")
'algo'

>>> "algorhythm".removesuffix("rhy")
'algorhythm'
```


---

### `replace`

Replaces all occurances of a substring within a string with another.


```python
>>> "alfalfa farm".replace("a", "g")
'glfglfg fgrm'

>>> "alfalfa farm".replace("alfalfa", "soul")
'soul farm'
```

---

### `rfind`

Returns the index of the last occurance of a substring within a string. Returns `-1` if the matching substring is not found.

```python
>>> "to be or not to be".rfind("be")
16

>>> "to be or not to be".rfind("to")
13

>>> "to be or not to be".rfind("42")
-1
```


---

### `rindex`


Returns the index of the last occurance of a substring within a string. Raises a `ValueError` if the matching substring is not found.

```python
>>> "to be or not to be".rindex("be")
16

>>> "to be or not to be".rindex("to")
13

>>> "to be or not to be".rindex("42")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
```

---

### `rjust`

Returns a right adjugested string padded with the indicated number of spaces.


```python
>>> "nuggets".rjust(20)
'             nuggets'
```


---

### `rpartition`

Returns a tuple with 3 elements. All of the strings before the last occurance of the match, the match itself, and everything after the match. 

```python
>>> "Make it so, so it will be".rpartition("it")
('Make it so, so ', 'it', ' will be')
```

---

### `rsplit`

Returns a list of the string based on the delimiter. The default delimiter is a space `" "`. This is only different from [`split`](#split) when the `maxsplit` parameter is used, in which case `rsplit` will split starting from the right side. The second `maxsplit` parameter indicates how many times the string will be split.

```python
>>> "guitar bass drums".rsplit()
['guitar', 'bass', 'drums']

>>> "guitar, bass, drums".rsplit(",")
['guitar', ' bass', ' drums']

>>> "guitar, bass, drums".rsplit(",", 1)
['guitar, bass', ' drums']
```
---

### `rstrip`

Returms the given string with trailing whitespace removed.

```python
>>> "heehaw           ".rstrip()
'heehaw'
```

---

### `split`

Returns a list of the string based on the delimiter. The default delimiter is a space `" "`. This is only different from [`rsplit`](#rsplit) when the `maxsplit` parameter is used, in which case `split` will split starting from the left side. The second `maxsplit` parameter indicates how many times the string will be split.


```python
>>> "guitar bass drums".split()
['guitar', 'bass', 'drums']

>>> "guitar, bass, drums".split(",")
['guitar', ' bass', ' drums']

>>> "guitar, bass, drums".split(",", 1)
['guitar', ' bass, drums']
```

---

### `splitlines`

Returns a list of the string split along new lines `\n`.


```python
>>> "There are\nbunch of lines".splitlines()
['There are', 'bunch of lines']
```

---

### `startswith`

Returns `True` if the string begins with the indicated substring, otherwise returns `False`.

```python
>>> "to be or not to be".startswith("t")
True

>>> "to be or not to be".startswith("to")
True

>>> "to be or not to be".startswith("be")
False
```

---

### `strip`

Returns the given string with leading and trailing whitespace removed.

```python
>>> "         hello        there              ".strip()
'hello        there'
```

---

### `swapcase`

Returns a new string where all of the uppercased letters from the original are lowercased, and all of the lowercased letters from the original are uppercased.

```python
>>> "Bob had a hamster named Jack".swapcase()
'bOB HAD A HAMSTER NAMED jACK'
```

---

### `title`

Returns the original string formatted in title case.

```python
>>> "this is the greatest title in the universe... tribute".title()
'This Is The Greatest Title In The Universe... Tribute'

>>> "THIS IS THE GREATEST TITLE IN THE UNIVERSE... TRIBUTE".title()
'This Is The Greatest Title In The Universe... Tribute'
```

---

### `translate`

Returns a string where the indicated substrings are swapped based on their ascii codes.

```python
>>> # swap "a" for "e"
>>> "bass guitar".translate({97: 101})
'bess guiter'
```

---

### `upper`

Returns a string where all letters are transformed to uppercase.

```python
>>> "lowercase".upper()
'LOWERCASE'
```

---

### `zfill`

Returns a new string that fills the beginning of the original with zeros `0` until the specified length has been reached.

```python
>>> "long enough?".zfill(25)
'0000000000000long enough?'
```

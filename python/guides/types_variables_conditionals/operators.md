---
title: Operators
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
## What are operators?

**Operators** are special symbols that perform operations on values. You've already used some operators like `+` for addition and `==` for comparison. Python has many operators for different tasks like doing math, comparing values, and modifying variables.

## Why this matters

Operators are the building blocks of Python expressions. They let you:
- Perform calculations (add, subtract, multiply, divide)
- Compare values (check if something is equal, greater than, etc.)
- Modify variables (increment, decrement, and more)
- Combine conditions (using `and`, `or`, `not`)

Understanding operators is essential for writing any useful Python code. You'll use them constantly, from simple math to complex conditionals.

## Arithmetic operators

Arithmetic operators perform mathematical operations on numbers:

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `10 - 4` | `6` |
| `*` | Multiplication | `3 * 4` | `12` |
| `/` | Division | `10 / 2` | `5.0` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |
| `**` | Exponentiation | `2 ** 3` | `8` |

### Basic arithmetic

```python
>>> 5 + 3
8

>>> 10 - 4
6

>>> 3 * 4
12

>>> 10 / 2
5.0
```

Notice that division (`/`) always returns a float (decimal number), even if the result is a whole number.

### Floor division and modulo

**Floor division** (`//`) divides and rounds down to the nearest whole number:

```python
>>> 10 // 3
3

>>> 7 // 2
3
```

**Modulo** (`%`) gives you the remainder after division:

```python
>>> 10 % 3
1    # 10 divided by 3 is 3 with remainder 1

>>> 7 % 2
1    # 7 divided by 2 is 3 with remainder 1

>>> 8 % 2
0    # 8 divided by 2 is 4 with no remainder
```

Modulo is useful for checking if a number is even or odd:
- If `number % 2 == 0`, the number is even
- If `number % 2 == 1`, the number is odd

### Exponentiation

The `**` operator raises a number to a power:

```python
>>> 2 ** 3
8    # 2 to the power of 3 = 2 × 2 × 2

>>> 5 ** 2
25   # 5 to the power of 2 = 5 × 5

>>> 10 ** 0
1    # Any number to the power of 0 is 1
```

## Comparison operators

Comparison operators compare two values and return `True` or `False`. You've already seen these in [conditionals](./conditionals):

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 10` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |

```python
>>> 5 == 5
True

>>> 5 != 3
True

>>> 5 > 3
True

>>> 5 < 10
True

>>> 5 >= 5
True

>>> 5 <= 5
True
```

:::important
**Remember:** `==` checks if values are equal, while `=` assigns a value to a variable. These are different!
- `x = 5` means "assign 5 to x"
- `x == 5` means "is x equal to 5?"
:::

## Assignment operators

Assignment operators combine assignment (`=`) with an operation. They're shortcuts for common operations.

### Basic assignment

The `=` operator assigns a value to a variable:

```python
x = 5
y = 10
```

### Augmented assignment operators

These operators perform an operation and assign the result back to the variable:

| Operator | Equivalent to | Example |
|----------|---------------|---------|
| `+=` | `x = x + y` | `x += 5` |
| `-=` | `x = x - y` | `x -= 3` |
| `*=` | `x = x * y` | `x *= 2` |
| `/=` | `x = x / y` | `x /= 2` |
| `//=` | `x = x // y` | `x //= 3` |
| `%=` | `x = x % y` | `x %= 3` |
| `**=` | `x = x ** y` | `x **= 2` |

### Examples

```python
# Instead of writing:
count = 5
count = count + 1
print(count)  # 6

# You can write:
count = 5
count += 1
print(count)  # 6

# More examples:
x = 10
x += 5    # x is now 15 (same as x = x + 5)
x -= 3    # x is now 12 (same as x = x - 3)
x *= 2    # x is now 24 (same as x = x * 2)
x /= 4    # x is now 6.0 (same as x = x / 4)
```

These operators are especially useful when you need to modify a variable's value. They're shorter and often clearer than writing the full assignment.

## Logical operators

Logical operators work with boolean values (`True` and `False`) and truthiness. You will see more on these in [conditionals](./conditionals) and [truthiness](./truthiness).

| Operator | Name | Example | Result |
|----------|------|---------|--------|
| `and` | Logical AND | `True and False` | `False` |
| `or` | Logical OR | `True or False` | `True` |
| `not` | Logical NOT | `not True` | `False` |

```python
>>> True and True
True

>>> True and False
False

>>> True or False
True

>>> not True
False
```

These operators work with truthiness too:

```python
>>> "hello" and "world"
"world"

>>> "" or "default"
"default"

>>> not ""
True
```

You'll learn more about how these work with truthiness in the [truthiness guide](./truthiness).

## Operator precedence

When Python evaluates an expression with multiple operators, it follows a specific order (called "precedence"). This is similar to math order of operations.

```python
>>> 2 + 3 * 4
14    # Not 20! Multiplication happens first: 3 * 4 = 12, then 2 + 12 = 14
```

You can use parentheses to control the order:

```python
>>> (2 + 3) * 4
20    # Parentheses force addition first: 2 + 3 = 5, then 5 * 4 = 20
```

**General order (from highest to lowest precedence):**
1. Parentheses `()` - highest priority
2. Exponentiation `**`
3. Multiplication, Division, Floor division, Modulo `*`, `/`, `//`, `%`
4. Addition, Subtraction `+`, `-`
5. Comparison operators `==`, `!=`, `>`, `<`, `>=`, `<=`
6. Logical operators `not`, `and`, `or`

When in doubt, use parentheses to make your intent clear!

## Common patterns

### Incrementing and decrementing

```python
count = 0
count += 1    # Increment by 1
count += 1    # Increment by 1 again
print(count)  # 2

count -= 1    # Decrement by 1
print(count)  # 1
```

### Checking ranges

```python
age = 25

if age >= 18 and age <= 65:
    print("Working age")
```

### Calculating with variables

```python
price = 10.50
quantity = 3
total = price * quantity
print(total)  # 31.5
```

## Best practices

1. **Use parentheses for clarity**: Even if you know the precedence rules, parentheses make your code easier to read:
   ```python
   # Clear - shows the intended grouping
   result = (a * b) + (c * d)
   
   # Less clear (but correct) - same result due to operator precedence
   result = a * b + c * d
   ```

2. **Use augmented assignment when appropriate**: `x += 1` is clearer than `x = x + 1` when you're modifying a variable.

3. **Be careful with division**: Remember that `/` always returns a float. If you need an integer, use `//` (floor division).

4. **Use `==` for comparison, `=` for assignment**: Don't mix these up!

## Operations between different types

When you use operators with different types, Python's behavior depends on the types involved. Some operations work, some don't, and some require type conversion.

### What works

**String concatenation and repetition:**
```python
>>> "Hello" + " " + "World"
"Hello World"

>>> "Hi" * 3
"HiHiHi"
```

**Numeric operations with mixed number types:**
```python
>>> 5 + 3.5
8.5    # int + float = float

>>> 10 * 2.5
25.0   # int * float = float
```

Python automatically converts integers to floats when needed.

**Comparisons between compatible types:**
```python
>>> 5 == 5.0
True    # Python compares the values, not the types

>>> "5" == 5
False   # String "5" is not equal to integer 5
```

### What doesn't work

**Arithmetic between incompatible types:**
```python
>>> 5 + "hello"
Traceback (most recent call last):
  ...
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

You can't add a number to a string. Python doesn't know how to combine them.

**Other incompatible operations:**
```python
>>> 10 - "5"
TypeError: unsupported operand type(s) for -: 'int' and 'str'

>>> "hello" * "world"
TypeError: can't multiply sequence by non-int of type 'str'
```

### Converting types for operations

If you need to perform operations between different types, convert them first:

```python
# Convert string to number for math
>>> age_str = "25"
>>> age = int(age_str)
>>> age + 5
30

# Convert number to string for concatenation
>>> age = 25
>>> message = "I am " + str(age) + " years old"
>>> message
"I am 25 years old"
```

**Common conversions:**
- `int(value)` - Convert to integer
- `float(value)` - Convert to float
- `str(value)` - Convert to string

```python
>>> int("42")
42

>>> float("3.14")
3.14

>>> str(42)
"42"
```

### String operations

Strings have some special behaviors with operators:

**Concatenation (`+`):**
```python
>>> "Hello" + "World"
"HelloWorld"

>>> "Hello" + " " + "World"
"Hello World"
```

**Repetition (`*`):**
```python
>>> "Hi" * 3
"HiHiHi"

>>> "-" * 10
"----------"
```

**Note:** You can only use `*` with a string and an integer (not two strings).

### Comparison between types

Python can compare some different types, but the results might surprise you:

```python
>>> 5 == 5.0
True    # Numeric values are compared

>>> "5" == 5
False   # String and number are different types

>>> "apple" < "banana"
True    # Strings are compared alphabetically

>>> "10" < "2"
True    # String comparison! "1" comes before "2" alphabetically
```

:::warning
When comparing strings that look like numbers, Python compares them as text, not as numbers. `"10" < "2"` is `True` because "1" comes before "2" in alphabetical order. To compare as numbers, convert them first: `int("10") < int("2")` is `False`.
:::

### Best practices

1. **Convert types explicitly when needed**: Don't rely on Python to guess what you want. Convert strings to numbers (or vice versa) before operations.

2. **Be careful with string comparisons**: If you're comparing numbers stored as strings, convert them first.

3. **Use `str()` for string formatting**: When combining numbers with strings, convert numbers to strings first:
   ```python
   # Good
   message = "I have " + str(count) + " items"
   
   # Error
   message = "I have " + count + " items"  # TypeError!
   ```

4. **Check types if unsure**: Use `type()` or `isinstance()` to check types before operations if you're not sure what type a value is.

## Summary

Operators are essential tools in Python:

- **Arithmetic operators**: `+`, `-`, `*`, `/`, `//`, `%`, `**` - for math operations
- **Comparison operators**: `==`, `!=`, `>`, `<`, `>=`, `<=` - for comparing values
- **Assignment operators**: `=`, `+=`, `-=`, `*=`, etc. - for assigning and modifying values
- **Logical operators**: `and`, `or`, `not` - for combining conditions
- **Operator precedence**: Python evaluates operators in a specific order; use parentheses to control it
- **Type compatibility**: Some operations work between different types (like string concatenation), while others require type conversion

You'll use these operators constantly as you write Python code. Practice with them, and they'll become second nature!

---
title: Conditionals
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
## What are conditionals?

**Conditionals** are statements that let your program make decisions based on values and conditions. Python uses `if`, `elif`, and `else` to control which code runs, allowing your program to respond differently to different situations.

## Why this matters

Conditionals are what make programs intelligent and interactive. Without them, your code would always execute the same way every time. With conditionals, you can check user input, validate data, handle different cases, and create programs that adapt to their environment. Almost every useful program uses conditionals, whether it's checking if a user is logged in, validating input, choosing which calculation to perform, or determining what message to display. Mastering conditionals is essential for writing programs that do more than just execute a fixed sequence of steps.

## Basic syntax

The basic form of a conditional statement looks like this:

```python
if <condition>:
    <code to run>
```

The *condition* is any expression that evaluates to `True` or `False` (or a truthy or falsy value). If the condition is truthy, Python executes the indented block. If it's falsy, Python skips the block and moves on to the next statement.

:::important
**Indentation matters!** The code that runs when the condition is true must be indented (usually 4 spaces). Python uses indentation to know which code belongs to the `if` statement. If you don't indent properly, you'll get an error.
:::


## If statements

The simplest conditional runs code only when a condition is truthy:

```python
age = 18

if age >= 18:
    print("You are an adult")
```

This checks if `age` is greater than or equal to 18. If it is, Python prints the message. Notice the indentation! The `print()` statement is indented to show it belongs to the `if` statement.

If the condition is falsy, nothing happens—Python skips the indented block entirely:

```python
age = 15

if age >= 18:
    print("You are an adult")  # This won't print because age is 15

print("This always prints")  # This runs regardless of the if statement
```

## `if` / `else`

Add `else` to provide an alternative when the condition is falsy:

```python
age = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

## `if` / `elif` / `else`

Use `elif` (short for "else if") to check multiple conditions in order:

```python
score = 85

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

**How it works:**
1. Python checks the first `if` condition (`score >= 90`). If it's true, it runs that block and stops.
2. If the first condition is false, Python checks the first `elif` (`score >= 80`). If it's true, it runs that block and stops.
3. This continues for each `elif`.
4. If none of the conditions are true, Python runs the `else` block (if there is one).

In the example above, `score` is 85, so:
- `score >= 90` is false (85 is not >= 90)
- `score >= 80` is true (85 is >= 80)
- Python prints "Grade: B" and stops. It skips over the remaining conditions.

**Important:** Only one block runs, even if multiple conditions could be true. **Python always uses the first matching condition**.

## Truthiness in conditionals

Python evaluates conditions based on truthiness (which you learned about in the [truthiness guide](./truthiness)). This means you can use any value in a condition, not just `True` or `False`.

These values are **falsy** (treated as `False`):
- `False`
- `None`
- `0` (or `0.0`)
- Empty collections: `""`, `[]`, `{}`, `set()`, `()`

Everything else is **truthy** (treated as `True`).

```python
name = "Alice"

if name:  # Non-empty string is truthy, so this runs
    print(f"Hello, {name}")

items = []

if items:  # Empty list is falsy, so this doesn't run
    print("List has items")
else:
    print("List is empty")  # This runs instead
```

This is why you can write `if name:` instead of `if name != "":`. This makes your code shorter and more Pythonic!

## Comparison operators

Use comparison operators to build conditions that compare values:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `==` | Equal to | `5 == 5` | `True` |
| `!=` | Not equal to | `5 != 3` | `True` |
| `>` | Greater than | `5 > 3` | `True` |
| `<` | Less than | `5 < 10` | `True` |
| `>=` | Greater than or equal to | `5 >= 5` | `True` |
| `<=` | Less than or equal to | `5 <= 5` | `True` |

```python
x = 5

if x == 5:   # Is x equal to 5? Yes!
    print("x is 5")

if x != 3:   # Is x not equal to 3? Yes!
    print("x is not 3")

if x > 3:    # Is x greater than 3? Yes!
    print("x is greater than 3")
```

These operators return `True` or `False`, which makes them perfect for use in `if` statements.

## Logical operators

Combine conditions with `and`, `or`, and `not`:

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")

if age < 18 or not has_license:
    print("You cannot drive")
```

### `and`

Both conditions must be truthy for the whole expression to be truthy:

```python
x = 5

if x > 0 and x < 10:
    print("x is between 0 and 10")
```

This only prints if **both** `x > 0` is true **and** `x < 10` is true. If either condition is false, nothing prints.

### `or`

At least one condition must be truthy for the whole expression to be truthy:

```python
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend")
```

This prints if the day is Saturday **or** Sunday (or both, though a day can't be both). If neither condition is true, nothing prints.

### `not`

Inverts the truthiness. `True` converts to `False` and `False` to `True`:

```python
is_raining = False

if not is_raining:
    print("Let's go outside")
```

Since `is_raining` is `False`, `not is_raining` is `True`, so the message prints. Think of `not` as asking "is this false?"

## Nested conditionals

You can put `if` statements inside other `if` blocks. This is called "nesting":

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("You can drive")
    else:
        print("You need a license")
else:
    print("You're too young to drive")
```

**How it works:**
1. First, Python checks if `age >= 18`. If true, it goes inside that block.
2. Inside that block, it checks if `has_license` is true.
3. If both are true, it prints "You can drive".
4. If `age >= 18` is false, it skips to the `else` and prints "You're too young to drive".

Notice the double indentation—the inner `if` statement is indented twice because it's inside the outer `if` block.

:::tip
You can often simplify nested conditionals using `and`:
```python
if age >= 18 and has_license:
    print("You can drive")
elif age >= 18:
    print("You need a license")
else:
    print("You're too young to drive")
```
This is usually easier to read than nesting!
:::

## Conditional expressions (ternary operator)

Python supports a compact one-line way to assign a value based on a condition. This is called a "ternary operator" or "conditional expression":

```python
age = 20
status = "adult" if age >= 18 else "minor"
print(status)  # "adult"
```

**Syntax:** `value_if_true if condition else value_if_false`

This is equivalent to the longer version:

```python
if age >= 18:
    status = "adult"
else:
    status = "minor"
```

:::note
This is a more advanced feature. If you find it confusing, stick with the regular `if/else` statements for now. You can always learn this later once you're more comfortable with conditionals.
:::

## Common patterns

### Checking membership

You can check if a value is in a collection using the `in` operator:

```python
color = "red"

if color in ["red", "green", "blue"]:
    print("Primary color")
```

This checks if `color` is one of the values in the list. You'll learn more about lists and the `in` operator in the [iterables section](../iterables/lists).

### Checking type (with `isinstance`)

You can check what type a value is using `isinstance()`:

```python
value = 42

if isinstance(value, int):
    print("It's an integer")
elif isinstance(value, str):
    print("It's a string")
```

`isinstance(value, int)` returns `True` if `value` is an integer, `False` otherwise. This is useful when you need to handle different types of data differently.

### Multiple conditions

Sometimes you want to check more than one thing at a time and handle different combinations of conditions.

```python
temperature = 75
is_sunny = True

if temperature > 70 and is_sunny:
    print("Perfect weather for a picnic")
elif temperature > 70:
    print("Warm but cloudy")
elif is_sunny:
    print("Sunny but cool")
else:
    print("Not ideal weather")
```

## Best practices

Here are some tips for writing clear, readable conditionals:

1. **Keep conditions simple**: If a condition is complex, store it in a variable with a clear name:
   ```python
   # Good: Clear and readable
   is_valid = age >= 18 and has_license
   
   if is_valid:
       print("You can drive")
   ```

2. **Use `elif` for mutually exclusive conditions**: If only one condition should be true, use `elif` instead of multiple `if` statements:
   ```python
   # Good: Only one will run
   if score >= 90:
       print("A")
   elif score >= 80:
       print("B")
   
   # Avoid: Multiple could run
   if score >= 90:
       print("A")
   if score >= 80:  # This might also run!
       print("B")
   ```

3. **Avoid deeply nested conditionals**: If you find yourself nesting many `if` statements, consider using `and` to combine conditions:
   ```python
   # Good: Flat structure
   if age >= 18 and has_license and not is_suspended:
       print("You can drive")
   
   # Avoid: Too nested (hard to read)
   if age >= 18:
       if has_license:
           if not is_suspended:
               print("You can drive")
   ```

4. **Use truthiness when it makes sense**: `if name:` is cleaner than `if name != ""`, but use explicit comparisons when the distinction matters (like checking for `None` specifically):
   ```python
    name = "Wolf"

   # Good: uses truthiness
   if name:
       print("Hello,", name)

   # Also good: explicit comparison to None
   if user is not None:
       print("User is set")
   ```

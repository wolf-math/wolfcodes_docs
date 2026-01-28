---
title: Function Basics
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
## What are functions?

**Functions** are reusable blocks of code that perform a specific task. They let you organize your code into logical units, avoid repetition, and make your programs easier to read and maintain. Once defined, a function can be called multiple times with different inputs.

Functions are:
- **Reusable**: Write once, use many times
- **Organized**: Group related code together
- **Parameterized**: Accept input values (arguments) to customize behavior
- **Returning**: Send results back to the caller
- **Named**: Give meaningful names to describe what they do

```python
def greet(name):
    """Return a greeting message."""
    return f"Hello, {name}!"

print(greet("Alice"))  # "Hello, Alice!"
print(greet("Bob"))    # "Hello, Bob!"
```

## Why this matters

Functions are fundamental to writing good Python code. Without functions, you'd repeat the same code over and over, making your programs longer, harder to maintain, and more error-prone. Functions let you break complex problems into smaller, manageable pieces. They make your code more readable. A well-named function like `calculate_total()` is clearer than seeing the calculation code repeated everywhere. Functions also make testing easier since you can test each function independently. Understanding how to create and use functions is essential because almost all Python programs use them, from simple scripts to large applications.

## Defining functions

Use the `def` keyword to define a function, followed by the function name, parentheses with parameters (if any), and a colon. The function body is indented.

### Basic function syntax

```python
def function_name(parameters):
    """Optional docstring describing the function."""
    # Function body
    return value  # Optional: return a value
```

### Simple function example

```python
def say_hello():
    """Print a greeting."""
    print("Hello, world!")

say_hello()  # Calls the function, prints "Hello, world!"
```

### Function with a return value

Functions can return values using the `return` statement:

```python
def add(a, b):
    """Add two numbers and return the result."""
    return a + b

result = add(3, 5)
print(result)  # 8
```

If a function doesn't have a `return` statement (or has `return` without a value), it returns `None`:

```python
def print_sum(a, b):
    """Print the sum but don't return anything."""
    print(a + b)

result = print_sum(3, 5)  # Prints 8
print(result)  # None, because there is no return value
```

## Calling functions

To use a function, write its name followed by parentheses. If the function takes parameters, provide arguments inside the parentheses.

```python
def greet(name):
    return f"Hello, {name}!"

# Call the function with an argument
message = greet("Alice")
print(message)  # "Hello, Alice!"
```

One thing that makes functions great is that they can be called multiple times:

```python
greet("Alice")  # "Hello, Alice!"
greet("Bob")    # "Hello, Bob!"
greet("Charlie")  # "Hello, Charlie!"
```

## Parameters and arguments

**Parameters** are the names listed in the function definition. **Arguments** are the values you pass to the function when you call it. Learn more about [variables](/docs/python/guides/types_variables_conditionals/variables) to understand how parameters work.

### Positional arguments

Positional arguments are passed in order, matching the parameter positions:

```python
def subtract(a, b):
    """Subtract b from a."""
    return a - b

result = subtract(10, 3)  # 10 is assigned to a, 3 to b
print(result)  # 7
```

### Keyword arguments

You can also pass arguments by name using keyword arguments:

```python
def divide(dividend, divisor):
    """Divide dividend by divisor."""
    return dividend / divisor

# Both calls produce the same result
result1 = divide(10, 2)
result2 = divide(dividend=10, divisor=2)
result3 = divide(divisor=2, dividend=10)  # Order doesn't matter with keywords

print(result1, result2, result3)  # 5.0 5.0 5.0
```

Keyword arguments make function calls more readable, especially when functions have many parameters:

```python
def create_user(name, age, email):
    """Create a user with the given information."""
    return {"name": name, "age": age, "email": email}

# Keyword arguments make this clearer
user = create_user(name="Alice", age=30, email="alice@example.com")
```

### Mixing positional and keyword arguments

You can mix positional and keyword arguments, but positional arguments must come before keyword arguments:

```python
def create_user(name, age, email):
    """Create a user with the given information."""
    return {"name": name, "age": age, "email": email}

# Mix positional and keyword
user1 = create_user("Alice", 30, email="alice@example.com")  # First two positional, last keyword
user2 = create_user("Bob", age=25, email="bob@example.com")  # First positional, rest keyword

# This would cause an error:
# create_user(name="Alice", 30, "alice@example.com")  # SyntaxError: positional follows keyword
```

## Default parameters

Default parameters let you make some arguments optional. If a caller doesn't provide a value, the default is used.

### Basic default parameters

Define default values in the function signature using `=`:

```python
def greet(name, greeting="Hello"):
    """Greet someone with an optional custom greeting."""
    return f"{greeting}, {name}!"

print(greet("Alice"))           # "Hello, Alice!" (uses default)
print(greet("Bob", "Hi"))       # "Hi, Bob!" (overrides default)
print(greet("Charlie", greeting="Good morning"))  # "Good morning, Charlie!"
```

### Multiple default parameters

You can have multiple parameters with defaults:

```python
def create_message(name, prefix="Hello", suffix="!", punctuation="."):
    """Create a message with customizable parts."""
    return f"{prefix}, {name}{suffix}{punctuation}"

print(create_message("Alice"))  # "Hello, Alice!."
print(create_message("Bob", "Hi", "?"))  # "Hi, Bob?."
```

### Important: Default parameter values

Default parameter values are evaluated only once when the function is defined, not each time it's called. This is important to understand:

```python
# Good: Use immutable defaults
def add_item(item, items=None):
    """Add an item to a list, creating a new list if needed."""
    if items is None:
        items = []
    items.append(item)
    return items

list1 = add_item("apple")  # ['apple']
list2 = add_item("banana")  # ['banana'] (not ['apple', 'banana'])
```

```python
# Avoid: Mutable defaults can cause unexpected behavior
def add_item_bad(item, items=[]):  # Don't do this!
    items.append(item)
    return items

list1 = add_item_bad("apple")  # ['apple']
list2 = add_item_bad("banana")  # ['apple', 'banana'] (unexpected!)
```

The problem is that Python creates the default list `[]` only once when the function is defined, not each time you call it. This means all function calls share the same list object. When you call `add_item_bad("apple")`, it modifies that shared list. When you call `add_item_bad("banana")` later, it's still working with the same list that already contains "apple", so both items end up in `list2`. This is why `list2` unexpectedly contains both items instead of just "banana".

Additionally, `list1` and `list2` reference the same object, so modifying one (like `list1.append("cherry")`) will also affect the other, which is rarely what you want.

:::warning
Use `None` as a default for mutable parameters (lists, dictionaries, etc.), then create a new one inside the function if needed. This prevents shared state between function calls.
:::

### Parameter order rules

When mixing parameters with and without defaults:
1. Parameters without defaults must come first
2. Parameters with defaults come after
3. You can't have a parameter without a default after one with a default

```python
# Correct order
def example(a, b, c=1, d=2):
    pass

# Incorrect (will cause SyntaxError)
# def bad_example(a=1, b):
#     pass
```

## Docstrings

Docstrings are optional but recommended. They document what a function does:

```python
def calculate_area(length, width):
    """
    Calculate the area of a rectangle.
    
    Args:
        length: The length of the rectangle
        width: The width of the rectangle
    
    Returns:
        The area (length * width)
    """
    return length * width
```

Access a function's docstring with `.__doc__` or `help()`:

```python
print(calculate_area.__doc__)

# Output:
#     Calculate the area of a rectangle.
#     
#     Args:
#         length: The length of the rectangle
#         width: The width of the rectangle
#     
#     Returns:
#         The area (length * width)

help(calculate_area)

# Output):
# Help on function calculate_area in module __main__:
# 
# calculate_area(length, width)
#     Calculate the area of a rectangle.
#     
#     Args:
#         length: The length of the rectangle
#         width: The width of the rectangle
#     
#     Returns:
#         The area (length * width)
```

## Common patterns

### Functions that don't return values

Functions that perform actions (like printing) rather than calculations often don't need to return values:

```python
def print_info(name, age):
    """Print user information."""
    print(f"Name: {name}")
    print(f"Age: {age}")

print_info("Alice", 30)
# Output:
# Name: Alice
# Age: 30

# Functions without a return statement return None
result = print_info("Bob", 25)
print(result)  # None
```

### Functions that return multiple values

Use tuples to return multiple values:

```python
def divide_and_remainder(dividend, divisor):
    """Divide and return both quotient and remainder."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder  # Returns a tuple

q, r = divide_and_remainder(17, 5)
print(f"17 ÷ 5 = {q} remainder {r}")  # "17 ÷ 5 = 3 remainder 2"
```

This works because Python automatically packs multiple return values into a tuple, and you can unpack them when calling.

### Early returns

Use early returns to simplify conditional logic:

```python
def is_positive(number):
    """Check if a number is positive."""
    if number <= 0:
        return False
    return True

# Simpler than:
# def is_positive(number):
#     if number > 0:
#         return True
#     else:
#         return False
```

## Best practices

- **Use descriptive names**: Function names should clearly describe what they do (e.g., `calculate_total()` not `calc()`)
- **Keep functions focused**: Each function should do one thing well
- **Use default parameters wisely**: Make frequently-used values defaults
- **Document with docstrings**: Especially for functions that might be reused
- **Avoid mutable defaults**: Use `None` and create new objects inside the function
- **Return values consistently**: If a function can return different types, document it clearly
- **Keep functions reasonably short**: If a function is too long, consider breaking it into smaller functions

```python
# Good: Clear, focused, documented
def calculate_discount(price, discount_percent=10):
    """
    Calculate the discounted price.
    
    Args:
        price: Original price
        discount_percent: Discount percentage (default: 10)
    
    Returns:
        Discounted price
    """
    discount = price * (discount_percent / 100)
    return price - discount

# Avoid: Unclear name, no documentation, too many responsibilities
def calc(p, d=10):
    # Does calculation and also prints - mixed concerns
    result = p - (p * d / 100)
    print(result)
    return result
```

## Summary

Functions let you organize code into reusable, well-named blocks. They accept parameters (with optional defaults) and can return values. Understanding how to define and call functions with positional and keyword arguments is essential for writing clean, maintainable Python code. Use default parameters to make functions more flexible, but be careful with mutable defaults, use `None` instead.

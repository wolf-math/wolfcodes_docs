---
title: First Class Functions
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
This guide explores what "first-class functions" actually means in Python and how they work under the hood. For practical examples of using functions as arguments and return values, see the [guide on higher-order functions](../../guides/functions/higher_order_functions).

Python learners use this before they understand it. You've passed functions to `map()`, stored functions in variables, and used decorators, but you may not have thought deeply about what's actually happening. This guide explores the mechanics behind these patterns.

## Functions as objects

In Python, functions are objects. This isn't just a metaphor or convenient abstraction. Functions are literally instances of a class, just like strings, lists, and dictionaries.

### What this means

When you define a function with `def`, Python creates a function object and binds it to a name:

```python
def greet(name):
    return f"Hello, {name}!"

# greet is a variable that holds a function object
print(type(greet))  # <class 'function'>
print(greet)        # <function greet at 0x...>
```

The name `greet` is just a variable that references a function object. There's nothing special about it. You can see this by checking its type, examining its attributes, or reassigning the name:

```python
def greet(name):
    return f"Hello, {name}!"

# Functions have attributes, just like other objects
print(greet.__name__)   # 'greet'
print(greet.__doc__)    # None (or docstring if present)

# The name is just a reference
original_greet = greet
def greet(name):
    return f"HI, {name}!"

print(original_greet("Alice"))  # "Hello, Alice!"
print(greet("Alice"))            # "HI, Alice!"
```

Because functions are objects, they exist in memory independently of their names. You can have multiple names pointing to the same function, or lose the original name entirely:

```python
def calculate(x):
    return x * 2

# Multiple references to the same function object
calc = calculate
compute = calculate

print(calc is compute)      # True (same object)
print(calc is calculate)    # True (same object)

# You can even delete the original name
del calculate
print(calc(5))              # 10 (still works!)
# print(calculate(5))       # NameError: name 'calculate' is not defined
```

### Why this matters

Understanding that functions are objects helps explain why you can:

- **Store them**: Variables can hold function objects just like they hold strings or numbers
- **Pass them**: Function objects can be passed as arguments like any other value
- **Return them**: Functions can create and return function objects
- **Put them in collections**: Lists, dictionaries, and other containers can hold function objects

This is what makes Python's "first-class functions" work. Functions aren't special syntax—they're just objects with a `__call__` method that makes them callable.

## Passing, returning, and storing functions

Because functions are objects, you can manipulate them like any other value. Let's explore the mechanics of these operations.

### Passing functions as arguments

When you pass a function as an argument, you're passing a reference to the function object:

```python
def apply(func, value):
    """Call func with value and return the result."""
    return func(value)  # func is just a variable holding a function object

def double(x):
    return x * 2

result = apply(double, 5)
print(result)  # 10
```

Here's what happens:

1. `double` is a name that references a function object
2. When you call `apply(double, 5)`, the function object is passed (not called)
3. Inside `apply`, the parameter `func` receives a reference to the same function object
4. `func(value)` calls the function through that reference

You can verify this by checking object identity:

```python
def apply(func, value):
    print(f"func is {func}")
    print(f"func's id: {id(func)}")
    return func(value)

def double(x):
    return x * 2

print(f"double's id: {id(double)}")
result = apply(double, 5)
# Output shows the same id—it's the same object
```

### Returning functions

Functions can create and return other functions. The returned function is just an object like any other:

```python
def make_multiplier(factor):
    """Create and return a function that multiplies by factor."""
    def multiply(x):
        return x * factor
    return multiply  # Returns the function object, doesn't call it

by_2 = make_multiplier(2)  # by_2 is now a function object
print(by_2(5))             # 10
```

Here's what's happening:

1. `make_multiplier(2)` is called, creating a new frame
2. Inside that frame, `multiply` is defined as a function
3. `multiply` is returned as a function object (not called)
4. The returned function object is assigned to `by_2`
5. Later, `by_2(5)` calls the returned function

The key insight: `make_multiplier` returns a function object, not a result. You call the returned function later.

### Storing functions

Functions can be stored in variables, lists, dictionaries, and other data structures:

```python
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

# Store in variables
operation = add
print(operation(5, 3))  # 8

# Store in a list
operations = [add, subtract, multiply]
for op in operations:
    print(op(10, 2))  # 12, 8, 20

# Store in a dictionary
math_ops = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply
}
result = math_ops['multiply'](4, 5)
print(result)  # 20
```

Again, these are just references to function objects. The functions don't change when you store them—you're just keeping references to the same objects.

## Function attributes

Function objects have attributes that store metadata about the function. These attributes are accessible just like attributes on any other object.

### Common function attributes

```python
def example(x, y=10):
    """This is a docstring."""
    return x + y

# Name and documentation
print(example.__name__)    # 'example'
print(example.__doc__)     # 'This is a docstring.'

# Function signature information
print(example.__code__)           # <code object example at 0x...>
print(example.__code__.co_varnames)  # ('x', 'y')
print(example.__code__.co_argcount)  # 2

# Default values
print(example.__defaults__)       # (10,)
print(example.__kwdefaults__)     # None

# Annotations (if used)
print(example.__annotations__)    # {} (or dict with type hints)
```

### Why attributes matter

Function attributes are used by Python's introspection system. Tools like `help()`, `inspect`, and decorators use these attributes:

```python
def documented_function(x):
    """A well-documented function."""
    return x * 2

# help() uses __doc__
help(documented_function)

# You can inspect the function
import inspect
print(inspect.signature(documented_function))
print(inspect.getdoc(documented_function))
```

### Adding custom attributes

Since functions are objects, you can add your own attributes to them:

```python
def process(data):
    return data.upper()

# Add metadata
process.version = "1.0"
process.author = "Alice"

print(process.version)  # "1.0"
print(process.author)   # "Alice"
```

This is rarely necessary, but it demonstrates that functions are just objects—you can attach attributes like any other object.

## Closures and free variables

When a function is defined inside another function, the inner function can "remember" variables from the outer function's scope. This mechanism is called a **closure**.

### What is a closure?

A closure is a function that remembers values from its enclosing scope even after that scope has finished executing:

```python
def make_multiplier(factor):
    """Create a function that multiplies by factor."""
    def multiply(x):
        return x * factor  # factor comes from the outer scope
    return multiply

by_3 = make_multiplier(3)
print(by_3(5))  # 15
```

Here's what's happening:

1. `make_multiplier(3)` creates a new frame with `factor = 3`
2. Inside that frame, `multiply` is defined
3. `multiply` references `factor`, which exists in the outer frame
4. `multiply` is returned, and `make_multiplier`'s frame ends
5. Yet `by_3` still has access to `factor = 3` when called later

### Free variables

Variables referenced in a function but not defined there are called **free variables**. In `multiply`, `factor` is a free variable because it's not defined in `multiply`'s scope—it comes from `make_multiplier`.

Python automatically captures free variables in a closure:

```python
def outer():
    x = 10
    y = 20
    
    def inner():
        return x + y  # x and y are free variables
    
    return inner

func = outer()
print(func())  # 30 (x and y are captured in the closure)
```

You can inspect what variables a function captures:

```python
def make_multiplier(factor):
    def multiply(x):
        return x * factor
    return multiply

by_3 = make_multiplier(3)
print(by_3.__closure__)           # (<cell at 0x...: int object at 0x...>,)
print(by_3.__code__.co_freevars)  # ('factor',)
```

### Why closures matter

Closures enable powerful patterns:

**Function factories**: Create functions with preset parameters

```python
def make_validator(min_val, max_val):
    """Create a validator function for a range."""
    def validate(value):
        return min_val <= value <= max_val
    return validate

age_validator = make_validator(0, 120)
print(age_validator(25))   # True
print(age_validator(150))  # False
```

**Stateful functions**: Functions that remember state between calls

```python
def make_counter():
    count = 0
    
    def counter():
        nonlocal count
        count += 1
        return count
    
    return counter

c1 = make_counter()
c2 = make_counter()
print(c1())  # 1
print(c1())  # 2
print(c2())  # 1 (separate counter with its own state)
```

**Configuration**: Capture configuration in closures

```python
def make_logger(level):
    """Create a logger with a specific level."""
    def log(message):
        print(f"[{level}] {message}")
    return log

error_log = make_logger("ERROR")
info_log = make_logger("INFO")

error_log("Something went wrong")  # [ERROR] Something went wrong
info_log("Everything is fine")     # [INFO] Everything is fine
```

### The closure capture gotcha

Closures capture variables by reference, not by value. This can cause unexpected behavior in loops:

```python
# Problem: all functions see the final value of i
functions = []
for i in range(3):
    functions.append(lambda: i)

print([f() for f in functions])  # [2, 2, 2] (all see i=2)

# Solution: capture the value using a default argument
functions = []
for i in range(3):
    functions.append(lambda i=i: i)  # i=i captures the current value

print([f() for f in functions])  # [0, 1, 2] (correct)
```

The issue: all lambdas capture the same variable `i`. By the time they're called, `i` has its final value. Using `i=i` creates a new parameter that captures the value at definition time.

### Closures vs. nonlocal

When you need to modify a captured variable, use `nonlocal`:

```python
def make_counter():
    count = 0  # Captured variable
    
    def increment():
        nonlocal count  # Allows modification
        count += 1
        return count
    
    return increment
```

Without `nonlocal`, Python would create a new local variable instead of modifying the captured one.

## Summary

- **Functions are objects**: They're instances of the `function` class, not special syntax. You can manipulate them like any other object.
- **Passing/returning/storing**: These operations work because functions are objects. You're passing references to function objects, not special function syntax.
- **Function attributes**: Functions have metadata stored as attributes (`__name__`, `__doc__`, `__code__`, etc.) that you can inspect and modify.
- **Closures**: Functions can capture variables from their enclosing scope, allowing function factories, stateful functions, and powerful abstractions.

Understanding these mechanics helps explain why Python's functional programming patterns work. Functions aren't magic—they're objects with a `__call__` method, and closures are Python's way of letting inner functions remember their outer scope.

For practical examples and common patterns, see the [guide on higher-order functions](../../guides/functions/higher_order_functions).

---
title: Parameters
sidebar_position: 2
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What are `*args` and `**kwargs`?

`*args` and `**kwargs` are special syntax in Python that allow functions to accept a variable number of arguments. The `*args` collects extra positional arguments into a tuple, while `**kwargs` collects extra keyword arguments into a dictionary. The names `args` and `kwargs` are just conventions, so you can use any names you want, but the `*` and `**` operators are what make them work.

```python
def example(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)

example(1, 2, 3, name="Alice", age=30)
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}
```

### Naming conventions

While `args` and `kwargs` are just variable names, they're widely used conventions. You can use any names:

```python
def example(*numbers, **options):
    # numbers is a tuple
    # options is a dict
    pass
```

However, using `args` and `kwargs` makes your code more readable to other Python developers.

## Why this matters

`*args` and `**kwargs` give you flexibility when you don't know ahead of time how many arguments a function will receive. They're essential for writing functions that can handle different numbers of inputs, which is common in real-world programming. For example, a function that prints multiple values, a function that processes a variable number of items, or a wrapper function that needs to pass arguments to another function all benefit from using `*args` and `**kwargs`. Understanding these concepts opens up powerful patterns in Python, from decorators to function wrappers to APIs that need to accept flexible input.

## `*args`: Variable positional arguments

The `*args` syntax collects any number of positional arguments into a tuple. The `*` operator unpacks arguments when calling a function, and collects them when defining a function.

### Basic `*args` example

```python
def sum_all(*args):
    """Sum all provided numbers."""
    total = 0
    for num in args:
        total += num
    return total

print(sum_all(1, 2, 3))         # 6
print(sum_all(10, 20, 30, 40))  # 100
print(sum_all(5))               # 5
print(sum_all())                # 0
```

Inside the function, `args` is a tuple containing all the positional arguments passed to the function:

```python
def show_args(*args):
    print(f"Type: {type(args)}")
    print(f"Value: {args}")

show_args(1, 2, 3)
# Type: <class 'tuple'>
# Value: (1, 2, 3)
```

### Combining regular parameters with `*args`

You can mix regular parameters with `*args`. Regular parameters must come before `*args`:

```python
def greet(greeting, *names):
    """Greet multiple people with the same greeting."""
    for name in names:
        print(f"{greeting}, {name}!")

greet("Hello", "Alice", "Bob", "Charlie")
# Hello, Alice!
# Hello, Bob!
# Hello, Charlie!
```

### Unpacking with `*args`

You can also use `*` to unpack a sequence when calling a function:

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
print(add(*numbers))  # 6
# Equivalent to: add(1, 2, 3)
```

This is particularly useful when you have a list or tuple and want to pass its elements as separate arguments:

```python
def multiply(x, y, z):
    return x * y * z

values = [2, 3, 4]
result = multiply(*values)  # 24
```

## `**kwargs`: Variable keyword arguments

The `**kwargs` syntax collects any number of keyword arguments into a dictionary. The `**` operator unpacks keyword arguments when calling a function, and collects them when defining a function.

### Basic `**kwargs` example

```python
def print_info(**kwargs):
    """Print all provided keyword arguments."""
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")
# name: Alice
# age: 30
# city: New York
```

Inside the function, `kwargs` is a dictionary containing all the keyword arguments:

```python
def show_kwargs(**kwargs):
    print(f"Type: {type(kwargs)}")
    print(f"Value: {kwargs}")

show_kwargs(a=1, b=2, c=3)
# Type: <class 'dict'>
# Value: {'a': 1, 'b': 2, 'c': 3}
```

### Combining regular parameters with `**kwargs`

You can mix regular parameters with `**kwargs`. Regular parameters and `*args` must come before `**kwargs`:

```python
def create_profile(name, **details):
    """Create a user profile with a name and optional details."""
    profile = {"name": name}
    profile.update(details)
    return profile

user = create_profile("Alice", age=30, city="NYC", role="Developer")
print(user)
# {'name': 'Alice', 'age': 30, 'city': 'NYC', 'role': 'Developer'}
```

### Unpacking with `**kwargs`

You can use `**` to unpack a dictionary when calling a function:

```python
def greet_person(name, age, city):
    return f"{name}, {age}, from {city}"

info = {"name": "Alice", "age": 30, "city": "New York"}
print(greet_person(**info))
# Alice, 30, from New York
```

This is useful when you have a dictionary and want to pass its key-value pairs as keyword arguments:

```python
def configure_app(host, port, debug):
    print(f"Host: {host}, Port: {port}, Debug: {debug}")

config = {"host": "localhost", "port": 8000, "debug": True}
configure_app(**config)
# Host: localhost, Port: 8000, Debug: True
```

## Using *args and `**kwargs` together

You can use both `*args` and `**kwargs` in the same function. The order must be: regular parameters, `*args`, then `**kwargs`:

```python
def example_func(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

example_func("hello", 1, 2, 3, name="Alice", age=30)
# Required: hello
# Args: (1, 2, 3)
# Kwargs: {'name': 'Alice', 'age': 30}
```

### Practical example: Flexible logger

```python
def log(message, *values, level="INFO", **metadata):
    """Log a message with optional values and metadata."""
    print(f"[{level}] {message}")
    if values:
        print(f"  Values: {values}")
    if metadata:
        print(f"  Metadata: {metadata}")

log("Processing started", 1, 2, 3, level="DEBUG", user="Alice", task="import")
# [DEBUG] Processing started
#   Values: (1, 2, 3)
#   Metadata: {'user': 'Alice', 'task': 'import'}
```

## Common use cases

### Function wrappers and decorators

:::note
You'll learn about decorators in depth in the coming sections. This example shows how `*args` and `**kwargs` are used with decorators to pass arguments through wrapper functions.
:::

`*args` and `**kwargs` are essential for creating wrapper functions that need to pass arguments to another function:

```python
def log_calls(func):
    """Decorator that logs function calls."""
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@log_calls
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Alice")
# Output:
# Calling greet with args=('Alice',), kwargs={}
# greet returned: Hello, Alice!
# Hello, Alice!

greet("Bob", greeting="Hi")
# Output:
# Calling greet with args=('Bob',), kwargs={'greeting': 'Hi'}
# greet returned: Hi, Bob!
# Hi, Bob!
```


### Flexible API functions

When building APIs or functions that need to accept various optional parameters:

```python
def create_user(username, email, *roles, **profile):
    """Create a user with required info, optional roles, and profile data."""
    user = {
        "username": username,
        "email": email,
        "roles": list(roles),
        "profile": profile
    }
    return user

user = create_user(
    "alice",
    "alice@example.com",
    "admin",
    "editor",
    first_name="Alice",
    last_name="Smith",
    age=30
)

print(user)
# {'username': 'alice', 'email': 'alice@example.com', 
#  'roles': ['admin', 'editor'], 
#  'profile': {'first_name': 'Alice', 'last_name': 'Smith', 'age': 30}}
```

This function takes all the provided information—required username and email, any number of optional roles (via `*roles`), and any additional profile data (via `**profile`), and returns a structured dictionary containing all of that information about the person. The `*roles` collects any number of role strings into a list, while `**profile` collects any keyword arguments into a profile dictionary, allowing the function to accept flexible combinations of user data.

### Forwarding arguments

Passing arguments from one function to another without knowing what they are:

```python
def process_data(data, *args, **kwargs):
    """Process data and forward extra arguments to format_output."""
    processed = data.upper()
    return format_output(processed, *args, **kwargs)

def format_output(text, prefix="", suffix="", style="normal"):
    """Format output text with optional prefix, suffix, and style."""
    return f"{prefix}{text}{suffix}"

result = process_data("hello", prefix=">>> ", suffix=" <<<")
print(result)  # >>> HELLO <<<
```

## Important notes

### Parameter order matters

When using `*args` and `**kwargs` together, the order must be:

1. Regular positional parameters
2. `*args`
3. Regular keyword-only parameters (if any)
4. `**kwargs`

```python
# Correct order
def correct(required, *args, keyword_only=None, **kwargs):
    pass

# This would cause a SyntaxError
# def wrong(required, **kwargs, *args):
#     pass
```

### Empty *args and **kwargs

Both `*args` and `**kwargs` can be empty:

```python
def example(*args, **kwargs):
    print(f"Args: {args}")      # Empty tuple: ()
    print(f"Kwargs: {kwargs}")  # Empty dict: {}

example()  # Both are empty
```

### Mixing with default parameters

You can combine default parameters with `*args` and `**kwargs`:

```python
def example(a, b=10, *args, c=20, **kwargs):
    print(f"a={a}, b={b}, args={args}, c={c}, kwargs={kwargs}")

example(1, 2, 3, 4, c=30, d=40)
# a=1, b=2, args=(3, 4), c=30, kwargs={'d': 40}
```

## Common pitfalls

### Forgetting to unpack

When calling a function with `*args` or `**kwargs`, remember to unpack:

```python
def add(a, b, c):
    return a + b + c

numbers = [1, 2, 3]
# Wrong - passes the list as a single argument
# add(numbers)  # TypeError

# Correct - unpacks the list
add(*numbers)  # 6
```

### Keyword arguments in `*args`

Keyword arguments that don't match parameter names go to `**kwargs`, not `*args`:

```python
def example(*args, **kwargs):
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

example(1, 2, 3, x=10, y=20)
# Args: (1, 2, 3)
# Kwargs: {'x': 10, 'y': 20}
```

### Modifying *args or **kwargs

Since `*args` is a tuple (immutable), you can't modify it directly. `**kwargs` is a dictionary (mutable), so you can modify it:

```python
def example(*args, **kwargs):
    # args[0] = 99  # TypeError: tuples are immutable
    kwargs['new_key'] = 'new_value'  # OK: dicts are mutable
    return args, kwargs
```

---
title: Dataclasses
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

## What are dataclasses?

**Dataclasses** are a standard-library tool for creating classes that mainly store data. They automatically generate common methods like `__init__` and `__repr__`, so you can write less boilerplate.

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


user = User("Alice", 30)
print(user)  # User(name='Alice', age=30)
```

**What happens:**
1. `@dataclass` tells Python to build extra class behavior for you.
2. The annotated attributes become instance fields.
3. Python automatically creates an `__init__` method.
4. You can create instances without writing that setup code by hand.

Dataclasses are a great fit when your class mostly holds values and only needs a small amount of behavior.

## Why this matters

Regular classes often repeat the same setup code again and again. You define attributes, write `__init__`, and usually want a readable string representation too.

Dataclasses solve that problem by turning a common pattern into a built-in tool. They help you:

- Write less repetitive class code
- Make data-focused classes easier to read
- Create objects with clearer field definitions
- Add useful defaults without a lot of ceremony

You will see dataclasses often in configuration objects, records, lightweight models, and classes that group related values together.

## Creating a basic dataclass

Here is the same idea written as a regular class first:

```python
class User:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

Now compare it to a dataclass:

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
```

**How it works:**
- `@dataclass` is a decorator from the standard library.
- Each annotated attribute becomes a field on the class.
- Python generates an `__init__` method using those fields.

You can create and use instances the normal way:

```python
user = User("Alice", 30)
print(user.name)  # Alice
print(user.age)   # 30
```

**Rule of thumb:** Use a dataclass when your class is mostly about storing named values.

## What `@dataclass` gives you automatically

A dataclass can generate several useful methods for you.

```python
from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


p1 = Point(2, 3)
p2 = Point(2, 3)

print(p1)       # Point(x=2, y=3)
print(p1 == p2) # True
```

**What this gives you by default:**
- `__init__` to create instances
- `__repr__` for a readable display
- `__eq__` for value-based equality

That means two dataclass instances with the same field values compare as equal, which is often what you want for data objects.

## Using default values

You can give fields default values just like function parameters.

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int = 0
    is_admin: bool = False


user = User("Alice")
print(user)  # User(name='Alice', age=0, is_admin=False)
```

**Important:** Fields with defaults must come after fields without defaults.

Good:

```python
@dataclass
class User:
    name: str
    age: int = 0
```

Bad:

```python
# This would cause an error:
# @dataclass
# class User:
#     age: int = 0
#     name: str
```

This rule is similar to function parameters: required values come first, optional values come after them.

## Avoiding shared mutable defaults with `field`

Be careful with mutable defaults like lists and dictionaries.

Bad:

```python
from dataclasses import dataclass


@dataclass
class Team:
    name: str
    members: list[str] = field(default=[])
```

That default list would be shared in a surprising way, just like a mutable default parameter in a function.

Use `field(default_factory=...)` instead:

```python
from dataclasses import dataclass, field


@dataclass
class Team:
    name: str
    members: list[str] = field(default_factory=list)
```

**What happens:**
1. `default_factory=list` tells Python to call `list()` for each new instance.
2. Each instance gets its own fresh list.

This is the safe default for mutable fields.

## Adding methods to a dataclass

Dataclasses can still have regular instance methods.

```python
from dataclasses import dataclass


@dataclass
class Rectangle:
    width: float
    height: float

    def area(self) -> float:
        return self.width * self.height


rect = Rectangle(4, 5)
print(rect.area())  # 20
```

`@dataclass` does not replace normal class behavior. It just saves you from writing repetitive field setup code.

## Controlling field behavior with `field()`

Use `field()` when a plain default value is not enough.

### `default_factory`

You already saw `default_factory` for mutable values:

```python
from dataclasses import dataclass, field


@dataclass
class Cart:
    items: list[str] = field(default_factory=list)
```

### Excluding a field from `repr`

Sometimes you do not want a field to appear when the object is printed:

```python
from dataclasses import dataclass, field


@dataclass
class Account:
    username: str
    password: str = field(repr=False)


account = Account("alice", "secret")
print(account)  # Account(username='alice')
```

**Use this when:** a field is noisy, sensitive, or not useful in debug output.

## Using `__post_init__` for extra setup

Sometimes you need extra work after the generated `__init__` runs. Use `__post_init__` for that.

```python
from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float

    def __post_init__(self):
        if self.price < 0:
            raise ValueError("price cannot be negative")


product = Product("Notebook", 9.99)
```

**How it works:**
1. Python generates the normal `__init__`.
2. That `__init__` sets the fields.
3. Python then calls `__post_init__`.

This is a good place for validation, normalization, or derived setup.

## Choosing a regular class vs a dataclass

Both are valid tools. The choice depends on what the class is for.

Use a **dataclass** when:

- The class mainly stores data
- You want less boilerplate
- Value-based equality makes sense
- The fields are the most important part of the class

Use a **regular class** when:

- The class has complex setup logic
- The class behavior matters more than its stored fields
- You need very custom construction from the start
- Automatically generated methods are not a good fit

**Use this by default:** If the class mostly groups named values together, start with a dataclass.

## Common patterns

### Representing a record-like object

```python
from dataclasses import dataclass


@dataclass
class Book:
    title: str
    author: str
    pages: int
```

This is a good fit when you want a clean object with named fields and little custom setup.

### Grouping configuration values

```python
from dataclasses import dataclass


@dataclass
class AppConfig:
    host: str
    port: int = 8000
    debug: bool = False
```

This pattern works well for settings and configuration objects.

### Validating fields after creation

```python
from dataclasses import dataclass


@dataclass
class Temperature:
    celsius: float

    def __post_init__(self):
        if self.celsius < -273.15:
            raise ValueError("temperature below absolute zero")
```

Use this when field values must follow rules.

## Common mistakes

### Forgetting `@dataclass`

```python
from dataclasses import dataclass


class User:
    name: str
    age: int
```

Without `@dataclass`, those annotations do not automatically create an `__init__` method.

Good:

```python
from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int
```

### Using a mutable default directly

Bad:

```python
from dataclasses import dataclass, field


@dataclass
class Cart:
    items: list[str] = field(default=[])
```

Good:

```python
from dataclasses import dataclass, field


@dataclass
class Cart:
    items: list[str] = field(default_factory=list)
```

### Using a dataclass for a behavior-heavy class

Dataclasses are best for data-focused classes. If most of the class is about complex behavior, a regular class may be clearer.

**Rule of thumb:** A dataclass should usually make the class simpler, not hide a complicated design.

## Best practices

- **Start with clear field names**: The field list is the heart of the class.
- **Use type hints on fields**: Dataclasses work best when the fields are explicit.
- **Use `field(default_factory=...)` for mutable values**: This avoids shared default state.
- **Keep `__post_init__` focused**: Use it for validation or light setup, not heavy business logic.
- **Choose dataclasses for data-rich classes**: If the class mostly stores values, dataclasses are often the cleanest tool.

## Summary

- Dataclasses are a standard-library way to build data-focused classes with less boilerplate.
- `@dataclass` can generate `__init__`, `__repr__`, and equality behavior for you.
- Use `field(default_factory=...)` for mutable defaults like lists and dictionaries.
- Use `__post_init__` when you need validation or setup after initialization.
- The safest default is to use a dataclass when a class mostly stores named values.

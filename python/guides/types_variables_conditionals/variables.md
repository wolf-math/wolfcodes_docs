---
title: Variables
sidebar_position: 0
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What are variables?

**Variables** are names that refer to values. They let you store data and give it meaningful labels, making your code readable and maintainable. Python doesn't use type declarations; a name is bound to an object at runtime and can later be rebound to another.

```python
message = "hello"   # name -> string object
count = 3           # name -> int object
pi = 3.14159        # name -> float object
```

## Why this matters

Variables are essential for writing useful programs. Without variables, you'd have to repeat values throughout your code, making it hard to maintain and update. Variables let you store user input, intermediate calculations, and results that you'll use later. They also make your code self-documenting. A well-named variable like `user_age` is much clearer than just using the number `25` scattered throughout your code. Understanding how variables work, especially how they reference objects and how mutability affects them, is crucial for avoiding bugs and writing clean Python code.

## Naming rules and style

- Letters, digits, and underscores. Cannot start with a digit.
- Case-sensitive: `name` and `Name` are different.
- Avoid [keywords](../../language_reference/keywords) like `for`, `if`, `class`.
- Follow PEP 8: use `lower_snake_case` for variables.

```python
user_name = "ada"
max_items = 10
```

## Assignment and rebinding

`=` binds a name to a value. Reassigning changes the binding, not the original object.

```python
x = 1
x = x + 2   # x now refers to 3
```

Multiple assignment is supported:

```python
a, b = 1, 2
a, b = b, a      # swap
```

Underscore is often used as a throwaway name:

```python
first, _, third = [10, 20, 30]
```

## Immutability vs mutability

Rebinding works the same for all objects, but mutating an object changes it in place.

```python
nums = [1, 2, 3]
alias = nums
alias.append(4)
print(nums)   # [1, 2, 3, 4] (same list, two names)
```

For immutable objects, you can only rebind:

```python
name = "hi"
name = name + " there"   # creates a new string; old one unchanged
```

## Identity vs equality

- `==` checks if values are equal.
- `is` checks if two names refer to the same object.

```python
a = [1, 2, 3]
b = [1, 2, 3]
c = a
a == b    # True  (same contents)
a is b    # False (different lists)
a is c    # True  (same list)
```

<!-- ## Shadowing and scope (brief)

- Names created inside a function are **local** to that function.
- Names defined at the top level of a module are **global** to that module.
- Avoid reusing names from outer scopes unintentionally (shadowing).

```python
value = "global"

def demo():
    value = "local"   # shadows the outer name
    return value

demo()      # 'local'
value       # 'global'
``` -->

## Tips for beginners

- Choose descriptive names: `total`, `user_age`, `items`.
- Keep a name’s meaning consistent; avoid reusing the same name for unrelated data.
- Print and inspect with `print(x)` or `type(x)` to see what a name currently refers to.


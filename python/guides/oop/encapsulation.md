---
title: Encapsulation
sidebar_position: 5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What is encapsulation?

**Encapsulation** is the OOP idea that an object should:

- **Hide its internal details**, and
- **Expose a clean public interface** for other code to use.

In practice, this means:

- Keeping internal data and helper methods private‑ish.
- Providing well‑named methods and properties to interact with an object safely.

Python doesn’t enforce strict privacy like some languages, but it gives you tools and conventions to signal *“this is internal”* vs *“this is part of the public API.”*

## Why this matters

Encapsulation helps you:

- Change how a class works **without** breaking the rest of your program.
- Prevent other code from depending on internal details that might change.
- Keep objects in a **valid state** by controlling how attributes are read and modified.

When you design a class, you’re really designing its *interface*: what other code can do with its instances. Encapsulation keeps that interface small, clear, and robust.

## Public vs “private” attributes (by convention)

Python uses **naming conventions** instead of strict access modifiers:

- No leading underscore → **public** API  
  - Safe to use from other modules; considered stable.
- Single leading underscore (`_name`) → **internal** implementation detail  
  - “You can access this, but you probably shouldn’t.”
- Double leading underscore (`__name`) → **name-mangled** to reduce accidental access/override  
  - Used sparingly for avoiding attribute collisions in subclasses.

### Example: simple encapsulation with `_` prefix

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius   # internal storage

    def to_fahrenheit(self):
        return self._celsius * 9 / 5 + 32
```

From the outside:

```python
t = Temperature(20)
print(t.to_fahrenheit())  # 68.0
# You *could* access t._celsius, but the underscore says "internal"
```

Other programmers will treat `_celsius` as an implementation detail, not part of the public API.

## Using properties to control access

[`@property`](https://docs.python.org/3/library/functions.html#property) lets you expose an attribute‑like interface **with method‑like control**.

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        """Public read access."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32
```

Usage:

```python
# Create a temperature
t = Temperature(25)
print(t.celsius)      # 25  (getter)
print(t.fahrenheit)   # 77.0 (computed property)

# Update the temperature (uses setter with validation)
t.celsius = 0
print(t.celsius)      # 0
print(t.fahrenheit)   # 32.0 (automatically recalculated)

# Try to set an invalid temperature
t.celsius = -300      # raises ValueError: Temperature below absolute zero!

# Fahrenheit is read-only (computed from celsius)
# t.fahrenheit = 100  # AttributeError: can't set attribute
```

From the outside, `celsius` and `fahrenheit` look like **normal attributes**, but internally you can:

- Validate values
- Compute derived values
- Change implementation later without breaking callers

## Hiding implementation details

Encapsulation lets you change *how* something is stored or computed while keeping the same public interface.

```python
class User:
    def __init__(self, username, password_plaintext):
        self.username = username
        self._password_hash = self._hash_password(password_plaintext)

    def _hash_password(self, plaintext):
        # Implementation detail (could change later)
        import hashlib
        return hashlib.sha256(plaintext.encode("utf-8")).hexdigest()

    def check_password(self, attempt):
        return self._hash_password(attempt) == self._password_hash
```

From the outside:

```python
u = User("alice", "secret123")
u.check_password("guess")      # False
u.check_password("secret123")  # True
```

Code using `User` doesn’t know or care how passwords are hashed. You can change `_hash_password` later without breaking callers, as long as the **public methods** (`check_password`, etc.) behave the same.

## Encapsulation and invariants

An **invariant** is a condition that should always be true for a valid object (e.g., balance ≥ 0).

Encapsulation helps enforce invariants by:

- Keeping raw attributes private.
- Only changing them through methods that validate inputs.

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Cannot deposit a negative amount")
        self._balance += amount

    def withdraw(self, amount):
        if amount < 0:
            raise ValueError("Cannot withdraw a negative amount")
        if amount > self._balance:
            raise ValueError("Insufficient funds")
        self._balance -= amount
```

Other code can read `balance`, but it can’t easily violate the invariant by setting `_balance` directly (unless it intentionally ignores the underscore convention).

## Name mangling with `__double_underscore`

Attributes starting with **two leading underscores** (and not ending with two) are *name‑mangled* to include the class name. This reduces accidental override/collision in subclasses.

```python
class Base:
    def __init__(self):
        self.__secret = 42   # name-mangled to _Base__secret

class Child(Base):
    def __init__(self):
        super().__init__()
        self.__secret = 99   # name-mangled to _Child__secret
```

Here, `Base` and `Child` each get their own `__secret` attribute internally:

```python
b = Base()
c = Child()

print(dir(b))  # contains '_Base__secret'
print(dir(c))  # contains '_Base__secret' and '_Child__secret'
```

Name mangling is mainly useful when you're building classes meant to be subclassed and want to avoid accidental attribute clashes. For most day‑to‑day code, a single underscore is enough.

## Restricting attributes with `__slots__`

The `__slots__` attribute lets you explicitly define which attributes an instance can have, preventing the creation of any other attributes. This provides both encapsulation (controlling what attributes exist) and memory optimization.

```python
class Point:
    __slots__ = ['x', 'y']  # Only these attributes are allowed

    def __init__(self, x, y):
        self.x = x
        self.y = y

p = Point(3, 4)
print(p.x)  # 3
print(p.y)  # 4

p.z = 5  # AttributeError: 'Point' object has no attribute 'z'
```

**When to use `__slots__`:**

- You want to prevent accidental attribute creation
- You're creating many instances and want to save memory (each instance uses less memory)
- You want to make it explicit which attributes a class supports

**When not to use `__slots__`:**

- You need dynamic attributes (adding attributes at runtime)
- You're using multiple inheritance with classes that don't have `__slots__`
- The memory savings aren't important for your use case

For most code, the underscore naming conventions are sufficient. Use `__slots__` when you specifically need to prevent attribute creation or optimize memory usage.

## Encapsulation at the module level

Encapsulation isn’t just for classes. Python modules also use naming conventions:

- Names starting with `_` (e.g., `_helper_function`) are treated as **internal** to the module.
- `from module import *` will skip names starting with `_` unless you define `__all__`.

```python
# mymodule.py

_cache = {}  # internal

def public_api(x):
    if x in _cache:
        return _cache[x]
    result = x * 2
    _cache[x] = result
    return result
```

Here, `_cache` is an internal detail; `public_api` is the public function other code should use.

## When to use encapsulation tools

**Use:**

- Leading underscores (`_name`) for **internal attributes and helpers**.
- Properties (`@property` and setters) when you need:
  - Validation
  - Computed values
  - The flexibility to change implementation later
- Double underscores (`__name`) sparingly, mainly to prevent accidental subclass collisions.
- `__slots__` when you need to prevent dynamic attribute creation or optimize memory for many instances.

**Avoid:**

- Exposing every attribute as public without thinking about invariants.
- Overusing `__double_underscore` when a single underscore and clear docs are enough.

## Summary

- Encapsulation is about hiding internal details and exposing a clean public interface.
- Python uses **conventions** (`_name`, `__name`) instead of strict access modifiers.
- Properties (`@property`) let you present attributes while still validating and controlling access.
- `__slots__` can restrict which attributes are allowed and optimize memory usage.
- Good encapsulation protects invariants and makes it easier to evolve your classes without breaking callers.

As you design classes, think in terms of: *“What should other code be allowed to do with this object?”* Then use encapsulation tools to keep that contract clear and stable.



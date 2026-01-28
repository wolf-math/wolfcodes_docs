---
title: Class Methods, Static Methods, and Properties
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
## What are these decorators?

Python provides three important decorators for methods and attributes:

- **`@property`** — Makes a method look like an attribute
- **`@classmethod`** — A method that receives the class as the first argument
- **`@staticmethod`** — A method that doesn't receive `self` or the class

These decorators let you control how methods are called and how attributes are accessed, giving you more flexibility in your class design.

## `@property`

The `@property` decorator lets you define methods that can be accessed like attributes, with the ability to add validation, computation, or other logic.

### Basic property (read-only)

```python
class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        """Calculate the area of the circle."""
        return 3.14159 * self.radius ** 2

    @property
    def diameter(self):
        """Calculate the diameter of the circle."""
        return self.radius * 2

circle = Circle(5)
print(circle.area)      # 78.53975 (no parentheses!)
print(circle.diameter)  # 10
```

Notice that you access `area` and `diameter` like attributes (no parentheses), even though they're methods. They're computed each time you access them.

### Property with setter

You can also create a setter to control how values are assigned:

```python
class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius  # private attribute

    @property
    def celsius(self):
        """Get the temperature in Celsius."""
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        """Set the temperature in Celsius with validation."""
        if value < -273.15:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value

    @property
    def fahrenheit(self):
        """Get the temperature in Fahrenheit (read-only)."""
        return self._celsius * 9 / 5 + 32

# Usage
t = Temperature(25)
print(t.celsius)      # 25
print(t.fahrenheit)   # 77.0

t.celsius = 0         # uses setter (valid)
print(t.fahrenheit)   # 32.0 (automatically recalculated)

t.celsius = -300      # raises ValueError: Temperature below absolute zero!
```

### Property with deleter

You can also define a deleter to control what happens when an attribute is deleted:

```python
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Name cannot be empty")
        self._name = value

    @name.deleter
    def name(self):
        print("Deleting name...")
        self._name = None

person = Person("Alice")
print(person.name)  # "Alice"

del person.name     # "Deleting name..."
print(person.name)  # None
```

### When to use `@property`

Use `@property` when you want to:
- Compute values on-the-fly (like `area` from `radius`)
- Add validation when setting values
- Make read-only attributes
- Maintain backward compatibility when changing implementation

## `@classmethod`

A `@classmethod` receives the **class** as the first argument (conventionally named `cls`) instead of an instance. This is useful for alternative constructors or methods that work with the class itself.

### Basic classmethod

```python
class Person:
    species = "Homo sapiens"  # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def get_species(cls):
        """Return the species for this class."""
        return cls.species

    @classmethod
    def from_birth_year(cls, name, birth_year):
        """Alternative constructor: create Person from birth year."""
        current_year = 2024
        age = current_year - birth_year
        return cls(name, age)  # Same as: return Person(name, age)

# Call on the class (not an instance)
print(Person.get_species())  # "Homo sapiens"

# Alternative constructor
person = Person.from_birth_year("Alice", 1990)
print(person.name)  # "Alice"
print(person.age)   # 34
```

::: note ⚠️ Important!!!
The key line is `return cls(name, age)`. Here, `cls` refers to the `Person` class itself, so `cls(name, age)` is exactly the same as writing `Person(name, age)`. This calls the class constructor (`__init__`) to create a new instance. Since `@classmethod` receives the class (not an instance), you don't have `self` available. Instead, you use `cls` to call the class constructor directly, which creates and returns a new instance.
:::

### Classmethod for alternative constructors

A common use of `@classmethod` is creating alternative ways to construct instances:

```python
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def from_tuple(cls, coords):
        """Create a Point from a tuple (x, y)."""
        return cls(coords[0], coords[1])

    @classmethod
    def origin(cls):
        """Create a Point at the origin (0, 0)."""
        return cls(0, 0)

    @classmethod
    def from_polar(cls, radius, angle):
        """Create a Point from polar coordinates."""
        import math
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        return cls(x, y)

# Different ways to create points
p1 = Point(3, 4)                    # standard constructor
p2 = Point.from_tuple((5, 6))       # from tuple
p3 = Point.origin()                 # at origin
p4 = Point.from_polar(5, math.pi/4) # from polar coordinates
```

### When to use `@classmethod`

Use `@classmethod` when you want to:
- Create alternative constructors
- Access or modify class-level data
- Create factory methods
- Work with the class itself rather than instances

## `@staticmethod`

A `@staticmethod` doesn't receive `self` or `cls`. It's just a regular function that happens to be defined inside a class. It can't access instance or class data directly.

### Basic staticmethod

```python
class MathUtils:
    @staticmethod
    def add(a, b):
        """Add two numbers."""
        return a + b

    @staticmethod
    def multiply(a, b):
        """Multiply two numbers."""
        return a * b

# Can be called on the class
result1 = MathUtils.add(5, 3)        # 8
result2 = MathUtils.multiply(4, 7)   # 28

# Can also be called on an instance
utils = MathUtils()
result3 = utils.add(10, 20)          # 30
```

### Staticmethod in a class context

Even though static methods don't receive `self` or `cls`, they're often placed in classes because they're logically related:

```python
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @staticmethod
    def is_leap_year(year):
        """Check if a year is a leap year."""
        return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

    @staticmethod
    def days_in_month(year, month):
        """Get the number of days in a month."""
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        elif month in [4, 6, 9, 11]:
            return 30
        elif month == 2:
            return 29 if Date.is_leap_year(year) else 28
        else:
            raise ValueError("Invalid month")

# Usage
print(Date.is_leap_year(2024))      # True
print(Date.days_in_month(2024, 2))  # 29

date = Date(2024, 2, 15)
print(date.is_leap_year(2020))      # True (can call on instance too)
```

### When to use `@staticmethod`

Use `@staticmethod` when you want to:
- Group related utility functions with a class
- Create helper methods that don't need instance or class data
- Organize code logically even if the function doesn't need `self` or `cls`

## Comparing the three

Here's a class that uses all three decorators to show the differences:

```python
class BankAccount:
    # Class attribute
    interest_rate = 0.05  # 5% annual interest

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance  # private attribute

    # Instance method (regular method)
    def deposit(self, amount):
        """Deposit money into the account."""
        self._balance += amount
        return self._balance

    # Property (looks like an attribute)
    @property
    def balance(self):
        """Get the account balance."""
        return self._balance

    @balance.setter
    def balance(self, value):
        """Set the balance with validation."""
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    # Classmethod (receives the class)
    @classmethod
    def set_interest_rate(cls, rate):
        """Set the interest rate for all accounts."""
        cls.interest_rate = rate

    @classmethod
    def from_string(cls, account_str):
        """Create account from string 'owner:balance'."""
        owner, balance = account_str.split(':')
        return cls(owner, float(balance))

    # Staticmethod (receives neither self nor cls)
    @staticmethod
    def calculate_interest(principal, rate, years):
        """Calculate compound interest."""
        return principal * (1 + rate) ** years - principal

# Usage
account = BankAccount("Alice", 1000)

# Instance method
account.deposit(500)
print(account.balance)  # 1500 (property, no parentheses)

# Property setter
account.balance = 2000
print(account.balance)  # 2000

# Classmethod
BankAccount.set_interest_rate(0.06)
print(BankAccount.interest_rate)  # 0.06

account2 = BankAccount.from_string("Bob:500")
print(account2.owner)   # "Bob"
print(account2.balance) # 500.0

# Staticmethod
interest = BankAccount.calculate_interest(1000, 0.05, 2)
print(interest)  # 102.5
```

## Summary

| Decorator | First Parameter | Access to | Use Case |
|-----------|----------------|-----------|----------|
| `@property` | `self` | Instance data | Computed attributes, validation |
| `@classmethod` | `cls` (class) | Class data | Alternative constructors, factory methods |
| `@staticmethod` | None | None (just a function) | Utility functions related to the class |

**Key differences:**

- **Regular methods** receive `self` and work with instance data
- **`@property`** methods look like attributes but can have logic
- **`@classmethod`** methods receive `cls` and work with the class
- **`@staticmethod`** methods are just functions grouped with the class

These decorators give you powerful tools for designing clean, flexible class interfaces.

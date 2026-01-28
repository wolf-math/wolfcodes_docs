---
title: Polymorphism
sidebar_position: 6
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
## What is polymorphism?

**Polymorphism** (from Greek: "many forms") is the ability to use the **same interface** for different types of objects. In Python, this means you can write code that works with multiple types as long as they implement the same methods or properties.

The core idea: **different objects can respond to the same method call in their own way.**

```python
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

class Duck:
    def speak(self):
        return "Quack!"
```

Even though `Dog`, `Cat`, and `Duck` are different classes, they all have a `speak()` method. You can write code that works with any of them:

```python
animals = [Dog(), Cat(), Duck()]

for animal in animals:
    print(animal.speak())
# Woof!
# Meow!
# Quack!
```

This is polymorphism in action: the same code (`animal.speak()`) works with different types, and each type responds appropriately.

## Why this matters

Polymorphism helps you write code that is:

- **More flexible** — works with many types without modification
- **Easier to extend** — add new types without changing existing code
- **More maintainable** — focus on what objects *do* rather than what they *are*

Instead of checking types with `isinstance()` everywhere, you can rely on objects implementing the methods you need. This is one of Python's core design principles: *"It's easier to ask for forgiveness than permission"* (EAFP) and *"duck typing"* (if it walks like a duck and quacks like a duck, it's a duck).

## Polymorphism through inheritance

The most common way to achieve polymorphism is through **inheritance**. A base class defines an interface, and subclasses implement it in their own way.

### Basic example

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement area()")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2
```

Usage:

```python
shapes = [
    Rectangle(5, 10),
    Circle(3),
    Rectangle(2, 4)
]

total_area = sum(shape.area() for shape in shapes)
print(total_area)  # ~58.27 (50 + 28.27 + 8)
```

All shapes have an `area()` method, so you can call it on any shape without checking the type. Each shape calculates its area differently, but from the caller's perspective, they all work the same way.

### With `super()` and shared behavior

You can combine polymorphism with shared base class behavior:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return "Some sound"  # default implementation

    def introduce(self):
        return f"I'm {self.name} and I say {self.make_sound()}"

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
```

Usage:

```python
pets = [Dog("Fido"), Cat("Whiskers")]

for pet in pets:
    print(pet.introduce())
# I'm Fido and I say Woof!
# I'm Whiskers and I say Meow!
```

Here, `introduce()` is defined once in the base class but uses the polymorphic `make_sound()` method, which each subclass overrides.

## Duck typing (Python's approach)

Python doesn't require inheritance for polymorphism. If an object has the methods you need, it works. This is called **"duck typing."**

```python
class Car:
    def drive(self):
        return "Vroom vroom!"

class Bicycle:
    def drive(self):
        return "Pedal pedal!"

class Horse:
    def drive(self):
        return "Clip clop!"
```

Even though `Car`, `Bicycle`, and `Horse` don't share a common base class, you can use them polymorphically:

```python
vehicles = [Car(), Bicycle(), Horse()]

for vehicle in vehicles:
    print(vehicle.drive())
# Vroom vroom!
# Pedal pedal!
# Clip clop!
```

Python doesn't care about the type, it only cares that each object has a `drive()` method.

### Real-world example: file-like objects

Python's standard library uses duck typing extensively. Many functions work with "file-like objects" (objects with `read()`, `write()`, etc.):

```python
def process_file(file_obj):
    content = file_obj.read()
    return content.upper()

# Works with actual files
with open("data.txt") as f:
    print(process_file(f))

# Works with StringIO (in-memory file)
from io import StringIO
memory_file = StringIO("hello world")
print(process_file(memory_file))  # "HELLO WORLD"

# Works with any object that has read()
class CustomReader:
    def read(self):
        return "custom content"

reader = CustomReader()
print(process_file(reader))  # "CUSTOM CONTENT"
```

All three objects work with `process_file()` because they all implement `read()` without requiring inheritance.

## Operator overloading (polymorphism with operators)

Python's [dunder methods](./dunder_methods) let you define how operators work with your classes, enabling polymorphism for operators like `+`, `==`, `len()`, etc.

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"
```

**Usage:**

```python
v1 = Vector(1, 2)
v2 = Vector(3, 4)
v3 = v1 + v2  # Uses __add__
print(v3)     # Vector(4, 6)
```

The `+` operator works with `Vector` objects just like it works with numbers or strings—polymorphism at the operator level.

## Built-in polymorphism

Python's built-in functions use polymorphism extensively:

```python
# len() works with many types
len([1, 2, 3])        # 3 (list)
len("hello")          # 5 (string)
len({"a": 1, "b": 2}) # 2 (dict)

# + works with many types
"hello" + "world"     # "helloworld" (strings)
[1, 2] + [3, 4]       # [1, 2, 3, 4] (lists)
10 + 20               # 30 (numbers)

# str() works with any type
str(42)               # "42"
str([1, 2, 3])        # "[1, 2, 3]"
str(Dog("Fido"))      # depends on __str__ or __repr__
```

Each type implements `__len__()`, `__add__()`, or `__str__()` differently, but you use them the same way.

## Abstract base classes (optional)

While duck typing is usually enough, you can use **Abstract Base Classes (ABCs)** to define a formal interface when you want to enforce that subclasses implement certain methods:

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Subclasses must implement this."""
        pass

    @abstractmethod
    def perimeter(self):
        """Subclasses must implement this."""
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Shape()  # Would raise TypeError (can't instantiate abstract class)
rect = Rectangle(5, 10)  # OK
```

ABCs make the interface explicit and prevent you from accidentally creating incomplete subclasses, but they're optional. Using duck typing works fine for most cases.

## When to use polymorphism

1. **You have multiple types that share an interface** — they all implement the same methods
2. **You want to write generic code** that works with any of those types
3. **You want to add new types easily** without changing existing code

**Avoid when:**

1. **Types are truly unrelated** — if there's no meaningful shared interface, forcing polymorphism adds complexity
2. **You need type-specific behavior** that can't be abstracted — sometimes `isinstance()` checks are appropriate

## Best practices

1. **Design around interfaces, not implementations** — think about what methods objects need, not what classes they are
2. **Use duck typing** when possible — it's more Pythonic than strict inheritance hierarchies
3. **Keep interfaces small and focused** — prefer "many small interfaces" over "one giant interface"
4. **Document expected methods** — use docstrings to clarify what methods a function expects objects to have
5. **Use ABCs sparingly** — only when you need to enforce an interface or provide shared default implementations

Polymorphism is one of OOP's most powerful tools. Combined with Python's duck typing, it lets you write flexible, extensible code that adapts easily to new requirements.


---
title: Inheritance
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
## What is inheritance?

**Inheritance** is an OOP feature that lets you create a **new class** that reuses and extends an **existing class**.

- The existing class is the **base class** (or parent / superclass / base class).
- The new class is the **subclass** (or child / derived class).

The subclass automatically gets:

- The base class’s **attributes** and **methods**
- The ability to **override** or **extend** behavior

In Python, you define inheritance by putting the base class in parentheses:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):   # Dog inherits from Animal
    def speak(self):
        return "Woof!"
```

## Why this matters

Inheritance helps you:

- **Avoid duplication** by putting shared behavior in a base class.
- **Organize related classes** into a hierarchy (e.g., `Shape` → `Circle`, `Rectangle`).
- Implement [**polymorphism**](./polymorphism)—code that works with many subclasses through a common interface.

Used well, inheritance makes code easier to reuse and extend. Used poorly, it can make code harder to understand, so it’s important to keep hierarchies simple and clear.

## Basic single inheritance

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow!"
```

**Usage:**

```python
pets = [Dog("Fido"), Cat("Whiskers")]

for pet in pets:
    print(pet.speak())
# Fido says woof!
# Whiskers says meow!
```

**Here:**

- `Dog` and `Cat` **inherit from** `Animal`.
- They override `speak` but still share the `name` attribute set up in `Animal.__init__`.

## Calling the base class with `super()`

When you override `__init__` or other methods, you often want to call the base class implementation as part of the subclass’s work. Use `super()` to do that:

```python
class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # call Animal.__init__
        self.breed = breed
```

**Usage:**

```python
d = Dog("Fido", "Labrador")
print(d.name)   # 'Fido'  (from Animal)
print(d.breed)  # 'Labrador'  (defined in Dog)
```

`super()` is especially important in multiple inheritance, but it's a good habit even in simple hierarchies.

## Multilevel inheritance

You can create inheritance chains where a subclass inherits from another subclass, forming multiple levels:

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("The animal moves")


class Fish(Animal):
    def __init__(self, name, water_type):
        super().__init__(name)   # calls Animal.__init__
        self.water_type = water_type

    def move(self):
        print("The fish swims")


class Tuna(Fish):
    def __init__(self, name, water_type, speed):
        super().__init__(name, water_type)  # calls Fish.__init__
        self.speed = speed

    def move(self):
        super().move()  # calls Fish.move
        print(f"The tuna swims at {self.speed} mph")
```

**Usage:**

```python
tuna = Tuna("Bluefin", "saltwater", 45)
print(tuna.name)        # "Bluefin" (from Animal)
print(tuna.water_type)  # "saltwater" (from Fish)
print(tuna.speed)       # 45 (from Tuna)

tuna.move()
# Output:
# The fish swims
# The tuna swims at 45 mph
```

**Here:**
- `Tuna` inherits from `Fish`, which inherits from `Animal`
- Each level calls `super()` to initialize the parent class
- `Tuna.move()` calls `Fish.move()` using `super()`, then adds its own behavior
- This creates a chain: `Tuna` → `Fish` → `Animal`

Multilevel inheritance is useful when you have a natural hierarchy, but keep it shallow (2-3 levels) to avoid complexity.

## Overriding methods

Subclasses can **override** methods from their base class to change behavior.

```python
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement area()")

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
        import math
        return math.pi * self.radius ** 2
```

**Usage:**

```python
shapes = [Rectangle(2, 3), Circle(1)]

for s in shapes:
    print(s.area())  # calls the appropriate subclass method

# Output:
# 6
# 3.141592653589793
```

This is the foundation of [**polymorphism**](./polymorphism): different subclasses implement the same method interface in their own way.

## Extending behavior instead of replacing it

Sometimes you want to *add* behavior to the base method rather than completely replace it:

```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class TimestampLogger(Logger):
    def log(self, message):
        import datetime
        timestamp = datetime.datetime.now().isoformat(timespec="seconds")  # Get current time as ISO string (e.g., "2025-01-01T12:00:00")
        super().log(f"{timestamp}: {message}")
```

Usage:

```python
l = TimestampLogger()
l.log("System started")
# [LOG] 2025-01-01T12:00:00: System started
```

`TimestampLogger.log` calls `super().log(...)` to reuse the base behavior and add extra information.

## Inheritance vs composition

Inheritance is not the only way to reuse code. Another common pattern is **composition**, which means having one object hold a reference to another and delegate work to it.

Use **inheritance** when:

- There is a clear **“is‑a”** relationship:
  - `Dog` is an `Animal`
  - `AdminUser` is a `User`

Use **composition** when:

- There is a **“has‑a”** or **“uses‑a”** relationship:
  - `Car` has an `Engine`
  - `Order` has a list of `LineItem`s

**Example of composition:**

```python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()   # composition

    def start(self):
        self.engine.start()
        print("Car is ready to go")
```

Keep hierarchies shallow and favor composition when inheritance doesn’t clearly match the problem.

## Multiple inheritance (overview)

Python supports **multiple inheritance**. A class can inherit from more than one base class:

```python
class Logger:
    def log(self, message):
        print(f"[LOG] {message}")

class Serializer:
    def serialize(self, data):
        import json
        return json.dumps(data)

class LoggedSerializer(Logger, Serializer):
    pass
```

**Usage:**

```python
ls = LoggedSerializer()
ls.log("Saving data")
print(ls.serialize({"x": 1}))
```

Multiple inheritance can be powerful but also complex.  
Python uses a *method resolution order* (MRO) to decide which base class method to call when there are conflicts.

**General advice:**

- Prefer **single inheritance + composition** for most designs.
- Keep multiple inheritance hierarchies small and well‑documented.

## `isinstance`, `issubclass`, And `super`

Useful built‑ins for working with inheritance:

```python
isinstance(obj, Class)    # is obj an instance of Class or its subclasses?
issubclass(Sub, Base)     # does Sub inherit from Base (directly or indirectly)?
super()                   # call base class methods in a cooperative way
```

Example:

```python
issubclass(Dog, Animal)   # True
isinstance(Dog("Fido"), Animal)  # True
```

## Summary

- Inheritance lets a subclass reuse and extend behavior from a base class.
- You use `class Sub(Base):` to declare inheritance.
- `super()` lets subclasses call base class implementations.
- Overriding methods is key to implementing polymorphism.
- Inheritance is best for clear “is‑a” relationships; composition is often a better choice otherwise.

The [**polymorphism**](./polymorphism) guide builds on this by showing how to write code that works with many different subclasses through a shared interface.



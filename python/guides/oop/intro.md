---
title: Python OOP Introduction
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
## What is object-oriented programming?

**Object-Oriented Programming (OOP)** is a way of organizing code around **objects** instead of just functions and data. An object bundles together:

- **Data** (attributes) — what the object *has*
- **Behavior** (methods) — what the object *does*

In Python, almost everything is an object: strings, lists, functions, even modules and classes themselves.

```python
name = "Alice"
print(name.upper())   # 'ALICE'  (method on a string object)
```

When you define your own classes, you create your own types of objects to model things in your program: users, orders, game characters, shapes, and more.

## Why this matters

OOP becomes important when your programs grow beyond a few functions. It helps you:

- **Group related data and behavior** together (easier to understand and change)
- **Avoid repetition** by sharing behavior between related classes
- **Model real-world concepts** directly in code (User, Car, BankAccount, etc.)
- **Encapsulate complexity** so other parts of your program don't need to know internal details

Most large Python codebases use OOP heavily, so understanding classes, instances, and methods is key to reading and writing professional Python.

## Key concepts

### Classes and instances

A **class** is a blueprint for creating objects. An **instance** is a specific object created from that blueprint. Think of a class like a cookie cutter that you can use to make many cookies (instances), all shaped the same way.

```python
# Car is the class (the blueprint)
class Car:
    pass

# my_car is an instance (a specific object created from Car)
my_car = Car()
```

### Attributes

**Attributes** are pieces of data stored on objects. Each instance can have its own attribute values:

```python
my_car.color = "Blue"  # attribute storing the car's color
your_car.color = "Red"  # different instance, different value
```

### Methods

**Methods** are functions attached to a class that work with the instance's data:

```python
my_car.start_engine()  # calling a method on the instance
```

The `instances` guide covers attributes and methods in depth.

### Encapsulation (preview)

**Encapsulation** means keeping an object's internal state private (by convention) and exposing a clear public interface through methods and attributes.

Python doesn't enforce strict privacy like some languages, but it uses naming conventions:
- Names without underscores: part of the public interface
- Single leading underscore: "internal use" 
- Double leading underscore: name-mangled to avoid accidental overrides

The [`encapsulation`](./encapsulation) guide covers these conventions and tools like `@property` in more depth.

### Inheritance and polymorphism (preview)

Two more key ideas in OOP:

- **Inheritance** — create new classes that reuse and extend existing ones
- **Polymorphism** — different classes can be used interchangeably if they share a common interface

Example of simple inheritance:

```python
class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

animals = [Dog(), Cat()]
for a in animals:
    print(a.speak())  # "Woof!", then "Meow!"
```

Here, `Dog` and `Cat` inherit from `Animal`, and both override `speak`, but you can treat them all as "animals that can speak."

You'll explore these ideas in detail in the `inheritance` and `polymorphism` guides.

## How this OOP section is organized

This OOP section builds up concepts step by step:

- **Intro (this page)** — big picture and key vocabulary
- **Instances** — creating and working with concrete objects, including instance attributes and methods
- **Attributes** — storing and accessing data on objects (class vs instance attributes)
- **Encapsulation** — hiding implementation details and designing clean interfaces
- **Inheritance** — reusing and extending behavior across classes
- **Polymorphism** — writing code that works with different types using a shared interface
- **Dunder methods** — special methods like `__str__`, `__len__`, and operators that make your classes feel built-in
- **Modules and packages** — organizing OOP code across multiple files

You don't need to master everything at once. Start by getting comfortable with **classes**, **instances**, **attributes**, and **methods**. Then, as your projects grow, you can come back to the later guides when you're ready to use more advanced OOP features.

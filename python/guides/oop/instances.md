---
title: Instances
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
## What is an instance?

An **instance** is a concrete object created from a **class**. If a class is a blueprint, an instance is the actual thing built from that blueprint.

Let's start with the simplest possible class:

```python
class Car:
    pass  # An empty class—does nothing yet, but it's valid Python!
```

You can create an instance by calling the class like a function:

```python
my_car = Car()
print(my_car)  # <__main__.Car object at 0x...>
```

- `Car` is the **class**—it's the blueprint
- `my_car` is an **instance**—it's a specific object created from the `Car` class
- The `Car()` call creates a new instance

### Adding attributes manually

You can add data to an instance by assigning to attributes directly:

```python
class Car:
    pass

my_car = Car()
my_car.color = "Blue"
my_car.make = "Toyota"
my_car.model = "Camry"

print(my_car.color)  # "Blue"
print(my_car.make)   # "Toyota"
print(my_car.model)  # "Camry"
```

Each instance can have its own attributes with different values:

```python
car1 = Car()
car1.color = "Blue"
car1.make = "Toyota"

car2 = Car()
car2.color = "Red"
car2.make = "Honda"

print(car1.color)  # "Blue"
print(car2.color)  # "Red"
```

Each instance has its own data (attributes), even though they share the same class definition. However, adding attributes manually like this isn't ideal because you might forget to set some, or set them inconsistently.

## Creating instances

You create an instance by **calling the class** like a function. While you can add attributes manually, it's better to set them up when creating the instance using `__init__`.

### Using `__init__` to set up attributes

The `__init__` method is a special method that runs automatically when you create a new instance. Let's first see that it runs:

```python
class Car:
    def __init__(self):
        print("Vrooom! A car was created!")

# create instances
my_car = Car()
# Output: Vrooom! A car was created!

your_car = Car()
# Output: Vrooom! A car was created!
```

Notice that the `print()` statement runs automatically each time you create a new instance. The `__init__` method is called automatically when you create an instance.

Now let's use `__init__` to set up attributes. It's where you set up the instance's initial state:

```python
class Car:
    def __init__(self, make, model, color):
        print("Vrooom! A car was created!")
        self.make = make    # attribute on the instance
        self.model = model  # attribute on the instance
        self.color = color  # attribute on the instance

# create instances
my_car = Car("Toyota", "Camry", "Blue")
# Output: Vrooom! A car was created!

your_car = Car("Honda", "Civic", "Red")
# Output: Vrooom! A car was created!
```

- `__init__` is a special method that runs when you create a new instance
- The parameters you pass to `Car()` (like `"Toyota"`, `"Camry"`, `"Blue"`) are passed to `__init__`
- `self` refers to the instance being created
- You typically assign attributes to `self` to store data on each instance

The name `__init__` stands for "initialize"—it initializes the new instance with whatever data you want it to start with.

### Behind the scenes

When you create an instance, here's what happens:

1. Python allocates a new, empty object
2. It calls the class's `__init__` method with that object as `self` and any extra arguments you passed

```python
my_car = Car("Toyota", "Camry", "Blue")
# roughly equivalent to:
my_car = Car.__new__(Car)              # create empty instance (advanced)
Car.__init__(my_car, "Toyota", "Camry", "Blue")  # initialize it
```

You don't normally call `__new__` or `__init__` directly. Just call the class, and Python handles the rest.

## Instance attributes

Instance attributes are pieces of data stored on **each individual object**. As you saw above, you can add attributes manually or set them up using `__init__`.

### Accessing and modifying attributes

You can read and modify attributes at any time:

```python
class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

my_car = Car("Toyota", "Camry", "Blue")
print(my_car.color)   # "Blue"
print(my_car.make)    # "Toyota"
print(my_car.model)   # "Camry"

# Modify attributes
my_car.color = "Green"
print(my_car.color)   # "Green"
```

Each instance has its own attributes with different values. Changing one instance does **not** affect another:

```python
car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red")

print(car1.color)  # "Blue"
print(car2.color)  # "Red"

car1.color = "Green"
print(car1.color)  # "Green"
print(car2.color)  # "Red" (unchanged)
```

### Accessing and modifying attributes

You can read and modify attributes at any time:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

account = BankAccount("Alice", 100)
print(account.balance)  # 100

account.balance = 150   # modify the attribute
print(account.balance)  # 150
```

### Attribute access and AttributeError

If you try to access an attribute that doesn't exist, you'll get an `AttributeError`:

```python
class Car:
    def __init__(self, make):
        self.make = make

my_car = Car("Toyota")
print(my_car.model)  # AttributeError: 'Car' object has no attribute 'model'
```

You can check if an attribute exists using `hasattr()`:

```python
if hasattr(my_car, 'model'):
    print(my_car.model)
else:
    print("No model attribute")
```

## Instance methods

**Instance methods** are functions attached to a class that work with the instance's data. They're defined like regular functions, but the first parameter is always `self`.

### Defining methods

```python
class Car:
    def __init__(self, make, model, color):
        self.make = make
        self.model = model
        self.color = color

    def get_info(self):
        return f"{self.color} {self.make} {self.model}"
    
    def repaint(self, new_color):
        self.color = new_color
        return f"The car is now {new_color}"

# create instances
my_car = Car("Toyota", "Camry", "Blue")
your_car = Car("Honda", "Civic", "Red")

print(my_car.get_info())   # "Blue Toyota Camry"
print(your_car.get_info()) # "Red Honda Civic"

print(my_car.repaint("Green"))  # "The car is now Green"
print(my_car.get_info())        # "Green Toyota Camry"
```

- `get_info()` is a **method** that uses the instance's data
- `repaint()` is a **method** that modifies the instance's data
- When you call `my_car.get_info()`, Python automatically passes `my_car` as the `self` parameter
- `self` inside methods refers to "this particular instance"

### The `self` parameter

Inside instance methods, `self` is a reference to **the instance that called the method**.

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1

c1 = Counter()
c2 = Counter()

c1.increment()   # changes c1.value to 1
c2.increment()   # changes c2.value to 1

print(c1.value)  # 1
print(c2.value)  # 1
```

Each call to `increment` works on the instance that invoked it. When you call `c1.increment()`, Python passes `c1` as `self`, so `self.value` refers to `c1.value`.

### Methods that modify instance state

Methods can modify the instance's attributes:

```python
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        return self.balance

    def get_balance(self):
        return self.balance

account = BankAccount("Alice", 100)
account.deposit(50)
print(account.get_balance())  # 150

account.withdraw(30)
print(account.get_balance())  # 120
```

### Methods that return values

Methods can return values based on the instance's state:

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

rect = Rectangle(5, 5)
print(rect.area())       # 25
print(rect.perimeter())  # 20
print(rect.is_square())  # True
```

### Calling methods from other methods

Methods can call other methods on the same instance:

```python
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = 0

    def drive(self, miles):
        self.mileage += miles
        print(f"Driven {miles} miles. Total mileage: {self.mileage}")

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

    def full_info(self):
        info = self.get_info()
        return f"{info} with {self.mileage} miles"

my_car = Car("Toyota", "Camry", 2020)
my_car.drive(100)
print(my_car.full_info())  # "2020 Toyota Camry with 100 miles"
```

Here, `full_info()` calls `get_info()` to build a complete description of the car.

### Methods with multiple parameters

Methods can accept multiple parameters beyond `self`:

```python
class Calculator:
    def __init__(self):
        self.history = []

    def add(self, a, b):
        result = a + b
        self.history.append(f"{a} + {b} = {result}")
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append(f"{a} * {b} = {result}")
        return result

calc = Calculator()
print(calc.add(5, 3))        # 8
print(calc.multiply(4, 7))   # 28
print(calc.history)          # ['5 + 3 = 8', '4 * 7 = 28']
```

## Instance vs class attributes

An attribute defined on `self` is **per-instance**. An attribute defined directly on the class is **shared** by all instances (unless shadowed).

```python
class Dog:
    species = "Canis familiaris"   # class attribute (shared)

    def __init__(self, name):
        self.name = name           # instance attribute

fido = Dog("Fido")
rex = Dog("Rex")

print(fido.species)  # 'Canis familiaris'
print(rex.species)   # 'Canis familiaris'
```

Changing an instance attribute:

```python
fido.name = "Mr. Fido"
print(fido.name)  # 'Mr. Fido'
print(rex.name)   # 'Rex'
```

Changing a class attribute affects all instances that haven't overridden it:

```python
Dog.species = "Canis lupus familiaris"
print(fido.species)  # 'Canis lupus familiaris'
print(rex.species)   # 'Canis lupus familiaris'
```

The [Class attributes](./class_attributes) guide will go deeper into this distinction.

## Checking an object's type

Use `isinstance` to check if an object is an instance of a class (or a subclass):

```python
class Animal:
    pass

class Dog(Animal):
    pass

fido = Dog()

isinstance(fido, Dog)     # True
isinstance(fido, Animal)  # True (Dog is a subclass of Animal)
isinstance(fido, object)  # True (everything inherits from object)
```

Use `type(obj)` when you need the exact class:

```python
type(fido) is Dog         # True
type(fido) is Animal      # False
```

## Multiple instances in collections

Instances often live inside lists, dicts, or other collections:

```python
class Task:
    def __init__(self, title, done=False):
        self.title = title
        self.done = done

    def complete(self):
        self.done = True

tasks = [
    Task("Write docs"),
    Task("Fix bugs", done=True),
]

for task in tasks:
    status = "✓" if task.done else " "
    print(f"[{status}] {task.title}")

# Mark first task as done
tasks[0].complete()
```

This is where OOP shines! You work with many objects that share the same interface (methods/attributes) but hold different data.

## Summary

In this section you learned that:

- An **instance** is a concrete object created from a class
- You create instances by **calling the class**
- **Instance attributes** live on each object and store data unique to that instance
- **Instance methods** are functions attached to a class that work with the instance's data
- `self` inside methods refers to the instance that called the method
- The `__init__` method runs automatically when you create a new instance
- Class attributes live on the class and are shared; instance attributes are per-instance
- `isinstance` is the preferred way to check if something is an instance of a given class

---
title: Class Attributes
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
## What are class attributes?

A **class attribute** is a variable that belongs to the **class itself**, not to any particular instance. All instances of the class share the same class attribute value (unless an instance shadows it with its own attribute of the same name).

```python
class Dog:
    species = "Canis familiaris"   # class attribute (shared by all dogs)

    def __init__(self, name):
        self.name = name           # instance attribute (unique per dog)

fido = Dog("Fido")
rex = Dog("Rex")

print(fido.species)  # 'Canis familiaris'
print(rex.species)   # 'Canis familiaris'
print(Dog.species)   # 'Canis familiaris' (accessed via class)
```

Here, `species` is defined at the class level, so every `Dog` instance shares it. Each dog has its own `name`, but they all share the same `species`.

## Why this matters

Class attributes are useful when you need:

- **Shared constants** — values that are the same for all instances of a class
- **Default values** — fallback values that instances can override
- **Class-level counters or state** — data that tracks something across all instances
- **Configuration** — settings that apply to the entire class

They help you avoid repetition and provide sensible defaults that instances can customize when needed.

## Class attributes vs instance attributes

The key difference:

- **Class attributes** — defined directly on the class; shared by all instances
- **Instance attributes** — defined on `self` in methods (usually `__init__`); unique to each instance

```python
class Counter:
    total_count = 0   # class attribute (shared)

    def __init__(self):
        self.count = 0   # instance attribute (unique per instance)

c1 = Counter()
c2 = Counter()

c1.count = 5
c2.count = 10

print(c1.count)        # 5
print(c2.count)        # 10
print(c1.total_count)  # 0 (same for all)
print(c2.total_count)  # 0 (same for all)
```

## Accessing class attributes

You can access class attributes through the class or any instance:

```python
class Circle:
    pi = 3.14159   # class attribute

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return Circle.pi * self.radius ** 2   # accessing via class name
        # or: return self.pi * self.radius ** 2   # works via instance too

c = Circle(5)
print(c.pi)        # 3.14159 (accessed via instance)
print(Circle.pi)   # 3.14159 (accessed via class)
```

When accessed through an instance, Python first looks for an instance attribute with that name. If it doesn't find one, it looks for a class attribute. This is how attribute lookup works in Python.

## Changing class attributes

### Changing via the class

When you change a class attribute via the class, it affects all instances that haven't overridden it:

```python
class Dog:
    species = "Canis familiaris"

fido = Dog()
rex = Dog()

Dog.species = "Canis lupus familiaris"   # change via class

print(fido.species)  # 'Canis lupus familiaris'
print(rex.species)   # 'Canis lupus familiaris'
```

### Shadowing with instance attributes

If you set an attribute with the same name on an instance, you **shadow** the class attribute for that instance only:

```python
class Dog:
    species = "Canis familiaris"

fido = Dog()
rex = Dog()

fido.species = "Custom species"   # creates instance attribute

print(fido.species)  # 'Custom species' (instance attribute)
print(rex.species)   # 'Canis familiaris' (class attribute)
print(Dog.species)   # 'Canis familiaris' (unchanged)
```

Now `fido.species` refers to an instance attribute, while `rex.species` still refers to the class attribute. The class attribute itself is unchanged.

### When this matters

Shadowing is usually unintentional. Be careful when you think you're modifying a class attribute through an instance:

```python
class Counter:
    count = 0   # class attribute

c1 = Counter()
c2 = Counter()

c1.count += 1   # This creates an instance attribute!

print(c1.count)  # 1 (instance attribute)
print(c2.count)  # 0 (still the class attribute)
print(Counter.count)  # 0 (unchanged)
```

The `+=` operator creates a new instance attribute because `c1.count += 1` is equivalent to `c1.count = c1.count + 1`, which assigns to the instance.

To modify a class attribute, access it through the class:

```python
Counter.count += 1   # modifies the class attribute
print(Counter.count)  # 1
```

## Common use cases

### Constants and defaults

Class attributes are perfect for values that should be the same for all instances:

```python
class User:
    MAX_LOGIN_ATTEMPTS = 3   # class constant
    DEFAULT_ROLE = "user"    # default value

    def __init__(self, username, role=None):
        self.username = username
        self.role = role or User.DEFAULT_ROLE   # use class default
```

### Class-level counters

You can track data across all instances:

```python
class Person:
    population = 0   # class attribute

    def __init__(self, name):
        self.name = name
        Person.population += 1   # increment class attribute

    def __del__(self):
        Person.population -= 1   # decrement when instance is deleted

p1 = Person("Alice")
p2 = Person("Bob")

print(Person.population)  # 2
```

### Shared configuration

Store configuration that applies to the whole class:

```python
class Logger:
    log_level = "INFO"   # default log level
    log_format = "{timestamp} - {level} - {message}"

    def log(self, message):
        if Logger.log_level == "DEBUG":
            print(Logger.log_format.format(
                timestamp=self._get_timestamp(),
                level=Logger.log_level,
                message=message
            ))

Logger.log_level = "DEBUG"   # change for all loggers
```

## Mutable class attributes (a cautionary tale)

When a class attribute is a **mutable object** (like a list or dict), all instances share the same object. This can lead to surprising behavior:

```python
class Dog:
    tricks = []   # class attribute (shared mutable object)

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)   # modifies shared list!

fido = Dog("Fido")
rex = Dog("Rex")

fido.add_trick("roll over")
rex.add_trick("sit")

print(fido.tricks)  # ['roll over', 'sit']  (shared!)
print(rex.tricks)   # ['roll over', 'sit']  (shared!)
```

Both dogs share the same `tricks` list, so tricks added to one appear in the other.

**Solution**: Use instance attributes for mutable data:

```python
class Dog:
    def __init__(self, name):
        self.name = name
        self.tricks = []   # instance attribute (unique per dog)

    def add_trick(self, trick):
        self.tricks.append(trick)

fido = Dog("Fido")
rex = Dog("Rex")

fido.add_trick("roll over")
rex.add_trick("sit")

print(fido.tricks)  # ['roll over']
print(rex.tricks)   # ['sit']
```

## Best practices

1. **Use class attributes for constants and defaults** — values that should be the same across all instances
2. **Use instance attributes for data that varies** — each instance should have its own copy
3. **Avoid mutable class attributes** — if you need mutable data, make it an instance attribute
4. **Access class attributes via the class name** — use `Class.attr` when you want to be explicit, especially when modifying them
5. **Be careful with `+=` and similar operations** — they create instance attributes, not modify class attributes
6. **Document class attributes** — use docstrings or comments to explain what they're for

Class attributes are a simple but powerful feature. Use them for shared values and constants, but remember that mutable class attributes are shared by all instances—a common source of bugs if you're not careful.


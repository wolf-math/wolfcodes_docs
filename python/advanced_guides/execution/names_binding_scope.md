---
title: Names, Binding, and Scope
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
Python doesn't have variables. It has **names** that are **bound** to **objects**. This distinction matters.

## Names are not variables

When you write `x = 5`, you're not storing `5` in a box labeled `x`. Instead you're creating a **binding**, which is a name tag attached to the object `5`.

```python
x = 5
y = x
```

What happened? Both `x` and `y` now point to the same object `5`. There's no copying, and no storing. These are just two names for the same thing.

```python
x = 5
y = x
x = 10
print(y)  # Still 5
```

Why? Because `x = 10` doesn't change the object `5`. It creates a new binding. `x` now points to `10`. The `5` object still exists, and `y` still points to it.

This mental model explains everything that follows.

## Assignment is binding, not mutation

Binding changes which object a name points to; mutation changes the object itself. In other words, binding moves a label from one box to another box, while mutation changes the contents inside the box while the label stays on the same box.

```python
x = [1, 2, 3]  # Binding
x = [4, 5, 6]  # New binding
x.append(7)    # Mutation
```

The first line creates a list object and binds `x` to it. The second line creates a different list object and rebinds `x`. The third line mutates the object that `x` is bound to.

This is why this works:

```python
def add_one(x):
    x = x + 1  # Rebinding the local name

n = 5
add_one(n)
print(n)  # Still 5
```

And this works differently:

```python
def append_item(lst):
    lst.append(4)  # Mutating the object

my_list = [1, 2, 3]
append_item(my_list)
print(my_list)  # [1, 2, 3, 4]
```

Same function call pattern. Different behavior. Because one rebinds, the other mutates.

## Legb: how Python finds names

Python looks up names in this order:

1. **Local** — names defined in the current function
2. **Enclosing** — names in enclosing functions (closures)
3. **Global** — names at module level
4. **Built-in** — names like `len`, `print`, `int`

Python looks up names at **runtime**, but which scope a name belongs to is determined when the function is compiled.

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        return x
    
    return inner()

outer()  # "local"
```

Python looks in `inner()` first, finds `x`, and stops. It never checks enclosing or global.

But what if `inner()` doesn't define `x`?

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        return x  # No local x
    
    return inner()

outer()  # "enclosing"
```

Now Python looks in `inner()`, finds nothing, looks in `outer()`, finds `x`, and stops.

This is **lexical scoping**—Python uses where the code is written, not where it's called.

## `global`: Breaking the legb rule

`global` tells Python: "when you see this name, skip Local and Enclosing and go straight to Global."

```python
x = 1

def func():
    global x
    x = 2  # Modifies the global x

func()
print(x)  # 2
```

Without `global`:

```python
x = 1

def func():
    x = 2  # Creates a local binding
    return x

func()  # 2
print(x)  # 1  (global unchanged)
```

`global` doesn't "bring the variable into the function." It changes where Python looks for the name.

## `nonlocal`: The middle ground

`nonlocal` says: "skip Local, but use the nearest Enclosing scope (not Global)."

```python
def outer():
    x = 1
    
    def inner():
        nonlocal x
        x = 2  # Modifies outer's x
    
    inner()
    return x

outer()  # 2
```

Without `nonlocal`:

```python
def outer():
    x = 1
    
    def inner():
        x = 2  # Creates a local binding
        return x
    
    inner()  # 2
    return x

outer()  # 1  (outer's x unchanged)
```

`nonlocal` lets you modify enclosing scope without reaching all the way to global.

## Closures: Names, not values

A closure captures a **name**, not a value. The name is looked up when the function is **called**, not when it's created.

```python
def make_func():
    x = 1
    def inner():
        return x
    x = 2  # Changed before returning
    return inner

f = make_func()
f()  # 2, not 1
```

The closure captured the **name** `x`. When `f()` runs, it looks up `x` in the enclosing scope and finds `2`.

This is why this classic gotcha happens:

```python
funcs = []
for i in range(3):
    funcs.append(lambda: i)

# What do these return?
funcs[0]()  # 2
funcs[1]()  # 2
funcs[2]()  # 2
```

All three functions capture the **name** `i`. When they're called, `i` has the value `2` (the last value from the loop).

Each lambda doesn't get its own copy of `i`. They all share the same name.

## Fixing the loop closure problem

You need to capture the **value**, not the name. Create a new binding for each iteration:

```python
funcs = []
for i in range(3):
    funcs.append(lambda i=i: i)  # Default argument creates new binding

funcs[0]()  # 0
funcs[1]()  # 1
funcs[2]()  # 2
```

Default arguments are evaluated at function definition time. Each lambda gets its own `i` parameter bound to the current loop value.

Or use a closure factory:

```python
def make_func(n):
    return lambda: n

funcs = []
for i in range(3):
    funcs.append(make_func(i))

funcs[0]()  # 0
funcs[1]()  # 1
funcs[2]()  # 2
```

Each call to `make_func(i)` creates a new scope where `n` is bound to the current `i` value.

## The mental model

- **Names are tags on objects**, not boxes storing values
- **Assignment binds names to objects**, it doesn't copy or store
- **LEGB is lookup order**—Python searches scopes in this order
- **Closures capture names**, which are resolved when called
- **`global` and `nonlocal` change lookup behavior**, not data flow

Everything else follows from these principles.

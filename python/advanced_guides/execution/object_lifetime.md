---
title: Object Lifetime
sidebar_position: 0.5
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---
This section explains when Python objects are created, how long they live, and why they eventually disappear. Understanding this clarifies `del`, `__del__`, context managers, and many "memory leak" misconceptions.

## The core mental model (read this first)

**Key idea:**

> Objects live as long as they are reachable. Names do not own objects.

### Objects vs names

Objects are created independently of variables. Names *bind* to objects; they do not *contain* or *own* them. Multiple names can refer to the same object.

```python
x = [1, 2, 3]  # Create an object, bind name 'x' to it
y = x          # Bind name 'y' to the same object
# Both x and y reference the same list object
```

### Binding, rebinding, unbinding

**Binding:** Creating a new association between a name and an object.

```python
x = [1, 2, 3]  # Bind 'x' to a new list object
```

**Rebinding:** Changing which object a name references.

```python
x = [1, 2, 3]  # x references first object
x = [4, 5, 6]  # x now references a different object
# The first object may still exist if other names reference it
```

**Unbinding:** Removing the association between a name and an object.

```python
x = [1, 2, 3]
y = x
del x  # Remove name 'x', object still reachable via 'y'
```

### Reachability as the true lifetime rule

An object lives as long as it's **reachable**—meaning it can be accessed through at least one name or reference.

```python
x = [1, 2, 3]
y = x
del x
# Object still reachable via y
print(y)  # [1, 2, 3] - object still exists
```

An object becomes unreachable when there are no names or references pointing to it. Only then can it be cleaned up.

:::note
We haven't discussed *how* Python cleans up unreachable objects yet. That's an implementation detail we'll cover later. For now, focus on the mental model: objects live while reachable.
:::

## Names, scope, and lifetime

**Where names live and die:**

- **Local scope:** Names in a function exist only while that function is executing. When the function returns, the frame (where local names live) is destroyed.
- **Global scope:** Names at module level exist as long as the module is loaded.
- **Enclosing scope:** Names in enclosing functions exist as long as those functions are executing.

### Name lifetime ≠ object lifetime

```python
def create_list():
    my_list = [1, 2, 3]  # Local name 'my_list'
    return my_list       # Return the object

result = create_list()
# Local name 'my_list' is gone (frame destroyed)
# But the object lives on, referenced by 'result'
print(result)  # [1, 2, 3]
```

**Key takeaway:** When a scope ends, names disappear—objects may not.

## Function calls and returned objects

### Each call creates new objects

Each function call creates its own objects:

```python
def create_list():
    return [1, 2, 3]

a = create_list()
b = create_list()
# a and b reference different objects
print(a is b)  # False
```

### Returning passes a reference

When you return an object from a function, you're passing a *reference* to it, not a copy:

```python
def process_data(data):
    data.append(4)  # Modifies the original object
    return data

original = [1, 2, 3]
result = process_data(original)
print(original)  # [1, 2, 3, 4] - same object!
print(result)    # [1, 2, 3, 4] - same object!
print(original is result)  # True
```

### Multiple calls → multiple objects

```python
def create_person(name):
    return {"name": name, "age": 0}

person1 = create_person("Alice")
person2 = create_person("Bob")
# Each call returns a different object
```

**Clarify explicitly:** The object survives *because something else now refers to it*, not because it "escaped" the function. If you don't capture the return value, the object becomes unreachable:

```python
def create_list():
    return [1, 2, 3]

create_list()  # Object is created and immediately becomes unreachable
# No names reference it, so it can be cleaned up
```

## What "deletion" actually means

### `del` removes a name

The `del` statement removes a binding between a name and an object. It does not destroy the object:

```python
x = [1, 2, 3]
y = x
del x  # Removes name 'x'

print(y)  # [1, 2, 3] - object still exists!
print(x)  # NameError: name 'x' is not defined
```

The object `[1, 2, 3]` continues to exist because `y` still references it. `del x` only removes the name `x`.

### `del` vs rebinding

These both remove the previous binding, but work differently:

```python
# Option 1: Remove the name entirely
del x

# Option 2: Bind to None instead
x = None
```

The difference: `x = None` creates a new binding to `None`, while `del x` removes the name entirely.

### `del` in different scopes

`del` only affects names in the current scope:

```python
x = [1, 2, 3]  # Global

def func():
    x = [4, 5, 6]  # Local
    del x  # Removes local 'x', global 'x' unaffected

func()
print(x)  # [1, 2, 3] - global name still exists
```

**Summary:**

| Operation | What it does |
|-----------|-------------|
| `del x` | Removes the name `x` entirely |
| `x = None` | Rebinds `x` to `None` (keeps the name) |
| `x = other` | Rebinds `x` to `other` |
| None of these | Directly destroy objects |

## How Python reclaims objects (high-level only)

**This section is intentionally shallow.**

Python may reclaim unreachable objects, but **you should not write code that depends on *when* an object is destroyed.**

### CPython uses reference counting + cycle detection

In CPython (the most common Python implementation):
- Objects often become unreachable immediately when their reference count reaches zero
- A cycle detector periodically finds and cleans up unreachable cycles

This is why Python often feels "predictable" in terms of memory—objects typically disappear as soon as they're no longer needed.

### Other implementations differ

**Python the language does not guarantee reference counting.** Other implementations (PyPy, Jython, IronPython) may use different garbage collection strategies.

### Timing is not guaranteed

Even in CPython:
- Objects with `__del__` methods may not be freed immediately
- Cycles delay cleanup until the cycle detector runs
- Cleanup timing depends on implementation details

**Key sentence:** You should not write code that depends on *when* an object is destroyed. Always use explicit resource management (context managers) for cleanup that must happen at a specific time.

## Cycles and why reachability isn't always obvious

### Reference cycles

Objects can reference each other, creating cycles:

```python
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create a cycle
node1 = Node(1)
node2 = Node(2)
node1.next = node2
node2.next = node1  # Cycle!

# Remove external references
node1 = None
node2 = None
# Both objects still reference each other, so neither is unreachable
# Their reference counts never reach zero
```

Even though `node1` and `node2` are no longer accessible from your code, they reference each other, so neither becomes unreachable through reference counting alone.

### Why GC exists

This is why Python's garbage collector includes a **cycle detector** that periodically finds and cleans up unreachable cycles. The cycle detector:
- Finds groups of objects that reference each other
- Checks if the group is reachable from "roots" (global names, stack frames, etc.)
- Frees unreachable cycles

This is why you might see objects disappear "later" rather than immediately—they're waiting for the cycle detector to run.

**Key point:** Cycles make reachability less obvious. An object might appear unreachable from your code, but still be referenced by other unreachable objects in a cycle.

## `__del__`, Resources, and why you should avoid magic cleanup

The `__del__` method (destructor) is intended to run when an object is about to be destroyed, but it's unreliable and should **not** be used for resource management.

### `__del__` is unreliable

**Non-deterministic timing:**
- `__del__` may run immediately, later, or not at all
- It's not guaranteed to run in any specific order
- During interpreter shutdown, `__del__` may run on objects that are still referenced

**Cycles make it worse:**
```python
class A:
    def __init__(self):
        self.other = None

    def __del__(self):
        print("A destroyed")

a = A()
b = A()
a.other = b
b.other = a  # Cycle

a = None
b = None
# __del__ may never run, or run in unpredictable order
```

**Interpreter shutdown issues:**
- During shutdown, modules may already be cleaned up
- `__del__` methods that try to import modules or access globals can fail
- The order of cleanup is undefined

### Objects surviving longer than expected

Because of cycles and the garbage collector, objects with `__del__` methods may survive longer than you expect:

```python
class Logger:
    def __del__(self):
        print("Logger destroyed")

def create_logger():
    logger = Logger()
    logger.log("message")
    # Logger object may not be destroyed immediately
    # It might wait for garbage collection

create_logger()
# Logger might still exist here
```

**Conclusion:** `__del__` is not a resource-management tool. Use context managers (`with` statements) for deterministic cleanup.

**Transition sentence:** Object lifetime is not resource lifetime.

## Deterministic resource management (the right way)

This is the **payoff** section.

### Why object destruction is unreliable

```python
# BAD: Relying on __del__ for cleanup
class FileHandler:
    def __init__(self, filename):
        self.file = open(filename)

    def __del__(self):
        self.file.close()  # Might never run, or run too late

handler = FileHandler("data.txt")
# File might stay open if __del__ doesn't run
```

The file might not be closed if:
- An exception occurs
- The object is part of a cycle
- The interpreter shuts down unexpectedly
- Garbage collection is delayed

### Context managers define explicit lifetimes

```python
# GOOD: Using context managers
with open("file.txt") as f:
    data = f.read()
# File is guaranteed to close here, even if an exception occurs
```

The `with` statement ensures the file is closed when the block exits, regardless of how it exits (normal completion or exception).

### Resource lifetime ≠ object lifetime

Files, locks, sockets, and database connections need **explicit boundaries** for their lifetimes. These resources are limited and must be released promptly:

```python
# Resource lifetime is explicit
with open("file1.txt") as f1:
    with open("file2.txt") as f2:
        # Both files are open
        data1 = f1.read()
        data2 = f2.read()
    # f2 is closed here
# f1 is closed here
```

The file objects may continue to exist in memory, but the underlying file handles are closed immediately when the `with` block exits.

### `try`/`finally` for manual cleanup

Before context managers, `try`/`finally` was used for explicit cleanup:

```python
f = open("data.txt")
try:
    data = f.read()
finally:
    f.close()  # Always runs
```

Context managers (`with` statements) are syntactic sugar for this pattern, making it cleaner and less error-prone.

**Key takeaway:** Use GC for memory. Use `with` for resources.

## Summary: rules you can rely on

### Core principles

- **Names bind to objects:** Names are labels that point to objects; they don't contain or own them
- **Objects live while reachable:** An object exists as long as at least one reference to it exists, regardless of scope
- **Scope ending removes names, not objects:** When a scope ends, names disappear—objects may not
- **GC timing is not guaranteed:** Objects may be freed immediately, later, or during interpreter shutdown—don't rely on timing
- **Never rely on `__del__`:** `__del__` is unreliable and should not be used for resource management
- **Use context managers for cleanup:** Use `with` statements for files, locks, connections, and any resource that must be cleaned up at a specific time

### Don't do this:

- Rely on `__del__` for resource cleanup
- Assume `del` destroys objects
- Expect objects to be freed when names go out of scope
- Write code that depends on cleanup timing
- Assume reference counting behavior in all Python implementations

### Do this instead

- Use context managers (`with` statements) for files, locks, connections
- Use `del` to remove names when you want to make objects unreachable
- Design with explicit resource lifetimes in mind
- Let Python handle object cleanup automatically

### Common misconceptions

**Myth:** "When a variable goes out of scope, the object is destroyed."  
**Reality:** Objects are destroyed when they become unreachable, which may be long after names go out of scope.

**Myth:** "`del` destroys objects."  
**Reality:** `del` removes bindings. Objects are destroyed when all references are gone.

**Myth:** "Python has memory leaks."  
**Reality:** Python manages object lifetimes well. "Leaks" are usually retained objects due to design choices.

**Myth:** "I need to manually manage garbage collection."  
**Reality:** Python's garbage collector works automatically. Manual control is rarely needed and often indicates a design issue.

Understanding object lifetime, references, and memory management helps you write more efficient Python code and avoid common pitfalls. Focus on explicit resource management with context managers, and let Python handle object cleanup automatically.

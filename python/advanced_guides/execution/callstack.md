---
title: Call Stack and Execution
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
This guide explains how Python executes function calls, what happens when you call a function, and how the call stack manages execution. Understanding this helps you debug code, understand recursion, and see why certain patterns work the way they do.

## The call stack

When Python executes your code, it keeps track of function calls using a **call stack**. Think of it as a stack of plates: each function call adds a new plate to the top, and when a function returns, that plate is removed.

```python
def greet(name):
    return f"Hello, {name}!"

def main():
    message = greet("Alice")
    print(message)

main()
```

When Python runs this:
1. `main()` is called → a frame is pushed onto the stack
2. `greet("Alice")` is called → another frame is pushed on top
3. `greet()` returns → its frame is popped off
4. `main()` continues → eventually returns and is popped off
5. Stack is empty → program ends

The call stack ensures Python knows where to return to when a function finishes.

## Stack frames

Each function call creates a **frame** (also called a stack frame or activation record). A frame contains:

- **Local variables** — names defined in that function
- **Parameters** — arguments passed to the function
- **Return address** — where to return when the function finishes
- **Code location** — which line is currently executing
- **References to enclosing scopes** — for closures and nested functions

```python
def calculate(x, y):
    result = x + y  # Local variable
    return result   # Return address tells Python where to go back

value = calculate(3, 4)
```

When `calculate(3, 4)` is called, Python creates a frame with:
- Parameters: `x = 3`, `y = 4`
- Local variables: `result = 7` (after the calculation)
- Return address: back to where `calculate()` was called

## How function calls work

Here's what happens step-by-step when you call a function:

```python
def add(a, b):
    total = a + b
    return total

def main():
    x = 5
    y = 10
    result = add(x, y)
    print(result)

main()
```

**Step 0:** Program starts
- The global frame (module-level scope) exists on its own at the bottom of the stack
- Stack now has only: global (bottom)

**Step 1:** `main()` is called
- A frame for `main()` is created and pushed onto the stack above the global frame
- Local variables `x = 5` and `y = 10` are stored in the `main()` frame
- Stack now has: global (bottom), `main()` (top)

**Step 2:** `add(x, y)` is called
- A new frame for `add()` is created and pushed on top of the `main()` frame
- Parameters `a = 5` and `b = 10` are stored in the new `add()` frame
- The return address (line after `add(x, y)`) is stored
- Stack now has: global (bottom), `main()`, `add()` (top)

**Step 3:** `add()` executes
- `total = a + b` creates `total = 15` in the `add()` frame
- `return total` returns `15` to the caller
- Stack still has: global (bottom), `main()`, `add()` (top)

**Step 4:** `add()` returns
- The `add()` frame is popped off the stack
- Control returns to `main()` at the line after `add(x, y)`
- `result = 15` is stored in the `main()` frame
- Stack now has: global (bottom), `main()` (top)

**Step 5:** `main()` continues and returns
- `print(result)` executes
- `main()` returns, its frame is popped off
- Stack now has only: global (bottom)

**Step 6:** Program ends
- The global frame remains on the stack
- Stack now has only: global (bottom)
- Program execution completes

<!-- Here's how the call stack changes across all stages:

```
  Stage 1           Stage 2           Stage 3           Stage 4  

                                    ┌─────────┐       
                  ┌─────────┐       │   add   │       
                  │   add   │       │ a = 5   │       
                  │ a = 5   │       │ b = 10  │       
                  │ b = 10  │       │total=15 │       ┌─────────┐
┌─────────┐       ├─────────┤       ├─────────┤       │  main   │
│  main   │       │  main   │       │  main   │       │ x = 5   │
│ x = 5   │       │ x = 5   │       │ x = 5   │       │ y = 10  │
│ y = 10  │       │ y = 10  │       │ y = 10  │       │result=15│
└─────────┘       └─────────┘       └─────────┘       └─────────┘
```

Each stage shows the stack state at that point in execution. The stack grows from Stage 1 to Stage 2, stays at 2 frames during Stage 3, then shrinks back to 1 frame in Stage 4, and finally becomes empty in Stage 5. -->


## Nested function calls

When functions call other functions, the stack grows:

```python
def level3():
    return "level 3"

def level2():
    result = level3()
    return f"level 2 -> {result}"

def level1():
    result = level2()
    return f"level 1 -> {result}"

print(level1())
# Output:
# level 1 -> level 2 -> level 3
```

The call stack during `level3()`:

```
┌─────────────┐
│ level3      │ ← Currently executing
├─────────────┤
│ level2      │ ← Waiting
├─────────────┤
│ level1      │ ← Waiting
├─────────────┤
│ module      │ ← Waiting
└─────────────┘
```

Each function waits for the one above it to return before continuing.

## Recursion and recursion limits

**Recursion** is when a function calls itself. Each recursive call adds a new frame to the stack:

```python
def countdown(n):
    if n <= 0:
        return
    print(n)
    countdown(n - 1)  # Recursive call

countdown(3)
# Output:
# 3
# 2
# 1
```

The stack during the deepest call (`countdown(0)`):

```
┌─────────────┐
│ countdown(0)│ ← Currently executing
├─────────────┤
│ countdown(1)│ ← Waiting
├─────────────┤
│ countdown(2)│ ← Waiting
├─────────────┤
│ countdown(3)│ ← Waiting
└─────────────┘
```

### Recursion limits

Python has a recursion limit to prevent infinite recursion from consuming all memory:

```python
import sys

print(sys.getrecursionlimit())  # Usually 1000 on most systems

def infinite():
    return infinite()  # Recursive call with no base case

# infinite()  # Would eventually raise RecursionError
```

If you exceed the limit, Python raises a `RecursionError`:

```python
def recursive(n):
    if n == 0:
        return 0
    return recursive(n - 1)

recursive(10000)  # RecursionError: maximum recursion depth exceeded
```

You can check and modify the limit (though this is rarely needed):

```python
import sys

old_limit = sys.getrecursionlimit()
sys.setrecursionlimit(2000)  # Increase limit (not recommended)
print(sys.getrecursionlimit())  # 2000
sys.setrecursionlimit(old_limit)  # Restore original
```

:::warning
Increasing the recursion limit can cause a stack overflow, crashing Python. It's usually better to rewrite recursive code to be iterative or use tail recursion techniques.
:::

## What happens when exceptions are raised

When an exception is raised, Python unwinds the call stack, looking for an exception handler:

```python
def inner():
    raise ValueError("Something went wrong!")  # Exception raised here

def middle():
    inner()  # Exception propagates up

def outer():
    try:
        middle()  # Exception propagates up
    except ValueError as e:
        print(f"Caught: {e}")  # Exception caught here

outer()
# Output:
# Caught: Something went wrong!
```

**What happens:**

1. `inner()` raises `ValueError`
2. Python looks for a `try/except` in `inner()` → none found
3. Python pops `inner()` frame and checks `middle()` → none found
4. Python pops `middle()` frame and checks `outer()` → found `except ValueError`
5. Exception is caught, stack unwinding stops
6. Code in the `except` block executes

If no handler is found, the exception reaches the top of the stack and Python prints a traceback:

```python
def cause_error():
    raise ValueError("Unhandled error!")

cause_error()
# Output:
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in cause_error
# ValueError: Unhandled error!
```

### Exception propagation

Exceptions propagate up the call stack until handled:

```python
def level3():
    raise ValueError("Error at level 3")

def level2():
    level3()  # Exception propagates through

def level1():
    try:
        level2()  # Exception propagates through
    except ValueError:
        print("Caught at level 1")

level1()
# Output:
# Caught at level 1
```

The traceback shows the entire path:

```python
def a():
    b()

def b():
    c()

def c():
    raise ValueError("Error")

a()
# Traceback shows: a() -> b() -> c() -> ValueError

# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
#   File "<stdin>", line 2, in a
#   File "<stdin>", line 2, in b
#   File "<stdin>", line 2, in c
# ValueError: Error
```

Tracebacks are useful because they show exactly where the exception originated and how it propagated through the call stack.

## Summary

- **Call stack** — Python uses a stack to track function calls, with frames added when functions are called and removed when they return
- **Stack frames** — Each function call creates a frame containing local variables, parameters, return address, and scope information
- **Function execution** — When a function is called, a frame is pushed onto the stack; when it returns, the frame is popped off
- **Recursion limits** — Python has a recursion limit (usually 1000) to prevent infinite recursion from consuming memory
- **No tail-call optimization** — Python doesn't optimize tail-recursive calls; use iteration for better performance and stack management
- **Exception handling** — When exceptions are raised, Python unwinds the stack looking for handlers; if none are found, a traceback is printed

Understanding the call stack and frames helps you:
- Debug code more effectively
- Understand recursion and its limits
- Read tracebacks to find error sources
- Make informed decisions about recursion vs iteration
- Comprehend how Python executes your code

The call stack is a fundamental part of Python's execution model. Every function call, return, and exception involves the stack in some way.

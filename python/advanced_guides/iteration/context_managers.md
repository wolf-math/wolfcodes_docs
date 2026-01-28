---
title: Context Managers
sidebar_position: 3
description: Learn how context managers and the with statement guarantee reliable setup and teardown for resources and temporary state, even when errors occur.
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Context Managers: : Deterministic Setup and Cleanup in Python

## Why context managers exist

Many things in real programs must be **cleaned up reliably**, no matter what happens:

- Files that must be **closed**.
- Locks that must be **released**.
- Database connections that must be **returned** to a pool.
- Temporary configuration or environment changes that must be **restored**.

The core problem:

- If you rely on “I’ll remember to clean up later,” you will eventually forget.
- If you sprinkle `try` / `finally` everywhere, your code gets noisy and error‑prone.

The big idea of context managers is:

> **Make setup and cleanup a single, reusable unit** that the language itself will call correctly, even when errors occur.

Context managers plus the `with` statement give you:

- Clear places for **setup** and **teardown**.
- A guarantee that teardown happens **exactly once**, even on exceptions.
- A readable, declarative style: “**borrow this resource for this block, then return it**.”


## The `with` statement at a glance

You’ve already seen code like:

```python
with open("data.txt") as f:
    process(f)
```

At a surface level, it looks like:

- “Open a file.”
- “Call `process(f)` in this block.”
- “Then close the file.”

But what it really means is:

- **Enter** a context (setup).
- **Run** the block.
- **Leave** the context (cleanup), even if the block raised an exception.

You can read a `with` block as a three‑step promise:

1. “Do this setup.”
2. “Run this block.”
3. “Always clean up afterward.”

The magic is not in `with` by itself; it’s in **the context manager protocol** behind it.


## The context manager protocol

An object can participate in a `with` block if it implements two methods:

- `__enter__(self)`
- `__exit__(self, exc_type, exc, tb)`

Conceptually:

- `__enter__`:
  - Runs **setup** code.
  - Returns a value that becomes the thing after `as` (if you use `as`).
- `__exit__`:
  - Runs **teardown** code.
  - Receives information about any exception that happened inside the block.
  - Can optionally **suppress** that exception.

`open("data.txt")` returns a file object whose class implements both of these methods, which is why it works in a `with` block.


## What `with` actually does under the hood

Take this code:

```python
with manager as value:
    body(value)
```

Python desugars it approximately to:

```python
mgr = manager              # evaluate the context manager expression
value = mgr.__enter__()    # setup
try:
    body(value)            # run the block
except BaseException as exc:
    # Call __exit__ with exception details
    suppress = mgr.__exit__(type(exc), exc, exc.__traceback__)
    if not suppress:
        raise              # re-raise if not suppressed
else:
    # No exception: call __exit__ with all Nones
    mgr.__exit__(None, None, None)
```

Important details:

- **`__enter__` is always called once** before the block.
- **`__exit__` is always called exactly once** after the block:
  - If the block completes normally, `exc_type`, `exc`, `tb` are all `None`.
  - If the block raises, they describe the exception.
- Cleanup is guaranteed because `__exit__` is called inside a `try`/`except`/`else` structure that covers the entire block.

You can think of `with` as a **named `try` / `finally` pattern**:

```python
resource = acquire()
try:
    use(resource)
finally:
    release(resource)
```

becomes:

```python
with acquire_context() as resource:
    use(resource)
```

Python takes responsibility for making sure `release` happens.


## Returning values from `__enter__`

When you write:

```python
with something() as name:
    ...
```

the `name` is bound to **whatever `__enter__` returns**.

That return value can be:

- The **resource** itself (common: file handles, database connections).
- The context manager object (`self`).
- A **wrapped helper object** that exposes only a safer or simpler interface.

### Examples:

- File objects:

  ```python
  f = open("data.txt")
  # inside open()'s class, __enter__ returns the file object itself
  ```

- Custom wrapper:

  ```python
  class Transaction:
      def __enter__(self):
          self.begin()
          return self   # or maybe return a narrow 'Session' view

      def __exit__(self, exc_type, exc, tb):
          if exc_type is None:
              self.commit()
          else:
              self.rollback()
  ```

Pattern to remember:

> `__enter__` = “set things up and give the caller **whatever object they should use inside the block**.”


## Exception handling inside `__exit__`

`__exit__` has the signature:

```python
def __exit__(self, exc_type, exc, tb):
    ...
```

Where:

- `exc_type` is the exception class (e.g., `ValueError`), or `None` if no exception occurred.
- `exc` is the exception instance, or `None`.
- `tb` is the traceback object, or `None`.

The return value is crucial:

- If `__exit__` returns **`True`**:
  - Python treats the exception as **handled**.
  - The exception is **suppressed**, and control continues after the `with` block.
- If `__exit__` returns **`False`** (or `None`):
  - Python **re‑raises** the exception after `__exit__` finishes.

Most context managers:

- Use `__exit__` to **clean up** and then **return `False`**, so exceptions are *not* swallowed.
- Only return `True` when they intentionally **suppress** specific exceptions (for example, `contextlib.suppress`).

Rule of thumb:

> Unless you are very sure, **don’t suppress exceptions**. Let them propagate after cleanup.


## Class-based context managers

The most explicit way to define a context manager is with a **class** that implements `__enter__` and `__exit__`.

Example: timing a block of code:

```python
import time


class Timer:
    def __enter__(self):
        self.start = time.perf_counter()
        return self      # expose timing info inside the block

    def __exit__(self, exc_type, exc, tb):
        self.end = time.perf_counter()
        self.duration = self.end - self.start
        # Don't suppress exceptions
        return False
```

Usage:

```python
with Timer() as t:
    do_work()

print(f"do_work() took {t.duration:.3f} seconds")
```

When to use a class:

- You need a **clear lifecycle** with explicit state.
- You want to attach **methods or attributes** to the object used inside the block.
- You may reuse the same context manager in many places.

When it might be overkill:

- The setup/teardown logic is **tiny**.
- There’s no interesting state to expose inside the block.
- You just want to wrap a simple “try/finally” once – function‑based context managers can be lighter for that.


## Function-based context managers (`contextlib`)

The `contextlib` module offers a more compact pattern via the `@contextmanager` decorator.

Example:

```python
from contextlib import contextmanager


@contextmanager
def open_upper(path, mode="r", encoding="utf-8"):
    f = open(path, mode, encoding=encoding)
    try:
        # Value yielded here becomes the object in `as`
        yield (line.upper() for line in f)
    finally:
        f.close()
```

Usage:

```python
with open_upper("data.txt") as lines:
    for line in lines:
        print(line.strip())
```

Mental model:

- A `@contextmanager` function is a generator where:
  - Code **before** `yield` is **setup** (`__enter__`).
  - The expression you `yield` is the **value bound after `as`**.
  - Code in the `finally` (or after `yield`) is **teardown** (`__exit__`).

You can imagine Python turning the generator into a class with `__enter__` and `__exit__` that manage the `try` / `finally` around the `yield`.

When this is the right tool:

- The logic is **small and linear**.
- You don’t need a full class with methods and attributes.
- You naturally think “setup/teardown around a block” rather than “object with behavior.”


## Context managers vs `try/finally`

You could write:

```python
f = open("data.txt")
try:
    process(f)
finally:
    f.close()
```

This **works**. So why does `with` exist?

Reasons:

- **Readability**:

  ```python
  with open("data.txt") as f:
      process(f)
  ```

  says directly, “open this, use it here, then close it.”

- **Composability**:
  - Once you encode the pattern in a context manager, you can use it everywhere with a single `with`.

- **Reusability**:
  - The same `__enter__` / `__exit__` logic works in any `with` block, not just one hand‑written `try/finally`.

- **Error resistance**:
  - It’s easier to get `try/finally` *slightly* wrong (multiple returns, early continues, etc.).
  - `with` centralizes the tricky part in one well‑tested implementation.

You can think of `with` as: **“try/finally turned into an interface.”**


## Nesting and composing context managers

Real code often needs **multiple** resources at once:

```python
with open("in.txt") as src, open("out.txt", "w") as dst:
    for line in src:
        dst.write(transform(line))
```

This is syntactic sugar for nested `with` statements:

```python
with open("in.txt") as src:
    with open("out.txt", "w") as dst:
        ...
```

Order matters:

- **Entry**:
  - `open("in.txt")` → `__enter__` for the first manager.
  - Then `open("out.txt", "w")` → `__enter__` for the second.
- **Exit**:
  - The second manager’s `__exit__` runs **first**.
  - The first manager’s `__exit__` runs **last**.

This LIFO order is important for resource safety:

- You typically want to tear down the “inner” things before the “outer” ones.
- If something fails, Python still calls all relevant `__exit__` methods in the correct order.

Remember:

> **Multiple `with` targets** mean “enter left to right, exit right to left.”


## Common standard-library context managers

You don’t need to memorize everything, but recognizing common ones helps.

- **`open`**:
  - Manages file handles; ensures `close()` is called.

- **`threading.Lock` (and `RLock`)**:

  ```python
  lock = threading.Lock()
  with lock:
      # section is protected
      ...
  ```

  - `__enter__` acquires the lock.
  - `__exit__` releases it, even if an exception occurs.

- **`contextlib.suppress(*exceptions)`**:

  ```python
  from contextlib import suppress

  with suppress(FileNotFoundError):
      os.remove("maybe_exists.txt")
  ```

  - Intentionally swallows specified exceptions.

- **`contextlib.redirect_stdout(target)`**:

  ```python
  from contextlib import redirect_stdout

  with open("log.txt", "w") as f, redirect_stdout(f):
      print("This goes into log.txt")
  ```

  - Temporarily redirects `sys.stdout` within the block.

There are many more (`contextlib.ExitStack`, temporary directories, decimal contexts, etc.), but these illustrate the main idea: **enter a temporary world; leave it cleaned up.**


## Context managers as temporary state changes

Context managers aren’t only for “open/close” style resources. They’re also perfect for **temporary configuration**:

- Changing logging levels.
- Overriding global settings.
- Enabling or disabling features for the duration of a block.

Example: temporarily changing a setting:

```python
from contextlib import contextmanager


@contextmanager
def temporary_setting(obj, name, value):
    old_value = getattr(obj, name)
    setattr(obj, name, value)
    try:
        yield
    finally:
        setattr(obj, name, old_value)
```

Usage:

```python
with temporary_setting(config, "debug", True):
    run_debug_only_things()

# Here, config.debug is back to its original value
```

Conceptual expansion:

> Context managers define a **temporary world**: “things look like this inside; when you leave, reality snaps back to normal.”

Not just “borrow a resource,” but also “borrow a configuration.”


## Common pitfalls and misconceptions

- **Forgetting that `__exit__` always runs**  
  Even if you `return` early or raise an exception, `__exit__` still runs.  
  This is a feature, but be aware that **teardown code always executes**.

- **Accidentally suppressing exceptions**  
  If your `__exit__` returns `True` by mistake, you may silently swallow errors and make debugging painful.  
  Usually, you should **return `False`** unless you explicitly want to hide certain exceptions.

- **Confusing context managers with decorators**  
  - Decorators wrap functions; they control **how and when a function is called**.
  - Context managers wrap a **block of code**, controlling **setup and cleanup** around that block.
  - The same object can sometimes be designed to act as both, but they solve different problems.

- **Thinking `with` is just syntactic sugar**  
  It is *partly* sugar over `try/finally`, but:
  - It standardizes an interface (`__enter__` / `__exit__`).
  - It lets many different objects integrate with the same control structure.
  - It encourages factoring lifecycle logic into reusable building blocks.


## When to use context managers (rules of thumb)

Use a context manager when:

- **Setup and teardown must be paired**:
  - Open/close, acquire/release, start/stop, push/pop.
- **Cleanup must be guaranteed**:
  - Even if the code inside the block fails, you can’t skip cleanup.
- **You want readable code** that makes the lifecycle obvious at the call site.

Prefer a simple function (or other pattern) when:

- There’s **no meaningful lifecycle**:
  - Nothing to undo after the operation.
- The operation is a **pure calculation** with no external resources or state.
- Wrapping it in `with` would **not add clarity**, only ceremony.

A good mental test:

> If you catch yourself writing `try` / `finally` more than once for the same pattern, it probably wants to be a context manager.


## Suggested callout blocks

- **Under the hood: `with` desugaring**

  ```python
  mgr = manager
  value = mgr.__enter__()
  try:
      # with-block body
      ...
  except BaseException as exc:
      if not mgr.__exit__(type(exc), exc, exc.__traceback__):
          raise
  else:
      mgr.__exit__(None, None, None)
  ```

- **Mental model: “Borrow, then return”**

  - Enter: “borrow this resource / configuration.”
  - Block: “use it safely here.”
  - Exit: “return it exactly as required, even if things went wrong.”

- **Pitfall alert: exception suppression**

  - `__exit__` returning `True` **hides** exceptions.
  - Only do this when you are deliberately ignoring specific error conditions.

- **Advanced note: generator-based context managers**

  - `@contextmanager` turns a generator into a context manager:
    - Code before `yield` → setup.
    - `yield` value → the object bound after `as`.
    - `finally` or code after `yield` → teardown.


## How this fits your Advanced Python section

- **Iteration protocol** → how Python **loops** (iterables, iterators, `for`).
- **Generators** → how Python **pauses** (lazy, stateful iteration via `yield`).
- **Context managers** → how Python **guarantees cleanup** (deterministic setup/teardown via `with`).

Together, they demystify three of the most misunderstood keywords in Python:

- `for` – built on the iteration protocol.
- `yield` – the heart of generators.
- `with` – the face of context managers.


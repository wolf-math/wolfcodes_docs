---
title: Generators
sidebar_position: 2
description: Learn how generator functions turn iteration into paused functions, enabling lazy, single-pass, memory-efficient pipelines.
author:
  name: Aaron Wolf
  url: https://wolfcodes.dev
license:
  type: CC BY-NC 4.0
  attribution_required: true
source:
  canonical_url: https://wolfcodes.dev
---

# Generators: Lazy Iteration and State Machines in Python

## Why generators exist

Generators are Python’s answer to a very modern problem:

- **You want a sequence of values**, but:
  - You **don’t want** to store them all in memory.
  - You **don’t want** to write a bunch of boilerplate iterator classes.

The big idea:

> Generators turn iteration into a **paused function**.

Instead of manually tracking “where you are” in a sequence, you write a normal‑looking function with `yield`. Python:

- Runs the function **until it hits `yield`**.
- Hands that value to the caller.
- **Pauses**, keeping all local variables and the call stack alive.
- Resumes right after `yield` the next time you ask for another value.

Generators shine when:

- **Streaming data** (log files, network data, large CSVs).
- **Building pipelines** (transform → filter → aggregate) without temporary lists.
- **Potentially infinite sequences** (`count()`, repeated polling, event streams).

They give you the power of custom iterators, with much less code.


## What a generator actually is

There are two pieces to understand:

1. **Generator function** – a function defined with `yield` in its body:

   ```python
   def countdown(n):
       while n > 0:
           yield n
           n -= 1
   ```

2. **Generator object** – the thing you get when you *call* a generator function:

   ```python
   gen = countdown(3)
   ```

Key points:

- Calling `countdown(3)` **does not run the loop immediately**.
- It returns a **generator object**.
- That generator object is an **iterator**:
  - It implements `__iter__` (returns itself).
  - It implements `__next__` (advance to the next `yield`).

So from the iteration protocol’s point of view, a generator object is “just another iterator” – it happens to be powered by a paused function.


## `yield` vs `return`

Inside a generator function, `yield` and `return` have very different jobs.

### `yield`

- **Produces a value** to the caller of `next()` or to the `for` loop.
- **Suspends execution** of the function at that point.
- **Preserves local state** (all local variables, the instruction pointer, the call stack).

You can think of:

> `yield value` ≈ “send `value` out, then pause here until next time.”

### `return`

- **Ends the generator completely**.
- Internally, this causes the generator’s `__next__` to raise `StopIteration`.
- If you write `return some_value`, that `some_value` becomes the `.value` attribute on the internal `StopIteration` object (rarely needed in everyday code, but useful to know).

### Mental model

- `yield` = **“pause here and hand back a value”**.
- `return` (or falling off the end) = **“we’re done; this iterator is exhausted.”**


## Execution flow: what really happens

Consider this generator:

```python
def demo():
    print("Start")
    yield 1
    print("After first yield")
    yield 2
    print("Done")
```

Walk through step by step:

```python
g = demo()      # Nothing printed yet

next(g)
# Prints:
# Start
# returns 1

next(g)
# Prints:
# After first yield
# returns 2

next(g)
# Prints:
# Done
# raises StopIteration
```

Important details:

- The **first** `next(g)` runs the function **from the start** until the first `yield`.
- Each subsequent `next(g)` resumes right after the previous `yield`.
- Local variables and control flow pick up exactly where they left off.

Contrast this with a normal function call:

- A regular function builds a stack frame, runs to completion, then **destroys** its local state.
- A generator function **keeps** its frame around between `next()` calls.

This “suspended stack frame” is what makes generators feel like **state machines written as ordinary functions**.


## Generators as state machines

Every `yield` line is a **state boundary**:

- “Run until this yield → pause → later, resume from here.”

Compare two styles.

### Manual state machine (class‑based iterator)

```python
class Countdown:
    def __init__(self, start):
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value
```

### Generator‑based state machine

```python
def countdown(start):
    current = start
    while current > 0:
        yield current
        current -= 1
```

In both cases:

- Something remembers “where you are” (`current`).
- Each step advances one state.

The generator version is usually:

- **Shorter** (no separate class, less boilerplate).
- **Clearer** to read: the control flow is just “normal code plus `yield`.”

So you can think of generators as **self‑contained cursors with memory**:

- Iterators are cursors.
- Generators are cursors whose logic lives inside a paused function.


## Generator expressions

Python also gives you a compact syntax for simple generators: **generator expressions**.

### Syntax comparison

- **List comprehension** (eager):

  ```python
  squares_list = [x * x for x in range(10)]
  ```

  - Builds a full list of 10 items **immediately**.

- **Generator expression** (lazy):

  ```python
  squares_gen = (x * x for x in range(10))
  ```

  - Creates a generator object that computes values **on demand**.

Both use almost the same syntax; the only difference is `[]` vs `()`.

### Key difference: eager vs lazy

- List comprehension:
  - Allocates memory for all results up front.
  - Great when the list is small and you need random access or multiple passes.
- Generator expression:
  - Computes each value only when requested.
  - Great for large or streaming data, especially when the consumer itself is another iterator‑style function like `sum`, `any`, `all`, or `max`.

Example:

```python
total = sum(x * x for x in range(10_000_000))
```

- This **never builds a 10‑million‑item list** in memory.
- `sum` just keeps asking the generator for the next value.

### Common pitfall: “Why did this only run once?”

Generator expressions produce **generators**, which are **single‑pass iterators**:

```python
gen = (x * x for x in range(3))

list(gen)   # [0, 1, 4]
list(gen)   # [] — already exhausted
```

If you need to loop again, recreate the generator expression or materialize to a list.


## Generator exhaustion (again, but deeper)

Generator objects are **fundamentally single‑pass**:

- Once a generator’s `__next__` raises `StopIteration`, the generator is **done forever**.
- There is no “reset” operation.

This isn’t an accident; it’s built into the design:

- The generator’s stack frame is torn down once it completes.
- Its local state is gone; there’s nothing to resume.

Common solutions when this bites you:

- **Recreate the generator**:

  ```python
  def numbers():
      for i in range(3):
          yield i

  g1 = numbers()
  g2 = numbers()  # fresh generator, independent state
  ```

- **Materialize with `list()`** if:
  - The data is small enough to fit in memory, and
  - You truly need to traverse it multiple times:

  ```python
  g = (expensive(x) for x in source)
  results = list(g)  # run once, keep results
  ```

- **Redesign your API**:
  - Instead of returning a pre‑built generator that may already be half used, return a **generator function** (or other iterable factory) so callers can get a fresh generator each time.


## `StopIteration` and generators

From the outside, generators obey the normal iteration protocol:

- When a generator has no more values to produce, its `__next__` raises `StopIteration`.
- `for` loops and most consumers catch that and stop cleanly.

Inside the generator:

- You **usually don’t raise `StopIteration` yourself**.
- You just:
  - Let the function run off the end, or
  - Use `return` when you’re done.
- Python automatically turns that into `StopIteration` for the caller.

### Why leaking `StopIteration` is dangerous (PEP 479 in one paragraph)

In older Python versions, if you accidentally wrote:

```python
def bad():
    # Don't do this
    raise StopIteration
    yield 1
```

then:

- The `StopIteration` could escape from inside the generator.
- To the caller, it looked exactly like “the generator is finished.”
- This made some bugs **silent**: a mistake inside the generator could quietly stop an outer loop.

Modern Python guards against this:

- If a `StopIteration` escapes from inside a generator, Python wraps it in a `RuntimeError`.
- That makes the bug visible instead of silently ending iteration.

You don’t need to remember PEP numbers; just remember:

> Inside generators, **don’t raise `StopIteration` yourself**. Let the generator finish naturally.


## Advanced generator features (light touch)

Generators are already powerful with just `yield`, but there are a few advanced methods you might see.

### `send()`: sending values *into* a generator

Normally, `next(gen)` is like `gen.send(None)`.

You can also send a value back in:

```python
def echo():
    received = yield "ready"
    while True:
        received = yield f"you said: {received}"

g = echo()
next(g)              # 'ready'
g.send("hello")      # 'you said: hello'
g.send("world")      # 'you said: world'
```

This is useful for:

- Coroutines in older styles of async code.
- Fancy control flows where the caller and generator “talk” to each other.

In modern everyday Python, you’ll see `send()` **rarely**; `async`/`await` is usually preferred for complex bidirectional flows.

### `throw()` and `close()`

- `gen.throw(exc_type, exc_value=None, traceback=None)`:
  - Injects an exception at the current `yield` point.
  - The generator can catch it with `try`/`except` and do cleanup.
- `gen.close()`:
  - Tells the generator, “we’re done; please clean up.”
  - Internally, it throws a `GeneratorExit` inside the generator.

These are mostly used for:

- Resource management patterns.
- Libraries that build advanced control‑flow constructs.

If you’re just using generators for iteration and pipelines, you can safely ignore these until you need them.


## `yield from`

`yield from` is syntactic sugar that **delegates iteration** to another iterable (often another generator).

Without `yield from`:

```python
def chain(a, b):
    for x in a:
        yield x
    for x in b:
        yield x
```

With `yield from`:

```python
def chain(a, b):
    yield from a
    yield from b
```

Conceptually, it means:

> “Keep yielding whatever this other iterator yields, until it’s done.”

It’s more than just shorter syntax:

- It correctly **forwards exceptions** from the sub‑generator.
- It correctly **captures the sub‑generator’s return value** (via the internal `StopIteration.value`) if you need it.

In everyday code, you mostly use it as:

- A clean way to **flatten** nested generators.
- A way to **delegate part of the work** to a helper generator.


## Generators vs iterators vs iterables (comparison)

Let’s place generators back into the bigger ecosystem.

- **Iterable**:
  - Something you can call `iter(x)` on.
  - Examples: lists, dicts, ranges, many custom containers.
- **Iterator**:
  - Has `__next__`, raises `StopIteration` when done.
  - Examples: list iterators, file objects, generator objects.
- **Generator object**:
  - A **specific kind of iterator** produced by calling a generator function.
  - Single‑pass, powered by a paused stack frame.
- **Generator function**:
  - A function defined with `yield` in its body.
  - Calling it creates a fresh generator object each time.

So:

- Generator objects **are iterators**.
- Generator functions **are factories** for those iterators.
- They sit directly on top of the iteration protocol you learned in the iteration protocol guide.


## Performance and memory characteristics

### Lazy evaluation

Generators compute values **only when requested**:

- If you never iterate, nothing runs.
- If you break out of a loop early, the rest of the generator body never executes.

### Memory usage

For many patterns, generators use **constant memory**:

- They hold only the current item and necessary state.
- They don’t keep all past items in memory.

This makes them ideal for:

- Large files.
- Network streams.
- Database cursors and paginated APIs.

### When generators are *not* a win

Generators are not magical speed boosters. They’re often **slower per item** than simple list operations because:

- Each `next()` call has overhead.
- There’s more Python‑level machinery per element.

They’re a great fit when:

- Memory is the bottleneck.
- You truly need only **one pass**.

They’re a poor fit when:

- You need **random access** or indexing.
- You need to traverse the data **many times**.
- You want to use vectorized operations or tools that expect concrete collections.

In those cases, a list (or another concrete data structure) may be better.


## Common misconceptions

- **“Generators are always faster than lists.”**  
  Not necessarily. They can be faster or slower depending on:
  - How many elements you actually consume.
  - Whether memory or CPU is the bottleneck.

- **“Generators are just syntactic sugar for iterators.”**  
  They’re more than that: they give you a **different way to express control flow**.  
  You could write the same thing with a class, but it would usually be more code and harder to read.

- **“`yield` returns from the function.”**  
  No. `yield` **pauses** the function and sends a value out.  
  The function can resume later and keep going.

- **“You can reuse a generator.”**  
  You can’t. Once a generator is exhausted, it stays exhausted.  
  To “reuse” the logic, call the generator function again to get a new generator object.


## When to use generators (rules of thumb)

Use generators when:

- **Data is large or unbounded** (log streams, sensor data, big files).
- You only need **one pass** over the data.
- You want **clear, step‑by‑step logic** expressed as a function, but also want laziness.
- You’re building **pipelines**: `source -> transform -> filter -> aggregate`.

Prefer other structures when:

- You need **indexing, slicing, or random access**.
- You need **multiple independent passes** over the same data.
- Simplicity is more important than laziness (e.g., small input, one‑off scripts).

A good heuristic:

> If you find yourself thinking “stream” or “pipeline,” reach for a generator.  
> If you find yourself thinking “array I want to poke at in many ways,” reach for a list (or similar).


## Suggested callout blocks

- **Mental model: Paused function**

  - A generator function runs until `yield`, then **pauses with all its state intact**.
  - Each `next()` resumes where it left off.

- **Under the hood: Generator object lifecycle**

  ```python
  def gen_func():
      # setup
      yield value1
      # more work
      yield value2
      # cleanup
      return  # or fall off the end
  ```

  - Call `gen_func()` → get generator object.
  - Repeatedly call `next()` → step through each `yield`.
  - When finished → `StopIteration`, generator is exhausted forever.

- **Pitfall alert: Exhaustion**

  - Generators are **single‑pass**.
  - Once you iterate them to the end, they’re empty.
  - To “start over,” call the generator function again or materialize the results.

- **Advanced note: `send()` / `yield from`**

  - `send()` lets you push values **into** a generator, not just pull them out.
  - `yield from` lets one generator **delegate** to another iterator, flattening or forwarding iteration.


## How this pairs with the iteration protocol page

- The **iteration protocol** describes the **contract**:
  - Iterables produce iterators.
  - Iterators support `__next__` and raise `StopIteration` to stop.
- **Generators** are a **convenient way to implement that contract**:
  - A generator object is an iterator.
  - A generator function is a factory for those iterators.

Together, they explain:

- How `for` loops work.
- How iterators and generators relate.
- How you can eventually understand async iteration too (`async def` + `async for` are the same ideas with `await` added on top).

